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
---

## 🚀 Features

<table>
  <tr>
    <td>🔍 <strong>ML Prediction</strong></td>
    <td>Classifies if a customer will churn based on form inputs</td>
  </tr>
  <tr>
    <td>📋 <strong>Simple Input Form</strong></td>
    <td>Collects key customer details like tenure, billing, services</td>
  </tr>
  <tr>
    <td>📊 <strong>Charts</strong></td>
    <td>Interactive Bar, Doughnut, and Polar Area charts</td>
  </tr>
  <tr>
    <td>🧾 <strong>PDF Export</strong></td>
    <td>Download results & visuals in a clean report</td>
  </tr>
  <tr>
    <td>🎨 <strong>Modern UI</strong></td>
    <td>Tailwind CSS, gradient background, AOS & particles</td>
  </tr>
  <tr>
    <td>📱 <strong>Responsive Design</strong></td>
    <td>Works across all screen sizes and devices</td>
  </tr>
  <tr>
    <td>⚙️ <strong>Flask Backend</strong></td>
    <td>Runs a trained machine learning pipeline in Python</td>
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
