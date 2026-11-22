
# 🧠 Mental Tiredness Prediction

### Machine Learning-Based Mental Tiredness Score Prediction

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python" />
  <img src="https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange" />
  <img src="https://img.shields.io/badge/Framework-Streamlit-red?logo=streamlit" />
  <img src="https://img.shields.io/badge/Status-Deployed-success" />
</p>

<p align="center">
  <b>An end-to-end Machine Learning project to predict mental tiredness scores using lifestyle and work-related factors.</b>
</p>

---

## 🌐 Live Application

🚀 **Try the application here:**

[Mental Tiredness Prediction – Streamlit App](https://mental-tiredness-prediction-kbzdnfgvhheznilqyzdsbf.streamlit.app/)

📂 **GitHub Repository:**

[View Project on GitHub](https://github.com/Bidyashreepanda/Mental-Tiredness-Prediction)

---

## 📌 Project Overview

Mental Tiredness Prediction is a Machine Learning regression project that predicts an individual's mental tiredness score based on lifestyle, sleep patterns, screen time, hydration, caffeine intake, mood, and work-related factors.

The project follows a structured **4-Sprint Machine Learning Development Methodology**, covering the complete ML lifecycle from data understanding to deployment and basic MLOps implementation.

The final trained model is integrated into an interactive Streamlit web application where users can enter their details and receive a predicted mental tiredness score.

---

## ❗ Problem Statement

Mental tiredness can affect an individual's concentration, productivity, decision-making, and overall daily performance.

Factors such as insufficient sleep, excessive screen time, inadequate hydration, caffeine consumption, mood, and work environment may contribute to mental fatigue.

Identifying potential patterns associated with mental tiredness using lifestyle and work-related information can help individuals become more aware of their daily habits.

The objective of this project is to develop a **Machine Learning-Based Mental Tiredness Prediction System** that analyzes relevant lifestyle and work-related inputs to predict a mental tiredness score.

The system uses a trained Random Forest Regression model and provides predictions through an interactive Streamlit web application.

**Expected Outcome:** A user-friendly application that predicts a mental tiredness score based on user inputs and demonstrates an end-to-end Machine Learning workflow.

*Note: This project is for educational and awareness purposes only. Predictions are estimates and are not a medical diagnosis.*

---

## 🎯 Project Objectives

- Understand and analyze the dataset.
- Perform data cleaning and preprocessing.
- Conduct Exploratory Data Analysis (EDA).
- Identify important patterns and relationships.
- Build multiple Machine Learning regression models.
- Evaluate models using regression metrics.
- Optimize the best-performing model.
- Save and reuse the trained ML pipeline.
- Develop an interactive Streamlit application.
- Deploy the application online.
- Implement basic experiment tracking and prediction monitoring.

---

## 🛠️ Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Manipulation | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Model Serialization | Joblib |
| Web Application | Streamlit |
| Development Environment | Jupyter Notebook, VS Code |
| Version Control | Git, GitHub |
| Deployment | Streamlit Community Cloud |
| MLOps | Experiment Tracking, Logging, Prediction Monitoring |

---

## 📊 Dataset Description

**Dataset:** `mental_tiredness_score_prediction_dataset.csv.csv`

The dataset contains lifestyle and work-related information used to predict the target variable:

**Target Variable:** `mental_tiredness_score`

Example input features include:

- Sleep hours
- Screen time (minutes)
- Hydration (litres)
- Caffeine intake (mg)
- Deep sleep percentage
- Mood
- Work environment
- Work type

The dataset is used for data preprocessing, exploratory analysis, model training, and evaluation.

---

## 🔄 Project Workflow – 4 Sprints

### 🟢 Sprint 1: Data Understanding & Preprocessing

- Dataset loading and inspection.
- Understanding rows, columns, and data types.
- Checking missing values and duplicate records.
- Exploratory Data Analysis (EDA).
- Data visualization and correlation analysis.
- Outlier analysis and treatment.
- Categorical encoding and feature scaling.
- Train-test split.

### 🔵 Sprint 2: Model Building & Evaluation

Implemented and evaluated multiple regression algorithms:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor

Evaluation metrics:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

### 🟣 Sprint 3: Optimization & Final Model

- Hyperparameter tuning.
- Cross-validation.
- Model performance comparison.
- Best model selection.
- Final model evaluation.
- Model serialization using Joblib.

**Final Model:** Random Forest Regression Pipeline.

### 🟠 Sprint 4: Deployment & MLOps

- Created an interactive Streamlit application.
- Integrated the trained ML model.
- Implemented input validation.
- Added logging functionality.
- Implemented basic experiment tracking.
- Implemented prediction activity monitoring.
- Managed source code using Git and GitHub.
- Deployed the application using Streamlit Community Cloud.

---

## 🏗️ Project Architecture

```text
User Input
    |
    v
Streamlit Web Application
    |
    v
Input Validation
    |
    v
Prediction Module
    |
    v
Trained Random Forest Pipeline
    |
    v
Predicted Mental Tiredness Score
    |
    v
Display Prediction to User
    |
    v
Logging & Prediction Monitoring
```

---

## 📁 Project Structure

```text
Mental_Triedness_Prediction/
│
├── data/
│
├── models/
│   └── mental_tiredness_model.joblib
│
├── notebooks/
│
├── src/
│   ├── __init__.py
│   ├── logger.py
│   ├── predict.py
│   ├── validation.py
│   ├── experiment_tracker.py
│   └── monitor.py
│
├── experiments/
│   └── experiment_tracking.csv
│
├── monitoring/
│   └── prediction_monitoring.csv
│
├── logs/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📈 Model Evaluation

The project evaluates regression models using the following performance metrics:

| Metric | Description |
|---|---|
| MAE | Measures average absolute prediction error |
| MSE | Measures average squared prediction error |
| RMSE | Measures the square root of average squared error |
| R² Score | Measures how well the model explains target variability |

The Random Forest Regression pipeline was selected as the final model after model comparison and optimization.

*Actual evaluation scores can be added here after verifying the final notebook results.*

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Bidyashreepanda/Mental-Tiredness-Prediction.git
```

### 2. Navigate to the Project Directory

```bash
cd Mental-Tiredness-Prediction
```

### 3. Create a Virtual Environment

```bash
python -m venv myenv
```

### 4. Activate the Virtual Environment

**Windows:**

```bash
myenv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## ⚙️ MLOps Implementation

Basic MLOps practices implemented in this project:

| Component | Implementation |
|---|---|
| Version Control | Git and GitHub |
| Model Serialization | Joblib |
| Experiment Tracking | CSV-based experiment records |
| Logging | Python logging module |
| Input Validation | Custom validation module |
| Prediction Monitoring | CSV-based prediction logs |
| Deployment | Streamlit Community Cloud |

These features help organize the project, record experiments, and maintain a history of predictions.

---

## 🔮 Future Enhancements

- Add advanced experiment tracking using MLflow.
- Implement data drift detection.
- Monitor model performance using actual observed outcomes.
- Improve model accuracy through additional feature engineering.
- Add interactive visualizations and prediction history.
- Automate model retraining.

---

## 👩‍💻 Author

**Bidyashree Panda**

- GitHub: [Bidyashreepanda](https://github.com/Bidyashreepanda)
- LinkedIn: [Bidyashree Panda](https://www.linkedin.com/in/bidyashree-panda/)

---

## ⭐ Acknowledgement

This project was developed as part of a structured Machine Learning learning and implementation process, covering data analysis, model development, optimization, deployment, and basic MLOps practices.

---

<p align="center">
  <b>Made with ❤️ using Python and Machine Learning</b>
</p>
