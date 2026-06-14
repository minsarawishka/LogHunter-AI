import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    client = OpenAI(api_key=api_key)
    MODEL_NAME = "gpt-4o-mini"
else:
    client = OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama"
    )
    MODEL_NAME = "llama3"

def analyze_logs_with_ai(logs_df):
    if logs_df.empty:
        return "No suspicious logs found to analyze."
    
    logs_text = logs_df.to_string(index=False)
    
    prompt = f"You are an expert Cybersecurity Analyst. Analyze these suspicious brute-force logs and provide a concise summary of the attack, threat level, and actionable mitigation steps:\n\n{logs_text}"
    
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": "You are a helpful cybersecurity assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI Analysis Error: {e}\n\n(Tip: If you are trying to use local AI, ensure Ollama is running with the '{MODEL_NAME}' model installed.)"