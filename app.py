
import sys
from pathlib import Path
import streamlit as st

# Add project root to Python path
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

# Import prediction and validation functions
from src.predict import predict_tiredness
from src.validation import validate_input

# Page configuration
st.set_page_config(
    page_title="Mental Tiredness Prediction",
    page_icon="🧠",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}

.main-title {
    text-align: center;
    color: #234b83;
    font-size: 36px;
    font-weight: bold;
}

.sub-title {
    text-align: center;
    color: #64748b;
    font-size: 17px;
}

.result-card {
    background-color: #e8f1ff;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    border: 1px solid #c5d9f5;
}

div.stButton > button {
    background-color: #234b83;
    color: white;
    width: 100%;
    border-radius: 10px;
    height: 48px;
    font-size: 17px;
}
</style>
""", unsafe_allow_html=True)

# Application heading
st.markdown(
    '<div class="main-title">🧠 Mental Tiredness Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Machine Learning Based Mental Tiredness Score Prediction</div>',
    unsafe_allow_html=True
)

st.divider()

st.write(
    "Enter your daily work habits, workload, sleep, "
    "and environmental details to estimate your mental tiredness score."
)

# Input form
with st.form("mental_tiredness_form"):

    st.subheader("📊 Workload Information")

    col1, col2 = st.columns(2)

    with col1:
        number_of_decisions_made = st.number_input(
            "Number of Decisions Made",
            min_value=0,
            value=0,
            step=1
        )

        context_switch_count = st.number_input(
            "Context Switch Count",
            min_value=0,
            value=0,
            step=1
        )

        notifications_received = st.number_input(
            "Notifications Received",
            min_value=0,
            value=0,
            step=1
        )

        screen_time_min = st.number_input(
            "Screen Time (Minutes)",
            min_value=0,
            value=120,
            step=10
        )

        deep_work_min = st.number_input(
            "Deep Work (Minutes)",
            min_value=0,
            value=60,
            step=10
        )

        task_complexity_avg = st.number_input(
            "Average Task Complexity",
            min_value=0.0,
            value=0.0,
            step=0.1
        )

        workload_score = st.number_input(
            "Workload Score",
            min_value=0.0,
            value=0.0,
            step=0.1
        )

    with col2:
        caffeine_mg = st.number_input(
            "Caffeine Intake (mg)",
            min_value=0,
            value=0,
            step=10
        )

        break_frequency = st.number_input(
            "Break Frequency",
            min_value=0,
            value=2,
            step=1
        )

        sleep_hours = st.number_input(
            "Sleep Hours",
            min_value=0.0,
            max_value=24.0,
            value=7.0,
            step=0.5
        )

        deep_sleep_pct = st.number_input(
            "Deep Sleep Percentage",
            min_value=0.0,
            max_value=100.0,
            value=20.0,
            step=1.0
        )

        hydration_l = st.number_input(
            "Hydration (Litres)",
            min_value=0.0,
            value=2.0,
            step=0.1
        )

        noise_level_db = st.number_input(
            "Noise Level (dB)",
            min_value=0.0,
            value=40.0,
            step=1.0
        )

        temperature_c = st.number_input(
            "Temperature (°C)",
            min_value=0.0,
            value=25.0,
            step=0.5
        )

    st.divider()

    st.subheader("😊 Personal & Environmental Information")

    col3, col4, col5 = st.columns(3)

    with col3:
        mood = st.selectbox(
            "Current Mood",
            ["Happy", "Low", "Neutral"]
        )

    with col4:
        work_environment = st.selectbox(
            "Work Environment",
            ["Moderate Noise", "Noisy", "Quiet"]
        )

    with col5:
        work_type = st.selectbox(
            "Work Type",
            ["Remote", "Office", "Manual", "Student"]
        )

    st.divider()

    submitted = st.form_submit_button(
        "🔍 Predict Mental Tiredness"
    )

# Prediction and validation
if submitted:

    input_data = {
        "number_of_decisions_made": number_of_decisions_made,
        "context_switch_count": context_switch_count,
        "notifications_received": notifications_received,
        "screen_time_min": screen_time_min,
        "deep_work_min": deep_work_min,
        "task_complexity_avg": task_complexity_avg,
        "caffeine_mg": caffeine_mg,
        "break_frequency": break_frequency,
        "sleep_hours": sleep_hours,
        "deep_sleep_pct": deep_sleep_pct,
        "hydration_l": hydration_l,
        "noise_level_db": noise_level_db,
        "temperature_c": temperature_c,
        "workload_score": workload_score,
        "mood": mood,
        "work_environment": work_environment,
        "work_type": work_type
    }

    # Validate input values
    errors = validate_input(input_data)

    if errors:

        st.error("Please correct the following input errors:")

        for error in errors:
            st.warning(error)

    else:

        try:
            prediction = predict_tiredness(input_data)

            st.divider()
            st.subheader("📈 Prediction Result")

            st.markdown(
                f"""
                <div class="result-card">
                    <h3>Predicted Mental Tiredness Score</h3>
                    <h1 style="color:#234b83;">
                        {prediction:.2f}
                    </h1>
                    <p>Predicted using the trained Random Forest model</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.success("Prediction generated successfully!")

            st.caption(
                "This is a machine learning estimate based on the "
                "provided dataset and is not a medical assessment."
            )

            with st.expander("View Submitted Input Data"):
                st.json(input_data)

        except Exception as e:

            st.error("Prediction failed. Please check the model and inputs.")
            st.exception(e)

# Footer
st.divider()

st.markdown(
    "<center>Developed using Python, Scikit-learn and Streamlit</center>",
    unsafe_allow_html=True
)
