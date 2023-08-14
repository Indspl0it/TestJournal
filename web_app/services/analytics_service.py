```python
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sns
from web_app.models import Journal, Mood

def analyze_mood(user_id):
    moods = Mood.query.filter_by(user_id=user_id).all()
    mood_list = [mood.mood for mood in moods]
    mood_count = {mood: mood_list.count(mood) for mood in mood_list}
    return mood_count

def analyze_sentiment(user_id):
    entries = Journal.query.filter_by(user_id=user_id).all()
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = [sia.polarity_scores(entry.text) for entry in entries]
    return sentiment_scores

def plot_mood(mood_count):
    plt.figure(figsize=(10, 5))
    sns.barplot(list(mood_count.keys()), list(mood_count.values()))
    plt.title('Mood Distribution')
    plt.xlabel('Mood')
    plt.ylabel('Count')
    plt.show()

def plot_sentiment(sentiment_scores):
    positive_scores = [score['pos'] for score in sentiment_scores]
    negative_scores = [score['neg'] for score in sentiment_scores]
    neutral_scores = [score['neu'] for score in sentiment_scores]
    plt.figure(figsize=(10, 5))
    plt.plot(positive_scores, label='Positive')
    plt.plot(negative_scores, label='Negative')
    plt.plot(neutral_scores, label='Neutral')
    plt.title('Sentiment Analysis Over Time')
    plt.xlabel('Entry Number')
    plt.ylabel('Sentiment Score')
    plt.legend()
    plt.show()
```