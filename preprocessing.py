# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

def preprocessing():
    # Streamlit App Title
    st.title("Interactive Data Preprocessing App")

    # File Uploader for Dataset
    uploaded_file = st.file_uploader("Upload your CSV dataset", type="csv")

    if uploaded_file is not None:
        # Load the dataset
        data = pd.read_csv(uploaded_file)
        st.write("### Dataset Overview")
        st.write(data.head())

        # Handle Missing Values
        st.write("### Handling Missing Values")
        missing_values = data.isnull().sum()
        st.write("#### Missing Values Before Imputation:")
        st.write(missing_values[missing_values > 0])
        data.fillna(data.median(numeric_only=True), inplace=True)  # Fill numeric missing values with the median
        st.write("#### Missing Values After Imputation:")
        st.write(data.isnull().sum())

        # Encode Categorical Variables
        st.write("### Encoding Categorical Variables")
        categorical_columns = data.select_dtypes(include=['object']).columns
        if len(categorical_columns) > 0:
            st.write(f"Categorical Columns: {list(categorical_columns)}")
            label_encoders = {}
            for column in categorical_columns:
                le = LabelEncoder()
                data[column] = le.fit_transform(data[column].astype(str))
                label_encoders[column] = le
            st.write("Categorical variables encoded successfully.")
        else:
            st.write("No categorical variables found.")

        # Scale or Normalize Numerical Features
        st.write("### Scaling Numerical Features")
        numeric_columns = data.select_dtypes(include=['int64', 'float64']).columns
        if len(numeric_columns) > 0:
            st.write(f"Numerical Columns: {list(numeric_columns)}")
            scaler = StandardScaler()
            data[numeric_columns] = scaler.fit_transform(data[numeric_columns])
            st.write("Numerical features scaled successfully.")
        else:
            st.write("No numerical variables found.")

        # Splitting the Dataset
        st.write("### Splitting the Dataset")
        # Here you can specify a suitable target column based on your dataset
        target_column = st.selectbox("Select the Target Column", data.columns)

        if target_column:
            X = data.drop(columns=[target_column])
            y = data[target_column]
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            st.write(f"Training Set: {X_train.shape[0]} samples")
            st.write(f"Testing Set: {X_test.shape[0]} samples")

            # Display Processed Data
            st.write("### Processed Data Overview")
            st.write("#### Sample of Processed Training Data:")
            st.write(X_train.head())
            st.write("#### Sample of Processed Testing Data:")
            st.write(X_test.head())
    else:
        st.write("Please upload a CSV file to start the preprocessing.")

# Run the preprocessing function
if __name__ == "__main__":
    preprocessing()
