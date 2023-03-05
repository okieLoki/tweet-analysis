## Sentiment Analysis of Russia Ukraine Tweets 

This project aims to perform sentiment analysis on Twitter data related to the Russia-Ukraine war. The goal is to predict whether a tweet has a positive or negative sentiment based on its text. The project consists of three components:

- Gathering Twitter data using the Tweepy library and filtering tweets based on a specific hashtag (#RussiaUkraineWar). The gathered data is stored in a CSV file.

- Preprocessing the data, performing sentiment analysis using the VADER sentiment analysis library, and training a Naive Bayes classifier on the preprocessed data. The trained classifier is saved using the pickle library.

- Creating a web application using Streamlit to allow users to input their own tweets and receive a sentiment prediction using the trained classifier.

###  Tools Used

- Python 3.8
- pandas
- tweepy
- nltk
- scikit-learn
- matplotlib
- pickle
- Streamlit


### Concept behind the Model

The model uses the VADER (Valence Aware Dictionary and sEntiment Reasoner) library for sentiment analysis. VADER is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media. It uses a combination of sentiment lexicons, grammatical rules, and word-order patterns to determine the sentiment of a piece of text.

After preprocessing the data, we trained a Naive Bayes classifier on the preprocessed data using scikit-learn. Naive Bayes is a probabilistic algorithm that is commonly used for sentiment analysis tasks. It calculates the probability of a tweet belonging to a particular class (positive or negative) based on the frequency of words in the tweet. The classifier then chooses the class with the highest probability as the predicted sentiment.

The web application was created using Streamlit, a Python library for building interactive web applications. The user can input a tweet, and the application uses the trained Naive Bayes classifier to predict its sentiment. The user is then presented with a sentiment label of "Positive" or "Negative".
