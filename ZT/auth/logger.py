# auth/logger.py
import datetime

def log_event(event):
    try:
        with open("data/logs.txt", "a") as file:
            file.write(f"{datetime.datetime.now()} - {event}\n")
        print(f"Log entry added: {event}")  
    except Exception as e:
        print(f"Error writing to log file: {e}")
