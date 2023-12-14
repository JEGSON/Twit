import tweepy
from tweepy import OAuthHandler
import requests
from io import BytesIO

# Set your Twitter API credentials
consumer_key = 'a5auUL8f30U0jwCCoJQFpg34s'
consumer_secret = 'J8A3eVl9qPjxCdKEpwuFNpHdWdaK13EuA1fLiFLgySsr1UAa70'
access_token = '1118274288849752069-FBfvEc7e9wit0YBbvBaJrBtuTSYXXk'
access_secret = 'eV9V9rDa6ccQQpOIpKVRIPiKqniV6Y0hcOZsRwFWm4oes'

# Authenticate with the Twitter API
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# Function to download a random image from the internet
def get_random_image_url():
    # Replace this with a service or website that provides random images
    # For example, using the Unsplash API to get a random photo
    response = requests.get('https://source.unsplash.com/random')
    return response.url

# Download a random image from the internet
image_url = get_random_image_url()
image_response = requests.get(image_url)

# Media Upload Example
try:
    # Open the image file using BytesIO
    image_file = BytesIO(image_response.content)

    # Upload media
    media = api.media_upload(filename='random_image.jpg', file=image_file)

    # Tweet with the uploaded media
    tweet_text = 'Check out this random image!'
    tweet = api.update_status(status=tweet_text, media_ids=[media.media_id])

    print(f"Tweet successfully posted with media! Tweet ID: {tweet.id}")

except tweepy.TweepError as e:
    print(f"Error uploading media: {e}")