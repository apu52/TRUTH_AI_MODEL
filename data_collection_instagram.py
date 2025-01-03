import requests
import json

ACCESS_TOKEN = 'your_instagram_access_token'
INSTAGRAM_ACCOUNT_ID = 'your_instagram_account_id'

def collect_instagram_data(query, max_results=50):
    url = f"https://graph.facebook.com/v12.0/{INSTAGRAM_ACCOUNT_ID}/media?fields=id,caption,media_type,media_url,thumbnail_url,timestamp&access_token={ACCESS_TOKEN}"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()['data']
        post_data = []
        for post in posts:
            if query.lower() in post.get('caption', '').lower():
                post_data.append({
                    'id': post['id'],
                    'caption': post.get('caption', ''),
                    'media_url': post.get('media_url', ''),
                    'timestamp': post.get('timestamp', '')
                })
        return post_data
    else:
        return None


instagram_posts = collect_instagram_data("misinformation", 50)
print(json.dumps(instagram_posts, indent=2))
