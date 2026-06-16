import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

df = pd.read_csv("data/youtube.csv")

# Take first 1000 titles for faster processing
sample = df.head(1000)

def get_sentiment(text):
    polarity = TextBlob(str(text)).sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

sample["Sentiment"] = sample["title"].apply(get_sentiment)

print(sample["Sentiment"].value_counts())

sample["Sentiment"].value_counts().plot(kind="bar")

plt.title("Sentiment Analysis of Video Titles")
plt.xlabel("Sentiment")
plt.ylabel("Count")

plt.show()