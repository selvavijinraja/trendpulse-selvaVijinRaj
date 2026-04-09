import requests
import time
import os
import json
from datetime import datetime

BASE_URL = "https://hacker-news.firebaseio.com/v0"
headers = {"User-Agent": "TrendPulse/1.0"}

# Categories and keywords
categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

all_stories = []

# Step 1: Get top story IDs
try:
    response = requests.get(f"{BASE_URL}/topstories.json", headers=headers)
    story_ids = response.json()[:500]
    print(f"Fetched {len(story_ids)} story IDs.")
except Exception as e:
    print("Failed to fetch top stories:", e)
    story_ids = []

# Step 2: Loop through categories
for i, (category, keywords) in enumerate(categories.items()):

    count = 0

    for story_id in story_ids:

        if count >= 25:
            break

        try:
            r = requests.get(f"{BASE_URL}/item/{story_id}.json", headers=headers, timeout=10)

            if r.status_code != 200:
                print(f"Failed request for story {story_id}: status {r.status_code}")
                continue

            story = r.json()

            if story is None:
                continue

        except Exception as e:
            print(f"Error fetching story {story_id}: {e}")
            continue

        title = story.get("title", "").lower()

        # Keyword matching
        if any(keyword in title for keyword in keywords):

            collected_story = {
                "post_id": story.get("id"),
                "title": story.get("title"),
                "category": category,
                "score": story.get("score", 0),
                "num_comments": story.get("descendants", 0),
                "author": story.get("by"),
                "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            all_stories.append(collected_story)
            count += 1

    print(f"  [{category}] collected {count} stories.")

    # Wait 2 seconds after each category (except the last one)
    if i < len(categories) - 1:
        time.sleep(2)

# Step 3: Save JSON
os.makedirs("data", exist_ok=True)

date_str = datetime.now().strftime("%Y%m%d")
filename = f"data/trends_{date_str}.json"

with open(filename, "w") as f:
    json.dump(all_stories, f, indent=2)

print(f"Collected {len(all_stories)} stories. Saved to {filename}")