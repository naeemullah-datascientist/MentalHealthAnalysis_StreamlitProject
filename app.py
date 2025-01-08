import streamlit as st
from introduction import introduction
from datasetView import dataset_overview
from EDA2 import eda2
from ml_model import ml_model
from preprocessing import preprocessing
from conclusion_and_insights import conclusion_and_insights
import os

# Set Page Configuration for a better look (make sure this is at the top)
st.set_page_config(
    page_title="Mental Health in Tech Survey", 
    page_icon="🧠", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# Add custom CSS for more aesthetics and modern theme
st.markdown("""
    <style>
    /* Main Page Styling */
    .main {
        background-color: #f7f7f7;
        font-family: 'Helvetica', sans-serif;
        padding: 30px;
    }

    /* Sidebar Customization */
    .sidebar .sidebar-content {
        background: linear-gradient(to bottom, #1a73e8, #234aa3);
        color: white;
        font-size: 1.2em;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .sidebar .sidebar-content a {
        color: white;
        font-weight: bold;
    }

    .sidebar .sidebar-content a:hover {
        color: #ffcc00;
        text-decoration: underline;
    }

    /* Custom Button Styling */
    .stButton>button {
        background-color: #ff6f61;
        color: white;
        font-size: 16px;
        border-radius: 8px;
        padding: 12px 24px;
    }
    .stButton>button:hover {
        background-color: #e55a47;
    }

    /* Footer Styling */
    footer {
        text-align: center;
        margin-top: 30px;
        font-size: 14px;
        color: #555;
        border-top: 1px solid #ddd;
        padding-top: 10px;
    }

    footer p {
        margin: 0;
    }

    </style>
""", unsafe_allow_html=True)

# Add a welcoming header to the main page
st.title("🌟 Mental Health in Tech Survey - Unlocking Insights")

# Sidebar for navigation with customizations
st.sidebar.title("🧠 Mental Health in Tech")

# Use local image path for sidebar image
image_path = r"C:\Users\abc\PycharmProjects\ids_project\pic1.jpg"
if os.path.exists(image_path):
    st.sidebar.image(image_path, use_container_width=True)
else:
    st.sidebar.image("https://via.placeholder.com/150", use_container_width=True)

st.sidebar.markdown("## Navigate through the sections:")

# Dictionary to map page names to functions
pages = {
    "Introduction": introduction,
    "Dataset Overview": dataset_overview,
    "EDA": eda2,
    "Machine Learning Model": ml_model,
    "Data Preprocessing": preprocessing,
    "Conclusion and Insights": conclusion_and_insights
}

# Sidebar Radio button navigation with icons
selection = st.sidebar.radio(
    "Go to",
    list(pages.keys()),
    index=0,
    help="Select a section to explore the insights"
)

# Display the selected page
pages[selection]()

# Custom footer
st.markdown("""
    <footer>
        <p>📊 Built with ❤️ by Naeem Ullah, Data Scientist. Explore and learn more about Mental Health in the Tech Industry.</p>
    </footer>
""", unsafe_allow_html=True)
