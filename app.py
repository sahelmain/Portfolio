import streamlit as st
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Sahel Azzam - Portfolio",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .project-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
        border-left: 4px solid #667eea;
    }
    .stButton > button {
        background-color: #667eea;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 1rem;
    }
    .stButton > button:hover {
        background-color: #5a6fd8;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🎓 Sahel Azzam</h1>
    <h3>Master's CS Student @ Texas Tech University</h3>
    <p>Exploring ML, Deep Learning, Neural Networks, and Stochastic Modeling</p>
</div>
""", unsafe_allow_html=True)

# Sidebar with contact info
st.sidebar.markdown("## 📞 Contact Information")
st.sidebar.markdown("**📧 Email:** saazzam@ttu.edu")
st.sidebar.markdown("**🎓 Institution:** Texas Tech University")
st.sidebar.markdown("**📍 Location:** Lubbock, Texas")
st.sidebar.markdown("**🔗 LinkedIn:** [sahel-azzam-0a0670223](https://www.linkedin.com/in/sahel-azzam-0a0670223)")
st.sidebar.markdown("**🐙 GitHub:** [sahelmain](https://github.com/sahelmain)")

st.sidebar.markdown("---")
st.sidebar.markdown("## 🔍 Filter Projects")
filter_language = st.sidebar.selectbox(
    "Filter by Language:",
    ["All", "Jupyter Notebook", "TypeScript", "Python", "HTML", "JavaScript"]
)

# Projects data
projects_data = [
    {
        "name": "streaming-pattern-matching-optimization",
        "description": "Streaming implementation of Naive and KMP pattern matching algorithms with performance benchmarking, data visualization, and real-time network anomaly detection.",
        "language": "Jupyter Notebook",
        "license": "MIT",
        "updated": "7 minutes ago",
        "url": "https://github.com/sahelmain/streaming-pattern-matching-optimization",
        "category": "Algorithm Optimization"
    },
    {
        "name": "AI-Human-Text-Detection-Deep-Learning",
        "description": "Advanced AI vs Human text detection using deep learning. Features CNN, LSTM, and RNN models with Streamlit web interface achieving 97.8% accuracy.",
        "language": "Jupyter Notebook",
        "license": "",
        "updated": "1 hour ago",
        "url": "https://github.com/sahelmain/AI-Human-Text-Detection-Deep-Learning",
        "category": "Deep Learning"
    },
    {
        "name": "AI-Human-Text-Detection-App",
        "description": "🤖 Streamlit web app detecting AI vs human text using SVM (96.38%), Decision Tree & AdaBoost. Features real-time predictions, model comparison & interactive UI. Production-ready deployment.",
        "language": "Jupyter Notebook",
        "license": "",
        "updated": "2 weeks ago",
        "url": "https://github.com/sahelmain/AI-Human-Text-Detection-App",
        "category": "Machine Learning"
    },
    {
        "name": "Advanced-Text-Classification-ML-Pipelines",
        "description": "Advanced ML Engineering: Production-ready text classification pipelines with GridSearchCV, ensemble methods, and statistical analysis. 96.25% accuracy with custom transformers and comprehensive evaluation.",
        "language": "Jupyter Notebook",
        "license": "",
        "updated": "3 weeks ago",
        "url": "https://github.com/sahelmain/Advanced-Text-Classification-ML-Pipelines",
        "category": "Machine Learning"
    },
    {
        "name": "Text-Classification-Human-vs-AI-",
        "description": "Text classification project focusing on distinguishing between human and AI-generated content.",
        "language": "Jupyter Notebook",
        "license": "",
        "updated": "3 weeks ago",
        "url": "https://github.com/sahelmain/Text-Classification-Human-vs-AI-",
        "category": "Machine Learning"
    },
    {
        "name": "M.SApplicants",
        "description": "Master's degree applicants management system.",
        "language": "TypeScript",
        "license": "",
        "updated": "May 4",
        "url": "https://github.com/sahelmain/M.SApplicants",
        "category": "Web Development"
    },
    {
        "name": "FinalApplicantsSet",
        "description": "Final applicants dataset management system.",
        "language": "TypeScript",
        "license": "",
        "updated": "May 2",
        "url": "https://github.com/sahelmain/FinalApplicantsSet",
        "category": "Web Development"
    },
    {
        "name": "PhD2025Applicants",
        "description": "PhD 2025 applicants tracking system.",
        "language": "HTML",
        "license": "",
        "updated": "Apr 10",
        "url": "https://github.com/sahelmain/PhD2025Applicants",
        "category": "Web Development"
    },
    {
        "name": "MeatCuttingML-",
        "description": "Machine learning application for meat cutting optimization.",
        "language": "Python",
        "license": "MIT",
        "updated": "Feb 1",
        "url": "https://github.com/sahelmain/MeatCuttingML-",
        "category": "Machine Learning"
    },
    {
        "name": "Serology",
        "description": "Serology data analysis and management system.",
        "language": "TypeScript",
        "license": "",
        "updated": "Dec 9, 2024",
        "url": "https://github.com/sahelmain/Serology",
        "category": "Data Analysis"
    },
    {
        "name": "SerologyDashboardWebsite",
        "description": "Medical Information Simulation - Forked from yuh137/medical_information_simulation",
        "language": "TypeScript",
        "license": "",
        "updated": "Dec 8, 2024",
        "url": "https://github.com/sahelmain/SerologyDashboardWebsite",
        "category": "Web Development"
    },
    {
        "name": "CalibrationOfConcrete",
        "description": "Concrete calibration analysis using machine learning techniques.",
        "language": "Jupyter Notebook",
        "license": "",
        "updated": "Oct 8, 2024",
        "url": "https://github.com/sahelmain/CalibrationOfConcrete",
        "category": "Data Analysis"
    },
    {
        "name": "TexasLotterySystem",
        "description": "Texas lottery system implementation and analysis.",
        "language": "JavaScript",
        "license": "",
        "updated": "Feb 3, 2024",
        "url": "https://github.com/sahelmain/TexasLotterySystem",
        "category": "Web Development"
    }
]

# Filter projects based on language selection
if filter_language != "All":
    filtered_projects = [p for p in projects_data if p["language"] == filter_language]
else:
    filtered_projects = projects_data

# Main content
st.markdown("## 🚀 Featured Projects")
st.markdown(f"**Total Projects:** {len(filtered_projects)}")

# Project categories
categories = list(set([p["category"] for p in filtered_projects]))
selected_category = st.selectbox("Filter by Category:", ["All"] + sorted(categories))

if selected_category != "All":
    filtered_projects = [p for p in filtered_projects if p["category"] == selected_category]

# Display projects in a grid layout
col1, col2 = st.columns(2)

for i, project in enumerate(filtered_projects):
    with col1 if i % 2 == 0 else col2:
        with st.container():
            st.markdown(f"""
            <div class="project-card">
                <h3>🔗 {project['name']}</h3>
                <p><strong>Category:</strong> {project['category']}</p>
                <p>{project['description']}</p>
                <p><strong>Language:</strong> {project['language']}</p>
                {f"<p><strong>License:</strong> {project['license']}</p>" if project['license'] else ""}
                <p><strong>Last Updated:</strong> {project['updated']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"View on GitHub", key=f"btn_{i}"):
                st.markdown(f"[Open {project['name']}]({project['url']})")

# Statistics section
st.markdown("---")
st.markdown("## 📊 Project Statistics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Projects", len(projects_data))

with col2:
    ml_projects = len([p for p in projects_data if p["category"] in ["Machine Learning", "Deep Learning"]])
    st.metric("ML/DL Projects", ml_projects)

with col3:
    web_projects = len([p for p in projects_data if p["category"] == "Web Development"])
    st.metric("Web Projects", web_projects)

with col4:
    recent_projects = len([p for p in projects_data if "weeks" in p["updated"] or "minutes" in p["updated"] or "hour" in p["updated"]])
    st.metric("Recent Updates", recent_projects)

# Language distribution
st.markdown("### 📈 Language Distribution")
language_counts = pd.DataFrame([p["language"] for p in projects_data], columns=["Language"]).value_counts().reset_index()
language_counts.columns = ["Language", "Count"]
st.bar_chart(language_counts.set_index("Language"))

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>© 2025 Sahel Azzam | Built with Streamlit 🚀</p>
    <p>Master's CS Student @ Texas Tech University</p>
</div>
""", unsafe_allow_html=True) 