import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv()

# Create tools
search_tool = SerperDevTool()

# Create agents
researcher = Agent(
    role='Senior Researcher',
    goal='Uncover essential technologies and processes for new data scientists',
    verbose=True,
    memory=True,
    backstory='An expert in identifying and explaining complex technical concepts to beginners, you are dedicated to helping new data scientists transition smoothly into their roles.',
    tools=[search_tool]
)

writer = Agent(
    role='Content Writer',
    goal='Create detailed explanations and further reading resources from the gathered information',
    verbose=True,
    memory=True,
    backstory='Skilled in crafting clear and informative content, you specialize in making technical concepts accessible and engaging for a broad audience.',
    allow_delegation=False
)

reviewer = Agent(
    role='Content Reviewer',
    goal='Review and edit the explanations for grammatical accuracy, proper source linking, and overall quality',
    verbose=True,
    memory=True,
    backstory='With a keen eye for detail, you ensure all content is polished, professional, and engaging. You make sure the information is accurate and the posts are visually appealing.',
    allow_delegation=False
)

def generate_content(topic):
    research_task = Task(
        description=f'Research and gather comprehensive information on {topic} for new data scientists.',
        expected_output=f'A detailed report on {topic}, providing a clear understanding of its importance and application in a corporate environment.',
        tools=[search_tool],
        agent=researcher
    )

    writing_task = Task(
        description=f'Create detailed explanations and further reading resources based on the research report about {topic}.',
        expected_output=f'A comprehensive explanation of {topic} formatted for easy understanding, along with further reading resources.',
        agent=writer,
        async_execution=False,
        output_file='topic_explanation_draft.md'
    )

    review_task = Task(
        description=f'Review and edit the explanation about {topic} for grammatical accuracy, proper source linking, and overall quality.',
        expected_output=f'A final explanation about {topic} that is ready to be published, free of errors, with proper source attribution, and enhanced with emojis.',
        agent=reviewer,
        async_execution=False,
        input_file='topic_explanation_draft.md',
        output_file='topic_explanation_final.md'
    )

    # Form the crew
    crew = Crew(
        agents=[researcher, writer, reviewer],
        tasks=[research_task, writing_task, review_task],
        process=Process.sequential
    )

    # Kickoff the process
    result = crew.kickoff(inputs={})
    return result