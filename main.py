import requests
import sys

message_text = 'Hey!'

webhook_url = sys.argv[1]

title = 'New commit'

username = 'Github bot'

color = 000000

payload = {
    'content': message_text,
    'username': username,
    'tts': False,
    'embeds': [{
        'title': title,
        'description': "New commit at you repo. Check you github repository",
        'color': color
    }]
}

response = requests.post(webhook_url, json=payload)

if response.status_code == 204:
    print('Message sent!')