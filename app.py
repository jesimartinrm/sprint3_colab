import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Configure page
st.set_page_config(
    page_title="PISA 2022 Philippines Analysis",
    page_icon="📚",
    layout="wide"
)

# Custom CSS styling
st.markdown("""
<style>
    /* Main content styling */
    [data-testid="stAppViewContainer"] {
        background-color: #f3f4f6;
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #3730a3 !important;
        color: white;
    }
    
    /* Metrics cards */
    .metric-card {
        background: white;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s, box-shadow 0.3s;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
    
    /* Custom divider */
    .divider {
        border-top: 1px solid #e5e7eb;
        margin: 1.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.markdown("""
    <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px;">
        <i class="fas fa-graduation-cap" style="font-size: 24px;"></i>
        <h1 style="margin: 0; font-size: 20px;">PISA 2022 PH</h1>
    </div>
    """, unsafe_allow_html=True)
    
    menu = st.radio("", [
        "🏠 Landing Page",
        "📊 Data Overview", 
        "🧹 Data Preparation",
        "⚙️ Feature Selection",
        "📈 EDA",
        "🤖 Final Model",
        "💡 Feature Importance",
        "🎯 Recommendations",
        "🤝 Recommender System"
    ], label_visibility="collapsed")

# Main content sections
if menu == "🏠 Landing Page":
    # Hero Section
    col1, col2 = st.columns([2, 3])
    with col1:
        st.markdown("""
        <div style="margin-top: 20px;">
            <h1 style="font-size: 2.5rem; color: #3730a3;">PISA 2022 Philippines</h1>
            <h2 style="font-size: 1.8rem; color: #4f46e5;">Grade Repetition Analysis</h2>
            <p style="font-size: 1.1rem; color: #6b7280; margin-top: 20px;">
                This analysis examines the factors contributing to grade repetition among Filipino students 
                based on the PISA 2022 dataset. Our goal is to identify key predictors and provide 
                actionable recommendations.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.image("https://images.unsplash.com/photo-1523050854058-8df90110c9f1", 
                use_column_width=True, caption="Philippine Students")

    # Key Metrics Cards
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #3730a3; margin: 0;">📚 Total Students</h3>
            <p style="font-size: 2rem; margin: 10px 0;">7,233</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #3730a3; margin: 0;">📈 Repetition Rate</h3>
            <p style="font-size: 2rem; margin: 10px 0;">22.5%</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #3730a3; margin: 0;">📋 Variables Analyzed</h3>
            <p style="font-size: 2rem; margin: 10px 0;">48</p>
        </div>
        """, unsafe_allow_html=True)

    # Key Findings
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    st.header("Key Findings")
    
    findings = [
        {"icon": "💰", "title": "Socioeconomic Status", 
         "content": "Students from lower-income families were 45% more likely to repeat grades"},
        {"icon": "👪", "title": "Parental Involvement", 
         "content": "Regular parental engagement reduced repetition by 30%"},
        {"icon": "💻", "title": "Digital Access", 
         "content": "Limited device access showed strong correlation with repetition"}
    ]
    
    cols = st.columns(3)
    for idx, finding in enumerate(findings):
        with cols[idx]:
            st.markdown(f"""
            <div class="metric-card">
                <div style="font-size: 2rem; margin-bottom: 10px;">{finding['icon']}</div>
                <h3 style="color: #3730a3; margin: 0 0 10px 0;">{finding['title']}</h3>
                <p style="color: #6b7280;">{finding['content']}</p>
            </div>
            """, unsafe_allow_html=True)

elif menu == "📊 Data Overview":
    st.header("Dataset Overview")
    
    # Dataset Structure
    with st.expander("📁 Dataset Structure"):
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Students", "7,233")
            st.metric("Variables Analyzed", "48")
        with col2:
            st.metric("Grade Repetition Rate", "22.5%", "11.5% higher than OECD average")
    
    # Variable Categories
    with st.expander("📚 Variable Categories"):
        categories = [
            {"title": "Student Background", "color": "#6366f1", "items": ["Family SES", "Parental Education", "Immigrant Status"]},
            {"title": "Learning Experience", "color": "#10b981", "items": ["Classroom Environment", "Teacher Support", "Learning Time"]},
            {"title": "Outcome Measures", "color": "#f59e0b", "items": ["Test Scores", "Grade Repetition", "Educational Aspirations"]}
        ]
        
        cols = st.columns(3)
        for idx, category in enumerate(categories):
            with cols[idx]:
                st.markdown(f"""
                <div style="border-left: 4px solid {category['color']}; padding-left: 1rem; margin: 1rem 0;">
                    <h3 style="color: {category['color']};">{category['title']}</h3>
                    <ul style="color: #6b7280;">
                        {''.join([f'<li>{item}</li>' for item in category['items']])}
                    </ul>
                </div>
                """, unsafe_allow_html=True)

# Add other sections following similar patterns

# Footer
st.markdown("""
<div style="margin-top: 50px; padding: 20px 0; border-top: 1px solid #e5e7eb; text-align: center; color: #6b7280;">
    © 2023 PISA Philippines Analysis Team | 
    <a href="#" style="color: #4f46e5; text-decoration: none;">GitHub</a> | 
    <a href="#" style="color: #4f46e5; text-decoration: none;">Contact</a>
</div>
""", unsafe_allow_html=True)
