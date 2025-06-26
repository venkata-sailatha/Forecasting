
# 🔌 Load Forecasting ML App (Streamlit)

This Streamlit web application allows you to upload an Excel file containing smart meter readings and performs basic **load forecasting** using a **Linear Regression** model. The app trains the model on time features (`hour`, `minute`, `dayofweek`) and predicts future `blockkwh` consumption.

---
![image](https://github.com/user-attachments/assets/ddb69b77-50aa-476f-98f1-a39da6da87ec)
![image](https://github.com/user-attachments/assets/889054eb-c4a9-41f4-bfcc-dbbbba5fc7db)

## 📁 Features

- Upload Excel files with smart meter data
- Automatic feature extraction from datetime (`rtc`)
- Trains a Linear Regression model
- Displays Mean Squared Error (MSE)
- Plots actual vs predicted `blockkwh` values

---

## 🧾 Example Input File

The Excel file (`.xlsx`) should contain exactly these 3 columns:

| meterid | rtc                 | blockkwh |
|---------|---------------------|----------|
| 1001    | 2024-01-01 00:00:00 | 2.35     |
| 1002    | 2024-01-01 00:15:00 | 3.12     |
| ...     | ...                 | ...      |

---

## 🚀 Getting Started

### 🔧 Install dependencies

Use the provided `requirements.txt` to install all required Python packages:

```bash
pip install -r requirements.txt
````

### ▶️ Run the Streamlit App

```bash
streamlit run app.py
```
live app
https://forecasting-cofm.onrender.com/

## 📂 Project Structure

```
load_forecasting_app/
│
├── load_forecasting_app.py     # Main Streamlit app
├── requirements.txt            # Required Python libraries
└── README.md                   # You're here!
```

---

## 📈 Libraries Used

streamlit
pandas
numpy
scikit-learn
matplotlib
openpyxl

---
