import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/youtube.csv")

top_channels = df["channel_title"].value_counts().head(10)

plt.figure(figsize=(10,5))
top_channels.plot(kind="bar")

plt.title("Top 10 YouTube Channels")
plt.xlabel("Channel Name")
plt.ylabel("Number of Trending Videos")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()