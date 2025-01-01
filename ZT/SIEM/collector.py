# A:\Project\ZT\SIEM\collector.py
import os
import time
import random


def collect_logs():
    
    if not os.path.exists("data"):
        os.makedirs("data")

    sources = ["Network", "User Behavior", "System Access"]
    actions = ["Login", "File Access", "Configuration Change", "Failed Login", "Data Transfer"]
    logs = []

    for _ in range(100):  # Simulate 100 logs
        source = random.choice(sources)
        action = random.choice(actions)
        status = "Success" if random.random() > 0.2 else "Failure"
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        logs.append(f"{timestamp} | {source} | {action} | {status}")
    
   
    with open("A:/Project/data/logs.txt", "w") as file:
        file.write("\n".join(logs))
    
    print("Logs collected and saved to A:/Project/data/logs.txt.")

if __name__ == "__main__":
    collect_logs()
