import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Title
st.title("🔌 Load Forecasting Using ML (100 Data Points)")
st.markdown("Upload an Excel file with columns: `meterid`, `rtc`, `blockkwh`")

# Upload file
uploaded_file = st.file_uploader("Choose your Excel file (.xlsx)", type="xlsx")

if uploaded_file:
    try:
        # Read Excel file
        df = pd.read_excel(uploaded_file)

        # Convert rtc column to datetime
        df['rtc'] = pd.to_datetime(df['rtc'])

        # Extract features
        df['hour'] = df['rtc'].dt.hour
        df['minute'] = df['rtc'].dt.minute
        df['dayofweek'] = df['rtc'].dt.dayofweek

        # Display raw data
        st.subheader("📄 Preview of Uploaded Data")
        st.dataframe(df.head())

        # Features and Target
        X = df[['hour', 'minute', 'dayofweek']]
        y = df['blockkwh']

        # Train-Test Split
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Predict
        y_pred = model.predict(X_test)

        # Evaluation
        mse = mean_squared_error(y_test, y_pred)
        st.subheader("📊 Model Performance")
        st.write(f"**Mean Squared Error (MSE):** {mse:.2f}")

        # Plotting
        st.subheader("📈 Actual vs Predicted Load (blockkwh)")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots()
        ax.plot(y_test.values, label='Actual', marker='o')
        ax.plot(y_pred, label='Predicted', linestyle='--')
        ax.set_title("Actual vs Predicted")
        ax.set_xlabel("Samples")
        ax.set_ylabel("blockkwh")
        ax.legend()
        st.pyplot(fig)

    except Exception as e:
        st.error(f"⚠️ Error: {e}")
