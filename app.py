from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import os
import csv
from datetime import datetime

app = Flask(__name__)

# Load model, scaler, and columns
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

        # Convert input values
        tenure = float(data.get("tenure", 0))
        monthly = float(data.get("MonthlyCharges", 0))
        total = float(data.get("TotalCharges", 0))
        expected_total = tenure * monthly

        warning_msg = ""
        if total > expected_total * 1.5:
            warning_msg = f"⚠️ TotalCharges seems high. Expected around ₹{round(expected_total)}."

        # Build input dictionary
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

        # Encode
        df = pd.DataFrame([input_dict])
        df_encoded = pd.get_dummies(df, drop_first=False)

        # Prepare final input
        input_final = pd.DataFrame([[0]*len(columns)], columns=columns)
        for col in df_encoded.columns:
            if col in input_final.columns:
                input_final[col] = df_encoded[col]

        # Scale and predict
        input_scaled = scaler.transform(input_final)
        proba = model.predict_proba(input_scaled)[0]
        prediction = int(proba[1] >= 0.5)
        confidence = round(proba[prediction] * 100, 2)
        result = "Churn" if prediction == 1 else "Not Churn"

        # Save log
        os.makedirs("logs", exist_ok=True)
        with open("logs/predictions.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                tenure, monthly, total,
                data['Contract'], data['InternetService'],
                data['TechSupport'], data['OnlineSecurity'],
                data['PaymentMethod'], result, f"{confidence}%"
            ])

        return jsonify({
            'result': f"{result}",
            'confidence': f"{confidence}%",
            'warning': warning_msg
        })

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({
            'result': '❌ Error',
            'confidence': '',
            'warning': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True)
