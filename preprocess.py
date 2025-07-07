
import re, json

def clean(text):
    # 去掉链接、@提及、#标签，去掉所有标点，然后按空白分词
    t = re.sub(r"http\S+|@\w+|#","", text)
    t = re.sub(r"[^\w\s]", "", t)
    return [w.lower() for w in t.split() if w]

if __name__ == "__main__":
    data = json.load(open("tweets.json", encoding="utf-8"))
    for item in data:
        item["tokens"] = clean(item["text"])
    with open("cleaned.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
