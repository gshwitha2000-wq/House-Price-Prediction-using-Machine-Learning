# 🏠 House Price Prediction System

A Machine Learning-based web application built using **Streamlit** that predicts house prices based on area and rate per square foot. The project also provides data visualization and analytics for Hyderabad housing prices.

## 📌 Project Overview

This project uses a **Random Forest Regressor** model to analyze housing data and predict property prices. The application allows users to:

* View a preview of the housing dataset.
* Analyze average house prices by location.
* Enter property details.
* Predict estimated house prices instantly.

---

## 🚀 Features

* Interactive web interface using Streamlit.
* Dataset preview and exploration.
* Location-wise average price analysis.
* House price prediction based on:

  * Area (Sqft)
  * Rate per Sqft
* Machine Learning model training using Random Forest Regressor.
* Model serialization using Pickle.

---

## 📂 Project Structure

```text
House-Price-Prediction/
│
├── app.py                      # Streamlit application
├── model_training.py           # Model training script
├── model.pkl                   # Trained ML model
├── Hyderbad_House_price.csv    # Dataset
├── README.md                   # Project documentation
└── requirements.txt            # Dependencies
```

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* Scikit-Learn
* Matplotlib
* Pickle

---

## 📊 Dataset Information

The dataset contains Hyderabad housing information including:

* Location
* Area in Sqft
* Rate per Sqft
* Price (Lakhs)

Data preprocessing steps include:

* Removing duplicate records
* Cleaning numerical columns
* One-Hot Encoding categorical features

---

## 🤖 Machine Learning Model

### Algorithm Used

**Random Forest Regressor**

### Training Steps

1. Load dataset.
2. Clean and preprocess data.
3. Remove duplicates.
4. Apply One-Hot Encoding.
5. Split data into training and testing sets.
6. Train Random Forest Regressor.
7. Save trained model using Pickle.

---

## ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/House-Price-Prediction.git
cd House-Price-Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Model Training

```bash
python model_training.py
```

This will generate:

```text
model.pkl
```

---

## ▶️ Run Streamlit Application

```bash
streamlit run app.py
```

---

## 📈 Application Workflow

1. Load trained model.
2. Display housing dataset preview.
3. Show top locations by average price.
4. Accept user inputs:

   * Area in Sqft
   * Rate per Sqft
5. Calculate and display predicted house price.

---

## 📷 Sample Output

* Dataset Preview
* Location-wise Price Analytics
* House Price Prediction Result

Example:

```text
Area: 1500 Sqft
Rate: ₹6000 per Sqft

Predicted Price: ₹90.00 Lakhs
```

---

## 🔮 Future Enhancements

* Location-based prediction.
* Bedroom and bathroom inputs.
* Interactive dashboards.
* Model performance metrics.
* Deployment on Streamlit Cloud.

---

## 👩‍💻 Author

**Ashwitha Gogikar**

Release Engineer | Data Analytics & Machine Learning Enthusiast

📧 Email: gashwitha2000@gmail.com

🔗 LinkedIn: https://www.linkedin.com/in/ashwitha-gogikar-35839a1b5/


---

## 📜 License

This project is developed for educational and learning purposes.
