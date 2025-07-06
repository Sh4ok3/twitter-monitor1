import os, json, requests

def send_pushplus(msg):
    token = os.getenv("PUSHPLUS_TOKEN")
    url = "https://www.pushplus.plus/send"
    payload = {
        "token": token,
        "title": "【舆情预警】情感异常检测",
        "content": msg,
        "template": "txt"
    }
    resp = requests.post(url, json=payload)
    if resp.status_code != 200 or resp.json().get("code") != 200:
        print("PushPlus 发送失败：", resp.text)

if __name__ == "__main__":
    # 读取分析结果
    a = json.load(open("analysis.json", encoding="utf-8"))
    # 当 z-score 低于 -3 时才推送
    if a["z"] < -3:
        msg = f"检测到 Z-score={a['z']:.2f}，可能有重大事件，请及时关注。"
        send_pushplus(msg)
