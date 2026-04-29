# Student Performance and Outcome Analytics Platform

## Overview

The Student Performance and Outcome Analytics Platform is a data-driven system designed to analyze student academic and behavioral data to predict performance, identify at-risk students, and provide personalized recommendations.

This project uses Data Analytics, Machine Learning, and Natural Language Processing (NLP) to convert raw educational data into meaningful insights for improving student outcomes and supporting informed decision-making.

---

## Problem Statement

Traditional education systems rely on manual observation and past performance records, which:

* Are time-consuming and subjective
* Lack predictive capability
* Fail to identify at-risk students early

This results in delayed intervention and poor academic outcomes.

---

## Objectives

* Analyze student academic and behavioral data
* Predict student final performance
* Identify at-risk students early
* Provide personalized recommendations
* Enable data-driven decision making
* Visualize insights using dashboards

---

## Key Features

* Data Analysis and Exploratory Data Analysis (EDA)
* Machine Learning Model for performance prediction
* Early Warning System for risk detection
* Recommendation System for personalized guidance
* NLP-based insight generation
* What-If Analysis for scenario simulation
* Interactive dashboard using Power BI

---

## System Architecture

The system follows a pipeline-based workflow:

1. Data Collection
2. Data Storage (SQLite)
3. Data Preprocessing
4. Exploratory Data Analysis
5. Feature Selection
6. Model Training
7. Risk Detection
8. Recommendation Generation
9. Visualization Dashboard

---

## Technologies Used

### Programming and Libraries

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib

### Database

* SQLite

### Visualization

* Power BI

---

## Dataset Information

The dataset includes both academic and behavioral features such as:

* Grades (G1, G2, G3)
* Study time
* Absences
* Previous failures
* Family background
* Travel time

These features help in building accurate predictive models.

---

## Machine Learning Model

* Model Used: Linear Regression
* Target Variable: G3 (Final Grade)

### Evaluation Metrics

* Mean Squared Error (MSE)
* R-squared (R² Score)

---

## Early Warning System

Students are classified into three categories:

* Safe
* Need Attention
* High Risk

Classification is based on:

* Study time
* Absences
* Previous failures
* Initial performance (G1)

---

## Recommendation System

The system provides personalized recommendations such as:

* Increasing study time
* Improving attendance
* Focusing on weak subjects
* Seeking academic support

---

## What-If Analysis

This module allows simulation of different scenarios:

* Increasing study time
* Reducing absences

It helps in understanding how changes affect performance outcomes.

---

## Dashboard Features

* Grade distribution
* Absences vs performance
* Risk level classification
* Study time analysis
* Key performance indicators (KPIs)

---

## How to Run the Project

1. Clone the repository

```bash
git clone https://github.com/your-username/student-performance-analytics.git
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the project

```bash
python main.py
```

---

## System Requirements

### Minimum

* Intel i3 processor
* 4 GB RAM

### Recommended

* Intel i5 processor or above
* 8 GB RAM

---

## Benefits

### For Students

* Better understanding of performance
* Personalized feedback
* Improved study habits

### For Teachers

* Early identification of at-risk students
* Reduced manual workload
* Improved teaching strategies

### For Institutions

* Better decision-making
* Improved academic performance
* Adoption of data-driven education systems

---

## Future Scope

* Integration with real-time student data
* Use of advanced machine learning models
* Development of a web-based interface
* Real-time alert system
* Mobile application support

---

## License

This project is for academic purposes.

---

## Acknowledgement

Developed as part of B.Tech (CSE) under faculty supervision.

---

## Author

Harshita
B.Tech CSE
SAITM, Gurugram
