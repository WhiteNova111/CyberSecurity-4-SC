from flask import Flask, render_template, request, redirect, session, send_file, url_for
import sqlite3
import pandas as pd
import json
import os

# Ensure the directory for the database exists
db_dir = os.path.join(os.path.dirname(__file__), 'ZT', 'data')
if not os.path.exists(db_dir):
    os.makedirs(db_dir)

# Ensure the path to the database is correct
db_path = os.path.join(db_dir, 'zta_users.db')


def init_db():
    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        
        c.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')

        
        c.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", ('admin', 'securepassword'))

        
        conn.commit()
        conn.close()
    except sqlite3.OperationalError as e:
        print(f"Error initializing database: {e}")

init_db()

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Route to the dashboard without login
@app.route('/')
def index():
    
    session['username'] = 'admin'
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
        return render_template('dashboard.html', username=username)  
    else:
        return redirect(url_for('login'))  
# Route: View Logs
@app.route('/logs')
def view_logs():
    logs = pd.read_csv('A:/Project/data/logs.txt', sep="|", header=None, names=["Timestamp", "Source", "Action", "Status"])
    return render_template('logs.html', logs=logs.to_dict(orient="records"))

# Route: View Anomalies
@app.route('/anomalies')
def view_anomalies():
    anomalies = pd.read_csv('A:/Project/data/anomalies.txt', sep="|")
    return render_template('anomalies.html', anomalies=anomalies.to_dict(orient="records"))

# Route: Generate and Download Report
@app.route('/generate_report')
def generate_report():
    report_path = 'A:/Project/data/siem_report.txt'
    return send_file(report_path, as_attachment=True)

# Route to render the zta.html page (Login page)
@app.route('/zta')
def zta():
    return render_template('zta.html')

# POST Route to handle ZTA authentication
@app.route('/zta_authenticate', methods=['POST'])
def zta_authenticate():
    
    username = request.form['username']
    password = request.form['password']

    
    user_db = {
        "admin": "securepassword",
        "employee": "password123",
    }

    
    if username in user_db and user_db[username] == password:
        session['zta_user'] = username  
        return redirect(url_for('zta_dashboard'))
    else:
        return "<h1>Access Denied</h1><a href='/zta'>Back</a>"

# Route for Zero Trust Dashboard (or OTP logic)
@app.route('/zta_dashboard')
def zta_dashboard():
    
    if 'zta_user' in session:
        return render_template('zta_dashboard.html', user=session['zta_user'])
    else:
        return redirect(url_for('zta'))  
    
# Route for network.html
@app.route('/network')
def network():
    return render_template('network.html')

# Route to serve logs as JSON data
@app.route('/logs_chart_data')
def logs_chart_data():
    logs = pd.read_csv('A:/Project/data/logs.txt', sep="|", header=None, names=["Timestamp", "Source", "Action", "Status"])
    logs_count = logs["Source"].value_counts().to_dict()  
    return json.dumps(logs_count)

# Route to serve dashboard data
@app.route('/dashboard_data')
def dashboard_data():
    logs = pd.read_csv('A:/Project/data/logs.txt', sep="|", header=None)
    anomalies = pd.read_csv('A:/Project/data/anomalies.txt', sep="|")
    return json.dumps({
        'total_logs': len(logs),
        'total_anomalies': len(anomalies),
    })

if __name__ == "__main__":
    app.run(debug=True)
