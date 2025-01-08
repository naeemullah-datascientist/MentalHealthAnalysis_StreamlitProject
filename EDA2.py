import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set Seaborn aesthetics for a clean and professional look
sns.set_theme(style="whitegrid")

def eda2():
    # Streamlit App
    st.title("Enhanced Exploratory Data Analysis")

    # Load the dataset
    data = pd.read_csv('survey.csv')

    # Display the first few rows of the dataset
    st.write("### Dataset Preview")
    st.dataframe(data.head())

    # Age Distribution: Histogram with KDE and Boxplot (Enhanced)
    st.write("### Age Distribution")
    if 'Age' in data.columns:
        # Clean Age Data by converting to numeric and handling errors
        data['Age'] = pd.to_numeric(data['Age'], errors='coerce')
        clean_age_data = data['Age'].dropna()

        # Histogram with KDE (Kernel Density Estimate)
        plt.figure(figsize=(10, 6))
        sns.histplot(clean_age_data, bins=20, kde=True, color='lightgreen', stat='density')
        plt.title('Age Distribution (Histogram with KDE)', fontsize=16)
        plt.xlabel('Age', fontsize=12)
        plt.ylabel('Density', fontsize=12)
        st.pyplot(plt)

        # Boxplot for Age Distribution
        plt.figure(figsize=(10, 6))
        sns.boxplot(x=clean_age_data, color='skyblue')
        plt.title('Age Distribution (Boxplot)', fontsize=16)
        plt.xlabel('Age', fontsize=12)
        st.pyplot(plt)

    else:
        st.write("The dataset does not contain an 'Age' column.")

    # Work Interference Analysis
    st.write("### Work Interference Analysis")
    if 'work_interfere' in data.columns:
        plt.figure(figsize=(8, 6))
        work_interfere_percentage = data['work_interfere'].value_counts(normalize=True) * 100
        sns.barplot(x=work_interfere_percentage.index, y=work_interfere_percentage, palette='viridis')
        plt.title('Work Interference (%)', fontsize=16)
        plt.xlabel('Work Interference', fontsize=12)
        plt.ylabel('Percentage', fontsize=12)
        st.pyplot(plt)
    else:
        st.write("The dataset does not contain a 'work_interfere' column.")

    # Correlation Matrix Heatmap
    st.write("### Correlation Matrix")
    numeric_data = data.select_dtypes(include=['int64', 'float64'])  # Select only numeric columns
    if not numeric_data.empty:
        correlation_matrix = numeric_data.corr()
        plt.figure(figsize=(12, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
        plt.title('Correlation Matrix', fontsize=16)
        st.pyplot(plt)
    else:
        st.write("No numeric columns found for correlation analysis.")

    # Missing Value Analysis
    st.write("### Missing Values by Feature")
    missing_values = data.isnull().sum()
    if missing_values.sum() > 0:
        plt.figure(figsize=(10, 6))
        sns.barplot(x=missing_values[missing_values > 0].index, y=missing_values[missing_values > 0], palette='rocket')
        plt.title('Missing Values by Feature', fontsize=16)
        plt.ylabel('Count', fontsize=12)
        plt.xlabel('Features', fontsize=12)
        plt.xticks(rotation=45)
        st.pyplot(plt)

        # Missing Data Heatmap
        st.write("### Missing Data Heatmap")
        plt.figure(figsize=(10, 6))
        sns.heatmap(data.isnull(), cbar=False, cmap='Blues')
        plt.title('Missing Data Heatmap', fontsize=16)
        st.pyplot(plt)
    else:
        st.write("No missing values found in the dataset.")

    # Outlier Detection Across Numeric Features (Updated)
    st.write("### Outlier Detection Across Numeric Features")
    numeric_data = data.select_dtypes(include=['int64', 'float64'])  # Select only numeric columns
    if not numeric_data.empty:
        plt.figure(figsize=(12, 8))
        sns.boxplot(data=numeric_data, orient='h', palette='Set2')
        plt.title('Outlier Detection Across Numeric Features', fontsize=16)
        st.pyplot(plt)
    else:
        st.write("No numeric columns found for outlier detection.")

    # Scatterplot for specific numeric pairs to avoid memory overload
    st.write("### Scatterplot for Numeric Features (Subset of Columns)")
    if not numeric_data.empty:
        selected_numeric_cols = numeric_data.columns[:4]  # Select first 4 numeric columns (adjust as needed)
        
        for i in range(len(selected_numeric_cols)):
            for j in range(i+1, len(selected_numeric_cols)):
                plt.figure(figsize=(8, 6))
                sns.scatterplot(data=numeric_data, x=selected_numeric_cols[i], y=selected_numeric_cols[j], alpha=0.5)
                plt.title(f'Scatterplot: {selected_numeric_cols[i]} vs {selected_numeric_cols[j]}', fontsize=16)
                plt.xlabel(selected_numeric_cols[i], fontsize=12)
                plt.ylabel(selected_numeric_cols[j], fontsize=12)
                st.pyplot(plt)

    # New Graph: Mental Health Issues Count (Alternative)
    st.write("### Work Interference Analysis")
    if 'work_interfere' in data.columns:
        plt.figure(figsize=(8, 6))
        sns.countplot(data=data, x='work_interfere', palette='muted')
        plt.title('Work Interference Count', fontsize=16)
        plt.xlabel('Work Interference', fontsize=12)
        plt.ylabel('Count', fontsize=12)
        st.pyplot(plt)
    else:
        st.write("The dataset does not contain a 'work_interfere' column.")

    # Data Types (Pie Chart) - Improved Aesthetics
    st.write("### Data Types Distribution")
    data_types_counts = data.dtypes.value_counts()
    plt.figure(figsize=(8, 8))
    data_types_counts.plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette('pastel'), startangle=90)
    plt.title('Data Types Distribution', fontsize=16)
    st.pyplot(plt)

if __name__ == "__main__":
    eda2()
