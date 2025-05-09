import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score

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
</style>
""", unsafe_allow_html=True)
    
    # .stMetric [data-testid="stMetricDelta"] {
    #     color: #dc2626 !important;  /* Red color for delta */
    #     font-size: 0.9rem !important;
    # }

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
        "⚙️ Feature Selection",
        "📈 EDA",
        "🔄 Machine Learning Pipeline",
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
            <h3 style="color: #3730a3; margin: 0;">👨 Total Students</h3>
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
        {"icon": "📚", "title": "Access to Books", 
         "content": "Fewer books of certain types don’t raise the likelihood of predicting a student as a repeater."},
        {"icon": "🎓", "title": "School Engagement", 
         "content": "A student's engagement in school plays a factor in repeating a grade."},
        {"icon": "💻", "title": "Digital Access and Usage", 
         "content": "Less access to digital tools as well as improper usage plays a factor in repeating a grade."},
        {"icon": "⏳", "title": "Learning Time", 
         "content": "More time spent learning leads to better performance and a lower chance of repeating a grade."},
        {"icon": "📅", "title": "School Absences", 
         "content": "Prolonged absence in school increases the chance of repeating a grade."},
        {"icon": "❤️", "title": "Sense of Belonging", 
         "content": "Increased feelings of safety and belongingness lower the chance of repeating a grade."},
        {"icon": "🧠", "title": "Student Curiosity and Engagement", 
         "content": "The more curious and engaged a student is, the lower the chance of repeating a grade."}
    ]
    
    # Create two rows of columns
    for i in range(2):
        cols = st.columns(3)
        for j in range(3):
            idx = i * 3 + j
            if idx >= len(findings):
                break
            finding = findings[idx]
            with cols[j]:
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
            st.metric(label = "Philippine Students", value = "7,193", delta = "1.17% of global dataset", delta_color="off")
            st.metric(label = "Grade Repetition Rate", value = "25.4%", delta = "+13.4% vs OECD average", delta_color="inverse")
        
        # Add bar chart comparing repetition rates
        fig, ax = plt.subplots()
        countries = ['Philippines', 'OECD Average']
        rates = [25.4, 12.0]
        ax.bar(countries, rates, color=['#4f46e5', '#a5b4fc'])
        ax.set_ylabel('Repetition Rate (%)')
        st.pyplot(fig)

# Combined Data Preparation & Feature Selection
elif menu == "⚙️ Feature Selection":
    st.header("Data Preparation & Feature Selection")
        
    with st.expander("🔧 Feature Engineering Process (Summary)", expanded=True):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("""
            **Original Features**: 1,278  
            **Final Features**: 90  
            
            **Feature Reduction**:
            - 863: High missing values (484 empty)
            - 55: Collinear features
            - 243: Irrelevant features
            - 33: Feature Engineering
            """)

        # with col2:
        #     st.image("images/0_Data_Prep_Funnel_Chart.png", 
        #             caption="Figure 1: Feature Engineering Funnel Chart",
        #             use_container_width=True)
        
        with col2:
            labels = ['Missing Values', 'Collinearity', 'Irrelevance', 'Feature Engineering', 'Retained']
            sizes = [863, 55, 243, 27, 90]
            colors = ['#ef4444', '#f59e0b', '#10b981', '#3b82f6', '#6366f1']
            
            fig, ax = plt.subplots()
            ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
                   startangle=90, wedgeprops={'edgecolor': 'white'})
            ax.axis('equal')
            st.pyplot(fig)

    with st.expander("🔧 Feature Engineering Process (Detailed)", expanded=True):
        col1, col2 = st.columns([3, 2])
        with col1:
            st.image("images/0_Data_Prep_Funnel_Chart.png", 
                    caption="Figure 1: Feature Engineering Funnel Chart",
                    use_container_width=True)
            
        with col2:
            st.markdown("""
            **Key Observations about the Dataset**:  
            The dataset initially contained **1,278 features**, but it underwent significant refinement to ensure quality and relevance.  
    
            - **863 features** were removed because they exceeded the **20% missing value threshold**, with **484 of these being completely empty**, rendering them unusable for analysis.  
            - An additional **55 features** were eliminated due to **collinearity**, as they provided redundant information.  
            - **243 features** were removed for being **irrelevant** to the study's objectives, streamlining the dataset further.  
            - **33 features**, which represented scores in **Math, Reading, and Science**, were consolidated into **two (2) representative features**, reducing dimensionality while preserving critical information.  
            - Finally, **4 new features** were added after applying **One Hot Encoding and VIF filtering**, enhancing the dataset's quality and utility.  
    
            By the end of this rigorous filtering process, the dataset was optimized for analysis, retaining only the **90** most meaningful and actionable features.  
            """)
    

# EDA Section
elif menu == "📈 EDA":
    st.header("Theme 1: Engagement in School", divider=True)
    
    # EDA Item 1.1
    with st.container():
        col1, col2 = st.columns([3, 2])
        with col1:
            st.image("images/1_EDA_Missed_School.png", 
                    caption="Figure 1: Grade Repetition of Students Missing School",
                    use_container_width=True)
        with col2:
            st.markdown("""
            **Absences**:  
            73% of Grade Repeaters have missed school for more than 3 months,
            indicating strong correlation between absences and chances of repeating a grade.
            """)
    
    st.divider()
    
    # EDA Item 1.2
    with st.container():
        col1, col2 = st.columns([2, 3])
        with col1:
            st.markdown("""
            **Experience in School**:  
            Grade Repeaters feel less safe, have a weaker sense of belonging, and experience more bullying in school.
            """)
        with col2:
            st.image("images/2_EDA_Safety_and_Belonging.png",
                    caption="Figure 2: Grade Repetition vs Safety and Belonging",
                    use_container_width=True)

    st.divider()

    # EDA Item 1.3
    with st.container():
        col1, col2 = st.columns([3, 2])
        with col1:
            st.image("images/3_EDA_Scores.png", 
                    caption="Figure 3: Performance on Standardized Exams",
                    use_container_width=True)
        with col2:
            st.markdown("""
            **Standardized Testing**:  
            Grade Repeaters perform below average PISA scores for Mathematics, Reading and Science.
            """)

    st.header("Theme 2: Socioeconomic Profile", divider=True)
    
    # EDA Item 2.1
    with st.container():
        col1, col2 = st.columns([3, 2])
        with col1:
            st.markdown("""
            **Parental Education**:  
            A large proportion of Repeaters have parents with higher levels of education.
            """)
        with col2:
            st.image("images/4_EDA_2_Parental_Education.png", 
                    caption="Figure 4: Grade Repetition vs Parental Education",
                    use_container_width=True)
    
    st.divider()
    
    # EDA Item 2.2
    with st.container():
        col1, col2 = st.columns([2, 3])
        with col1:
            st.image("images/5_EDA_2_Support.png",
                    caption="Figure 5: Grade Repetition vs Support Received",
                    use_container_width=True)
        with col2:
            st.markdown("""
            **Familial and Teacher Support**:  
            Grade Repeaters generally receive less frequent support from their family.
            """)

    st.header("Theme 3: Digital Learning and Access", divider=True)
    
    # EDA Item 3.1
    with st.container():
        col1, col2 = st.columns([3, 2])
        with col1:
            st.markdown("""
            **ICT Resources**:  
            Grade Repeaters report lower digital access at home.
            """)
        with col2:
            st.image("images/6_EDA_3_Digital_Access.png", 
                    caption="Figure 6: Grade Repetition vs digital resource availability",
                    use_container_width=True)
    
if menu == "🔄 Machine Learning Pipeline":
    st.header("Machine Learning Pipeline")
    
    # Title block with image
    st.image("images/7_MS_Pipeline.png", 
            caption="Figure 1: Machine Learning Pipeline",
            use_container_width=True)
    
    with st.expander("📊 Baseline Results", expanded=True):
        st.subheader("Model Performance Comparison (Baseline)")
        
        # Create a table of baseline results
        st.markdown("### Baseline Metrics")
        
        # Example baseline metrics (replace with your actual results)
        baseline_results = {
            "Metric": ["Train Recall", "Validation Recall", "Holdout Recall"],
            "Decision Tree": ['100%', '55.05%', '64.20%'],
            "Random Forest": ['100%', '59.63%', '55.80%'],
            "Gradient Boosting": ['69.14%', '62.68%', '58.93%'],
            "AdaBoost": ['86.38%', '63.64%', '58.71%'],
            "XGBoost": ['87.59%', '61.65%', '67.16%'],
            "CatBoost": ['88.45%', '61.72%', '67.16%'],
        }
        
        # Create a DataFrame for the table
        df = pd.DataFrame(baseline_results).set_index("Metric")
        
        # Display the table
        st.table(df)
        
        # Add interpretation of results
        st.markdown("""
        ### Key Observations:
        - To be filled
        - To be filled
        - To be filled
        - To be filled
        """)

    
elif menu == "🤖 Final Model":
    st.header("Grade Repetition Predictor")

    # Debugging: Show section is loading
    st.write("Section initialization started...")

    # Import necessary functions
    from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
    import os
    import pickle
    import pandas as pd

    # Load model and data with enhanced debugging
    @st.cache_resource
    def load_model():
        try:
            st.write("Attempting model load...")
            model_path = os.path.join("scripts", "gb_tk_cat.pkl")
            with open(model_path, 'rb') as f:
                model = pickle.load(f)
            st.write("Model loaded successfully!")
            return model
        except Exception as e:
            st.error(f"Model loading failed: {str(e)}")
            return None

    @st.cache_data
    def load_holdout():
        try:
            st.write("Attempting holdout data load...")
            data_path = os.path.join("data", "holdout.csv")
            df = pd.read_csv(data_path)
            st.write(f"Data loaded successfully! Shape: {df.shape}")
            return df
        except Exception as e:
            st.error(f"Data loading failed: {str(e)}")
            return None

    # Load resources with progress indicators
    with st.spinner("Loading resources..."):
        model = load_model()
        holdout_data = load_holdout()

    # if model is None or holdout_data is None:
    #     st.error("Critical resources failed to load. Stopping execution.")
    #     st.stop()

    # Debugging: Show data overview
    st.header("Holdout Data Preview")
    st.write(holdout_data.head(5))
    
    # Column exploration section
    with st.container():
        st.write("Explore the features in the holdout dataset:")
        
        # Display column names with checkboxes
        col1, col2 = st.columns([2, 3])
        
        with col1:
            st.write("### Feature Browser")
            columns = holdout_data.columns.tolist()
            selected_columns = st.multiselect(
                "Select features to display",
                options=columns,
                default=columns[:5]  # Show first 5 columns by default
            )
        
        with col2:
            st.write("### Feature Data Preview")
            if selected_columns:
                st.dataframe(
                    holdout_data[selected_columns].head(),
                    use_container_width=True,
                    height=300
                )
            else:
                st.warning("No features selected. Please choose features to view data.")
        
        # Display summary statistics
        st.write("### Summary Statistics")
        summary_stats = holdout_data[selected_columns].describe()
        st.dataframe(
            summary_stats.T,
            use_container_width=True
        )

    try:
        st.write("Preparing holdout data...")
        if "REPEAT" not in holdout_data.columns:
            raise KeyError("REPEAT column not found in holdout data")
            
        X_holdout = holdout_data.drop("REPEAT", axis=1)
        y_true = holdout_data["REPEAT"]
        
        st.write("Generating predictions...")
        y_pred = model.predict(X_holdout)
        
        # Create columns for metrics
        st.write("Model Performance Metrics:")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            precision = precision_score(y_true, y_pred)
            st.metric("Precision", f"{precision:.2f}")
        
        with col2:
            f1 = f1_score(y_true, y_pred)
            st.metric("F1 Score", f"{f1:.2f}")
        
        with col3:
            roc_auc = roc_auc_score(y_true, y_pred)
            st.metric("ROC AUC", f"{roc_auc:.2f}")
            
    except Exception as e:
        st.error(f"Error calculating model performance: {e}")
        st.stop()

    st.success("Model performance metrics loaded successfully!")

    # # Prediction form
    # with st.form("prediction_form"):
    #     st.subheader("Predict Student Risk")
        
    #     # Example features - modify based on your actual model features
    #     col1, col2 = st.columns(2)
    #     with col1:
    #         escs = st.number_input("Economic/Social/Cultural Status", -3.0, 3.0, 0.0)
    #         st004d01t = st.selectbox("Gender", ["Female", "Male"])
            
    #     with col2:
    #         lmins = st.number_input("Learning Minutes", 0, 500, 180)
    #         hisei = st.number_input("Highest Parent Education (Years)", 0, 20, 12)

    #     if st.form_submit_button("Generate Prediction"):
    #         # Create input DataFrame matching model expectations
    #         input_df = pd.DataFrame({
    #             "ESCS": [escs],
    #             "ST004D01T": [1 if st004d01t == "Male" else 0],
    #             "LMINS": [lmins],
    #             "HISEI": [hisei]
    #         })
            
    #         prediction = model.predict_proba(input_df)[0][1]
            
    #         # Display results
    #         st.subheader("Prediction Results")
    #         st.metric("Grade Repetition Risk", 
    #                  f"{prediction:.1%}",
    #                  "High Risk" if prediction > 0.5 else "Low Risk")
            
    #         # Show feature importance using SHAP
    #         explainer = shap.TreeExplainer(model)
    #         shap_values = explainer.shap_values(input_df)
            
    #         fig, ax = plt.subplots()
    #         shap.plots.waterfall(shap_values[0], max_display=10, show=False)
    #         st.pyplot(fig)

# # For Recommender System
# elif menu == "🎯 Recommendations":
#     st.header("Personalized Recommendations")
    
#     # Add similar model loading and input processing
#     # Use feature importance from model to generate recommendations
#     # Example:
#     if 'prediction' in locals():
#         st.subheader("Recommended Interventions")
        
#         if prediction > 0.5:
#             st.markdown("""
#             - **Priority 1:** Improve digital access through school device loans
#             - **Priority 2:** Implement after-school tutoring program
#             - **Priority 3:** Parental education workshops
#             """)

# Add other sections following similar patterns

# Footer
st.markdown("""
<div style="margin-top: 50px; padding: 20px 0; border-top: 1px solid #e5e7eb; text-align: center; color: #6b7280;">
    © 2023 PISA Philippines Analysis Team | 
    <a href="#" style="color: #4f46e5; text-decoration: none;">GitHub</a> | 
    <a href="#" style="color: #4f46e5; text-decoration: none;">Contact</a>
</div>
""", unsafe_allow_html=True)
