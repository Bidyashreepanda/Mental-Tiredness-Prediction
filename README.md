
# 🧠 Mental Tiredness Prediction

### Machine Learning-Based Mental Tiredness Score Prediction

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python" />
  <img src="https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange" />
  <img src="https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit" />
  <img src="https://img.shields.io/badge/Docker-Containerized-blue?logo=docker" />
  <img src="https://img.shields.io/badge/Deployment-Success-brightgreen" />
</p>

<p align="center">
  <b>An end-to-end Machine Learning project to predict mental tiredness scores using lifestyle and work-related factors.</b>
</p>

---

## 🌐 Live Application & Project Links

🚀 **Streamlit Application:**

https://mental-tiredness-prediction-kbzdnfgvhheznilqyzdsbf.streamlit.app/

📂 **GitHub Repository:**

https://github.com/Bidyashreepanda/Mental-Tiredness-Prediction

🐳 **Docker Hub Repository:**

https://hub.docker.com/r/bidyashree25/mental-tiredness-prediction

---

## 📌 Project Overview

Mental Tiredness Prediction is a Machine Learning regression project that predicts an individual's mental tiredness score based on lifestyle, sleep patterns, screen time, hydration, caffeine intake, mood, and work-related factors.

The project follows a structured **4-Sprint Machine Learning Development Methodology**, covering the complete ML lifecycle from data understanding and preprocessing to model development, optimization, deployment, and basic MLOps implementation.

The final trained Random Forest Regression pipeline is integrated into an interactive Streamlit web application and containerized using Docker.

---

## ❗ Problem Statement

Mental tiredness can affect an individual's concentration, productivity, decision-making, and overall daily performance.

Factors such as insufficient sleep, excessive screen time, inadequate hydration, caffeine consumption, mood, and work environment may contribute to mental fatigue.

Identifying patterns associated with mental tiredness using lifestyle and work-related information can help individuals become more aware of their daily habits.

The objective of this project is to develop a **Machine Learning-Based Mental Tiredness Prediction System** that analyzes relevant lifestyle and work-related inputs to predict a mental tiredness score.

The system uses a trained Random Forest Regression model and provides predictions through an interactive Streamlit web application.

**Expected Outcome:** A user-friendly application that predicts a mental tiredness score based on user inputs.

*Note: This project is intended for educational and awareness purposes. Predictions are estimates and are not a medical diagnosis.*

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
- Containerize the application using Docker.
- Publish the Docker image on Docker Hub.
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
| Containerization | Docker |
| Container Registry | Docker Hub |
| Deployment | Streamlit Community Cloud |
| MLOps | Logging, Experiment Tracking, Prediction Monitoring |

---

## 📊 Dataset Description

**Dataset:** `mental_tiredness_score_prediction_dataset.csv.csv`

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

The dataset is used for data preprocessing, exploratory data analysis, model training, and evaluation.

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

**Evaluation Metrics:**

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
- Containerized the application using Docker.
- Built and tested Docker images.
- Published the Docker image to Docker Hub.
- Pulled and ran the published image successfully.

---

## 🏗️ Project Architecture

```text
                 User
                   |
                   v
          Streamlit Application
                   |
                   v
             Input Validation
                   |
                   v
             Prediction Module
                   |
                   v
          Random Forest Pipeline
                   |
                   v
        Predicted Tiredness Score
                   |
                   v
          Logging and Monitoring
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
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📈 Model Evaluation

The project evaluates regression models using:

| Metric | Description |
|---|---|
| MAE | Measures average absolute prediction error |
| MSE | Measures average squared prediction error |
| RMSE | Measures the square root of average squared error |
| R² Score | Measures how well the model explains target variability |

The Random Forest Regression pipeline was selected as the final model after model comparison and optimization.

*Actual evaluation scores can be added after verifying the final notebook results.*

---

## 🚀 Streamlit Deployment

The application is deployed using Streamlit Community Cloud.

**Live Application:**

https://mental-tiredness-prediction-kbzdnfgvhheznilqyzdsbf.streamlit.app/

Users can enter relevant lifestyle and work-related information and receive a predicted mental tiredness score.

---

## 🐳 Docker Deployment

The application is containerized using Docker to make it easier to build, distribute, and run consistently across different environments.

### Docker Hub Image

**Repository:**

https://hub.docker.com/r/bidyashree25/mental-tiredness-prediction

**Image Name:**

`bidyashree25/mental-tiredness-prediction:latest`

### 1. Pull Docker Image

```bash
docker pull bidyashree25/mental-tiredness-prediction:latest
```

### 2. Run Docker Container

```bash
docker run -d --name mental-tiredness-app -p 8501:8501 bidyashree25/mental-tiredness-prediction:latest
```

### 3. Access the Application

Open the following address in your browser:

```text
http://localhost:8501
```

### 4. Check Running Containers

```bash
docker ps
```

### 5. View Container Logs

```bash
docker logs mental-tiredness-app
```

### 6. Stop the Container

```bash
docker stop mental-tiredness-app
```

### 7. Remove the Container

```bash
docker rm mental-tiredness-app
```

### Docker Configuration

The project includes:

- `Dockerfile` – Instructions for building the application image.
- `.dockerignore` – Excludes unnecessary files from the Docker build context.
- Docker image – Contains the application and its required dependencies.
- Docker container – Runs the Streamlit application.

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
| Containerization | Docker |
| Image Registry | Docker Hub |
| Deployment | Streamlit Community Cloud |

These implementations help organize the project, record experiment metadata, and maintain a history of predictions.

---

## 💻 Local Installation & Setup

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

### 4. Activate the Environment

**Windows:**

```bash
myenv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
streamlit run app.py
```

---

## 🔮 Future Enhancements

- Add advanced experiment tracking using MLflow.
- Implement data drift detection.
- Monitor model performance using actual observed outcomes.
- Improve model performance through additional feature engineering.
- Add interactive visualizations and prediction history.
- Automate model retraining.

---

## 👩‍💻 Author

**Bidyashree Panda**

- GitHub: https://github.com/Bidyashreepanda
- LinkedIn: https://www.linkedin.com/in/bidyashree-panda/

---

## ⭐ Acknowledgement

This project demonstrates an end-to-end Machine Learning workflow, including data analysis, preprocessing, model development, optimization, deployment, Docker containerization, and basic MLOps practices.

---

<p align="center">
  <b>Made with ❤️ using Python, Machine Learning, Streamlit, and Docker</b>
</p>

