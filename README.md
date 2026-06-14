# 🛡️ LogHunter AI: Threat Investigator & Log Analyzer

LogHunter AI is a lightweight, automated security log analysis dashboard designed for modern SecOps. It parses server authentication logs, detects potential brute-force attack vectors using behavioral analysis, visualizes threat metrics, and provides automated mitigation strategies using Artificial Intelligence (OpenAI / Local LLMs via Ollama).

## 🚀 Features
- **Automated Log Parsing:** Efficiently reads and structures raw server authorization logs using optimized Regular Expressions (Regex) and Pandas.
- **Behavioral Threat Detection:** Automatically triggers critical alerts when failed login attempts cross user-defined thresholds from a single IP.
- **Interactive SOC Dashboards:** Dynamic visualizations built with Streamlit and Plotly to track targeted users and attacker infrastructure.
- **Next-Gen SecOps AI Analysis:** Integrates with OpenAI APIs or Local LLMs (Llama3/Mistral via Ollama) to output incident summaries and immediate defensive remediation steps.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Data Engineering:** Pandas, Regex (`re`)
- **Frontend Dashboard:** Streamlit
- **Data Visualization:** Plotly Express
- **AI Integration:** OpenAI SDK / Ollama API

## 💻 Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/minsarawishka/LogHunter-AI.git](https://github.com/minsarawishka/LogHunter-AI.git)
   cd LogHunter-AI