import re
import nltk
import pandas as pd
from nltk.corpus import stopwords
from textblob import TextBlob


nltk.download('stopwords')

# ---------------- POST TEXT ----------------

post_text = """
🌍 We’re proud to announce the launch of our AI for Climate Resilience Program.

AI already powers everything we do at Klarna — and now we’re turning that same expertise toward the front lines of climate change. We take pride in our legacy as a climate leader, and we’re committed to driving positive change for the future. The AI for Climate Resilience Program will support pioneering projects that harness artificial intelligence to help climate-vulnerable communities adapt and thrive.

This is technology in service of both people and the planet.

This program will support local, practical, and community-owned solutions. From strengthening food security and improving health systems to building coastal resilience in the face of climate change.

What’s on offer:
💸 Grants of up to $300,000
🧑‍🎓 Mentorship, training, and a supportive community of practice

We encourage applications from organizations working to reduce vulnerability of local communities to climate-related risks in low- and middle-income countries. We welcome early stage applications as well, from teams that need support in developing technical details further. Whether you’re using AI to support smallholder farmers, build early warning systems, or translate complex risk data into community action plans, we want to hear from you!

Find out more about the program and apply here 👉 https://lnkd.in/d3tFWFHJ
"""

# ---------------- TEXT CLEANING ----------------

def clean_text(text):
    text = re.sub(r"http\S+|www\S+", "", text)
    text = re.sub(r"[^a-zA-Z ]", " ", text)
    text = text.lower()

    words = text.split()
    stop_words = set(stopwords.words("english"))
    words = [w for w in words if w not in stop_words]

    return words

words = clean_text(post_text)
print("Cleaned Words Sample:", words[:20])

# ---------------- HASHTAG EXTRACTION ----------------

hashtags = re.findall(r"#\w+", post_text)
print("Hashtags:", hashtags)

# ---------------- SENTIMENT ANALYSIS ----------------

blob = TextBlob(post_text)
sentiment = blob.sentiment.polarity
subjectivity = blob.sentiment.subjectivity

print("Sentiment Polarity:", sentiment)
print("Subjectivity:", subjectivity)

# ---------------- PERFORMANCE SCORING ----------------

keyword_score = min(len(words), 80) * 0.08   # cap influence
hashtag_score = len(hashtags) * 2
sentiment_score = sentiment * 10

performance_score = round(keyword_score + hashtag_score + sentiment_score, 2)


print("Predicted Performance Score:", performance_score)

# ---------------- AI IMPROVEMENT SUGGESTIONS ----------------

def generate_suggestions(sentiment, hashtags, keywords):
    suggestions = []

    if sentiment < 0.2:
        suggestions.append("Add more emotional or inspiring language to increase engagement.")

    if len(hashtags) < 3:
        suggestions.append("Use at least 3–5 trending hashtags for better reach.")

    if len(keywords) < 10:
        suggestions.append("Include more strong keywords related to your product, industry, and value proposition.")

    suggestions.append("Add a call-to-action such as a question or invitation to comment.")
    suggestions.append("Consider adding numbers, stats, or results to increase credibility.")

    return suggestions

suggestions = generate_suggestions(sentiment, hashtags, words)

print("\nAI Post Improvement Suggestions:")
for s in suggestions:
    print("-", s)

# ---------------- SAVE POST ANALYSIS CSV ----------------

post_df = pd.DataFrame({
    "text_sample": [post_text[:100]],
    "hashtags": [",".join(hashtags)],
    "sentiment": [sentiment],
    "performance_score": [performance_score]
})

post_df.to_csv("data/post_analysis.csv", index=False)

pd.DataFrame({"suggestions": suggestions}).to_csv("data/suggestions.csv", index=False)

# ---------------- AUDIENCE ANALYSIS ----------------

df = pd.read_csv("data/audience.csv")

def score_audience(row):
    score = 0

    if row["role"] in ["Marketing Manager", "Founder", "Sales Manager"]:
        score += 5

    if row["seniority"] in ["Senior", "Mid"]:
        score += 4

    if row["company_type"] in ["SaaS", "Startup"]:
        score += 3

    return score

df["relevance_score"] = df.apply(score_audience, axis=1)

df = df.sort_values(by="relevance_score", ascending=False)

print("\nAudience Relevance Ranking:\n")
print(df)

df.to_csv("data/audience_analysis.csv", index=False)

print("\nCSV Reports Generated Successfully")
