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
                use_container_width=True, caption="Philippine Students")

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
            labels = ['Missing Values', 'Collinearity', 'Irrelevance', 'Feature Engineering', 'Retained']
            sizes = [863, 55, 243, 27, 90]
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
                    use_container_width=True)
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
                    use_container_width=True)

elif menu == "🤖 Final Model":
    st.header("Grade Repetition Predictor")
    
    # Load model and data
    @st.cache_resource
    def load_model():
        import joblib
        import os
        model_path = os.path.join("scripts", "gb_tk_cat.pkl")
        return joblib.load(model_path)

    @st.cache_data
    def load_holdout():
        import os
        import pandas as pd
        data_path = os.path.join("data", "holdout.csv")
        return pd.read_csv(data_path)

    model = load_model()
    holdout_data = load_holdout()

    # Display model performance
    with st.expander("Model Performance on Holdout Data"):
        X_holdout = holdout_data.drop("REPEAT", axis=1)
        y_true = holdout_data["REPEAT"]
        y_pred = model.predict(X_holdout)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Accuracy", f"{accuracy_score(y_true, y_pred):.1%}")
        with col2:
            st.metric("F1 Score", f"{f1_score(y_true, y_pred):.2f}")
        with col3:
            st.metric("ROC AUC", f"{roc_auc_score(y_true, y_pred):.2f}")

    # Prediction form
    with st.form("prediction_form"):
        st.subheader("Predict Student Risk")
        
        # Example features - modify based on your actual model features
        col1, col2 = st.columns(2)
        with col1:
            escs = st.number_input("Economic/Social/Cultural Status", -3.0, 3.0, 0.0)
            st004d01t = st.selectbox("Gender", ["Female", "Male"])
            
        with col2:
            lmins = st.number_input("Learning Minutes", 0, 500, 180)
            hisei = st.number_input("Highest Parent Education (Years)", 0, 20, 12)

        if st.form_submit_button("Generate Prediction"):
            # Create input DataFrame matching model expectations
            input_df = pd.DataFrame({
                "ESCS": [escs],
                "ST004D01T": [1 if st004d01t == "Male" else 0],
                "LMINS": [lmins],
                "HISEI": [hisei]
            })
            
            prediction = model.predict_proba(input_df)[0][1]
            
            # Display results
            st.subheader("Prediction Results")
            st.metric("Grade Repetition Risk", 
                     f"{prediction:.1%}",
                     "High Risk" if prediction > 0.5 else "Low Risk")
            
            # Show feature importance using SHAP
            explainer = shap.TreeExplainer(model)
            shap_values = explainer.shap_values(input_df)
            
            fig, ax = plt.subplots()
            shap.plots.waterfall(shap_values[0], max_display=10, show=False)
            st.pyplot(fig)

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
