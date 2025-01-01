# A:\Project\ZT\SIEM\report_generator.py
import pandas as pd
from datetime import datetime

def generate_report(log_path, anomaly_path, output_path):
    logs = pd.read_csv(log_path, sep="|", header=None, names=["Timestamp", "Source", "Action", "Status"])
    anomalies = pd.read_csv(anomaly_path, sep="|")

    with open(output_path, "w") as file:
        file.write("SIEM Report\n")
        file.write(f"Generated on: {datetime.now()}\n")
        file.write(f"Total Logs Analyzed: {len(logs)}\n")
        file.write(f"Anomalies Detected: {len(anomalies)}\n")
        file.write("\nDetails of Anomalies:\n")
        file.write(anomalies.to_string(index=False))
    
    print(f"Report generated and saved to {output_path}")

if __name__ == "__main__":
    generate_report("A:/Project/data/logs.txt", "data/anomalies.txt", "data/siem_report.txt")
