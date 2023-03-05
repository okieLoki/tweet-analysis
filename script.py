from decouple import config
import re
import pandas as pd
import tweepy

def cleanText(tweet):
    if hasattr(tweet, 'retweeted_status'):
        try:
            text = tweet.retweeted_status.extended_tweet.full_text
        except AttributeError:
            text = tweet.retweeted_status.full_text
    else:
        try:
            text = tweet.extended_tweet.full_text
        except AttributeError:
            text = tweet.full_text
    text = re.sub(r'@[A-Za-z0-9]+', '', text)
    text = re.sub(r'(RT[\s]+|:[\s]+)', '', text)
    text = re.sub(r'#', '', text)
    text = re.sub(r'https?:\/\/\S+', '', text)
    return text

if __name__ == '__main__':

    api_key = config('API_KEY')
    api_key_secret = config('API_KEY_SECRET')
    access_token = config('ACCESS_TOKEN')
    access_token_secret = config('ACCESS_TOKEN_SECRET')

    auth = tweepy.OAuthHandler(api_key,api_key_secret)
    auth.set_access_token(access_token,access_token_secret)

    api = tweepy.API(auth)

    limit = 1000
    tweets = tweepy.Cursor(api.search_tweets, q='#RussiaUkraineWar', tweet_mode='extended', lang = 'en').items(limit)

    columns = ['Tweet']
    data = []

    for tweet in tweets:
        final_tweet = cleanText(tweet)
        data.append([final_tweet])

    df = pd.DataFrame(data, columns=columns)

    df.to_csv('tweets2.csv')

