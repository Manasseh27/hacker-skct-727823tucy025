# Name: Manasseh M | Roll: 727823tucy025

from datetime import datetime
import tool_main

print("=== RUN TOOL SCRIPT ===")
print("Roll No:", "727823tucy025")
print("Timestamp:", datetime.now())

# predefined test query
query = 'intitle:"index of" password'

results = tool_main.google_dork_search(query)
tool_main.save_results(results)

print("[+] Tool execution completed")
