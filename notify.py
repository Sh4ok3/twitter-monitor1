import os, json, requests

def send_pushplus(msg):
    token = os.getenv("PUSHPLUS_TOKEN")
    url = "https://www.pushplus.plus/send"
    payload = {
        "token": token,
        "title": "【舆情预警-测试】",
        "content": msg,
        "template": "txt"
    }
    resp = requests.post(url, json=payload)
    print("HTTP:", resp.status_code, resp.text)

if __name__ == "__main__":
    a = json.load(open("analysis.json", encoding="utf-8"))
    # 直接发送，无论 z 值
    send_pushplus(f"测试推送，当前 Z-score={a['z']}")
