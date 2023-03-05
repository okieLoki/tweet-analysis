import streamlit as st
import pickle

with open('model.pkl', 'rb') as f:
    vectorizer, clf = pickle.load(f)

def app():

    st.title('Russia Ukraine Twitter Sentiment Analysis')

    tweet = st.text_input('Enter a tweet: ')
    if st.button('Submit'):
        if tweet:
            X_test_vect = vectorizer.transform([tweet])
            y_pred = clf.predict(X_test_vect)[0]
            if y_pred == 0:
                response = 'Negative'
            else:
                response = 'Positive'
            st.write(f'Sentiment: {response}')

if __name__ == '__main__':
    app()
