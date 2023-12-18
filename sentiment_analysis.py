# sentiment_analysis.py
from nltk.sentiment import SentimentIntensityAnalyzer

def perform_sentiment_analysis(text):
    sia = SentimentIntensityAnalyzer()
    compound_score = sia.polarity_scores(text)['compound']
    sentiment_label = 1 if compound_score > 0 else 0
    return sentiment_label
