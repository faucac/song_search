import requests
import json
from base64 import b64encode
from datetime import datetime


def create_wp_draft(title, html, keys):
    url = "https://songpier.com//wp-json/wp/v2/posts"
    user = keys['wp_user']
    password = keys['wp_password']
    credentials = str(user) + ':' + str(password)
    token = b64encode(credentials.encode())
    header = {'Authorization': 'Basic ' + token.decode('utf-8')}
    post = {
        'title': title,
        'status': 'draft',
        'content': html,
        'categories': 1,  # category ID
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    print("Creating wordpress draft...")
    print(post)

    requests.post(url, headers=header, json=post)

    return
