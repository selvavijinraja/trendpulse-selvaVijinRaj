import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Task 1 — Setup (2 marks)
# -----------------------------

# Load the CSV file from Task 3
df = pd.read_csv("data/trends_analysed.csv")

# Create outputs/ folder if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# -----------------------------
# Task 2 — Chart 1: Top 10 Stories by Score (6 marks)
# -----------------------------

# Sort by score and take top 10
top10 = df.sort_values(by="score", ascending=False).head(10)

# Shorten titles longer than 50 characters
top10["short_title"] = top10["title"].apply(lambda x: x[:50] + "..." if len(x) > 50 else x)

# Horizontal bar chart
plt.figure(figsize=(10,6))
plt.barh(top10["short_title"], top10["score"], color="skyblue")
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")
plt.gca().invert_yaxis()  # Highest score at top
plt.tight_layout()
plt.savefig("outputs/chart1_top_stories.png")
plt.close()

# -----------------------------
# Task 3 — Chart 2: Stories per Category (6 marks)
# -----------------------------

# Count stories per category
category_counts = df.groupby("category")["title"].count()

# Bar chart with different colors
plt.figure(figsize=(10,6))
plt.bar(category_counts.index, category_counts.values, color=plt.cm.tab10.colors)
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Number of Stories per Category")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/chart2_categories.png")
plt.close()

# -----------------------------
# Task 4 — Chart 3: Score vs Comments (6 marks)
# -----------------------------

plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x="score", y="num_comments", hue="is_popular", palette="Set1", alpha=0.7)
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Number of Comments (Popular vs Non-Popular)")
plt.legend(title="Is Popular")
plt.tight_layout()
plt.savefig("outputs/chart3_scatter.png")
plt.close()

# -----------------------------
# Bonus — Dashboard (+3 marks)
# -----------------------------

fig, axes = plt.subplots(1, 3, figsize=(18,6))

# Chart 1 in dashboard
axes[0].barh(top10["short_title"], top10["score"], color="skyblue")
axes[0].set_xlabel("Score")
axes[0].set_ylabel("Story Title")
axes[0].set_title("Top 10 Stories by Score")
axes[0].invert_yaxis()

# Chart 2 in dashboard
axes[1].bar(category_counts.index, category_counts.values, color=plt.cm.tab10.colors)
axes[1].set_xlabel("Category")
axes[1].set_ylabel("Number of Stories")
axes[1].set_title("Stories per Category")
axes[1].tick_params(axis='x', rotation=45)

# Chart 3 in dashboard
sns.scatterplot(data=df, x="score", y="num_comments", hue="is_popular", palette="Set1", alpha=0.7, ax=axes[2])
axes[2].set_xlabel("Score")
axes[2].set_ylabel("Number of Comments")
axes[2].set_title("Score vs Comments")
axes[2].legend(title="Is Popular")

fig.suptitle("TrendPulse Dashboard", fontsize=16)
plt.tight_layout()
plt.savefig("outputs/dashboard.png")
plt.close()

print("All charts saved in outputs/ folder")
