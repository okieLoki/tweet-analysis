from decouple import config
import pandas as pd
import tweepy

api_key = config('API_KEY')
api_key_secret = config('API_KEY_SECRET')
access_token = config('ACCESS_TOKEN')
access_token_secret = config('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

limit = 300
tweets = tweepy.Cursor(api.search_tweets, q='#RussiaUkraineWar', tweet_mode='extended', lang = 'en').items(limit)

columns = ['Time','USer', 'Tweet']
data = []

for tweet in tweets:
    data.append([tweet.created_at,tweet.user.screen_name, tweet.full_text])

df = pd.DataFrame(data, columns=columns)

df.to_csv('tweets.csv')
