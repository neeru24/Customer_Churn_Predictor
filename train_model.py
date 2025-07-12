import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import SMOTE
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Load and preprocess
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.dropna(inplace=True)
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

# Feature selection
features = [
    'tenure', 'MonthlyCharges', 'TotalCharges',
    'Contract', 'InternetService', 'TechSupport',
    'OnlineSecurity', 'PaymentMethod'
]
df = df[features + ['Churn']]

# One-hot encode
df_encoded = pd.get_dummies(df, drop_first=False)

# X and y
X = df_encoded.drop('Churn', axis=1)
y = df_encoded['Churn']

# Save model columns
joblib.dump(X.columns.tolist(), 'model_columns.pkl')

# Balance classes
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_resampled)

# Split and train
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_resampled, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save
joblib.dump(model, 'churn_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

# Evaluate
y_pred = model.predict(X_test)
print("\n📊 Evaluation Report")
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
