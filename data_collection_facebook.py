import requests
import json

ACCESS_TOKEN = 'your_facebook_access_token'
FACEBOOK_PAGE_ID = 'your_facebook_page_id'

def collect_facebook_data(query, max_results=50):
    url = f"https://graph.facebook.com/{FACEBOOK_PAGE_ID}/posts?fields=id,message,created_time&access_token={ACCESS_TOKEN}"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()['data']
        post_data = []
        for post in posts:
            if query.lower() in post.get('message', '').lower():
                post_data.append({
                    'id': post['id'],
                    'message': post.get('message', ''),
                    'created_time': post.get('created_time', '')
                })
        return post_data
    else:
        return None


facebook_posts = collect_facebook_data("misinformation", 50)
print(json.dumps(facebook_posts, indent=2))
