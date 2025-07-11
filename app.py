# app.py
from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

model = joblib.load('churn_model.pkl')
scaler = joblib.load('scaler.pkl')
columns = joblib.load('model_columns.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form.to_dict()

        input_data = {
            'tenure': float(data['tenure']),
            'MonthlyCharges': float(data['MonthlyCharges']),
            'TotalCharges': float(data['TotalCharges']),
        }

        # One-hot encode manually
        for field in ['Contract', 'InternetService', 'TechSupport', 'OnlineSecurity', 'PaymentMethod']:
            key = f"{field}_{data[field]}"
            input_data[key] = 1

        # Create dataframe with all model columns
        full_input = pd.DataFrame([0]*len(columns), index=columns).T
        for k, v in input_data.items():
            if k in full_input.columns:
                full_input.at[0, k] = v

        scaled_input = scaler.transform(full_input)
        prediction = model.predict(scaled_input)[0]

        return jsonify({'result': "Churn" if prediction == 1 else "No Churn"})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
