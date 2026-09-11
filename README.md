# Customer Churn Intelligence

An end-to-end Machine Learning project that predicts customer churn probability and provides actionable churn-risk insights through a Streamlit dashboard and FastAPI API.

## 📌 Project Overview

Customer Churn Intelligence is a Machine Learning project designed to predict whether a customer is likely to churn.

The project takes customer information as input and generates a churn prediction along with churn probability and risk level.

The system combines Machine Learning, FastAPI, and Streamlit to create a practical end-to-end ML application.

### Key Features

- Customer churn prediction
- Churn probability estimation
- Risk-level classification
- Interactive Streamlit dashboard
- FastAPI prediction API
- Machine Learning model
- Data analysis and visualization
- Feature engineering
- Git and GitHub version control

---

## 🎯 Business Problem

Customer churn is an important challenge for subscription-based businesses.

When customers leave a company, businesses may lose recurring revenue and customer lifetime value.

The objective of this project is to identify customers who may be at risk of leaving so that businesses can take proactive retention actions.

Instead of providing only a Churn / No Churn prediction, this system also provides:

- Churn probability
- Risk level
- Customer information
- Business-oriented risk message

This makes the Machine Learning prediction easier to understand and use for business decisions.

---

## 🤖 Machine Learning Approach

The project follows an end-to-end Machine Learning workflow.

### Workflow

1. Data Collection
2. Data Understanding
3. Data Cleaning
4. Exploratory Data Analysis
5. Feature Engineering
6. Model Training
7. Model Evaluation
8. Model Serialization
9. API Development
10. Dashboard Development

### Machine Learning Model

The current implementation uses:

**Logistic Regression**

The trained model is saved as:

```text
models/logistic_regression_churn_model.pkl
```

## 📊 Prediction Output

The application generates a customer churn prediction.

The prediction contains three important outputs:

### 1. Churn Prediction

The system predicts whether the customer is likely or unlikely to churn.

### 2. Churn Probability

The system provides the probability of customer churn as a percentage.

### 3. Risk Level

The churn probability is converted into a business-friendly risk category:

- 🟢 Low Risk
- 🟡 Moderate Risk
- 🔴 High Risk

### Example Prediction

```text
Churn Probability: 38.4%

Prediction: Customer is unlikely to churn

Risk Level: Moderate Risk
```

## 🖥️ Streamlit Dashboard

The project includes an interactive Streamlit dashboard for customer churn prediction.

Users can enter customer information and get a real-time prediction.

### Dashboard Features

- Customer information input
- Churn prediction
- Churn probability
- Risk level
- Customer details
- Easy-to-understand results

---

## 🗂️ Project Structure

```text
customer-churn-intelligence/
│
├── api/
│   └── app.py
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── raw/
│   │   └── Telco-Customer-Churn.csv
│   │
│   └── processed/
│       └── telco_customer_churn_processed.csv
│
├── models/
│   └── logistic_regression_churn_model.pkl
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_feature_engineering.ipynb
│   └── 04_modeling.ipynb
│
├── .gitignore
├── README.md
└── requirements.txt
```

## ⚡ FastAPI

The project includes a FastAPI-based REST API for customer churn prediction.

The API allows applications to send customer information and receive a churn prediction in real time.

### API Features

- Real-time customer churn prediction
- Churn probability
- Risk level assessment
- Structured JSON response
- Input validation using Pydantic
- Fast and lightweight REST API
- Interactive API documentation with Swagger UI

### Run the API

Start the FastAPI server using:

```bash
uvicorn api.app:app --reload
```
## 🗂️ Project Structure

The project is organized into separate folders for data, machine learning, API, dashboard, and notebooks.

```text
customer-churn-intelligence/
│
├── api/
│   └── app.py
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── raw/
│   │   └── Telco-Customer-Churn.csv
│   │
│   └── processed/
│       └── telco_customer_churn_processed.csv
│
├── models/
│   └── logistic_regression_churn_model.pkl
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_feature_engineering.ipynb
│   └── 04_modeling.ipynb
│
├── .gitignore
├── README.md
└── requirements.txt
```

## 🛠️ Technologies Used

The project uses the following technologies to build the complete Machine Learning application.

### Programming Language

- Python

### Data Analysis

- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn

### Machine Learning

- Scikit-learn
- Logistic Regression
- Joblib

### API Development

- FastAPI
- Pydantic
- Uvicorn

### Dashboard

- Streamlit

### Development & Version Control

- Jupyter Notebook
- VS Code
- Git
- GitHub

## 📦 Installation

Follow these steps to run the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/aashish-ml/customer-churn-intelligence.git
```

## ▶️ Run the Streamlit Dashboard

The Streamlit dashboard provides an interactive interface for customer churn prediction.

### Step 1: Make Sure the Virtual Environment Is Active

For Windows:

```bash
.venv\Scripts\activate
```

## 🚀 Run the FastAPI Server

FastAPI provides the backend API for real-time customer churn prediction.

### Step 1: Make Sure the Virtual Environment Is Active

For Windows:

```bash
.venv\Scripts\activate
```

## 🔍 Example Prediction

The application takes customer information as input and returns a churn prediction with probability and risk level.

### Example Customer Input

```text
Tenure: 12 months
Monthly Charges: $70.00
Total Charges: $840.00
```

## 💡 Business Value

Customer churn prediction can help businesses identify customers who may be at risk of leaving.

This project provides the following business benefits:

- 🎯 **Early Churn Detection**  
  Identify customers who are likely to churn before they leave.

- 💰 **Improve Customer Retention**  
  Help businesses take timely retention actions and reduce customer loss.

- 📊 **Data-Driven Decisions**  
  Use customer data and Machine Learning predictions to support business decisions.

- 🚨 **Risk Identification**  
  Categorize customers based on their churn probability and risk level.

- ⚡ **Real-Time Prediction**  
  The FastAPI backend allows churn predictions to be generated quickly.

- 🖥️ **Interactive Dashboard**  
  The Streamlit dashboard provides a simple interface for business users to enter customer information and view predictions.

- 📈 **Scalable Solution**  
  The project structure can be extended with additional customer features, improved models, and deployment options.

### Overall Impact

The Customer Churn Intelligence project demonstrates how Machine Learning can be used to transform customer data into actionable business insights and support customer retention strategies.


## 📈 Future Improvements

The project can be further improved with the following features:

- 🤖 **Advanced Machine Learning Models**  
  Experiment with XGBoost, Gradient Boosting, and other advanced models to improve prediction performance.

- 🔄 **Complete Feature Input**  
  Add customer demographic, contract, payment, internet service, and other relevant features to the prediction form.

- 🧩 **ML Pipeline**  
  Build a complete preprocessing and Machine Learning pipeline to handle data transformation and prediction consistently.

- 📊 **Advanced Dashboard Analytics**  
  Add customer churn trends, charts, filters, and detailed business insights to the Streamlit dashboard.

- 🎯 **Customer Segmentation**  
  Group customers based on their characteristics and churn risk.

- 🚀 **Cloud Deployment**  
  Deploy the FastAPI backend and Streamlit dashboard to a cloud platform for public access.

- 🔐 **API Security**  
  Add authentication and authorization to secure the prediction API.

- 📈 **Model Monitoring**  
  Monitor model performance and data changes after deployment.

- 🔁 **Model Retraining**  
  Add an automated process to retrain the model when new customer data becomes available.

### Future Goal

The ultimate goal is to transform this project into a production-ready Customer Churn Intelligence platform that helps businesses identify high-risk customers and improve customer retention.


## 👨‍💻 Author

# **Aashish**

AI/ML & Data Analytics Enthusiast

Interested in:
- Machine Learning
- Artificial Intelligence
- Data Analysis
- Python
- Business Intelligence
- Building real-world ML applications

### 🔗 GitHub

[Aashish's GitHub](https://reference-url-citation.invalid/0)

### 📌 Project Repository

[Customer Churn Intelligence](https://reference-url-citation.invalid/1)


## ⭐ Project Highlights

- 🤖 Built an end-to-end **Customer Churn Prediction** Machine Learning project.
- 📊 Performed **Exploratory Data Analysis (EDA)** to identify important churn patterns.
- 🧹 Cleaned and prepared customer data for Machine Learning.
- ⚙️ Applied **Feature Engineering** and categorical encoding.
- 🧠 Trained and compared **Logistic Regression** and **Random Forest** models.
- 📈 Achieved **0.840 ROC-AUC** with the selected Logistic Regression model.
- 💾 Saved the trained Machine Learning model using **Joblib**.
- 🚀 Developed a **FastAPI REST API** for real-time churn prediction.
- 🖥️ Built an interactive **Streamlit Dashboard** for customer churn analysis.
- 📊 Added **Churn Probability** and **Risk Level** to make predictions easier to understand.
- 🔗 Connected the Streamlit frontend with the FastAPI backend.
- 🧪 Tested API predictions using real customer input examples.
- 📦 Created a `requirements.txt` file for project dependencies.
- 🐙 Version-controlled the project using **Git and GitHub**.
- 📁 Organized the project using a professional, scalable folder structure.

### 🎯 Key Outcome

This project demonstrates the complete Machine Learning workflow — from **raw customer data to model training, API development, interactive dashboard, and GitHub deployment-ready project structure**.
