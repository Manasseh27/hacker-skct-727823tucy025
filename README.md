# 🔍 Google Dorking Automation

## 📌 Project Details
- **Student Name:** Manasseh M  
- **Roll Number:** 727823tucy025  
- **Project Title:** Google Dorking Automation  
- **Category:** Cybersecurity  

---

## 🚀 Project Description
This project automates Google Dorking techniques to identify potentially sensitive information exposed on the internet. It executes advanced search queries (dorks), extracts links, and stores results for analysis.

---

## 🎯 Objectives
- Automate Google dork queries  
- Extract useful links from search results  
- Store results in structured format  
- Analyze multiple outputs  

---

## 🛠️ Tools & Technologies
- **OS:** Kali Linux  
- **Language:** Python 3  
- **Libraries:** requests, beautifulsoup4, colorama  
- **Tools:** Git, GitHub, VirtualBox  

---

## ⚙️ Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/Manasseh27/hacker-skct-727823tucy025.git
cd hacker-skct-727823tucy025/code

2. Install Dependencies
pip install requests beautifulsoup4 colorama
▶️ Usage
Run Main Tool
python3 tool_main.py
Run Pipeline Scripts
python3 setup_lab.py
python3 run_tool.py
python3 analyze_results.py
🧪 Test Cases
Test Case	Query	Output
1	intitle:"index of" password	3 links
2	site:example.com filetype:pdf	2 links
3	inurl:admin login	3 links
📊 Sample Output
Results saved in timestamped .txt files
Each execution generates unique output
🔄 Pipeline

The project includes a pipeline with three stages:

Setup Lab
Run Tool
Analyze Results

Defined in:

pipeline_727823tucy025.yml
⚠️ Error Encountered

Error: Failed to resolve 'www.google.com
'
Cause: Network misconfiguration
Solution: Added NAT adapter for internet access

🔐 Ethical Considerations

This project is intended for educational purposes only. All testing was performed in a controlled environment with authorized systems.

📌 GitHub Repository

🔗 https://github.com/Manasseh27/hacker-skct-727823tucy025

💡 Future Enhancements
Integration with real APIs
AI-based risk detection
Web dashboard visualization
