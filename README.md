# Twitter API Media Upload

This Python script demonstrates how to use the Twitter API to upload media (images) and post a tweet with the uploaded media. It uses the Tweepy library for interacting with the Twitter API.

## Prerequisites

Before running the script, make sure you have the following:

- Python installed on your machine
- Tweepy library installed (you can install it using `pip install tweepy`)

## Twitter API Credentials

To use this script, you need to set up a Twitter Developer account and obtain API credentials. Replace the placeholder values in the script with your actual credentials.

```python
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_secret = 'your_access_token_secret'

#HOW to Run
git clone https://github.com/your-username/twitter-api-media-upload.git
cd twitter-api-media-upload
#install dependencies 
pip install tweepy
#run the script
python twitter.py


Notes

The script fetches a random image from the internet using the Unsplash API. You can replace the get_random_image_url function with your preferred method of obtaining images.
If you encounter issues with media upload, check your Twitter Developer App permissions and ensure you are using valid API credentials.
