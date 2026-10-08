import streamlit as st
import pandas as pd
from datetime import datetime
import html

# Page configuration
st.set_page_config(
    page_title="Sahel Azzam - Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dark mode toggle state
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# Custom CSS for modern, professional styling with dark mode support
def get_css_theme():
    if st.session_state.dark_mode:
        return """
        .stApp {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 25%, #0f3460 50%, #533483 75%, #e94560 100%);
            color: #ffffff;
        }
        
        .main-container {
            background: rgba(30, 30, 30, 0.95);
            color: #ffffff;
        }
        
        .hero-section {
            background: linear-gradient(135deg, 
                rgba(26, 26, 46, 0.9) 0%, 
                rgba(22, 33, 62, 0.9) 25%, 
                rgba(15, 52, 96, 0.9) 50%,
                rgba(83, 52, 131, 0.9) 75%,
                rgba(233, 69, 96, 0.9) 100%);
            color: white;
        }
        
        .project-card {
            background: rgba(30, 30, 30, 0.95);
            color: #ffffff;
        }
        
        .section-title {
            color: #ffffff;
        }
        """
    else:
        return """
        .stApp {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #f5576c 75%, #4facfe 100%);
        }
        
        .main-container {
            background: rgba(255, 255, 255, 0.95);
        }
        
        .hero-section {
            background: linear-gradient(135deg, 
                rgba(102, 126, 234, 0.9) 0%, 
                rgba(118, 75, 162, 0.9) 25%, 
                rgba(240, 147, 251, 0.9) 50%,
                rgba(245, 87, 108, 0.9) 75%,
                rgba(79, 172, 254, 0.9) 100%);
            color: white;
        }
        
        .project-card {
            background: rgba(255, 255, 255, 0.95);
        }
        """

theme_css = get_css_theme()

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
    
    {theme_css}
    
    .stApp {{
        font-family: 'Inter', sans-serif;
        background-size: 400% 400%;
        animation: gradientShift 15s ease infinite;
        min-height: 100vh;
        position: relative;
    }}
    
    @keyframes gradientShift {{
        0% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
        100% {{ background-position: 0% 50%; }}
    }}
    
    .dark-mode-toggle {{
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 1000;
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 50px;
        padding: 0.75rem 1.5rem;
        font-weight: 700;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 8px 24px rgba(102, 126, 234, 0.3);
    }}
    
    .dark-mode-toggle:hover {{
        transform: translateY(-2px) scale(1.05);
        box-shadow: 0 12px 32px rgba(102, 126, 234, 0.4);
    }}
    
    .stApp::before {{
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            radial-gradient(circle at 20% 80%, rgba(120, 119, 198, 0.3) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(255, 119, 198, 0.3) 0%, transparent 50%),
            radial-gradient(circle at 40% 40%, rgba(120, 219, 255, 0.3) 0%, transparent 50%);
        z-index: -1;
        animation: floatingOrbs 20s ease-in-out infinite;
    }}
    
    @keyframes floatingOrbs {{
        0%, 100% {{ transform: translateY(0px) rotate(0deg); }}
        33% {{ transform: translateY(-20px) rotate(120deg); }}
        66% {{ transform: translateY(10px) rotate(240deg); }}
    }}
    
    .main-container {{
        backdrop-filter: blur(25px);
        border-radius: 32px;
        padding: 2rem;
        margin: 1rem;
        box-shadow: 
            0 32px 64px rgba(0, 0, 0, 0.25),
            0 0 0 1px rgba(255, 255, 255, 0.1),
            inset 0 1px 0 rgba(255, 255, 255, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.18);
    }}
    
    .hero-section {{
        text-align: center;
        padding: 5rem 2rem;
        background-size: 400% 400%;
        animation: gradientShift 12s ease infinite;
        border-radius: 32px;
        margin-bottom: 3rem;
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(15px);
        border: 2px solid rgba(255, 255, 255, 0.2);
        box-shadow: 
            0 25px 50px rgba(0, 0, 0, 0.3),
            inset 0 1px 0 rgba(255, 255, 255, 0.3);
    }}
    
    .hero-section::before {{
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: conic-gradient(
            from 0deg,
            transparent,
            rgba(255, 255, 255, 0.1),
            transparent,
            rgba(255, 255, 255, 0.1),
            transparent
        );
        animation: rotate 25s linear infinite;
    }}
    
    .hero-section::after {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(45deg, transparent 30%, rgba(255, 255, 255, 0.1) 50%, transparent 70%);
        animation: shimmer 3s ease-in-out infinite;
    }}
    
    @keyframes rotate {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate(360deg); }}
    }}
    
    @keyframes shimmer {{
        0%, 100% {{ transform: translateX(-100%); }}
        50% {{ transform: translateX(100%); }}
    }}
    
    .hero-content {{
        position: relative;
        z-index: 2;
    }}
    
    .hero-title {{
        font-size: 4.5rem;
        font-weight: 900;
        margin-bottom: 1.5rem;
        background: linear-gradient(45deg, 
            #ffffff, 
            #f0f9ff, 
            #fef3c7, 
            #fce7f3, 
            #ffffff);
        background-size: 400% 400%;
        animation: gradientShift 8s ease infinite;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
        letter-spacing: -0.02em;
        filter: drop-shadow(0 0 30px rgba(255, 255, 255, 0.5));
    }}
    
    .hero-subtitle {{
        font-size: 1.8rem;
        font-weight: 600;
        margin-bottom: 1rem;
        color: #f1f5f9;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
        background: linear-gradient(135deg, #f1f5f9, #e2e8f0, #f8fafc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }}
    
    .contact-badges {{
        display: flex;
        justify-content: center;
        gap: 2rem;
        flex-wrap: wrap;
        margin-top: 3rem;
    }}
    
    .contact-badge {{
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.25), 
            rgba(255, 255, 255, 0.15));
        backdrop-filter: blur(15px);
        padding: 1.2rem 2.5rem;
        border-radius: 50px;
        color: white;
        text-decoration: none;
        font-weight: 700;
        font-size: 1.1rem;
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        border: 2px solid rgba(255, 255, 255, 0.3);
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
        position: relative;
        overflow: hidden;
        transform-style: preserve-3d;
        box-shadow: 
            0 15px 35px rgba(0, 0, 0, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 0.4);
    }}
    
    .contact-badge::before {{
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, 
            transparent, 
            rgba(255, 255, 255, 0.3), 
            transparent);
        transition: left 0.6s ease;
    }}
    
    .contact-badge:hover::before {{
        left: 100%;
    }}
    
    .contact-badge:hover {{
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.35), 
            rgba(255, 255, 255, 0.25));
        transform: translateY(-6px) scale(1.05) rotateX(10deg);
        box-shadow: 
            0 25px 50px rgba(0, 0, 0, 0.4),
            0 0 50px rgba(255, 255, 255, 0.3),
            inset 0 1px 0 rgba(255, 255, 255, 0.5);
        border-color: rgba(255, 255, 255, 0.6);
    }}
    
    .section-title {{
        font-size: 3.5rem;
        font-weight: 900;
        margin-bottom: 3rem;
        text-align: center;
        background: linear-gradient(135deg, 
            #667eea, 
            #764ba2, 
            #f093fb, 
            #f5576c, 
            #4facfe, 
            #00f2fe);
        background-size: 400% 400%;
        animation: gradientShift 10s ease infinite;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        position: relative;
        letter-spacing: -0.02em;
        filter: drop-shadow(0 4px 12px rgba(102, 126, 234, 0.4));
    }}
    
    .section-title::after {{
        content: '';
        position: absolute;
        bottom: -20px;
        left: 50%;
        transform: translateX(-50%);
        width: 120px;
        height: 6px;
        background: linear-gradient(90deg, 
            #667eea, 
            #764ba2, 
            #f093fb, 
            #f5576c, 
            #4facfe);
        background-size: 400% 400%;
        animation: gradientShift 8s ease infinite;
        border-radius: 4px;
        box-shadow: 
            0 4px 15px rgba(102, 126, 234, 0.6),
            0 0 30px rgba(240, 147, 251, 0.4);
    }}
    
    .project-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));
        gap: 2.5rem;
        margin-top: 2rem;
    }}
    
    .project-card {{
        backdrop-filter: blur(20px);
        border-radius: 24px;
        overflow: hidden;
        box-shadow: 
            0 20px 40px rgba(0, 0, 0, 0.15),
            0 0 0 1px rgba(255, 255, 255, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 0.3);
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        position: relative;
        border: 1px solid rgba(102, 126, 234, 0.2);
        transform-style: preserve-3d;
    }}
    
    .project-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, 
            rgba(102, 126, 234, 0.05), 
            rgba(240, 147, 251, 0.05), 
            rgba(245, 87, 108, 0.05));
        opacity: 0;
        transition: opacity 0.4s ease;
        z-index: 1;
    }}
    
    .project-card:hover::before {{
        opacity: 1;
    }}
    
    .project-card:hover {{
        transform: translateY(-12px) rotateX(5deg) rotateY(2deg);
        box-shadow: 
            0 35px 70px rgba(0, 0, 0, 0.25),
            0 0 50px rgba(102, 126, 234, 0.3),
            inset 0 1px 0 rgba(255, 255, 255, 0.4);
        border-color: rgba(102, 126, 234, 0.4);
    }}
    
    .project-thumbnail {{
        height: 220px;
        background: linear-gradient(135deg, 
            #1e3a8a 0%, 
            #3730a3 25%, 
            #7c3aed 50%, 
            #db2777 75%, 
            #dc2626 100%);
        background-size: 400% 400%;
        animation: gradientShift 12s ease infinite;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 3.5rem;
        color: white;
        position: relative;
        overflow: hidden;
        filter: drop-shadow(0 4px 12px rgba(0, 0, 0, 0.3));
    }}
    
    .project-thumbnail::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><defs><pattern id="grid" width="10" height="10" patternUnits="userSpaceOnUse"><path d="M 10 0 L 0 0 0 10" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="0.5"/></pattern></defs><rect width="100" height="100" fill="url(%23grid)"/></svg>');
        animation: float 6s ease-in-out infinite;
    }}
    
    @keyframes float {{
        0%, 100% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-10px); }}
    }}
    
    .project-content {{
        padding: 2.5rem;
        position: relative;
        z-index: 2;
    }}
    
    .project-title {{
        font-size: 1.7rem;
        font-weight: 800;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, 
            #1e293b, 
            #3730a3, 
            #7c3aed);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -0.01em;
    }}
    
    .project-description {{
        color: #475569;
        line-height: 1.7;
        margin-bottom: 1.5rem;
        font-weight: 500;
        font-size: 1.05rem;
    }}
    
    .project-meta {{
        display: flex;
        gap: 1rem;
        margin-bottom: 1.5rem;
        flex-wrap: wrap;
    }}
    
    .project-badge {{
        background: linear-gradient(135deg, 
            rgba(248, 250, 252, 0.9), 
            rgba(241, 245, 249, 0.9));
        color: #1e293b;
        padding: 0.6rem 1.2rem;
        border-radius: 25px;
        font-size: 0.9rem;
        font-weight: 700;
        border: 1px solid rgba(226, 232, 240, 0.6);
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    }}
    
    .project-badge:hover {{
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
    }}
    
    .project-badge.language {{
        background: linear-gradient(135deg, 
            #1e3a8a, 
            #3730a3, 
            #7c3aed);
        color: white;
        border: none;
        box-shadow: 0 4px 15px rgba(30, 58, 138, 0.3);
    }}
    
    .project-badge.category {{
        background: linear-gradient(135deg, 
            #e0e7ff, 
            #c7d2fe, 
            #ddd6fe);
        color: #3730a3;
        border: 1px solid rgba(199, 210, 254, 0.6);
    }}
    
    .project-actions {{
        display: flex;
        gap: 1rem;
    }}
    
    .btn-primary {{
        background: linear-gradient(135deg, 
            #1e3a8a, 
            #3730a3, 
            #7c3aed);
        background-size: 300% 300%;
        animation: gradientShift 8s ease infinite;
        color: white;
        padding: 1rem 2rem;
        border-radius: 15px;
        text-decoration: none;
        font-weight: 700;
        font-size: 1.05rem;
        transition: all 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        border: none;
        cursor: pointer;
        display: inline-flex;
        align-items: center;
        gap: 0.7rem;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        box-shadow: 
            0 10px 25px rgba(30, 58, 138, 0.3),
            inset 0 1px 0 rgba(255, 255, 255, 0.2);
        position: relative;
        overflow: hidden;
    }}
    
    .btn-primary::before {{
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
        transition: left 0.5s;
    }}
    
    .btn-primary:hover::before {{
        left: 100%;
    }}
    
    .btn-primary:hover {{
        transform: translateY(-4px) scale(1.02);
        box-shadow: 
            0 20px 40px rgba(30, 58, 138, 0.4),
            0 0 30px rgba(124, 58, 237, 0.3),
            inset 0 1px 0 rgba(255, 255, 255, 0.3);
    }}
    
    .stats-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2.5rem;
        margin: 3rem 0;
    }}
    
    .stat-card {{
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.95), 
            rgba(255, 255, 255, 0.85));
        backdrop-filter: blur(20px);
        padding: 3rem;
        border-radius: 28px;
        text-align: center;
        box-shadow: 
            0 25px 50px rgba(0, 0, 0, 0.15),
            0 0 0 1px rgba(255, 255, 255, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 0.4);
        transition: all 0.5s cubic-bezier(0.25, 0.46, 0.45, 0.94);
        border: 1px solid rgba(255, 255, 255, 0.3);
        position: relative;
        overflow: hidden;
        transform-style: preserve-3d;
    }}
    
    .stat-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(135deg, 
            rgba(102, 126, 234, 0.08), 
            rgba(240, 147, 251, 0.08), 
            rgba(245, 87, 108, 0.08));
        opacity: 0;
        transition: opacity 0.4s;
    }}
    
    .stat-card:hover::before {{
        opacity: 1;
    }}
    
    .stat-card:hover {{
        transform: translateY(-10px) rotateX(5deg) scale(1.02);
        box-shadow: 
            0 40px 80px rgba(0, 0, 0, 0.2),
            0 0 50px rgba(102, 126, 234, 0.3),
            inset 0 1px 0 rgba(255, 255, 255, 0.5);
        border-color: rgba(102, 126, 234, 0.4);
    }}
    
    .stat-number {{
        font-size: 4rem;
        font-weight: 900;
        background: linear-gradient(135deg, 
            #667eea, 
            #764ba2, 
            #f093fb, 
            #f5576c);
        background-size: 400% 400%;
        animation: gradientShift 8s ease infinite;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
        filter: drop-shadow(0 4px 12px rgba(102, 126, 234, 0.3));
    }}
    
    .stat-label {{
        font-size: 1.3rem;
        color: #475569;
        font-weight: 700;
        letter-spacing: 0.02em;
        background: linear-gradient(135deg, #475569, #64748b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }}
    
    .filter-section {{
        background: linear-gradient(135deg, 
            rgba(255, 255, 255, 0.95), 
            rgba(255, 255, 255, 0.85));
        backdrop-filter: blur(20px);
        padding: 3rem;
        border-radius: 28px;
        margin-bottom: 3rem;
        box-shadow: 
            0 25px 50px rgba(0, 0, 0, 0.15),
            0 0 0 1px rgba(255, 255, 255, 0.2),
            inset 0 1px 0 rgba(255, 255, 255, 0.4);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }}
    
    .filter-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 2rem;
        align-items: center;
    }}
    
    .stSelectbox > div > div {{
        background: linear-gradient(135deg, 
            rgba(248, 250, 252, 0.9), 
            rgba(241, 245, 249, 0.9));
        border: 2px solid rgba(226, 232, 240, 0.6);
        border-radius: 15px;
        padding: 0.8rem;
        font-weight: 600;
        color: #1e293b;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    }}
    
    .stSelectbox > div > div:hover {{
        border-color: rgba(102, 126, 234, 0.5);
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.2);
    }}
    
    .footer {{
        text-align: center;
        padding: 5rem 2rem;
        background: linear-gradient(135deg, 
            rgba(30, 41, 59, 0.95), 
            rgba(15, 23, 42, 0.95), 
            rgba(30, 41, 59, 0.95));
        backdrop-filter: blur(20px);
        color: white;
        border-radius: 32px;
        margin-top: 4rem;
        border: 2px solid rgba(255, 255, 255, 0.1);
        position: relative;
        overflow: hidden;
        box-shadow: 
            0 25px 50px rgba(0, 0, 0, 0.3),
            inset 0 1px 0 rgba(255, 255, 255, 0.1);
    }}
    
    .footer::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(45deg, 
            transparent 30%, 
            rgba(102, 126, 234, 0.1) 40%, 
            rgba(240, 147, 251, 0.1) 50%, 
            rgba(245, 87, 108, 0.1) 60%, 
            transparent 70%);
        animation: shimmer 4s ease-in-out infinite;
    }}
    
    /* Hide Streamlit elements */
    .stDeployButton {{display: none;}}
    .stDecoration {{display: none;}}
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    
    /* Enhanced scrollbar */
    ::-webkit-scrollbar {{
        width: 12px;
    }}
    
    ::-webkit-scrollbar-track {{
        background: linear-gradient(135deg, #f1f1f1, #e2e8f0);
        border-radius: 10px;
    }}
    
    ::-webkit-scrollbar-thumb {{
        background: linear-gradient(135deg, #667eea, #764ba2, #f093fb);
        border-radius: 10px;
        border: 2px solid #f1f1f1;
    }}
    
    ::-webkit-scrollbar-thumb:hover {{
        background: linear-gradient(135deg, #5a6fd8, #6b4f9b, #e088f0);
    }}
    
    /* Rainbow loading animation */
    @keyframes rainbow {{
        0% {{ filter: hue-rotate(0deg); }}
        100% {{ filter: hue-rotate(360deg); }}
    }}
    
    .rainbow-element {{
        animation: rainbow 3s linear infinite;
    }}
    
    /* Enhanced glassmorphism effects */
    .glass-effect {{
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 
            0 8px 32px rgba(0, 0, 0, 0.1),
            inset 0 1px 0 rgba(255, 255, 255, 0.2);
    }}
    
    /* Floating animation for interactive elements */
    @keyframes floating {{
        0%, 100% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-10px); }}
    }}
    
    .floating {{
        animation: floating 3s ease-in-out infinite;
    }}
</style>
""", unsafe_allow_html=True)

PROFILE = {
    "name": "Sahel Azzam",
    "role": "IT & Automation Engineer",
    "qualification": "M.S. in Computer Science, Texas Tech University — completed",
    "location": "Amman, Jordan",
    "email": "saazzam@ttu.edu",
    "linkedin": "https://www.linkedin.com/in/sahel-azzam-0a0670223",
    "github": "https://github.com/sahelmain",
}

# Curated source snapshots, reviewed on 2026-10-08. These are not live metrics.
PROJECTS = [
    {
        "name": "DriftWatch",
        "repo": "DriftWatch",
        "category": "Full-Stack Engineering",
        "languages": ["Python", "TypeScript"],
        "stack": "FastAPI · React · PostgreSQL · Celery · Redis · Docker",
        "description": (
            "LLM evaluation and drift-monitoring project with a FastAPI backend, "
            "React/TypeScript dashboard, persisted evaluation runs, and provider integrations."
        ),
        "implementation": (
            "The repository includes an evaluation engine, statistical drift comparisons, "
            "background-job configuration, API/SDK tests, and a CI workflow."
        ),
        "scope": "Engineering project; deployment configuration and tests are available in the repository.",
        "commit": "c714f205a62bbe03d06c60c076f6b87ef106b680",
        "date": "2026-04-25",
        "evidence": [
            ("API application", "backend/app/main.py"),
            ("Evaluation engine", "driftwatch/eval/engine.py"),
            ("Dashboard routes", "frontend/src/App.tsx"),
            ("CI workflow", ".github/workflows/ci.yml"),
        ],
    },
    {
        "name": "TruthfulQA LLM Evaluation Study",
        "repo": "llm-hallucination-phoenix",
        "category": "LLM Evaluation",
        "languages": ["Python"],
        "stack": "Python · Ollama · TruthfulQA · pandas · Phoenix",
        "description": (
            "Co-authored study of category-level hallucination patterns in local "
            "open-source LLMs, comparing models, prompt templates, and prompt clarity."
        ),
        "implementation": (
            "Experiment scripts, deterministic reference-scoring code, category-level "
            "analysis, a run manifest, saved results, and a report are checked in."
        ),
        "scope": (
            "Collaborative research project. Reported scores use a word-overlap reference "
            "heuristic; interpret them within that scoring method."
        ),
        "commit": "e820cd473d9afc74ca50d44205f717e44c71d37d",
        "date": "2026-04-24",
        "evidence": [
            ("Experiment configuration", "config/experiment.yaml"),
            ("Experiment runner", "src/run_experiment.py"),
            ("Scoring and metrics", "src/evaluate_metrics.py"),
            ("Run manifest", "data/run_manifest_worddet_latest_19608.json"),
        ],
    },
    {
        "name": "AI vs Human Text Detection — Deep Learning",
        "repo": "AI-Human-Text-Detection-Deep-Learning",
        "category": "Deep Learning",
        "languages": ["Python"],
        "stack": "PyTorch · CNN/LSTM/RNN · NLTK · Streamlit",
        "description": (
            "Text-classification project comparing CNN, LSTM, and RNN models, "
            "with token-sequence preprocessing and a Streamlit interface."
        ),
        "implementation": (
            "Includes model definitions, training/evaluation code, saved notebook outputs, "
            "model artifacts, and application code for model comparison and document input."
        ),
        "scope": "Academic project; accuracy depends on the dataset and evaluation procedure.",
        "commit": "7d2638fe854a1e47e5e2b7b12f3d306b86237032",
        "date": "2025-07-12",
        "evidence": [
            ("Training notebook", "Project2_Deep_Learning_Models.ipynb"),
            ("Model and inference helpers", "utils.py"),
            ("Streamlit application", "streamlit_app.py"),
        ],
    },
    {
        "name": "Text Classification ML Pipelines",
        "repo": "Advanced-Text-Classification-ML-Pipelines",
        "category": "Machine Learning",
        "languages": ["Python"],
        "stack": "scikit-learn · TF-IDF · SVM · GridSearchCV · pandas",
        "description": (
            "Notebook-based text-classification experiments with preprocessing pipelines, "
            "TF-IDF features, SVM and decision-tree models, and hyperparameter search."
        ),
        "implementation": (
            "Includes custom transformers, cross-validation, voting/stacking experiments, "
            "statistical comparisons, and prediction exports."
        ),
        "scope": "Academic project; saved scores describe individual notebook experiments.",
        "commit": "f02c8f60c6f429eb8b0e071ac9120204350a70ab",
        "date": "2025-06-21",
        "evidence": [
            ("Pipeline notebook", "advanced_text_classification_ml_pipelines.ipynb"),
            ("Prediction export", "data/predictions/Sahel_Azzam_assignment2_predictions.csv"),
        ],
    },
    {
        "name": "Streaming Pattern Matching",
        "repo": "streaming-pattern-matching-optimization",
        "category": "Algorithms",
        "languages": ["Python"],
        "stack": "Python · Naive/KMP algorithms · pandas · matplotlib",
        "description": (
            "Implementation and comparison of Naive and KMP pattern matching on "
            "simulated character streams and sequences derived from network-flow data."
        ),
        "implementation": (
            "Includes comparison counters, timing experiments, CSV results, and "
            "visualization scripts for investigating algorithm behavior."
        ),
        "scope": "Academic algorithm study; measured speedups vary by workload and implementation.",
        "commit": "ba62257f551e6e893c6249995e47b80591347c2b",
        "date": "2025-07-12",
        "evidence": [
            ("Streaming algorithms", "functions.py"),
            ("Experiment driver", "main.py"),
            ("Performance summary", "analysis/algorithm_performance_summary.csv"),
        ],
    },
    {
        "name": "Heartbeat Protocol Simulation",
        "repo": "csim-heartbeat-protocol",
        "category": "Systems",
        "languages": ["C", "Python"],
        "stack": "C · CSIM · Hello/Hello_Ack · Python visualization",
        "description": (
            "Discrete-event simulation of node communication using Hello/Hello_Ack "
            "messages, acknowledgement handling, timeouts, retries, and packet loss."
        ),
        "implementation": (
            "Includes a CSIM implementation, local mock implementation, Makefile, "
            "test scripts, and performance-visualization code."
        ),
        "scope": "Academic systems project; simulated behavior rather than a deployed network service.",
        "commit": "7a46c2a6faa7467bbb905a6c45fa4195ca030dc8",
        "date": "2025-07-24",
        "evidence": [
            ("CSIM implementation", "proj2_azzam_sahel.c"),
            ("Local mock implementation", "local.c"),
            ("Build targets", "Makefile"),
        ],
    },
]


def repository_url(project):
    return f"{PROFILE['github']}/{project['repo']}"


def evidence_links(project):
    base = f"{repository_url(project)}/blob/{project['commit']}"
    return " · ".join(
        f"[{label}]({base}/{path})" for label, path in project["evidence"]
    )


def show_section(section):
    return page in (section, "🌟 All Sections")


# Keep the existing theme toggle and visual design.
st.sidebar.markdown("---")
if st.sidebar.button(
    "🌙 Toggle Dark Mode" if not st.session_state.dark_mode else "☀️ Toggle Light Mode",
    use_container_width=True,
):
    st.session_state.dark_mode = not st.session_state.dark_mode
    st.rerun()

st.sidebar.title(PROFILE["name"])
st.sidebar.write(PROFILE["role"])
st.sidebar.caption(PROFILE["qualification"])
st.sidebar.caption(PROFILE["location"])
page = st.sidebar.selectbox(
    "📌 Choose Section",
    [
        "🏠 Home", "👨‍💻 About Me", "💼 Experience", "🤖 AI & Automation",
        "🚀 Projects", "📊 Technical Skills", "📝 Engineering Notes",
        "📞 Contact", "🌟 All Sections",
    ],
    index=0,
)
st.sidebar.markdown(f"**{len(PROJECTS)} selected public projects**")
st.sidebar.markdown(f"[GitHub]({PROFILE['github']}) · [LinkedIn]({PROFILE['linkedin']})")

if show_section("🏠 Home"):
    st.markdown(f"""
    <div class="hero-section">
        <div class="hero-content">
            <h1 class="hero-title">{html.escape(PROFILE['name'])}</h1>
            <p class="hero-subtitle">{html.escape(PROFILE['role'])}</p>
            <p>{html.escape(PROFILE['qualification'])}</p>
            <p>Software engineering, applied AI, and industrial automation</p>
            <div class="contact-badges">
                <a href="{PROFILE['github']}" class="contact-badge" target="_blank" rel="noopener noreferrer">GitHub</a>
                <a href="{PROFILE['linkedin']}" class="contact-badge" target="_blank" rel="noopener noreferrer">LinkedIn</a>
                <span class="contact-badge">📍 {html.escape(PROFILE['location'])}</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.write(
        "I am an IT & Automation Engineer based in Amman, Jordan, with a completed "
        "M.S. in Computer Science from Texas Tech University. My work combines "
        "industrial automation with software integration. My public projects cover "
        "web applications, LLM evaluation, machine learning, algorithms, and systems."
    )
    st.markdown("**Professional focus:** software engineering, AI engineering, and automation opportunities.")

if show_section("👨‍💻 About Me"):
    st.header("👨‍💻 About Me")
    st.subheader("Completed qualifications")
    st.markdown(
        "- **M.S. in Computer Science — Texas Tech University, completed**\n"
        "- **B.S. in Computer Science — Texas Tech University, completed**"
    )
    st.write(
        "I bring a computer-science background and practical experience with "
        "PLC/SCADA integration, plant data, and frontend development. I am interested "
        "in roles that connect software, data, and reliable operational workflows."
    )
    st.markdown(f"**Based in:** {PROFILE['location']}")

if show_section("💼 Experience"):
    st.header("💼 Engineering Experience")
    st.subheader("IT & Automation Engineer — Amman, Jordan")
    st.markdown(
        "- Work on plant digitalization through Ignition SCADA and PLC integration.\n"
        "- Experience with Siemens S7-1200 and S7-200 SMART PLCs, tag mapping, "
        "Modbus communication, and monitoring/control workflows.\n"
        "- Troubleshoot PLC/SCADA communication and OT network issues; support "
        "plant data visibility and operating workflows."
    )
    st.subheader("Frontend Internship — June–August 2024")
    st.markdown(
        "- Worked on a React frontend redesign.\n"
        "- Used Axios to connect frontend components to REST APIs."
    )

if show_section("🤖 AI & Automation"):
    st.header("🤖 AI & Automation")
    st.subheader("Applied AI projects")
    st.write(
        "My public work includes LLM evaluation and drift monitoring, a co-authored "
        "TruthfulQA study, and AI-versus-human text-classification experiments. "
        "The project links provide implementation and evaluation details."
    )
    st.subheader("Industrial automation experience")
    st.write(
        "My professional experience includes PLC/SCADA integration using Ignition "
        "and Siemens PLCs, with work on tag mapping, Modbus communications, "
        "plant monitoring, and troubleshooting."
    )
    st.subheader("Engineering interests")
    st.write(
        "I am interested in applying software and AI to monitoring, diagnostics, "
        "and operational decision support."
    )

if show_section("🚀 Projects"):
    st.header("🚀 Selected Technical Projects")
    st.caption(
        "Source snapshots reviewed on 8 October 2026. Dates below identify the "
        "reviewed repository commits. Open GitHub for subsequent changes."
    )
    col1, col2 = st.columns(2)
    with col1:
        language = st.selectbox(
            "Filter by Language:",
            ["All"] + sorted({lang for project in PROJECTS for lang in project["languages"]}),
        )
    with col2:
        category = st.selectbox(
            "Filter by Category:",
            ["All"] + sorted({project["category"] for project in PROJECTS}),
        )
    selected = [
        project for project in PROJECTS
        if (language == "All" or language in project["languages"])
        and (category == "All" or category == project["category"])
    ]
    if not selected:
        st.info("No projects match both filters. Choose All to broaden the selection.")
    for project in selected:
        st.subheader(project["name"])
        st.caption(f"{project['category']} | {project['stack']}")
        st.write(project["description"])
        st.write(project["implementation"])
        st.caption(project["scope"])
        st.markdown(f"[View repository]({repository_url(project)})")
        st.markdown(evidence_links(project))
        st.caption(f"Reviewed commit: {project['date']} · {project['commit'][:7]}")
        st.divider()
    st.markdown(
        "**Related text-classification work:** "
        "[Streamlit ML app](https://github.com/sahelmain/AI-Human-Text-Detection-App) · "
        "[Baseline classification notebook](https://github.com/sahelmain/Text-Classification-Human-vs-AI-)"
    )
    st.markdown(f"[Browse all public repositories]({PROFILE['github']}?tab=repositories)")

if show_section("📊 Technical Skills"):
    st.header("📊 Technical Skills")
    rows = [
        {
            "Area": "Backend and web applications",
            "Tools": "Python, FastAPI, React, TypeScript, REST APIs, PostgreSQL",
            "Experience / project": "DriftWatch; React frontend internship",
        },
        {
            "Area": "AI and machine learning",
            "Tools": "PyTorch, scikit-learn, pandas, NLTK, Streamlit, Ollama",
            "Experience / project": "LLM evaluation; text-classification projects",
        },
        {
            "Area": "Industrial automation",
            "Tools": "Ignition, Siemens S7-1200 / S7-200 SMART, Modbus, PLC tags",
            "Experience / project": "IT & Automation Engineer",
        },
        {
            "Area": "Systems and engineering tooling",
            "Tools": "C, CSIM, Git, Docker, CI workflows, Python test suites",
            "Experience / project": "Heartbeat simulation; DriftWatch",
        },
    ]
    st.dataframe(pd.DataFrame(rows), hide_index=True, use_container_width=True)

if show_section("📝 Engineering Notes"):
    st.header("📝 Engineering Notes")
    st.subheader("Model evaluation")
    st.write(
        "Classification accuracy describes a model on a particular dataset and split. "
        "Text-detection projects require careful validation before use on new writing "
        "styles or model outputs. Project notebooks provide the experiment context."
    )
    st.subheader("Algorithm benchmarking")
    st.write(
        "Streaming pattern-matching experiments compare execution time and character "
        "comparisons across workloads. Benchmark results should be read alongside "
        "the implementation and input configuration."
    )
    st.subheader("LLM scoring")
    st.write(
        "The TruthfulQA study uses deterministic word-overlap reference scoring. "
        "That method defines the reported results and has limitations when answers "
        "use different wording. The scoring code and run manifest document the setup."
    )

if show_section("📞 Contact"):
    st.header("📞 Contact")
    st.write("Connect with me about software engineering, AI, or industrial automation opportunities.")
    st.markdown(
        f"- **LinkedIn:** [Sahel Azzam]({PROFILE['linkedin']})\n"
        f"- **GitHub:** [sahelmain]({PROFILE['github']})\n"
        f"- **Email:** [{PROFILE['email']}](mailto:{PROFILE['email']})\n"
        f"- **Location:** {PROFILE['location']}"
    )

st.divider()
st.caption(
    f"© {datetime.now().year} {PROFILE['name']} | {PROFILE['role']} | "
    f"M.S. Computer Science, Texas Tech University | {PROFILE['location']}"
)
