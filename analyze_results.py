# Name: Manasseh M | Roll: 727823tucy025

from datetime import datetime
import os

print("=== ANALYZE RESULTS SCRIPT ===")
print("Roll No:", "727823tucy025")
print("Timestamp:", datetime.now())

files = [f for f in os.listdir() if f.startswith("results_")]

print(f"[+] Total result files found: {len(files)}")

for file in files:
    with open(file, "r") as f:
        lines = f.readlines()
        print(f"{file} → {len(lines)} links")
