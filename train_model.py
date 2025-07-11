# train_model.py
import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load and clean the data
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(inplace=True)
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

# Select relevant features
features = [
    'tenure', 'MonthlyCharges', 'TotalCharges',
    'Contract', 'InternetService', 'TechSupport',
    'OnlineSecurity', 'PaymentMethod'
]
df = df[features + ['Churn']]

# One-hot encoding
df_encoded = pd.get_dummies(df, drop_first=True)
X = df_encoded.drop('Churn', axis=1)
y = df_encoded['Churn']

# Save columns for prediction input
joblib.dump(list(X.columns), 'model_columns.pkl')

# Scale and train
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
joblib.dump(scaler, 'scaler.pkl')

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
joblib.dump(model, 'churn_model.pkl')

print("✅ Model trained and saved.")
