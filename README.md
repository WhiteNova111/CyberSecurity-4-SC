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

---

## **Project Structure**
```
A:/Project/
│
├── ZT/
│   ├── auth/
│   │   └── authenticate.py  # Handles user authentication and OTP-based 2FA.
│   ├── SIEM/
│   │   ├── collector.py      # Simulates log generation and saves logs to a file.
│   │   ├── ai_analyzer.py    # Processes logs and detects anomalies using AI.
│   │   └── logger.py         # Logs system events for auditing.
│   └── data/                 # Directory for storing logs and anomaly files.
│       ├── logs.txt          # Collected log entries.
│       └── anomalies.txt     # Detected anomalies.
└── README.md                 # Project documentation.
```

---

## **Installation**
1. Clone the repository:
 
2. Install dependencies:
   - Install required Python packages:
     ```terminal
     pip install pandas numpy scikit-learn matplotlib
     ```

---

## **Usage**

## 1. **Log Collection**
Run the `collector.py` script to generate simulated logs:
```terminal
python ZT/SIEM/collector.py
```
Logs will be saved to `data/logs.txt`.

---

## 2. **Anomaly Detection**
Process logs and detect anomalies using AI:
```terminal
python ZT/SIEM/ai_analyzer.py
```
Anomalies will be saved to `data/anomalies.txt`.

---

## 3. **Authentication**
Run the authentication system with 2FA:
```terminal
python ZT/auth/authenticate.py
```
- Enter your credentials.
- Verify the OTP sent to your email.

---

## **How It Works**

1. **Log Collection**:
   - Generates logs with random sources, actions, and statuses.
   - Saves logs in a structured format for further analysis.

2. **Log Preprocessing**:
   - Encodes categorical data for machine learning.

3. **Anomaly Detection**:
   - Uses **KMeans clustering** to identify unusual behavior in logs.

4. **Authentication**:
   - Verifies user credentials with **bcrypt**.
   - Ensures 2FA using OTPs sent via email.

5. **Auditing**:
   - Logs events (e.g., authentication attempts, anomalies) for future review.

---

## **Tech Stack**
- **Programming Language**: Python
- **Machine Learning**: scikit-learn
- **Data Processing**: pandas, numpy
- **Email Service**: smtplib
- **Log Visualization**: matplotlib


---

#Let me know if anything comes up.
