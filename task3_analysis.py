import pandas as pd
import numpy as np

# -----------------------------
# 1 — Load and Explore
# -----------------------------
df = pd.read_csv("data/trends_clean.csv")

print("First 5 rows:\n", df.head())
print("Shape:", df.shape)

avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()
print("Average score:", avg_score)
print("Average num_comments:", avg_comments)

# -----------------------------
# 2 — Basic Analysis with NumPy
# -----------------------------
scores = df["score"].values
comments = df["num_comments"].values
categories = df["category"].values
titles = df["title"].values

# Mean, Median, Std Dev
print("Mean score:", np.mean(scores))
print("Median score:", np.median(scores))
print("Std Dev score:", np.std(scores))

# Highest and Lowest score
print("Highest score:", np.max(scores))
print("Lowest score:", np.min(scores))

# Category with most stories
unique, counts = np.unique(categories, return_counts=True)
most_common_category = unique[np.argmax(counts)]
most_common_count = counts[np.argmax(counts)]
print("Category with most stories:", most_common_category, "(", most_common_count, "stories )")

# Story with most comments
max_comments_index = np.argmax(comments)
print("Story with most comments:", titles[max_comments_index], 
      "with", comments[max_comments_index], "comments")

# -----------------------------
# 3 — Add New Columns
# -----------------------------
df["engagement"] = df["num_comments"] / (df["score"] + 1)
df["is_popular"] = df["score"] > avg_score

print("New columns added: engagement, is_popular")
print(df.head())

# -----------------------------
# 4 — Save the Result
# -----------------------------
df.to_csv("data/trends_analysed.csv", index=False)
print("✅ Saved updated DataFrame to data/trends_analysed.csv")
