import streamlit as st
from agent import generate_content

# Set page configuration
st.set_page_config(
    page_title="Data Scientist Learning Hub",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .reportview-container {
        background: #f0f2f6;
    }
    .sidebar .sidebar-content {
        background: #e1e5eb;
    }
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 5rem;
        padding-right: 5rem;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        border-radius: 8px;
    }
    .stSelectbox>div {
        background-color: #ffffff;
        border: 1px solid #ddd;
        border-radius: 4px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar configuration
st.sidebar.title("Navigation")
st.sidebar.markdown("Use the dropdown below to select a topic.")

# Main page title and description
st.title('Data Scientist Learning Hub')
st.markdown("""
Welcome to the Data Scientist Learning Hub! Here, new data scientists can learn about essential technologies and processes.
Select a topic from the dropdown below to get detailed explanations and further reading resources.
""")

# List of topics
topics = [
    'Model Deployment',
    'Git',
    'Linux Commands',
    'Data Cleaning',
    'Feature Engineering',
    'Model Evaluation',
    'Version Control for Data Science',
    'Big Data Tools',
    'Cloud Computing for Data Science',
    'SQL for Data Scientists'
]

# Topic selection
selected_topic = st.sidebar.selectbox('Select a topic to learn about:', topics)

# Button to generate content
if st.sidebar.button('Generate Explanation'):
    with st.spinner('Generating content...'):
        result = generate_content(selected_topic)
        st.success('Content generated successfully!')
        st.markdown(result)

# Footer
st.markdown("""
---
*Created with 💖 by the Data Scientist Learning Hub Team*
""")
