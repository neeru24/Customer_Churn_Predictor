from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__, static_folder='../static', template_folder='../templates')

model = joblib.load("churn_model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("model_columns.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/form')
def form():
    return render_template("form.html")

@app.route('/how-to-use')
def how_to_use():
    return render_template("how-to-use.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form.to_dict()
        tenure = float(data.get("tenure", 0))
        monthly = float(data.get("MonthlyCharges", 0))
        total = float(data.get("TotalCharges", 0))

        input_dict = {
            'tenure': tenure,
            'MonthlyCharges': monthly,
            'TotalCharges': total,
            'Contract': data['Contract'],
            'InternetService': data['InternetService'],
            'TechSupport': data['TechSupport'],
            'OnlineSecurity': data['OnlineSecurity'],
            'PaymentMethod': data['PaymentMethod']
        }

        df = pd.DataFrame([input_dict])
        df_encoded = pd.get_dummies(df, drop_first=False)

        input_final = pd.DataFrame([[0]*len(columns)], columns=columns)
        for col in df_encoded.columns:
            if col in input_final.columns:
                input_final[col] = df_encoded[col]

        input_scaled = scaler.transform(input_final)
        proba = model.predict_proba(input_scaled)[0]
        prediction = int(proba[1] >= 0.5)
        confidence = round(proba[prediction] * 100, 2)
        result = "Churn" if prediction == 1 else "Not Churn"

        return jsonify({
            'result': result,
            'confidence': f"{confidence}%"
        })

    except Exception as e:
        return jsonify({'result': '❌ Error', 'confidence': '', 'warning': str(e)})

# Required handler for Vercel
def handler(request, context=None):
    return app(request.environ, start_response=context)
