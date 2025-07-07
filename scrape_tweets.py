import json
import subprocess

def fetch_tweets_snscrape(username="realDonaldTrump", max_results=100):
    cmd = [
        "snscrape",
        f"--max-results={max_results}",
        f"twitter-user:{username}",
        "--jsonl"
    ]
    tweets = []
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True)
    for line in proc.stdout:
        obj = json.loads(line)
        tweets.append({
            "time": obj["date"],
            "text": obj["content"]
        })
    proc.wait()
    with open("tweets.json", "w", encoding="utf-8") as f:
        json.dump(tweets, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    fetch_tweets_snscrape()
