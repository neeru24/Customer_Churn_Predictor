# 🔍 Customer Churn Predictor

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)
![Tailwind CSS](https://img.shields.io/badge/TailwindCSS-3.x-38B2AC?logo=tailwind-css)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)

> An intelligent AI/ML-based web application that enables businesses to **predict customer churn** by analyzing behavioral and billing patterns. Designed with a clean Tailwind-powered UI, real-time visualizations, and PDF export capabilities, this tool streamlines retention strategies for telecom and subscription-based industries.

---
## 🔍 Overview

Customer churn refers to when an existing customer stops doing business with a company. This predictor uses a **supervised machine learning pipeline** to analyze structured customer data and forecast churn probability with precision. The app serves as a decision-support system for customer success teams.

---
## 🚀 Key Capabilities


  <img src="static/Key Capabilities.png" width="700"/>


---


## ⚙️ Architecture

```mermaid
flowchart TD
    A[User Input Form] --> B[Flask Backend]
    B --> C[Preprocessing & Scaling]
    C --> D[ML Model Prediction]
    D --> E[Churn Result + Confidence %]
    E --> F[Chart.js Visualization]
    F --> G[PDF Export]
```

---
## 📸 UI Snapshots

<table>
  <tr>
    <td><img src="static/Home.png" width="500"/></td>
    <td><img src="static/Features.png" width="500"/></td>
  </tr>
   <tr>
    <td><img src="static/form.png" width="500"/></td>
    <td><img src="static/charts.png" width="500"/></td>
  </tr>
</table>


---

## 🛠️ Tech Stack

| 💡 Layer         | 🚀 Technologies                                                                 |
|------------------|----------------------------------------------------------------------------------|
| 🌐 **Frontend**   | ![HTML5](https://img.shields.io/badge/-HTML5-E34F26?logo=html5&logoColor=white) ![TailwindCSS](https://img.shields.io/badge/-TailwindCSS-38B2AC?logo=tailwind-css&logoColor=white) ![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?logo=javascript&logoColor=black) ![AOS](https://img.shields.io/badge/-AOS-lightgrey) |
| 🔙 **Backend**    | ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/-Flask-000000?logo=flask&logoColor=white) |
| 🧠 **ML Model**   | ![Scikit-learn](https://img.shields.io/badge/-Scikit--learn-F7931E?logo=scikit-learn&logoColor=white) ![Pandas](https://img.shields.io/badge/-Pandas-150458?logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/-NumPy-013243?logo=numpy&logoColor=white) ![Joblib](https://img.shields.io/badge/-Joblib-blue) |
| 📊 **Visualization** | ![Chart.js](https://img.shields.io/badge/-Chart.js-FF6384?logo=chartdotjs&logoColor=white) |
| 📎 **Export**      | ![xhtml2pdf](https://img.shields.io/badge/-xhtml2pdf-blueviolet) |
| ✨ **Aesthetics**   | ![tsparticles](https://img.shields.io/badge/-tsparticles-blue?logo=data:image/svg+xml;base64,<svg></svg>) |

--- 

## 📁 Folder Structure

```
customer-churn-predictor/
│
├── static/                 # Static files (CSS, JS, icons)
│   └── styles, particles, icons
│
├── templates/              # HTML templates for rendering pages
│   ├── index.html          # Landing page
│   ├── form.html           # Input form for user data
│   └── how-to-use.html     # User Guide
│
├── churn_model.pkl         # Trained machine learning model
├── scaler.pkl              # Scaler for preprocessing
├── model_columns.pkl       # Feature columns used by the model
|
├── train_model.py          # Script to train & export ML model artifacts
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```


---

## 🧪 ML Model Details

| 🧩 **Component**       | 📌 **Details**                                                                 |
|------------------------|--------------------------------------------------------------------------------|
| 🧠 **Model Type**      | Logistic Regression *(Binary Classification)*                                  |
| 📚 **Dataset**         | [Telco Customer Churn](https://www.kaggle.com/blastchar/telco-customer-churn) |
| 📊 **Features Used**   | Tenure, Monthly Charges, Contract Type, Internet Service, Security Add-ons, Payment Method |
| 🧹 **Preprocessing**   | Label Encoding, Standard Scaling                                                |
| 📈 **Evaluation**      | Accuracy, ROC-AUC Score, Confusion Matrix                                      |
| 🛠️ **Tools/Libraries** | Scikit-learn, Pandas, NumPy, Seaborn                                            |

---

## ⚙️ Setup & Installation

**⚙️ Clone the Repository**
```bash
git clone https://github.com/your-username/customer-churn-predictor.git
cd customer-churn-predictor
```

**🧪 (Optional) Create & Activate Virtual Environment**
```bash
# For macOS / Linux
python -m venv venv
source venv/bin/activate
```

```bash
# For Windows
python -m venv venv
venv\Scripts\activate
```

**📦 Install Dependencies**
```bash
pip install -r requirements.txt
```

**🚀 Run the Flask App**
```bash
python app.py
```

**🌐 Access the App** 
```bash
http://127.0.0.1:5000
```

---

## 📬 Contact

**👩‍💻 Developed by:** Neeru Gangarh  
**🔗 LinkedIn:** [linkedin.com/in/neerugangarh](https://www.linkedin.com/in/neerugangarh)  
**📂 Contributions:** Feel free to fork or contribute!

---

## 📝 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for more details.
