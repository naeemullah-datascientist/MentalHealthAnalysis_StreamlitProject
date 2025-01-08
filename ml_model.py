import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import LabelEncoder
import streamlit as st
import joblib

def ml_model():
    # Streamlit app title
    st.title("Random Forest: Mental Health Issues Classification")

    # File uploader for the dataset
    uploaded_file = st.file_uploader("Upload your CSV dataset", type="csv")

    if uploaded_file is not None:
        # Load the dataset
        try:
            data = pd.read_csv(uploaded_file)
            st.write("### Dataset Overview")
            st.write("Preview of the dataset:")
            st.write(data.head())
        except Exception as e:
            st.error(f"Error loading the file: {e}")
            st.stop()

        # Handle Timestamp column: Convert to usable features
        data['Timestamp'] = pd.to_datetime(data['Timestamp'])
        data['year'] = data['Timestamp'].dt.year
        data['month'] = data['Timestamp'].dt.month
        data['day'] = data['Timestamp'].dt.day
        data = data.drop(columns=['Timestamp'])

        # Define target column `has_mental_health_issues`
        data['has_mental_health_issues'] = (data['treatment'] == 'Yes') | (data['seek_help'] == 'Yes') | (data['mental_health_consequence'] != 'No')

        # Encode categorical variables
        categorical_columns = data.select_dtypes(include=['object']).columns
        label_encoders = {}
        for column in categorical_columns:
            le = LabelEncoder()
            data[column] = le.fit_transform(data[column])
            label_encoders[column] = le
        
        # Split the dataset into features and target
        X = data.drop(columns=['treatment', 'has_mental_health_issues'])
        y = data['has_mental_health_issues']

        # Split into train/test sets
        test_size = st.slider("Select Test Size (Percentage)", min_value=10, max_value=50, value=20, step=5) / 100
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

        # Train Random Forest Model
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Evaluate the model
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        st.metric("Model Accuracy", f"{accuracy:.2f}")

        conf_matrix = confusion_matrix(y_test, y_pred)
        conf_matrix_df = pd.DataFrame(conf_matrix, index=["No Issues (0)", "Has Issues (1)"], columns=["Predicted 0", "Predicted 1"])
        st.write("**Confusion Matrix:**")
        st.dataframe(conf_matrix_df)

        class_report = classification_report(y_test, y_pred, output_dict=True)
        class_report_df = pd.DataFrame(class_report).transpose()
        st.write("**Classification Report:**")
        st.dataframe(class_report_df)

        # Option to save the trained model
        if st.button("Save Model"):
            joblib.dump(model, 'random_forest_model.pkl')
            st.success("Model saved as `random_forest_model.pkl`!")

        # Interactive prediction form
        st.write("### Make Predictions with New Data")
        with st.form("prediction_form"):
            user_input = {}
            for col in X.columns:
                user_input[col] = st.number_input(f"{col} (numeric)", min_value=float(X[col].min()), max_value=float(X[col].max()), step=1.0)

            submit = st.form_submit_button("Predict")
            if submit:
                user_df = pd.DataFrame([user_input])
                prediction = model.predict(user_df)[0]
                prediction_label = "Has Mental Health Issues (1)" if prediction == 1 else "No Mental Health Issues (0)"
                st.success(f"Prediction: {prediction_label}")

    else:
        st.warning("Please upload a CSV file to proceed.")

if __name__ == "__main__":
    ml_model()
