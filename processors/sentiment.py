from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

def sentiment_score(text):
    if not text:
        return 0.0
    return analyzer.polarity_scores(text).get("compound", 0.0)
