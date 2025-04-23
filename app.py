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
    [data-testid="stAppViewContainer"] {
        background-color: white;
        color: #333333;
    }
    
    section[data-testid="stSidebar"] {
        background-color: #3730a3 !important;
    }
    
    section[data-testid="stSidebar"] * {
        color: #ffffff !important;  /* White font for sidebar */
    }
    
    .metric-card {
        background: #f8f9fa;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    /* Custom metric styling */
    .stMetric [data-testid="stMetricLabel"] {
        color: #4b5563 !important;  /* Neutral dark for label */
    }
    
    .stMetric [data-testid="stMetricValue"] {
        color: #1f2937 !important;  /* Darker font for values */
        font-size: 1.5rem !important;
    }
    
    .stMetric [data-testid="stMetricDelta"] {
        color: #dc2626 !important;  /* Red color for delta */
        font-size: 0.9rem !important;
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
        "⚙️ Data Prep & Feature Selection",
        "📈 EDA",
        "🤖 Final Model",
        "💡 Feature Importance",
        "🎯 Recommendations"
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
            <p style="font-size: 2rem; margin: 10px 0;">7,193</p>
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

# Combined Data Preparation & Feature Selection
elif menu == "⚙️ Data Prep & Feature Selection":
    st.header("Data Preparation & Feature Selection")
    
    with st.expander("🔧 Feature Engineering Process", expanded=True):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("""
            **Original Features**: 1,278  
            **Final Features**: 90  
            
            **Feature Reduction**:
            - 863: High missing values (484 empty)
            - 55: Collinear features
            - 242: Irrelevant features
            - 10: Post-OHE removal
            """)
            
        with col2:
            labels = ['Missing Values', 'Collinearity', 'Irrelevance', 'Post-OHE', 'Retained']
            sizes = [863, 55, 242, 10, 90]
            colors = ['#ef4444', '#f59e0b', '#10b981', '#3b82f6', '#6366f1']
            
            fig, ax = plt.subplots()
            ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
                   startangle=90, wedgeprops={'edgecolor': 'white'})
            ax.axis('equal')
            st.pyplot(fig)

# EDA Section with New Format
elif menu == "📈 EDA":
    st.header("Exploratory Data Analysis")
    
    # Example EDA Item 1
    with st.container():
        col1, col2 = st.columns([3, 2])
        with col1:
            st.image("images/grade_repetition_distribution.png", 
                    caption="Figure 1: Grade Repetition Distribution",
                    use_column_width=True)
        with col2:
            st.markdown("""
            **Key Observation**:  
            25.4% of Filipino students reported repeating at least one grade,
            significantly higher than the OECD average of 11%. The distribution
            shows consistent patterns across different geographic regions.
            """)
    
    st.divider()
    
    # Example EDA Item 2
    with st.container():
        col1, col2 = st.columns([2, 3])
        with col1:
            st.markdown("""
            **SES vs Repetition Rate**:  
            Students from lower socioeconomic status (SES) families show
            3x higher repetition rates compared to high SES counterparts.
            """)
        with col2:
            st.image("images/ses_vs_repetition.png",
                    caption="Figure 2: Socioeconomic Status Impact",
                    use_column_width=True)

elif menu == "🤖 Final Model":
    st.header("Grade Repetition Predictor")
    
    # Load model
    @st.cache_resource
    def load_model():
        import joblib
        return joblib.load('grade_repetition_model.pkl')
    
    model = load_model()
    
    # Create input form
    with st.form("prediction_form"):
        st.subheader("Student Information")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            ses = st.slider("Socioeconomic Status (1-10)", 1, 10, 5)
            parent_edu = st.selectbox("Parental Education", ["High School", "College", "Postgrad"])
            
        with col2:
            digital_access = st.radio("Digital Access", ["None", "Limited", "Full"])
            books_in_home = st.number_input("Books in Home", 0, 500, 25)
            
        with col3:
            school_type = st.selectbox("School Type", ["Public", "Private"])
            study_time = st.slider("Daily Study Hours", 0.0, 8.0, 2.5)

        if st.form_submit_button("Predict Repetition Risk"):
            # Convert inputs to model format
            input_data = pd.DataFrame({
                'ses': [ses],
                'parent_edu': [parent_edu],
                'digital_access': [digital_access],
                'books_in_home': [books_in_home],
                'school_type': [school_type],
                'study_time': [study_time]
            })
            
            # Get prediction
            prediction = model.predict_proba(input_data)[0][1]
            risk_level = "High Risk" if prediction > 0.5 else "Low Risk"
            
            # Display results
            st.metric("Repetition Probability", f"{prediction:.1%}", risk_level)
            st.progress(prediction)

# For Recommender System
elif menu == "🎯 Recommendations":
    st.header("Personalized Recommendations")
    
    # Add similar model loading and input processing
    # Use feature importance from model to generate recommendations
    # Example:
    if 'prediction' in locals():
        st.subheader("Recommended Interventions")
        
        if prediction > 0.5:
            st.markdown("""
            - **Priority 1:** Improve digital access through school device loans
            - **Priority 2:** Implement after-school tutoring program
            - **Priority 3:** Parental education workshops
            """)

# Add other sections following similar patterns

# Footer
st.markdown("""
<div style="margin-top: 50px; padding: 20px 0; border-top: 1px solid #e5e7eb; text-align: center; color: #6b7280;">
    © 2023 PISA Philippines Analysis Team | 
    <a href="#" style="color: #4f46e5; text-decoration: none;">GitHub</a> | 
    <a href="#" style="color: #4f46e5; text-decoration: none;">Contact</a>
</div>
""", unsafe_allow_html=True)
