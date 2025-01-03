from kafka import KafkaProducer
import json
from data_collection_twitter import collect_tweets
from data_collection_youtube import collect_youtube_data
from data_collection_instagram import collect_instagram_data
from data_collection_facebook import collect_facebook_data

# Initialize Kafka Producer
producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Send data to Kafka topic
def send_to_kafka(data, topic='truth_ai_topic'):
    producer.send(topic, data)
    producer.flush()

# Collect data from all platforms and send to Kafka
def collect_and_send_to_kafka(query):
    # Twitter
    twitter_data = collect_tweets(query)
    send_to_kafka(twitter_data, topic='truth_ai_twitter')

    # YouTube
    youtube_data = collect_youtube_data(query)
    send_to_kafka(youtube_data, topic='truth_ai_youtube')

    # Instagram
    instagram_data = collect_instagram_data(query)
    send_to_kafka(instagram_data, topic='truth_ai_instagram')

    # Facebook
    facebook_data = collect_facebook_data(query)
    send_to_kafka(facebook_data, topic='truth_ai_facebook')

# Example usage
collect_and_send_to_kafka("misinformation")
