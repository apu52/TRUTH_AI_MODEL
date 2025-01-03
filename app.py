from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client['truth_ai_db']
collection = db['tweets']

@app.route('/get_twitter_data', methods=['GET'])
def get_twitter_data():
    tweets = list(collection.find({"source": "twitter"}, {'_id': 0}))
    return jsonify(tweets)

@app.route('/get_youtube_data', methods=['GET'])
def get_youtube_data():
    youtube_videos = list(collection.find({"source": "youtube"}, {'_id': 0}))
    return jsonify(youtube_videos)

@app.route('/get_instagram_data', methods=['GET'])
def get_instagram_data():
    instagram_posts = list(collection.find({"source": "instagram"}, {'_id': 0}))
    return jsonify(instagram_posts)

@app.route('/get_facebook_data', methods=['GET'])
def get_facebook_data():
    facebook_posts = list(collection.find({"source": "facebook"}, {'_id': 0}))
    return jsonify(facebook_posts)

if __name__ == '__main__':
    app.run(debug=True)
