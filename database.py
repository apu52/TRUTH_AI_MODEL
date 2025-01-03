from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['truth_ai_db']
collection = db['tweets']

# Insert tweet into MongoDB
def insert_tweet(tweet):
    collection.insert_one(tweet)

# Example usage
from data_collection import collect_tweets
tweets = collect_tweets("misinformation", 50)
insert_tweet(tweets[0])
