# shortener/slack_bot.py

import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from urlshortener.shortener.utils import generate_short_url

slack_token = os.environ['xoxb-6672385283233-6662213692868-oL57pr3U63B1Q8GTKjXpsSHJ']
client = WebClient(token=slack_token)

def shorten_url_in_slack(long_url):
    short_url = generate_short_url(long_url)
    response = client.chat_postMessage(
        channel='#general',  # Change to your desired channel
        text=f"Shortened URL: {short_url}"
    )
    return short_url
