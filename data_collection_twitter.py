import tweepy
import json


consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'


auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)


def collect_tweets(keyword, count=100):
    tweets = tweepy.Cursor(api.search_tweets, q=keyword, lang="en").items(count)
    tweet_data = []
    
    for tweet in tweets:
        tweet_data.append({
            'id': tweet.id,
            'created_at': tweet.created_at,
            'text': tweet.text,
            'user': tweet.user.screen_name,
            'followers_count': tweet.user.followers_count
        })
    
    return tweet_data


tweets = collect_tweets("misinformation", 50)
print(json.dumps(tweets, indent=2))
