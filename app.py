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
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        min-height: 100vh;
        position: relative;
    }
    
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000"><defs><radialGradient id="glow" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="%23ffffff" stop-opacity="0.1"/><stop offset="100%" stop-color="%23ffffff" stop-opacity="0"/></radialGradient></defs><circle cx="150" cy="150" r="80" fill="url(%23glow)"/><circle cx="850" cy="200" r="120" fill="url(%23glow)"/><circle cx="300" cy="800" r="100" fill="url(%23glow)"/><circle cx="700" cy="600" r="90" fill="url(%23glow)"/></svg>');
        opacity: 0.6;
        z-index: -1;
    }
    
    .main-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-radius: 24px;
        padding: 2rem;
        margin: 1rem;
        box-shadow: 0 32px 64px rgba(0, 0, 0, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .hero-section {
        text-align: center;
        padding: 4rem 2rem;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.95) 0%, rgba(118, 75, 162, 0.95) 100%);
        color: white;
        border-radius: 24px;
        margin-bottom: 3rem;
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .hero-section::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: conic-gradient(from 0deg, transparent, rgba(255, 255, 255, 0.1), transparent);
        animation: rotate 20s linear infinite;
    }
    
    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    
    .hero-content {
        position: relative;
        z-index: 2;
    }
    
    .hero-title {
        font-size: 4rem;
        font-weight: 800;
        margin-bottom: 1.5rem;
        background: linear-gradient(45deg, #ffffff, #f0f9ff, #ffffff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        letter-spacing: -0.02em;
    }
    
    .hero-subtitle {
        font-size: 1.6rem;
        font-weight: 500;
        margin-bottom: 1rem;
        color: #f1f5f9;
        text-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }
    
    .contact-badges {
        display: flex;
        justify-content: center;
        gap: 1.5rem;
        flex-wrap: wrap;
        margin-top: 3rem;
    }
    
    .contact-badge {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        padding: 1rem 2rem;
        border-radius: 50px;
        color: white;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        border: 2px solid rgba(255, 255, 255, 0.3);
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        position: relative;
        overflow: hidden;
    }
    
    .contact-badge::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
        transition: left 0.5s;
    }
    
    .contact-badge:hover::before {
        left: 100%;
    }
    
    .contact-badge:hover {
        background: rgba(255, 255, 255, 0.25);
        transform: translateY(-4px) scale(1.05);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        border-color: rgba(255, 255, 255, 0.5);
    }
    
    .section-title {
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 3rem;
        text-align: center;
        background: linear-gradient(135deg, #667eea, #764ba2, #f093fb);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        position: relative;
        letter-spacing: -0.02em;
    }
    
    .section-title::after {
        content: '';
        position: absolute;
        bottom: -15px;
        left: 50%;
        transform: translateX(-50%);
        width: 100px;
        height: 5px;
        background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
        border-radius: 3px;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
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
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(15px);
        padding: 2.5rem;
        border-radius: 24px;
        text-align: center;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        border: 1px solid rgba(255, 255, 255, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .stat-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.05), rgba(118, 75, 162, 0.05));
        opacity: 0;
        transition: opacity 0.3s;
    }
    
    .stat-card:hover::before {
        opacity: 1;
    }
    
    .stat-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 32px 64px rgba(0, 0, 0, 0.15);
        border-color: rgba(102, 126, 234, 0.3);
    }
    
    .stat-number {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
    }
    
    .stat-label {
        font-size: 1.2rem;
        color: #475569;
        font-weight: 600;
        letter-spacing: 0.02em;
    }
    
    .filter-section {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(15px);
        padding: 2.5rem;
        border-radius: 24px;
        margin-bottom: 3rem;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.3);
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
        padding: 4rem 2rem;
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.95), rgba(15, 23, 42, 0.95));
        backdrop-filter: blur(15px);
        color: white;
        border-radius: 24px;
        margin-top: 4rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        position: relative;
        overflow: hidden;
    }
    
    .footer::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(45deg, transparent 30%, rgba(255, 255, 255, 0.05) 50%, transparent 70%);
        animation: shimmer 3s ease-in-out infinite;
    }
    
    @keyframes shimmer {
        0%, 100% { transform: translateX(-100%); }
        50% { transform: translateX(100%); }
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

# About Me Section
st.markdown('<h2 class="section-title">👨‍💻 About Me</h2>', unsafe_allow_html=True)

st.markdown("""
<div style="background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(20px); padding: 3rem; border-radius: 24px; margin-bottom: 3rem; box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15); border: 1px solid rgba(255, 255, 255, 0.3);">
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 3rem; align-items: start;">
        <div style="background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1)); padding: 2.5rem; border-radius: 20px; border: 1px solid rgba(102, 126, 234, 0.2); position: relative; overflow: hidden;">
            <div style="position: absolute; top: -50%; right: -50%; width: 200%; height: 200%; background: conic-gradient(from 0deg, transparent, rgba(102, 126, 234, 0.1), transparent); animation: rotate 20s linear infinite; z-index: 1;"></div>
            <div style="position: relative; z-index: 2;">
                <h3 style="color: #1e293b; font-weight: 800; font-size: 1.8rem; margin-bottom: 1.5rem; background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">🎓 Academic Journey</h3>
                <div style="margin-bottom: 1.5rem;">
                    <h4 style="color: #374151; font-weight: 700; margin-bottom: 0.5rem;">Master's in Computer Science</h4>
                    <p style="color: #6b7280; margin-bottom: 0.5rem;">Texas Tech University | Lubbock, Texas</p>
                    <p style="color: #475569; line-height: 1.6;">Specializing in Machine Learning, Deep Learning, Neural Networks, and Stochastic Modeling. Currently advancing the frontiers of AI through research in pattern matching optimization, text classification, and neural network architectures.</p>
                </div>
                <div style="margin-bottom: 1.5rem;">
                    <h4 style="color: #374151; font-weight: 700; margin-bottom: 0.5rem;">Jordanian Heritage</h4>
                    <p style="color: #475569; line-height: 1.6;">Originally from Jordan, bringing a global perspective to computational research and cross-cultural collaboration in the tech industry. Fluent in multiple languages and experienced in international academic environments.</p>
                </div>
            </div>
        </div>
        
        <div style="background: linear-gradient(135deg, rgba(34, 197, 94, 0.1), rgba(16, 185, 129, 0.1)); padding: 2.5rem; border-radius: 20px; border: 1px solid rgba(34, 197, 94, 0.2); position: relative; overflow: hidden;">
            <div style="position: absolute; top: -50%; right: -50%; width: 200%; height: 200%; background: conic-gradient(from 0deg, transparent, rgba(34, 197, 94, 0.1), transparent); animation: rotate 25s linear infinite; z-index: 1;"></div>
            <div style="position: relative; z-index: 2;">
                <h3 style="color: #1e293b; font-weight: 800; font-size: 1.8rem; margin-bottom: 1.5rem; background: linear-gradient(135deg, #22c55e, #16a34a); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">🔬 Research Expertise</h3>
                <div style="margin-bottom: 1rem;">
                    <span style="background: rgba(34, 197, 94, 0.2); color: #065f46; padding: 0.5rem 1rem; border-radius: 20px; font-weight: 600; margin-right: 0.5rem; margin-bottom: 0.5rem; display: inline-block;">Machine Learning</span>
                    <span style="background: rgba(59, 130, 246, 0.2); color: #1e3a8a; padding: 0.5rem 1rem; border-radius: 20px; font-weight: 600; margin-right: 0.5rem; margin-bottom: 0.5rem; display: inline-block;">Deep Learning</span>
                    <span style="background: rgba(168, 85, 247, 0.2); color: #581c87; padding: 0.5rem 1rem; border-radius: 20px; font-weight: 600; margin-right: 0.5rem; margin-bottom: 0.5rem; display: inline-block;">Neural Networks</span>
                    <span style="background: rgba(239, 68, 68, 0.2); color: #7f1d1d; padding: 0.5rem 1rem; border-radius: 20px; font-weight: 600; margin-right: 0.5rem; margin-bottom: 0.5rem; display: inline-block;">Stochastic Modeling</span>
                    <span style="background: rgba(245, 158, 11, 0.2); color: #92400e; padding: 0.5rem 1rem; border-radius: 20px; font-weight: 600; margin-right: 0.5rem; margin-bottom: 0.5rem; display: inline-block;">Algorithm Optimization</span>
                    <span style="background: rgba(20, 184, 166, 0.2); color: #134e4a; padding: 0.5rem 1rem; border-radius: 20px; font-weight: 600; margin-right: 0.5rem; margin-bottom: 0.5rem; display: inline-block;">Text Classification</span>
                </div>
                <p style="color: #475569; line-height: 1.7; margin-top: 1.5rem;">Focused on developing production-ready AI solutions that bridge theoretical research with real-world applications. Experienced in advanced statistical methods, probabilistic models, and cutting-edge deep learning architectures.</p>
            </div>
        </div>
    </div>
    
    <div style="background: linear-gradient(135deg, rgba(239, 68, 68, 0.1), rgba(220, 38, 127, 0.1)); padding: 2.5rem; border-radius: 20px; border: 1px solid rgba(239, 68, 68, 0.2); margin-top: 3rem; position: relative; overflow: hidden;">
        <div style="position: absolute; top: -50%; right: -50%; width: 200%; height: 200%; background: conic-gradient(from 0deg, transparent, rgba(239, 68, 68, 0.1), transparent); animation: rotate 15s linear infinite; z-index: 1;"></div>
        <div style="position: relative; z-index: 2;">
            <h3 style="color: #1e293b; font-weight: 800; font-size: 1.8rem; margin-bottom: 1.5rem; background: linear-gradient(135deg, #ef4444, #dc2626); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">🚀 Professional Vision</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
                <div>
                    <h4 style="color: #374151; font-weight: 700; margin-bottom: 1rem; display: flex; align-items: center;"><span style="margin-right: 0.5rem;">🎯</span> Current Focus</h4>
                    <p style="color: #475569; line-height: 1.6;">Advancing AI research through innovative approaches to pattern matching, neural network optimization, and human-AI text classification. Committed to developing ethical AI solutions that enhance human capabilities.</p>
                </div>
                <div>
                    <h4 style="color: #374151; font-weight: 700; margin-bottom: 1rem; display: flex; align-items: center;"><span style="margin-right: 0.5rem;">💡</span> Innovation Drive</h4>
                    <p style="color: #475569; line-height: 1.6;">Passionate about creating AI systems that solve real-world problems. From achieving 97.8% accuracy in text classification to optimizing streaming algorithms, I focus on practical impact and measurable results.</p>
                </div>
                <div>
                    <h4 style="color: #374151; font-weight: 700; margin-bottom: 1rem; display: flex; align-items: center;"><span style="margin-right: 0.5rem;">🌍</span> Global Impact</h4>
                    <p style="color: #475569; line-height: 1.6;">Leveraging diverse cultural perspectives and international experience to build inclusive AI solutions. Committed to democratizing AI technology and making it accessible across different communities and industries.</p>
                </div>
            </div>
        </div>
    </div>
    
    <div style="background: linear-gradient(135deg, rgba(168, 85, 247, 0.1), rgba(139, 92, 246, 0.1)); padding: 2.5rem; border-radius: 20px; border: 1px solid rgba(168, 85, 247, 0.2); margin-top: 3rem; text-align: center; position: relative; overflow: hidden;">
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(45deg, transparent 30%, rgba(255, 255, 255, 0.05) 50%, transparent 70%); animation: shimmer 4s ease-in-out infinite;"></div>
        <div style="position: relative; z-index: 2;">
            <h3 style="color: #1e293b; font-weight: 800; font-size: 2rem; margin-bottom: 1.5rem; background: linear-gradient(135deg, #a855f7, #8b5cf6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">🤝 Let's Collaborate</h3>
            <p style="color: #475569; font-size: 1.2rem; line-height: 1.7; max-width: 700px; margin: 0 auto 2rem;">Always eager to connect with fellow researchers, industry professionals, and innovators. Whether it's discussing the latest in AI research, exploring collaboration opportunities, or sharing insights on machine learning applications, I'm excited to engage with the global tech community.</p>
            <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
                <span style="background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 1rem 2rem; border-radius: 25px; font-weight: 700; font-size: 1rem; display: inline-block; box-shadow: 0 8px 24px rgba(102, 126, 234, 0.3);">
                    🔬 Research Collaboration
                </span>
                <span style="background: linear-gradient(135deg, #22c55e, #16a34a); color: white; padding: 1rem 2rem; border-radius: 25px; font-weight: 700; font-size: 1rem; display: inline-block; box-shadow: 0 8px 24px rgba(34, 197, 94, 0.3);">
                    💼 Industry Projects
                </span>
                <span style="background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 1rem 2rem; border-radius: 25px; font-weight: 700; font-size: 1rem; display: inline-block; box-shadow: 0 8px 24px rgba(245, 158, 11, 0.3);">
                    🎓 Academic Exchange
                </span>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Why Hire Me Section
st.markdown('<h2 class="section-title">💼 Why Hire Me</h2>', unsafe_allow_html=True)

st.markdown("""
<div style="background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(20px); padding: 3rem; border-radius: 24px; margin-bottom: 3rem; box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15); border: 1px solid rgba(255, 255, 255, 0.3);">
    <div style="text-align: center; margin-bottom: 3rem;">
        <h3 style="color: #1e293b; font-size: 2.5rem; font-weight: 800; margin-bottom: 1rem; background: linear-gradient(135deg, #059669, #0d9488); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">Your Next AI Engineer</h3>
        <p style="color: #475569; font-size: 1.3rem; line-height: 1.6; max-width: 800px; margin: 0 auto;">Proven track record of delivering production-ready AI solutions that drive business value and solve real-world problems.</p>
    </div>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 2.5rem; margin-bottom: 3rem;">
        <div style="background: linear-gradient(135deg, rgba(34, 197, 94, 0.1), rgba(16, 185, 129, 0.1)); padding: 2.5rem; border-radius: 20px; border: 1px solid rgba(34, 197, 94, 0.2); position: relative; overflow: hidden; transition: all 0.4s ease;" onmouseover="this.style.transform='translateY(-8px)'; this.style.boxShadow='0 25px 50px rgba(34, 197, 94, 0.2)'" onmouseout="this.style.transform='translateY(0px)'; this.style.boxShadow='none'">
            <div style="position: absolute; top: -50%; right: -50%; width: 200%; height: 200%; background: conic-gradient(from 0deg, transparent, rgba(34, 197, 94, 0.1), transparent); animation: rotate 15s linear infinite; z-index: 1;"></div>
            <div style="position: relative; z-index: 2;">
                <div style="font-size: 3.5rem; margin-bottom: 1.5rem; text-align: center;">🎯</div>
                <h4 style="color: #1e293b; font-weight: 700; font-size: 1.5rem; margin-bottom: 1rem; text-align: center;">Proven Results</h4>
                <div style="margin-bottom: 1.5rem;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                        <span style="color: #374151; font-weight: 600;">AI Text Detection</span>
                        <span style="background: #dcfce7; color: #15803d; padding: 0.25rem 0.75rem; border-radius: 12px; font-weight: 700;">97.8%</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                        <span style="color: #374151; font-weight: 600;">ML Pipeline Accuracy</span>
                        <span style="background: #dcfce7; color: #15803d; padding: 0.25rem 0.75rem; border-radius: 12px; font-weight: 700;">96.25%</span>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.5rem;">
                        <span style="color: #374151; font-weight: 600;">Pattern Matching Optimization</span>
                        <span style="background: #dbeafe; color: #1d4ed8; padding: 0.25rem 0.75rem; border-radius: 12px; font-weight: 700;">3x Faster</span>
                    </div>
                </div>
                <p style="color: #374151; line-height: 1.7; font-size: 1rem;">Delivered production-ready solutions with measurable business impact. My models consistently achieve industry-leading accuracy rates while maintaining optimal performance.</p>
            </div>
        </div>
        
        <div style="background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(37, 99, 235, 0.1)); padding: 2.5rem; border-radius: 20px; border: 1px solid rgba(59, 130, 246, 0.2); position: relative; overflow: hidden; transition: all 0.4s ease;" onmouseover="this.style.transform='translateY(-8px)'; this.style.boxShadow='0 25px 50px rgba(59, 130, 246, 0.2)'" onmouseout="this.style.transform='translateY(0px)'; this.style.boxShadow='none'">
            <div style="position: absolute; top: -50%; right: -50%; width: 200%; height: 200%; background: conic-gradient(from 0deg, transparent, rgba(59, 130, 246, 0.1), transparent); animation: rotate 20s linear infinite; z-index: 1;"></div>
            <div style="position: relative; z-index: 2;">
                <div style="font-size: 3.5rem; margin-bottom: 1.5rem; text-align: center;">⚡</div>
                <h4 style="color: #1e293b; font-weight: 700; font-size: 1.5rem; margin-bottom: 1rem; text-align: center;">Rapid Deployment</h4>
                <div style="margin-bottom: 1.5rem;">
                    <span style="background: rgba(59, 130, 246, 0.2); color: #1e40af; padding: 0.5rem 1rem; border-radius: 20px; font-weight: 600; margin-right: 0.5rem; margin-bottom: 0.5rem; display: inline-block; font-size: 0.9rem;">Streamlit</span>
                    <span style="background: rgba(168, 85, 247, 0.2); color: #7c2d12; padding: 0.5rem 1rem; border-radius: 20px; font-weight: 600; margin-right: 0.5rem; margin-bottom: 0.5rem; display: inline-block; font-size: 0.9rem;">Docker</span>
                    <span style="background: rgba(34, 197, 94, 0.2); color: #14532d; padding: 0.5rem 1rem; border-radius: 20px; font-weight: 600; margin-right: 0.5rem; margin-bottom: 0.5rem; display: inline-block; font-size: 0.9rem;">CI/CD</span>
                    <span style="background: rgba(245, 158, 11, 0.2); color: #92400e; padding: 0.5rem 1rem; border-radius: 20px; font-weight: 600; margin-right: 0.5rem; margin-bottom: 0.5rem; display: inline-block; font-size: 0.9rem;">Cloud Platforms</span>
                </div>
                <p style="color: #374151; line-height: 1.7; font-size: 1rem;">Expert in modern deployment pipelines and DevOps practices. I build scalable applications that go from prototype to production quickly, ensuring your AI solutions reach users fast.</p>
            </div>
        </div>
        
        <div style="background: linear-gradient(135deg, rgba(168, 85, 247, 0.1), rgba(139, 92, 246, 0.1)); padding: 2.5rem; border-radius: 20px; border: 1px solid rgba(168, 85, 247, 0.2); position: relative; overflow: hidden; transition: all 0.4s ease;" onmouseover="this.style.transform='translateY(-8px)'; this.style.boxShadow='0 25px 50px rgba(168, 85, 247, 0.2)'" onmouseout="this.style.transform='translateY(0px)'; this.style.boxShadow='none'">
            <div style="position: absolute; top: -50%; right: -50%; width: 200%; height: 200%; background: conic-gradient(from 0deg, transparent, rgba(168, 85, 247, 0.1), transparent); animation: rotate 12s linear infinite; z-index: 1;"></div>
            <div style="position: relative; z-index: 2;">
                <div style="font-size: 3.5rem; margin-bottom: 1.5rem; text-align: center;">🧠</div>
                <h4 style="color: #1e293b; font-weight: 700; font-size: 1.5rem; margin-bottom: 1rem; text-align: center;">Full-Stack AI</h4>
                <div style="margin-bottom: 1.5rem;">
                    <div style="display: flex; align-items: center; margin-bottom: 0.75rem;">
                        <div style="width: 8px; height: 8px; background: #a855f7; border-radius: 50%; margin-right: 0.75rem;"></div>
                        <span style="color: #374151; font-weight: 600;">Deep Learning (CNN, LSTM, RNN)</span>
                    </div>
                    <div style="display: flex; align-items: center; margin-bottom: 0.75rem;">
                        <div style="width: 8px; height: 8px; background: #3b82f6; border-radius: 50%; margin-right: 0.75rem;"></div>
                        <span style="color: #374151; font-weight: 600;">ML Pipelines & AutoML</span>
                    </div>
                    <div style="display: flex; align-items: center; margin-bottom: 0.75rem;">
                        <div style="width: 8px; height: 8px; background: #10b981; border-radius: 50%; margin-right: 0.75rem;"></div>
                        <span style="color: #374151; font-weight: 600;">Web Applications & APIs</span>
                    </div>
                    <div style="display: flex; align-items: center; margin-bottom: 0.75rem;">
                        <div style="width: 8px; height: 8px; background: #f59e0b; border-radius: 50%; margin-right: 0.75rem;"></div>
                        <span style="color: #374151; font-weight: 600;">Data Visualization & Analytics</span>
                    </div>
                </div>
                <p style="color: #374151; line-height: 1.7; font-size: 1rem;">Complete AI solution development from data preprocessing to user interfaces. I handle the entire pipeline, ensuring seamless integration across all components.</p>
            </div>
        </div>
        
        <div style="background: linear-gradient(135deg, rgba(239, 68, 68, 0.1), rgba(220, 38, 127, 0.1)); padding: 2.5rem; border-radius: 20px; border: 1px solid rgba(239, 68, 68, 0.2); position: relative; overflow: hidden; transition: all 0.4s ease;" onmouseover="this.style.transform='translateY(-8px)'; this.style.boxShadow='0 25px 50px rgba(239, 68, 68, 0.2)'" onmouseout="this.style.transform='translateY(0px)'; this.style.boxShadow='none'">
            <div style="position: absolute; top: -50%; right: -50%; width: 200%; height: 200%; background: conic-gradient(from 0deg, transparent, rgba(239, 68, 68, 0.1), transparent); animation: rotate 18s linear infinite; z-index: 1;"></div>
            <div style="position: relative; z-index: 2;">
                <div style="font-size: 3.5rem; margin-bottom: 1.5rem; text-align: center;">🌍</div>
                <h4 style="color: #1e293b; font-weight: 700; font-size: 1.5rem; margin-bottom: 1rem; text-align: center;">Global Perspective</h4>
                <div style="margin-bottom: 1.5rem;">
                    <div style="background: rgba(34, 197, 94, 0.1); padding: 1rem; border-radius: 12px; border: 1px solid rgba(34, 197, 94, 0.2); margin-bottom: 1rem;">
                        <div style="font-weight: 700; color: #065f46; margin-bottom: 0.5rem;">🇯🇴 Jordanian Heritage</div>
                        <div style="color: #374151; font-size: 0.95rem;">Cross-cultural communication and international market understanding</div>
                    </div>
                    <div style="background: rgba(59, 130, 246, 0.1); padding: 1rem; border-radius: 12px; border: 1px solid rgba(59, 130, 246, 0.2);">
                        <div style="font-weight: 700; color: #1e40af; margin-bottom: 0.5rem;">🇺🇸 US Education</div>
                        <div style="color: #374151; font-size: 0.95rem;">Advanced technical training and research methodology</div>
                    </div>
                </div>
                <p style="color: #374151; line-height: 1.7; font-size: 1rem;">Unique blend of international experience and American technical excellence. I bring diverse perspectives to problem-solving and can work effectively with global teams.</p>
            </div>
        </div>
    </div>
    
    <div style="background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1)); padding: 3rem; border-radius: 20px; border: 1px solid rgba(102, 126, 234, 0.2); margin-bottom: 2rem; position: relative; overflow: hidden;">
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(45deg, transparent 30%, rgba(255, 255, 255, 0.05) 50%, transparent 70%); animation: shimmer 4s ease-in-out infinite;"></div>
        <div style="position: relative; z-index: 2;">
            <h4 style="color: #1e293b; font-weight: 800; font-size: 2rem; margin-bottom: 2rem; text-align: center; background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">🚀 What I Bring to Your Team</h4>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
                <div style="background: rgba(255, 255, 255, 0.6); padding: 2rem; border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.4); backdrop-filter: blur(10px);">
                    <h5 style="color: #1e293b; font-weight: 700; margin-bottom: 1rem; display: flex; align-items: center;"><span style="margin-right: 0.5rem;">💡</span>Innovation Mindset</h5>
                    <p style="color: #475569; line-height: 1.6; margin-bottom: 1rem;">Constantly exploring cutting-edge AI techniques and implementing novel solutions. I stay ahead of industry trends and bring fresh perspectives to challenging problems.</p>
                    <div style="font-size: 0.9rem; color: #6b7280; font-style: italic;">Recent: Achieved 97.8% accuracy in AI vs Human text detection</div>
                </div>
                <div style="background: rgba(255, 255, 255, 0.6); padding: 2rem; border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.4); backdrop-filter: blur(10px);">
                    <h5 style="color: #1e293b; font-weight: 700; margin-bottom: 1rem; display: flex; align-items: center;"><span style="margin-right: 0.5rem;">⚡</span>Rapid Prototyping</h5>
                    <p style="color: #475569; line-height: 1.6; margin-bottom: 1rem;">From concept to working prototype in days, not weeks. I excel at quickly validating ideas and building MVPs that demonstrate business value immediately.</p>
                    <div style="font-size: 0.9rem; color: #6b7280; font-style: italic;">Recent: Built AI detection app with Streamlit interface in under a week</div>
                </div>
                <div style="background: rgba(255, 255, 255, 0.6); padding: 2rem; border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.4); backdrop-filter: blur(10px);">
                    <h5 style="color: #1e293b; font-weight: 700; margin-bottom: 1rem; display: flex; align-items: center;"><span style="margin-right: 0.5rem;">🔧</span>Production Focus</h5>
                    <p style="color: #475569; line-height: 1.6; margin-bottom: 1rem;">Building robust, scalable solutions ready for production deployment. Experience with model optimization, monitoring, and maintenance in live environments.</p>
                    <div style="font-size: 0.9rem; color: #6b7280; font-style: italic;">Expertise: GridSearchCV, ensemble methods, statistical validation</div>
                </div>
                <div style="background: rgba(255, 255, 255, 0.6); padding: 2rem; border-radius: 16px; border: 1px solid rgba(255, 255, 255, 0.4); backdrop-filter: blur(10px);">
                    <h5 style="color: #1e293b; font-weight: 700; margin-bottom: 1rem; display: flex; align-items: center;"><span style="margin-right: 0.5rem;">📈</span>Business Impact</h5>
                    <p style="color: #475569; line-height: 1.6; margin-bottom: 1rem;">Understanding that great AI serves business goals. I translate technical capabilities into measurable business outcomes and ROI.</p>
                    <div style="font-size: 0.9rem; color: #6b7280; font-style: italic;">Focus: Real-world applications with clear value propositions</div>
                </div>
            </div>
        </div>
    </div>
    
    <div style="background: linear-gradient(135deg, rgba(245, 158, 11, 0.1), rgba(217, 119, 6, 0.1)); padding: 2.5rem; border-radius: 20px; border: 1px solid rgba(245, 158, 11, 0.2); text-align: center; position: relative; overflow: hidden;">
        <div style="position: absolute; top: -50%; right: -50%; width: 200%; height: 200%; background: conic-gradient(from 0deg, transparent, rgba(245, 158, 11, 0.1), transparent); animation: rotate 25s linear infinite; z-index: 1;"></div>
        <div style="position: relative; z-index: 2;">
            <h4 style="color: #1e293b; font-weight: 800; font-size: 1.8rem; margin-bottom: 1.5rem; background: linear-gradient(135deg, #f59e0b, #d97706); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">Ready to Start Contributing</h4>
            <p style="color: #374151; font-size: 1.2rem; line-height: 1.7; max-width: 700px; margin: 0 auto 2rem;">Available for full-time opportunities, internships, or contract work. Passionate about joining teams that are building the future with AI technology.</p>
            <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
                <span style="background: linear-gradient(135deg, #059669, #047857); color: white; padding: 1rem 2rem; border-radius: 25px; font-weight: 700; font-size: 1rem; display: inline-block; box-shadow: 0 8px 24px rgba(5, 150, 105, 0.3);">
                    ✅ Available Now
                </span>
                <span style="background: linear-gradient(135deg, #dc2626, #b91c1c); color: white; padding: 1rem 2rem; border-radius: 25px; font-weight: 700; font-size: 1rem; display: inline-block; box-shadow: 0 8px 24px rgba(220, 38, 38, 0.3);">
                    🔥 Immediate Impact
                </span>
                <span style="background: linear-gradient(135deg, #7c3aed, #6d28d9); color: white; padding: 1rem 2rem; border-radius: 25px; font-weight: 700; font-size: 1rem; display: inline-block; box-shadow: 0 8px 24px rgba(124, 58, 237, 0.3);">
                    🎯 Results Driven
                </span>
            </div>
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
                    .stContainer > div {
                        background: rgba(255, 255, 255, 0.9) !important;
                        backdrop-filter: blur(20px) !important;
                        border: 1px solid rgba(255, 255, 255, 0.3) !important;
                        border-radius: 24px !important;
                        padding: 2rem !important;
                        margin-bottom: 2rem !important;
                        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15) !important;
                        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94) !important;
                        position: relative !important;
                        overflow: hidden !important;
                    }
                    .stContainer > div::before {
                        content: '' !important;
                        position: absolute !important;
                        top: 0 !important;
                        left: 0 !important;
                        width: 100% !important;
                        height: 100% !important;
                        background: linear-gradient(135deg, rgba(102, 126, 234, 0.03), rgba(118, 75, 162, 0.03)) !important;
                        opacity: 0 !important;
                        transition: opacity 0.3s !important;
                        z-index: 1 !important;
                    }
                    .stContainer > div:hover::before {
                        opacity: 1 !important;
                    }
                    .stContainer > div:hover {
                        transform: translateY(-8px) scale(1.02) !important;
                        box-shadow: 0 32px 64px rgba(0, 0, 0, 0.2) !important;
                        border-color: rgba(102, 126, 234, 0.4) !important;
                    }
                    .project-card {
                        background: transparent !important;
                        border: none !important;
                        border-radius: 0 !important;
                        padding: 0 !important;
                        margin: 0 !important;
                        box-shadow: none !important;
                        position: relative !important;
                        z-index: 2 !important;
                    }
                    .project-header {
                        display: flex !important;
                        align-items: center !important;
                        margin-bottom: 1.5rem !important;
                        background: rgba(255, 255, 255, 0.6) !important;
                        backdrop-filter: blur(10px) !important;
                        padding: 1rem !important;
                        border-radius: 16px !important;
                        border: 1px solid rgba(255, 255, 255, 0.4) !important;
                        position: relative !important;
                        z-index: 3 !important;
                    }
                    .project-icon {
                        font-size: 3rem !important;
                        background: linear-gradient(135deg, #667eea, #764ba2, #f093fb) !important;
                        color: white !important;
                        border-radius: 16px !important;
                        padding: 1rem !important;
                        margin-right: 1.5rem !important;
                        width: 70px !important;
                        height: 70px !important;
                        display: flex !important;
                        align-items: center !important;
                        justify-content: center !important;
                        box-shadow: 0 8px 24px rgba(102, 126, 234, 0.4) !important;
                        position: relative !important;
                        overflow: hidden !important;
                    }
                    .project-icon::before {
                        content: '' !important;
                        position: absolute !important;
                        top: -50% !important;
                        left: -50% !important;
                        width: 200% !important;
                        height: 200% !important;
                        background: conic-gradient(from 0deg, transparent, rgba(255, 255, 255, 0.2), transparent) !important;
                        animation: rotate 3s linear infinite !important;
                    }
                    .project-title {
                        color: #1e293b !important;
                        font-weight: 800 !important;
                        font-size: 1.6rem !important;
                        margin: 0 !important;
                        background: linear-gradient(135deg, #667eea, #764ba2) !important;
                        -webkit-background-clip: text !important;
                        -webkit-text-fill-color: transparent !important;
                        background-clip: text !important;
                        letter-spacing: -0.02em !important;
                        position: relative !important;
                        z-index: 3 !important;
                    }
                    .project-description {
                        color: #374151 !important;
                        background: rgba(248, 250, 252, 0.8) !important;
                        backdrop-filter: blur(10px) !important;
                        padding: 1.5rem !important;
                        border-radius: 16px !important;
                        border: 1px solid rgba(102, 126, 234, 0.2) !important;
                        margin-bottom: 1.5rem !important;
                        font-weight: 500 !important;
                        line-height: 1.7 !important;
                        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.1) !important;
                        position: relative !important;
                        z-index: 3 !important;
                    }
                    .project-badge {
                        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1)) !important;
                        color: #1e293b !important;
                        padding: 0.75rem 1rem !important;
                        border-radius: 12px !important;
                        margin-bottom: 0.75rem !important;
                        font-weight: 700 !important;
                        border: 1px solid rgba(102, 126, 234, 0.2) !important;
                        backdrop-filter: blur(10px) !important;
                        transition: all 0.3s ease !important;
                        position: relative !important;
                        z-index: 3 !important;
                    }
                    .project-badge:hover {
                        transform: translateY(-2px) !important;
                        box-shadow: 0 8px 16px rgba(102, 126, 234, 0.2) !important;
                    }
                    .project-badge-license {
                        background: linear-gradient(135deg, rgba(34, 197, 94, 0.1), rgba(16, 185, 129, 0.1)) !important;
                        color: #065f46 !important;
                        padding: 0.75rem 1rem !important;
                        border-radius: 12px !important;
                        margin-bottom: 0.75rem !important;
                        font-weight: 700 !important;
                        border: 1px solid rgba(34, 197, 94, 0.3) !important;
                        backdrop-filter: blur(10px) !important;
                        transition: all 0.3s ease !important;
                        position: relative !important;
                        z-index: 3 !important;
                    }
                    .project-badge-time {
                        background: rgba(249, 250, 251, 0.8) !important;
                        color: #6b7280 !important;
                        padding: 0.75rem 1rem !important;
                        border-radius: 12px !important;
                        font-weight: 600 !important;
                        border: 1px solid rgba(229, 231, 235, 0.6) !important;
                        backdrop-filter: blur(10px) !important;
                        position: relative !important;
                        z-index: 3 !important;
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

# Why AI Matters Section
st.markdown('<h2 class="section-title">🤖 Why AI Matters</h2>', unsafe_allow_html=True)

st.markdown("""
<div style="background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(20px); padding: 3rem; border-radius: 24px; margin-bottom: 3rem; box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15); border: 1px solid rgba(255, 255, 255, 0.3);">
    <div style="text-align: center; margin-bottom: 3rem;">
        <h3 style="color: #1e293b; font-size: 2.5rem; font-weight: 800; margin-bottom: 1rem; background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">Transforming Our World</h3>
        <p style="color: #475569; font-size: 1.3rem; line-height: 1.6; max-width: 800px; margin: 0 auto;">AI isn't just technology—it's the catalyst for humanity's next evolutionary leap, reshaping how we solve problems, make decisions, and understand our world.</p>
    </div>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 2.5rem; margin-bottom: 3rem;">
        <div style="background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(147, 51, 234, 0.1)); padding: 2.5rem; border-radius: 20px; border: 1px solid rgba(59, 130, 246, 0.2); position: relative; overflow: hidden; transition: all 0.4s ease;" onmouseover="this.style.transform='translateY(-8px)'; this.style.boxShadow='0 25px 50px rgba(59, 130, 246, 0.2)'" onmouseout="this.style.transform='translateY(0px)'; this.style.boxShadow='none'">
            <div style="position: absolute; top: -50%; right: -50%; width: 200%; height: 200%; background: conic-gradient(from 0deg, transparent, rgba(59, 130, 246, 0.1), transparent); animation: rotate 15s linear infinite; z-index: 1;"></div>
            <div style="position: relative; z-index: 2;">
                <div style="font-size: 3.5rem; margin-bottom: 1.5rem; text-align: center;">🧠</div>
                <h4 style="color: #1e293b; font-weight: 700; font-size: 1.5rem; margin-bottom: 1rem; text-align: center;">Augmenting Human Intelligence</h4>
                <p style="color: #374151; line-height: 1.7; font-size: 1.1rem;">AI doesn't replace human creativity—it amplifies it. From diagnosing diseases faster than any human doctor to discovering new materials for sustainable energy, AI empowers us to tackle challenges that seemed impossible just decades ago.</p>
            </div>
        </div>
        
        <div style="background: linear-gradient(135deg, rgba(34, 197, 94, 0.1), rgba(16, 185, 129, 0.1)); padding: 2.5rem; border-radius: 20px; border: 1px solid rgba(34, 197, 94, 0.2); position: relative; overflow: hidden; transition: all 0.4s ease;" onmouseover="this.style.transform='translateY(-8px)'; this.style.boxShadow='0 25px 50px rgba(34, 197, 94, 0.2)'" onmouseout="this.style.transform='translateY(0px)'; this.style.boxShadow='none'">
            <div style="position: absolute; top: -50%; right: -50%; width: 200%; height: 200%; background: conic-gradient(from 0deg, transparent, rgba(34, 197, 94, 0.1), transparent); animation: rotate 20s linear infinite; z-index: 1;"></div>
            <div style="position: relative; z-index: 2;">
                <div style="font-size: 3.5rem; margin-bottom: 1.5rem; text-align: center;">🌍</div>
                <h4 style="color: #1e293b; font-weight: 700; font-size: 1.5rem; margin-bottom: 1rem; text-align: center;">Solving Global Challenges</h4>
                <p style="color: #374151; line-height: 1.7; font-size: 1.1rem;">Climate change, poverty, disease—AI is our most powerful tool for addressing humanity's greatest challenges. Machine learning models predict weather patterns, optimize resource distribution, and accelerate drug discovery to save millions of lives.</p>
            </div>
        </div>
        
        <div style="background: linear-gradient(135deg, rgba(239, 68, 68, 0.1), rgba(220, 38, 127, 0.1)); padding: 2.5rem; border-radius: 20px; border: 1px solid rgba(239, 68, 68, 0.2); position: relative; overflow: hidden; transition: all 0.4s ease;" onmouseover="this.style.transform='translateY(-8px)'; this.style.boxShadow='0 25px 50px rgba(239, 68, 68, 0.2)'" onmouseout="this.style.transform='translateY(0px)'; this.style.boxShadow='none'">
            <div style="position: absolute; top: -50%; right: -50%; width: 200%; height: 200%; background: conic-gradient(from 0deg, transparent, rgba(239, 68, 68, 0.1), transparent); animation: rotate 12s linear infinite; z-index: 1;"></div>
            <div style="position: relative; z-index: 2;">
                <div style="font-size: 3.5rem; margin-bottom: 1.5rem; text-align: center;">🚀</div>
                <h4 style="color: #1e293b; font-weight: 700; font-size: 1.5rem; margin-bottom: 1rem; text-align: center;">Democratizing Innovation</h4>
                <p style="color: #374151; line-height: 1.7; font-size: 1.1rem;">AI is breaking down barriers to innovation. A student with a laptop can now build applications that compete with multinational corporations. This democratization of powerful tools is creating unprecedented opportunities for breakthrough discoveries.</p>
            </div>
        </div>
        
        <div style="background: linear-gradient(135deg, rgba(168, 85, 247, 0.1), rgba(139, 92, 246, 0.1)); padding: 2.5rem; border-radius: 20px; border: 1px solid rgba(168, 85, 247, 0.2); position: relative; overflow: hidden; transition: all 0.4s ease;" onmouseover="this.style.transform='translateY(-8px)'; this.style.boxShadow='0 25px 50px rgba(168, 85, 247, 0.2)'" onmouseout="this.style.transform='translateY(0px)'; this.style.boxShadow='none'">
            <div style="position: absolute; top: -50%; right: -50%; width: 200%; height: 200%; background: conic-gradient(from 0deg, transparent, rgba(168, 85, 247, 0.1), transparent); animation: rotate 18s linear infinite; z-index: 1;"></div>
            <div style="position: relative; z-index: 2;">
                <div style="font-size: 3.5rem; margin-bottom: 1.5rem; text-align: center;">⚡</div>
                <h4 style="color: #1e293b; font-weight: 700; font-size: 1.5rem; margin-bottom: 1rem; text-align: center;">Accelerating Discovery</h4>
                <p style="color: #374151; line-height: 1.7; font-size: 1.1rem;">What once took years of research can now be accomplished in months or weeks. AI is compressing the innovation cycle, from protein folding predictions to autonomous vehicle development, pushing the boundaries of what's possible.</p>
            </div>
        </div>
    </div>
    
    <div style="background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1)); padding: 2.5rem; border-radius: 20px; border: 1px solid rgba(102, 126, 234, 0.2); text-align: center; position: relative; overflow: hidden;">
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(45deg, transparent 30%, rgba(255, 255, 255, 0.05) 50%, transparent 70%); animation: shimmer 4s ease-in-out infinite;"></div>
        <div style="position: relative; z-index: 2;">
            <h4 style="color: #1e293b; font-weight: 800; font-size: 1.8rem; margin-bottom: 1.5rem; background: linear-gradient(135deg, #667eea, #764ba2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text;">My Mission in AI</h4>
            <p style="color: #374151; font-size: 1.2rem; line-height: 1.7; max-width: 700px; margin: 0 auto;">As a Master's CS student specializing in Machine Learning and Deep Learning, I'm passionate about developing AI solutions that make a real difference. From text classification systems that combat misinformation to neural networks that enhance human decision-making, I believe AI should serve humanity's greatest aspirations.</p>
            <div style="margin-top: 2rem;">
                <span style="background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 1rem 2rem; border-radius: 25px; font-weight: 700; font-size: 1.1rem; display: inline-block; box-shadow: 0 8px 24px rgba(102, 126, 234, 0.3);">
                    🎯 Building AI for Good
                </span>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

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

# Contact Section
st.markdown('<h2 class="section-title">📞 Contact Me</h2>', unsafe_allow_html=True)

st.markdown("""
<div style="background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(20px); padding: 3rem; border-radius: 24px; margin-bottom: 3rem; box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15); border: 1px solid rgba(255, 255, 255, 0.3);">
    <div style="text-align: center; margin-bottom: 3rem;">
        <h3 style="color: #1e293b; font-size: 2rem; font-weight: 700; margin-bottom: 1rem;">Let's Connect & Collaborate</h3>
        <p style="color: #475569; font-size: 1.2rem; margin-bottom: 2rem;">Ready to work on exciting ML/DL projects? Reach out!</p>
    </div>
    
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-bottom: 3rem;">
        <div style="background: rgba(102, 126, 234, 0.1); padding: 2rem; border-radius: 20px; text-align: center; border: 1px solid rgba(102, 126, 234, 0.2); transition: all 0.3s ease;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 15px 30px rgba(102, 126, 234, 0.2)'" onmouseout="this.style.transform='translateY(0px)'; this.style.boxShadow='none'">
            <div style="font-size: 3rem; margin-bottom: 1rem;">📧</div>
            <h4 style="color: #1e293b; font-weight: 700; margin-bottom: 0.5rem;">Email</h4>
            <p style="color: #475569; margin-bottom: 1rem;">saazzam@ttu.edu</p>
            <a href="mailto:saazzam@ttu.edu" style="background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 0.75rem 1.5rem; border-radius: 10px; text-decoration: none; font-weight: 600; display: inline-block; transition: all 0.3s ease;" onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 10px 20px rgba(102, 126, 234, 0.3)'" onmouseout="this.style.transform='translateY(0px)'; this.style.boxShadow='none'">Send Email</a>
        </div>
        
        <div style="background: rgba(0, 119, 181, 0.1); padding: 2rem; border-radius: 20px; text-align: center; border: 1px solid rgba(0, 119, 181, 0.2); transition: all 0.3s ease;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 15px 30px rgba(0, 119, 181, 0.2)'" onmouseout="this.style.transform='translateY(0px)'; this.style.boxShadow='none'">
            <div style="font-size: 3rem; margin-bottom: 1rem;">💼</div>
            <h4 style="color: #1e293b; font-weight: 700; margin-bottom: 0.5rem;">LinkedIn</h4>
            <p style="color: #475569; margin-bottom: 1rem;">Professional Network</p>
            <a href="https://www.linkedin.com/in/sahel-azzam-0a0670223" target="_blank" style="background: linear-gradient(135deg, #0077b5, #00a0dc); color: white; padding: 0.75rem 1.5rem; border-radius: 10px; text-decoration: none; font-weight: 600; display: inline-block; transition: all 0.3s ease;" onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 10px 20px rgba(0, 119, 181, 0.3)'" onmouseout="this.style.transform='translateY(0px)'; this.style.boxShadow='none'">Connect</a>
        </div>
        
        <div style="background: rgba(36, 41, 47, 0.1); padding: 2rem; border-radius: 20px; text-align: center; border: 1px solid rgba(36, 41, 47, 0.2); transition: all 0.3s ease;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 15px 30px rgba(36, 41, 47, 0.2)'" onmouseout="this.style.transform='translateY(0px)'; this.style.boxShadow='none'">
            <div style="font-size: 3rem; margin-bottom: 1rem;">🐙</div>
            <h4 style="color: #1e293b; font-weight: 700; margin-bottom: 0.5rem;">GitHub</h4>
            <p style="color: #475569; margin-bottom: 1rem;">View My Code</p>
            <a href="https://github.com/sahelmain" target="_blank" style="background: linear-gradient(135deg, #24292f, #57606a); color: white; padding: 0.75rem 1.5rem; border-radius: 10px; text-decoration: none; font-weight: 600; display: inline-block; transition: all 0.3s ease;" onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 10px 20px rgba(36, 41, 47, 0.3)'" onmouseout="this.style.transform='translateY(0px)'; this.style.boxShadow='none'">Follow</a>
        </div>
        
        <div style="background: rgba(34, 197, 94, 0.1); padding: 2rem; border-radius: 20px; text-align: center; border: 1px solid rgba(34, 197, 94, 0.2); transition: all 0.3s ease;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 15px 30px rgba(34, 197, 94, 0.2)'" onmouseout="this.style.transform='translateY(0px)'; this.style.boxShadow='none'">
            <div style="font-size: 3rem; margin-bottom: 1rem;">📍</div>
            <h4 style="color: #1e293b; font-weight: 700; margin-bottom: 0.5rem;">Location</h4>
            <p style="color: #475569; margin-bottom: 1rem;">Lubbock, Texas</p>
            <span style="background: linear-gradient(135deg, #22c55e, #16a34a); color: white; padding: 0.75rem 1.5rem; border-radius: 10px; font-weight: 600; display: inline-block;">Available</span>
        </div>
    </div>
    
    <div style="background: rgba(248, 250, 252, 0.8); padding: 2rem; border-radius: 20px; border: 1px solid rgba(102, 126, 234, 0.2);">
        <h4 style="color: #1e293b; font-weight: 700; margin-bottom: 1.5rem; text-align: center;">💬 Quick Message</h4>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-bottom: 1.5rem;">
            <div>
                <label style="color: #374151; font-weight: 600; margin-bottom: 0.5rem; display: block;">Name</label>
                <div style="background: white; border: 2px solid #e5e7eb; border-radius: 10px; padding: 0.75rem; width: 100%;">
                    <input type="text" placeholder="Your Name" style="border: none; outline: none; width: 100%; font-size: 1rem;">
                </div>
            </div>
            <div>
                <label style="color: #374151; font-weight: 600; margin-bottom: 0.5rem; display: block;">Email</label>
                <div style="background: white; border: 2px solid #e5e7eb; border-radius: 10px; padding: 0.75rem; width: 100%;">
                    <input type="email" placeholder="your.email@example.com" style="border: none; outline: none; width: 100%; font-size: 1rem;">
                </div>
            </div>
        </div>
        <div style="margin-bottom: 1.5rem;">
            <label style="color: #374151; font-weight: 600; margin-bottom: 0.5rem; display: block;">Message</label>
            <div style="background: white; border: 2px solid #e5e7eb; border-radius: 10px; padding: 0.75rem; width: 100%;">
                <textarea placeholder="Tell me about your project or collaboration idea..." rows="4" style="border: none; outline: none; width: 100%; font-size: 1rem; resize: vertical;"></textarea>
            </div>
        </div>
        <div style="text-align: center;">
            <button onclick="sendMessage()" style="background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 1rem 2rem; border: none; border-radius: 10px; font-weight: 700; font-size: 1.1rem; cursor: pointer; transition: all 0.3s ease;" onmouseover="this.style.transform='translateY(-2px)'; this.style.boxShadow='0 15px 30px rgba(102, 126, 234, 0.4)'" onmouseout="this.style.transform='translateY(0px)'; this.style.boxShadow='none'">
                🚀 Send Message
            </button>
        </div>
        <p style="text-align: center; color: #6b7280; font-size: 0.9rem; margin-top: 1rem;">
            <em>Note: This will open your default email client with the message details</em>
        </p>
    </div>
</div>

<script>
function sendMessage() {
    const name = document.querySelector('input[placeholder="Your Name"]').value;
    const email = document.querySelector('input[placeholder="your.email@example.com"]').value;
    const message = document.querySelector('textarea').value;
    
    const subject = encodeURIComponent(`Portfolio Contact from ${name || 'Visitor'}`);
    const body = encodeURIComponent(`Name: ${name || 'Not provided'}
Email: ${email || 'Not provided'}

Message:
${message || 'No message provided'}

---
Sent from Sahel Azzam's Portfolio Website`);
    
    window.location.href = `mailto:saazzam@ttu.edu?subject=${subject}&body=${body}`;
}
</script>
""", unsafe_allow_html=True)

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