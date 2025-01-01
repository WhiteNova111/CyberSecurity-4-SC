# **Zero Trust SIEM with AI-Powered Anomaly Detection**

## **Project Overview**
This project implements a **Zero Trust Architecture (ZTA)** and **Security Information and Event Management (SIEM)** system with AI-powered anomaly detection. It simulates log collection, processes logs for security insights, detects anomalies using machine learning, and integrates Zero Trust principles for enhanced security. 

The project is designed to monitor network traffic, user behavior, and system events while automating threat detection and response.

---

## **Key Features**
1. **Zero Trust Architecture**:
   - Implements the "never trust, always verify" principle.
   - Authentication includes password verification and OTP-based 2FA.

2. **SIEM Functionality**:
   - Log collection from multiple sources (e.g., network, user behavior, system access).
   - Centralized log storage and processing.

3. **AI-Powered Anomaly Detection**:
   - Uses **KMeans clustering** to detect suspicious patterns in logs.
   - Preprocessing includes label encoding for categorical data.

4. **Integration with Machine Learning**:
   - Processes logs to detect and flag anomalies.
   - Saves anomalies to a designated file for further analysis.

5. **Scalability**:
   - Modular design to accommodate additional data sources and machine learning models.

6. **Real-Time Email Notifications**:
   - Sends OTPs during authentication and logs security events.

```
A:/Project/
│
├── ZT/
│   ├── auth/
│   │   └── authenticate.py   # Handles user authentication with 2FA.
│   ├── SIEM/
│   │   ├── collector.py      # Simulates log generation.
│   │   ├── ai_analyzer.py    # Processes logs and detects anomalies.
│   │   └── logger.py         # Logs events for audit trails.
│   ├── web_app/
│   │   ├── templates/
│   │   │   └── index.html    # Main dashboard template.
│   │   ├── static/
│   │   │   └── style.css     # Web app styling.
│   │   └── app.py            # Flask app for the dashboard.
│   └── data/
│       ├── logs.txt          # Collected logs.
│       └── anomalies.txt     # Detected anomalies.
└── README.md                 # Documentation.
```

## **Installation**
1. Clone the repository:
 
2. Install dependencies:
   - Install required Python packages:
     
terminal
     pip install pandas numpy scikit-learn matplotlib

``
## **Usage**

### **1. Start the Web Application**
Launch the Flask web app:
```bash
python ZT/web_app/app.py
```
Access it at `http://127.0.0.1:5000`.

---

### **2. Log Collection**
Run the log collector to simulate log entries:
```bash
python ZT/SIEM/collector.py
```
Logs will be saved to `data/logs.txt`.

---

### **3. Anomaly Detection**
Process logs for anomalies using AI:
```bash
python ZT/SIEM/ai_analyzer.py
```
Anomalies will be saved to `data/anomalies.txt`.

---

### **4. Authentication**
Run the authentication system with OTP-based 2FA:
```bash
python ZT/auth/authenticate.py
```
- Enter your credentials.
- Verify the OTP sent to your email.

---

## **Web App Features**
1. **Dashboard**:
   - Centralized interface for real-time monitoring.
   
2. **View Logs**:
   - Access logs stored in `logs.txt`.

3. **Anomaly Tracking**:
   - Visualize flagged anomalies.

4. **Explore Zero Trust**:
   - Learn about Zero Trust principles and implementation.

5. **Download Reports**:
   - Generate and download security reports.

6. **Dark Mode**:
   - Toggle between light and dark modes for accessibility.

---

## **How It Works**

### **Log Collection**:
- Simulates logs from random sources and saves them to a file.

### **Log Preprocessing**:
- Encodes categorical fields for compatibility with machine learning.

### **Anomaly Detection**:
- Uses **KMeans clustering** to flag unusual behavior.

### **Web App**:
- Interactive dashboard powered by Flask.
- Secure authentication with password hashing and OTP verification.

---

## **Tech Stack**
- **Programming Language**: Python
- **Web Framework**: Flask
- **Machine Learning**: scikit-learn
- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib
- **Email Service**: smtplib
- **Real-Time Updates**: Flask-SocketIO


Let me know if you need further assistance!

