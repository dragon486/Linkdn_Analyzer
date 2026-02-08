import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Wavess 1.0 – LinkedIn Growth Analyzer", layout="wide")

st.title("Wavess 1.0 – LinkedIn Growth Analyzer")
st.markdown("Analyze LinkedIn post performance & audience relevance using AI.")

# Loading CSV reports
post_df = pd.read_csv("data/post_analysis.csv")
audience_df = pd.read_csv("data/audience_analysis.csv")
suggestions_df = pd.read_csv("data/suggestions.csv")

# ---------------- POST ANALYSIS ----------------
st.header("📊 Post Performance Analysis")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Sentiment Score", round(post_df["sentiment"][0], 2))

with col2:
    st.metric("Performance Score", round(post_df["performance_score"][0], 2))

with col3:
    hashtags = post_df["hashtags"][0]

    if isinstance(hashtags, str) and hashtags.strip() != "":
        hashtag_count = len(hashtags.split(","))
    else:
        hashtag_count = 0
        st.metric("Hashtag Count", hashtag_count)


st.subheader("Post Summary")
st.write(post_df)

# ---------------- AUDIENCE ANALYSIS ----------------
st.header("🎯 Audience Relevance Ranking")

st.write(audience_df)

# ---------------- CHART ----------------
st.subheader("Audience Relevance Chart")

fig, ax = plt.subplots(figsize=(6, 3))  

ax.barh(audience_df["name"], audience_df["relevance_score"])
ax.set_xlabel("Relevance Score")
ax.set_ylabel("Audience")
ax.set_title("Audience Relevance")

st.pyplot(fig, use_container_width=False)

st.header("🤖 AI Improvement Suggestions")

for tip in suggestions_df["suggestions"]:
    st.write("•", tip)


st.success("Analysis Completed Successfully 🚀")
