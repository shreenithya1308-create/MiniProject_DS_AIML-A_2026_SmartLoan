import pandas as pd

def preprocess_data(df):
    # Drop unnecessary column (if exists)
    if 'Loan_ID' in df.columns:
        df = df.drop('Loan_ID', axis=1)

    # Fill categorical missing values
    df['Gender'] = df['Gender'].fillna(df['Gender'].mode()[0])
    df['Married'] = df['Married'].fillna(df['Married'].mode()[0])
    df['Dependents'] = df['Dependents'].fillna(df['Dependents'].mode()[0])
    df['Self_Employed'] = df['Self_Employed'].fillna(df['Self_Employed'].mode()[0])

    # Fill numerical missing values
    df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].median())
    df['Loan_Amount_Term'] = df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].median())

    # Important feature
    df['Credit_History'] = df['Credit_History'].fillna(df['Credit_History'].mode()[0])

    # Encoding categorical variables
    df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
    df['Married'] = df['Married'].map({'Yes': 1, 'No': 0})
    df['Education'] = df['Education'].map({'Graduate': 1, 'Not Graduate': 0})
    df['Self_Employed'] = df['Self_Employed'].map({'Yes': 1, 'No': 0})
    df['Loan_Status'] = df['Loan_Status'].map({'Y': 1, 'N': 0})

    # Handle Dependents column
    df['Dependents'] = df['Dependents'].replace('3+', 3)
    df['Dependents'] = df['Dependents'].astype(int)

    # One-hot encoding
    df = pd.get_dummies(df, columns=['Property_Area'], drop_first=True)

    # Convert all to int
    df = df.astype(int)

    return df