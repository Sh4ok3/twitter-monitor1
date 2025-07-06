import json, numpy as np
from transformers import pipeline

sentiment = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

def score(text):
    r = sentiment(text[:512])[0]
    stars = int(r["label"].split()[0])
    return stars / 5.0

if __name__ == "__main__":
    data = json.load(open("cleaned.json", encoding="utf-8"))
    scores = [score(item["text"]) for item in data]
    mean, std = np.mean(scores), np.std(scores)
    today = scores[0] if scores else mean
    z = (today - mean) / std if std else 0
    result = {"mean": mean, "std": std, "today": today, "z": z}
    with open("analysis.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
