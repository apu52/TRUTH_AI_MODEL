from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client['truth_ai_db']
collection = db['tweets']


def insert_tweet(tweet):
    collection.insert_one(tweet)


from data_collection import collect_tweets
tweets = collect_tweets("misinformation", 50)
insert_tweet(tweets[0])
