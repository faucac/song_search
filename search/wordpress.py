import requests
import json
from base64 import b64encode
from datetime import datetime


def create_wp_draft(title, html, keys):
    url = "https://songpier.com//wp-json/wp/v2/posts"
    user = keys['wp_user']
    password = keys['wp_password']
    credentials = str(user) + ':' + str(password)
    token = b64encode(credentials.encode('utf-8')).decode('ascii')
    header = {'Authorization': 'Basic ' + token}
    post = {
        'title': title,
        'status': 'draft',
        'content': html,
        'categories': 1,  # category ID
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    print("Creating wordpress draft...")
    print("Requesting")

    response = requests.post(url, json=post, auth=(user, password))#, headers=header)
    
    print(response.json())

    if response.status_code==401 or response.status_code=="401":
        response = requests.post(url, json=post, headers=header)

        print(response.json())

    
    return
