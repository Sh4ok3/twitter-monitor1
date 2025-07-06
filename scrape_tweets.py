import os, json
import tweepy

def fetch_tweets(username="realDonaldTrump", max_results=100):
    client = tweepy.Client(bearer_token=os.getenv("TWITTER_BEARER_TOKEN"))
    user = client.get_user(username=username)
    tweets = client.get_users_tweets(user.data.id,
                                     max_results=max_results,
                                     tweet_fields=["created_at","text"])
    data = [{"time": t.created_at.isoformat(), "text": t.text}
            for t in tweets.data]
    with open("tweets.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    fetch_tweets()
