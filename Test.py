import random
import smtplib
import getpass
from email.mime.text import MIMEText

def send_otp(email):
    otp = random.randint(100000, 999999)
    msg = MIMEText(f"Your OTP is: {otp}")
    msg["Subject"] = "Your OTP Code"
    msg["From"] = "your-email@example.com"
    msg["To"] = email

    # Configure and send email (replace with real email server details)
    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login("your-email@example.com", "your-email-password")
        server.sendmail("your-email@example.com", email, msg.as_string())
    
    return otp

def authenticate_user():
    # Step 1: Basic username and password authentication
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")

    # This is a placeholder. Replace with actual authentication logic (e.g., database lookup)
    if username == "admin" and password == "securepassword":
        print("Password verified.")
        
        # Step 2: Send OTP for second factor authentication
        email = input("Enter your email for OTP verification: ")
        otp_sent = send_otp(email)
        
        # Verify OTP
        otp_entered = int(input("Enter the OTP sent to your email: "))
        if otp_entered == otp_sent:
            print("Authenticated successfully!")
        else:
            print("Invalid OTP. Authentication failed.")
    else:
        print("Invalid username or password.")

authenticate_user()
