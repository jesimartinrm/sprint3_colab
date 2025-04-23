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

# Custom CSS styling with dark fonts
st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background-color: white;
        color: #333333;
    }
    
    section[data-testid="stSidebar"] {
        background-color: #3730a3 !important;
        color: white !important;
    }
    
    .metric-card {
        background: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #2d3748 !important;
    }
    
    p, li {
        color: #4a5568 !important;
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
            <p style="font-size: 2rem; margin: 10px 0;">25.4%</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3 style="color: #3730a3; margin: 0;">📋 Features Analyzed</h3>
            <p style="font-size: 2rem; margin: 10px 0;">90</p>
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

# Dataset Overview Section
elif menu == "📊 Data Overview":
    st.header("Dataset Overview")
    
    with st.expander("🌐 Dataset Structure", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **OECD PISA 2022 Student Questionnaire Dataset**
            - International standardized assessment measuring 15-year-old students' literacy
            - Covers reading, math, and science competencies
            - Global dataset: 613,744 students (80 countries)
            """)
            
        with col2:
            st.metric("Philippine Students", "7,193", "1.17% of global dataset")
            st.metric("Grade Repetition Rate", "25.4%", "+13.4% vs OECD average")
        
        # Add bar chart comparing repetition rates
        fig, ax = plt.subplots()
        countries = ['Philippines', 'OECD Average']
        rates = [25.4, 12.0]
        ax.bar(countries, rates, color=['#4f46e5', '#a5b4fc'])
        ax.set_ylabel('Repetition Rate (%)')
        st.pyplot(fig)

# Data Preparation Section
elif menu == "🧹 Data Preparation":
    st.header("Data Preparation Pipeline")
    
    with st.expander("📉 Feature Reduction Process", expanded=True):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("""
            **Original Features**: 1,278  
            **Final Features**: 90  
            
            **Removal Criteria**:
            - 863: Excessive missing values (484 completely empty)
            - 55: Collinearity issues
            - 242: Irrelevant to analysis
            - 10: Post-OHE removal
            """)
            
        with col2:
            # Create feature reduction pie chart
            labels = ['Missing Values', 'Collinearity', 'Irrelevance', 'Post-OHE', 'Retained']
            sizes = [863, 55, 242, 10, 90]
            colors = ['#ef4444', '#f59e0b', '#10b981', '#3b82f6', '#6366f1']
            
            fig, ax = plt.subplots()
            ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
                   startangle=90, wedgeprops={'edgecolor': 'white'})
            ax.axis('equal')
            st.pyplot(fig)

# Add other sections following similar patterns

# Footer
st.markdown("""
<div style="margin-top: 50px; padding: 20px 0; border-top: 1px solid #e5e7eb; text-align: center; color: #6b7280;">
    © 2023 PISA Philippines Analysis Team | 
    <a href="#" style="color: #4f46e5; text-decoration: none;">GitHub</a> | 
    <a href="#" style="color: #4f46e5; text-decoration: none;">Contact</a>
</div>
""", unsafe_allow_html=True)
