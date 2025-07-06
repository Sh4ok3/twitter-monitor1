import os, json, requests

def send_email(msg):
    url = "https://api.sendgrid.com/v3/mail/send"
    headers = {
        "Authorization": f"Bearer {os.getenv('EMAIL_API_KEY')}",
        "Content-Type": "application/json"
    }
    payload = {
        "personalizations":[{"to":[{"email":"your_email@example.com"}]}],
        "from":{"email":"noreply@monitor.com"},
        "subject":"【舆情预警】情感异常检测",
        "content":[{"type":"text/plain","value":msg}]
    }
    requests.post(url, headers=headers, json=payload)

if __name__ == "__main__":
    a = json.load(open("analysis.json", encoding="utf-8"))
    if a["z"] < -3:
        send_email(f"检测到 Z-score={a['z']:.2f}，请关注。")
