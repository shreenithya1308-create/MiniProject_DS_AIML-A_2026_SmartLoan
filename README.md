# SmartLoan: Loan Approval Prediction Using Machine Learning

## 📌 Abstract
Predicting loan approval is a critical task for financial institutions to ensure accurate and efficient decision-making. This project uses machine learning techniques to predict whether a loan application will be approved or rejected based on applicant details such as income, loan amount, credit history, and demographic factors. Data preprocessing and visualization were performed to understand patterns in the dataset. A Logistic Regression model was developed, achieving an accuracy of approximately 79%. The results highlight the importance of credit history in loan approval decisions.

---

## ❗ Problem Statement
Financial institutions receive a large number of loan applications and must decide whether to approve or reject them based on multiple factors. Manual evaluation can be time-consuming and may lead to inconsistent decisions. This project aims to build a machine learning model that predicts loan approval status using applicant data, enabling faster and more reliable decision-making.

---

## 📊 Dataset Source
Loan Prediction Dataset (Kaggle)

- Number of records: ~614  
- Features include:
  - Applicant Income  
  - Loan Amount  
  - Credit History  
  - Education, Gender, etc.  
- Target variable: Loan_Status (Y/N)

---

## ⚙️ Methodology / Workflow
1. Data Understanding  
2. Data Preprocessing  
3. Exploratory Data Analysis  
4. Data Visualization  
5. Model Building (Logistic Regression)  
6. Model Evaluation  

---

## 🛠️ Tools & Technologies
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Scikit-learn  

---

## 📈 Results
- Accuracy: ~79%  
- Model performs better in predicting loan approvals than rejections  
- Credit history is the most important factor influencing loan approval  

---

## 📊 Visualizations
- Loan Status Distribution  
- Income vs Loan Status  
- Credit History vs Loan Status  
- Correlation Heatmap  

---

## 📁 Project Structure

MiniProject_DS_AIML-A_2026_SmartLoan/
│
├── README.md
├── requirements.txt
│
├── docs/
│ ├── abstract.pdf
│ ├── problem_statement.pdf
│ └── presentation.pptx
│
├── dataset/
│ ├── raw_data/
│ │ └── loan.csv
│ └── processed_data/
│ └── cleaned_data.csv
│
├── notebooks/
│ ├── data_understanding.ipynb
│ ├── preprocessing.ipynb
│ └── visualization.ipynb
│
├── src/
│ ├── preprocessing.py
│ ├── model.py
│ └── analysis.py
│
├── outputs/
│ ├── graphs/
│ └── results/
│ └── result.txt
│
└── report/
└── mini_project_report.pdf

---

## 👥 Team Members
- Nithya Shree M  
- Sridharshan S

---

## 📌 Conclusion
The model successfully predicts loan approval with good accuracy. However, it performs better for majority class (approved loans). Future improvements can include handling class imbalance and using advanced models.
