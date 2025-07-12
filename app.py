import streamlit as st
import pandas as pd
from datetime import datetime
import base64
import html

# Page configuration
st.set_page_config(
    page_title="Sahel Azzam - Portfolio",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for modern, professional styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .stApp {
        font-family: 'Inter', sans-serif;
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        min-height: 100vh;
    }
    
    .main-container {
        background: rgba(255, 255, 255, 1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.4);
    }
    
    .hero-section {
        text-align: center;
        padding: 3rem 0;
        background: linear-gradient(135deg, #1e3a8a 0%, #3730a3 100%);
        color: white;
        border-radius: 20px;
        margin-bottom: 3rem;
        position: relative;
        overflow: hidden;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000"><defs><radialGradient id="a" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="%23ffffff" stop-opacity="0.2"/><stop offset="100%" stop-color="%23ffffff" stop-opacity="0"/></radialGradient></defs><circle cx="200" cy="200" r="100" fill="url(%23a)"/><circle cx="800" cy="300" r="150" fill="url(%23a)"/><circle cx="400" cy="700" r="120" fill="url(%23a)"/></svg>');
        opacity: 0.4;
    }
    
    .hero-content {
        position: relative;
        z-index: 1;
    }
    
    .hero-title {
        font-size: 3.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.5);
        color: #ffffff;
    }
    
    .hero-subtitle {
        font-size: 1.5rem;
        font-weight: 500;
        margin-bottom: 2rem;
        color: #f1f5f9;
        text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.3);
    }
    
    .contact-badges {
        display: flex;
        justify-content: center;
        gap: 1rem;
        flex-wrap: wrap;
        margin-top: 2rem;
    }
    
    .contact-badge {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(10px);
        padding: 0.8rem 1.5rem;
        border-radius: 50px;
        color: white;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s ease;
        border: 2px solid rgba(255, 255, 255, 0.4);
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
    }
    
    .contact-badge:hover {
        background: rgba(255, 255, 255, 0.4);
        transform: translateY(-3px);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);
        border-color: rgba(255, 255, 255, 0.6);
    }
    
    .section-title {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 2rem;
        text-align: center;
        color: #1e293b;
        position: relative;
    }
    
    .section-title::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 80px;
        height: 4px;
        background: linear-gradient(90deg, #1e3a8a, #3730a3);
        border-radius: 2px;
    }
    
    .project-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
        gap: 2rem;
        margin-top: 2rem;
    }
    
    .project-card {
        background: white;
        border-radius: 20px;
        overflow: hidden;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15);
        transition: all 0.3s ease;
        position: relative;
        border: 2px solid rgba(30, 58, 138, 0.1);
    }
    
    .project-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.2);
        border-color: rgba(30, 58, 138, 0.3);
    }
    
    .project-thumbnail {
        height: 200px;
        background: linear-gradient(135deg, #1e3a8a 0%, #3730a3 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 3rem;
        color: white;
        position: relative;
        overflow: hidden;
    }
    
    .project-thumbnail::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grid" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M 10 0 L 0 0 0 10" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="0.5"/></pattern></defs><rect width="100" height="100" fill="url(%23grid)"/></svg>');
    }
    
    .project-content {
        padding: 2rem;
    }
    
    .project-title {
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        color: #1e293b;
    }
    
    .project-description {
        color: #475569;
        line-height: 1.6;
        margin-bottom: 1.5rem;
        font-weight: 400;
    }
    
    .project-meta {
        display: flex;
        gap: 1rem;
        margin-bottom: 1.5rem;
        flex-wrap: wrap;
    }
    
    .project-badge {
        background: #f8fafc;
        color: #1e293b;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.875rem;
        font-weight: 600;
        border: 1px solid #e2e8f0;
    }
    
    .project-badge.language {
        background: linear-gradient(135deg, #1e3a8a, #3730a3);
        color: white;
        border: none;
    }
    
    .project-badge.category {
        background: #e0e7ff;
        color: #3730a3;
        border: 1px solid #c7d2fe;
    }
    
    .project-actions {
        display: flex;
        gap: 1rem;
    }
    
    .btn-primary {
        background: linear-gradient(135deg, #1e3a8a, #3730a3);
        color: white;
        padding: 0.75rem 1.5rem;
        border-radius: 10px;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s ease;
        border: none;
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
    }
    
    .btn-primary:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 30px rgba(30, 58, 138, 0.4);
        background: linear-gradient(135deg, #1e40af, #4338ca);
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 2rem;
        margin: 3rem 0;
    }
    
    .stat-card {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        text-align: center;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
        border: 2px solid rgba(30, 58, 138, 0.1);
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
        border-color: rgba(30, 58, 138, 0.3);
    }
    
    .stat-number {
        font-size: 3rem;
        font-weight: 700;
        color: #1e3a8a;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        font-size: 1.1rem;
        color: #475569;
        font-weight: 600;
    }
    
    .filter-section {
        background: white;
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 3rem;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
        border: 2px solid rgba(30, 58, 138, 0.1);
    }
    
    .filter-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 2rem;
        align-items: center;
    }
    
    .stSelectbox > div > div {
        background: #f8fafc;
        border: 2px solid #e2e8f0;
        border-radius: 10px;
        padding: 0.5rem;
        font-weight: 500;
        color: #1e293b;
    }
    
    .footer {
        text-align: center;
        padding: 3rem 0;
        background: #1e293b;
        color: white;
        border-radius: 20px;
        margin-top: 3rem;
    }
    
    /* Hide Streamlit elements */
    .stDeployButton {display: none;}
    .stDecoration {display: none;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Fix any HTML rendering issues */
    .project-card * {
        box-sizing: border-box;
    }
    
    .project-meta {
        flex-wrap: wrap;
    }
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f1f1;
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #667eea, #764ba2);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #5a6fd8, #6b4f9b);
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-section">
    <div class="hero-content">
        <h1 class="hero-title">Sahel Azzam</h1>
        <p class="hero-subtitle">Master's CS Student @ Texas Tech University</p>
        <p style="font-size: 1.2rem; opacity: 0.9;">Exploring ML, Deep Learning, Neural Networks, and Stochastic Modeling</p>
        <div class="contact-badges">
            <a href="mailto:saazzam@ttu.edu" class="contact-badge">
                📧 Email
            </a>
            <a href="https://www.linkedin.com/in/sahel-azzam-0a0670223" class="contact-badge" target="_blank">
                🔗 LinkedIn
            </a>
            <a href="https://github.com/sahelmain" class="contact-badge" target="_blank">
                🐙 GitHub
            </a>
            <span class="contact-badge">
                📍 Lubbock, Texas
            </span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Filter Section
st.markdown("""
<div class="filter-section">
    <h3 style="margin-bottom: 1.5rem; color: #2d3748;">🔍 Filter Projects</h3>
    <div class="filter-grid">
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    filter_language = st.selectbox(
        "Filter by Language:",
        ["All", "Jupyter Notebook", "TypeScript", "Python", "HTML", "JavaScript"]
    )

with col2:
    # This will be populated after we define the projects
    pass

st.markdown("</div></div>", unsafe_allow_html=True)

# Projects data
projects_data = [
    {
        "name": "streaming-pattern-matching-optimization",
        "description": "Streaming implementation of Naive and KMP pattern matching algorithms with performance benchmarking, data visualization, and real-time network anomaly detection.",
        "language": "Jupyter Notebook",
        "license": "MIT",
        "updated": "7 minutes ago",
        "url": "https://github.com/sahelmain/streaming-pattern-matching-optimization",
        "category": "Algorithm Optimization",
        "icon": "🔍"
    },
    {
        "name": "AI-Human-Text-Detection-Deep-Learning",
        "description": "Advanced AI vs Human text detection using deep learning. Features CNN, LSTM, and RNN models with Streamlit web interface achieving 97.8% accuracy.",
        "language": "Jupyter Notebook",
        "license": "",
        "updated": "1 hour ago",
        "url": "https://github.com/sahelmain/AI-Human-Text-Detection-Deep-Learning",
        "category": "Deep Learning",
        "icon": "🧠"
    },
    {
        "name": "AI-Human-Text-Detection-App",
        "description": "🤖 Streamlit web app detecting AI vs human text using SVM (96.38%), Decision Tree & AdaBoost. Features real-time predictions, model comparison & interactive UI. Production-ready deployment.",
        "language": "Jupyter Notebook",
        "license": "",
        "updated": "2 weeks ago",
        "url": "https://github.com/sahelmain/AI-Human-Text-Detection-App",
        "category": "Machine Learning",
        "icon": "🤖"
    },
    {
        "name": "Advanced-Text-Classification-ML-Pipelines",
        "description": "Advanced ML Engineering: Production-ready text classification pipelines with GridSearchCV, ensemble methods, and statistical analysis. 96.25% accuracy with custom transformers and comprehensive evaluation.",
        "language": "Jupyter Notebook",
        "license": "",
        "updated": "3 weeks ago",
        "url": "https://github.com/sahelmain/Advanced-Text-Classification-ML-Pipelines",
        "category": "Machine Learning",
        "icon": "⚙️"
    },
    {
        "name": "Text-Classification-Human-vs-AI-",
        "description": "Text classification project focusing on distinguishing between human and AI-generated content.",
        "language": "Jupyter Notebook",
        "license": "",
        "updated": "3 weeks ago",
        "url": "https://github.com/sahelmain/Text-Classification-Human-vs-AI-",
        "category": "Machine Learning",
        "icon": "🎯"
    },
    {
        "name": "M.SApplicants",
        "description": "Master's degree applicants management system.",
        "language": "TypeScript",
        "license": "",
        "updated": "May 4",
        "url": "https://github.com/sahelmain/M.SApplicants",
        "category": "Web Development",
        "icon": "🎓"
    },
    {
        "name": "FinalApplicantsSet",
        "description": "Final applicants dataset management system.",
        "language": "TypeScript",
        "license": "",
        "updated": "May 2",
        "url": "https://github.com/sahelmain/FinalApplicantsSet",
        "category": "Web Development",
        "icon": "📊"
    },
    {
        "name": "PhD2025Applicants",
        "description": "PhD 2025 applicants tracking system.",
        "language": "HTML",
        "license": "",
        "updated": "Apr 10",
        "url": "https://github.com/sahelmain/PhD2025Applicants",
        "category": "Web Development",
        "icon": "🏆"
    },
    {
        "name": "MeatCuttingML-",
        "description": "Machine learning application for meat cutting optimization.",
        "language": "Python",
        "license": "MIT",
        "updated": "Feb 1",
        "url": "https://github.com/sahelmain/MeatCuttingML-",
        "category": "Machine Learning",
        "icon": "🥩"
    },
    {
        "name": "Serology",
        "description": "Serology data analysis and management system.",
        "language": "TypeScript",
        "license": "",
        "updated": "Dec 9, 2024",
        "url": "https://github.com/sahelmain/Serology",
        "category": "Data Analysis",
        "icon": "🔬"
    },
    {
        "name": "SerologyDashboardWebsite",
        "description": "Medical Information Simulation - Forked from yuh137/medical_information_simulation",
        "language": "TypeScript",
        "license": "",
        "updated": "Dec 8, 2024",
        "url": "https://github.com/sahelmain/SerologyDashboardWebsite",
        "category": "Web Development",
        "icon": "🏥"
    },
    {
        "name": "CalibrationOfConcrete",
        "description": "Concrete calibration analysis using machine learning techniques.",
        "language": "Jupyter Notebook",
        "license": "",
        "updated": "Oct 8, 2024",
        "url": "https://github.com/sahelmain/CalibrationOfConcrete",
        "category": "Data Analysis",
        "icon": "🏗️"
    },
    {
        "name": "TexasLotterySystem",
        "description": "Texas lottery system implementation and analysis.",
        "language": "JavaScript",
        "license": "",
        "updated": "Feb 3, 2024",
        "url": "https://github.com/sahelmain/TexasLotterySystem",
        "category": "Web Development",
        "icon": "🎰"
    }
]

# Update the category filter in the second column
categories = list(set([p["category"] for p in projects_data]))
with col2:
    selected_category = st.selectbox("Filter by Category:", ["All"] + sorted(categories))

# Filter projects based on selections
filtered_projects = projects_data
if filter_language != "All":
    filtered_projects = [p for p in filtered_projects if p["language"] == filter_language]
if selected_category != "All":
    filtered_projects = [p for p in filtered_projects if p["category"] == selected_category]

# Main content
st.markdown('<h2 class="section-title">🚀 Featured Projects</h2>', unsafe_allow_html=True)

# Create a responsive grid layout using Streamlit native components
cols_per_row = 2
for i in range(0, len(filtered_projects), cols_per_row):
    cols = st.columns(cols_per_row, gap="large")
    for j, col in enumerate(cols):
        if i + j < len(filtered_projects):
            project = filtered_projects[i + j]
            with col:
                # Use Streamlit's native container with custom CSS
                with st.container():
                    # Add custom CSS for this specific container
                    st.markdown("""
                    <style>
                    .project-card {
                        background: white !important;
                        border: 2px solid #e5e7eb !important;
                        border-radius: 16px !important;
                        padding: 1.5rem !important;
                        margin-bottom: 1rem !important;
                        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15) !important;
                    }
                    .project-header {
                        display: flex !important;
                        align-items: center !important;
                        margin-bottom: 1rem !important;
                    }
                    .project-icon {
                        font-size: 2.5rem !important;
                        background: linear-gradient(135deg, #1e3a8a, #3730a3) !important;
                        color: white !important;
                        border-radius: 12px !important;
                        padding: 10px !important;
                        margin-right: 1rem !important;
                        width: 60px !important;
                        height: 60px !important;
                        display: flex !important;
                        align-items: center !important;
                        justify-content: center !important;
                    }
                    .project-title {
                        color: #1e293b !important;
                        font-weight: 700 !important;
                        font-size: 1.3rem !important;
                        margin: 0 !important;
                    }
                    .project-description {
                        color: #374151 !important;
                        background: #f8fafc !important;
                        padding: 1rem !important;
                        border-radius: 8px !important;
                        border-left: 4px solid #1e3a8a !important;
                        margin-bottom: 1rem !important;
                    }
                    .project-badge {
                        background: #f1f5f9 !important;
                        color: #1e293b !important;
                        padding: 0.5rem !important;
                        border-radius: 6px !important;
                        margin-bottom: 0.5rem !important;
                        font-weight: 700 !important;
                    }
                    .project-badge-license {
                        background: #ecfdf5 !important;
                        color: #1e293b !important;
                        padding: 0.5rem !important;
                        border-radius: 6px !important;
                        margin-bottom: 0.5rem !important;
                        font-weight: 700 !important;
                    }
                    .project-badge-time {
                        background: #f9fafb !important;
                        color: #6b7280 !important;
                        padding: 0.5rem !important;
                        border-radius: 6px !important;
                        font-weight: 600 !important;
                    }
                    </style>
                    """, unsafe_allow_html=True)
                    
                    # Project header
                    col_icon, col_title = st.columns([1, 4])
                    with col_icon:
                        st.markdown(f'<div class="project-icon">{project["icon"]}</div>', unsafe_allow_html=True)
                    with col_title:
                        st.markdown(f'<h3 class="project-title">{project["name"]}</h3>', unsafe_allow_html=True)
                    
                    # Project description
                    st.markdown(f'<div class="project-description">{project["description"]}</div>', unsafe_allow_html=True)
                    
                    # Project metadata
                    st.markdown(f'<div class="project-badge">💻 {project["language"]}</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="project-badge">📁 {project["category"]}</div>', unsafe_allow_html=True)
                    if project["license"]:
                        st.markdown(f'<div class="project-badge-license">📄 {project["license"]}</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="project-badge-time">🕒 {project["updated"]}</div>', unsafe_allow_html=True)
                    
                    # GitHub link
                    if st.button(f"🔗 View on GitHub", key=f"btn_{project['name']}", use_container_width=True):
                        st.markdown(f'<script>window.open("{project["url"]}", "_blank");</script>', unsafe_allow_html=True)
                    
                    st.markdown("---")

# Statistics section
st.markdown('<h2 class="section-title">📊 Project Statistics</h2>', unsafe_allow_html=True)

st.markdown('<div class="stats-grid">', unsafe_allow_html=True)

# Calculate statistics
total_projects = len(projects_data)
ml_projects = len([p for p in projects_data if p["category"] in ["Machine Learning", "Deep Learning"]])
web_projects = len([p for p in projects_data if p["category"] == "Web Development"])
recent_projects = len([p for p in projects_data if "weeks" in p["updated"] or "minutes" in p["updated"] or "hour" in p["updated"]])

stats = [
    {"label": "Total Projects", "value": total_projects, "icon": "📚"},
    {"label": "ML/DL Projects", "value": ml_projects, "icon": "🤖"},
    {"label": "Web Projects", "value": web_projects, "icon": "🌐"},
    {"label": "Recent Updates", "value": recent_projects, "icon": "🔄"}
]

for stat in stats:
    st.markdown(f"""
    <div class="stat-card">
        <div style="font-size: 2rem; margin-bottom: 1rem;">{stat['icon']}</div>
        <div class="stat-number">{stat['value']}</div>
        <div class="stat-label">{stat['label']}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Language distribution chart
st.markdown('<h2 class="section-title">📈 Technology Stack</h2>', unsafe_allow_html=True)

# Create a more visually appealing chart
language_counts = pd.DataFrame([p["language"] for p in projects_data], columns=["Language"]).value_counts().reset_index()
language_counts.columns = ["Language", "Count"]

# Custom chart styling
st.markdown("""
<div style="background: white; padding: 2rem; border-radius: 20px; box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1); margin-bottom: 2rem;">
""", unsafe_allow_html=True)

st.bar_chart(language_counts.set_index("Language"), height=400)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <h3>🚀 Let's Connect!</h3>
    <p style="font-size: 1.2rem; margin: 1rem 0;">Ready to collaborate on exciting projects?</p>
    <div style="margin: 2rem 0;">
        <a href="mailto:saazzam@ttu.edu" class="contact-badge" style="margin: 0 0.5rem;">
            📧 Email Me
        </a>
        <a href="https://www.linkedin.com/in/sahel-azzam-0a0670223" class="contact-badge" style="margin: 0 0.5rem;" target="_blank">
            💼 LinkedIn
        </a>
        <a href="https://github.com/sahelmain" class="contact-badge" style="margin: 0 0.5rem;" target="_blank">
            🐙 GitHub
        </a>
    </div>
    <p style="margin-top: 2rem; opacity: 0.8;">© 2025 Sahel Azzam | Built with Streamlit 🚀</p>
    <p style="opacity: 0.6;">Master's CS Student @ Texas Tech University</p>
</div>
""", unsafe_allow_html=True) 