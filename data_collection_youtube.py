import requests
import json

API_KEY = 'your_google_api_key'

def collect_youtube_data(query, max_results=50):
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={query}&maxResults={max_results}&key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        videos = response.json()['items']
        video_data = []
        for video in videos:
            video_data.append({
                'video_id': video['id']['videoId'],
                'title': video['snippet']['title'],
                'description': video['snippet']['description'],
                'published_at': video['snippet']['publishedAt'],
                'channel': video['snippet']['channelTitle']
            })
        return video_data
    else:
        return None

# Example usage
youtube_videos = collect_youtube_data("misinformation", 50)
print(json.dumps(youtube_videos, indent=2))
