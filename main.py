import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('Fraud Detection/creditCard.csv')

df = df.drop(['Time'], axis=1)

scaler = StandardScaler()
df['Amount'] = scaler.fit_transform(df[['Amount']])

X = df.drop('Class', axis=1)
y = df['Class']

iso_forest = IsolationForest(contamination=0.0017, random_state=42)
iso_forest.fit(X)

y_pred = iso_forest.predict(X)
y_pred = np.where(y_pred == -1, 1, 0)

conf_matrix = confusion_matrix(y, y_pred)
class_report = classification_report(y, y_pred)

print("Confusion Matrix:\n")
print(conf_matrix)
print("\nClassification Report:")
print(class_report)