# A:\Project\ZT\SIEM\ai_analyzer.py
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt


def load_logs(file_path):
    logs = pd.read_csv(file_path, sep="|", header=None, names=["Timestamp", "Source", "Action", "Status"])
    return logs


def preprocess_logs(logs):
    le = LabelEncoder()
    logs["Source"] = le.fit_transform(logs["Source"])
    logs["Action"] = le.fit_transform(logs["Action"])
    logs["Status"] = le.fit_transform(logs["Status"])
    return logs


def detect_anomalies(logs):
    model = KMeans(n_clusters=2, random_state=42)
    logs["Cluster"] = model.fit_predict(logs[["Source", "Action", "Status"]])
    anomalies = logs[logs["Cluster"] == 1]  # Assume cluster 1 contains anomalies
    return anomalies


def save_anomalies(anomalies, output_path):
    anomalies.to_csv(output_path, sep="|", index=False)
    print(f"Anomalies saved to {output_path}")

if __name__ == "__main__":
    file_path = "A:/Project/data/logs.txt"
    output_path = "data/anomalies.txt"

    logs = load_logs(file_path)
    logs = preprocess_logs(logs)
    anomalies = detect_anomalies(logs)
    save_anomalies(anomalies, output_path)
