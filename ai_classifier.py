import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def classify_alert(alert_text):
    prompt = f"""
You are a SOC analyst.

Classify the following alert as:
- BENIGN
- SUSPICIOUS
- MALICIOUS

Alert:
{alert_text}

Respond with only one word.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )

    result = response.json()
    return result["response"].strip()

if __name__ == "__main__":
    test_alert = "User account created on Windows host"
    classification = classify_alert(test_alert)

    print("Alert:", test_alert)
    print("Classification:", classification)