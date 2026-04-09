import pandas as pd
import json

# 1 — Load the JSON File
df = pd.read_json("data/trends_20260403.json")
print(f"Loaded {len(df)} stories from data/trends_20260403.json")

# 2 — Clean the Data

# Duplicates — remove rows with same post_id
df = df.drop_duplicates(subset='post_id')
print(f"After removing duplicates: {len(df)}")

# Missing values — drop rows where post_id, title, or score is missing
df = df.dropna(subset=['post_id', 'title', 'score'])
print(f"After removing nulls: {len(df)}")

# Data types — make sure score and num_comments are integers
df['score'] = df['score'].astype(int)
df['num_comments'] = df['num_comments'].astype(int)

# Low quality — remove stories where score < 5
df = df[df['score'] >= 5]
print(f"After removing low scores: {len(df)}")

# Whitespace — strip extra spaces from title column
df['title'] = df['title'].str.strip()

# 3 — Save as CSV
df.to_csv("data/trends_clean.csv", index=False)
print(f"\nSaved {len(df)} rows to data/trends_clean.csv")

# Quick summary: how many stories per category
summary = df['category'].value_counts()
print("\nStories per category:")
print(summary)