
# auth/authenticate.py
import sqlite3
import bcrypt
import random
import smtplib
from email.mime.text import MIMEText
import getpass
from logger import log_event  

def send_otp(email):
    otp = random.randint(100000, 999999)
    msg = MIMEText(f"Your OTP is: {otp}")
    msg["Subject"] = "Your OTP Code"
    msg["From"] = "gyan2623@gmail.com"
    msg["To"] = email

    
    with smtplib.SMTP("smtp.gmail.com", 587) as server:  

        server.starttls()
        server.login("gyan2623@gmail.com", "nbvu yrgi pnlq tlaz")
        server.sendmail("gyan2623@gmail.com", email, msg.as_string())
    
    
    log_event(f"OTP sent to {email}")
    return otp


def authenticate_user():
    print("Starting authentication script...")  
    
    username = input("Enter your username: ")
    print(f"Username entered: {username}")  
    password = getpass.getpass("Enter your password: ")
    print(f"Password entered: {password}")  
    
    print("Log entry for starting authentication process added")

    
    conn = sqlite3.connect("data/zta_users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password, role FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()

    if result and bcrypt.checkpw(password.encode(), result[0]):  # Encoding the entered password

        log_event(f"Password verified for user {username}")  # Log successful password verification
        print("Password verified.")

        
        email = input("Enter your email for OTP verification: ")
        otp_sent = send_otp(email)
        otp_entered = int(input("Enter the OTP sent to your email: "))
        
        if otp_entered == otp_sent:
            log_event(f"OTP sent to {email}")
            log_event(f"User {username} authenticated successfully")  
            print("Authenticated successfully!")
        else:
            log_event(f"User {username} failed OTP verification")  
            print("Invalid OTP. Authentication failed.")
    else:
        log_event(f"Invalid login attempt for username {username}")  
        print("Invalid username or password.")


print("Starting authentication script...")

authenticate_user()