# 🚀 Wavess 1.0 – LinkedIn Growth Analyzer

**An AI-powered LinkedIn post analytics and audience relevance system** that analyzes post content using NLP, predicts engagement performance, ranks audience relevance based on ICP, and provides actionable improvement suggestions via an interactive dashboard.

---

## 📌 Project Overview

This project is a **prototype built for Task 1 – Wavess 1.0: LinkedIn Growth Solution.**

The system helps **marketing and growth teams** to:

- Understand how well a LinkedIn post might perform  
- Identify which audience segment is most relevant  
- Receive AI-powered content improvement suggestions  
- Visualize all insights through a real-time dashboard  

---

## 🎯 Features

### 1️⃣ Post Performance Analysis (NLP)

- Text cleaning & preprocessing  
- Hashtag extraction  
- Sentiment analysis  
- Engagement performance scoring  

---

### 2️⃣ Audience Relevance Scoring

- Role-based ICP scoring  
- Seniority evaluation  
- Company-type relevance ranking  

---

### 3️⃣ AI Improvement Suggestions

- Emotion & engagement optimization  
- Hashtag optimization  
- Call-to-action suggestions  
- Content enhancement recommendations  

---

### 4️⃣ Interactive Dashboard (Streamlit)

- Performance metrics  
- Audience ranking table  
- Visual charts  
- AI-generated improvement tips  

---

## 🧠 System Architecture

```text
app.py
   ↓
analysis.py  →  NLP + scoring + AI logic → CSV outputs
   ↓
dashboard.py →  Interactive visualization (Streamlit UI)
🛠 Tech Stack
Python 3

NLTK – text processing

TextBlob – sentiment analysis

Pandas – data processing

Streamlit – dashboard UI

Matplotlib – visualization

📂 Project Structure
LinkedIn_Analyzer/
│
├── analysis.py        # Core AI + NLP + scoring engine
├── app.py             # Main pipeline runner
├── dashboard.py       # Streamlit dashboard UI
│
├── data/
│   ├── post_analysis.csv
│   ├── audience.csv
│   ├── audience_analysis.csv
│   ├── suggestions.csv
│
└── README.md
🚀 How to Run
1️⃣ Install Dependencies
pip install nltk pandas textblob streamlit matplotlib
2️⃣ Run Analysis Pipeline
python app.py
This generates structured CSV outputs.

3️⃣ Launch Dashboard
streamlit run dashboard.py
Open the displayed browser link.

📊 Sample Output
Post performance score

Sentiment score

Hashtag count

Audience relevance ranking

AI-powered improvement suggestions

Visual charts

🏆 Key Learning Outcomes
Natural Language Processing (NLP)

Data-driven growth analytics

ICP-based audience targeting

Machine-learning inspired scoring systems

Dashboard development

Modular software architecture

🔮 Future Improvements
Multi-post comparison

AI-based post rewriting

Auto LinkedIn scraping

Viral probability prediction

Real-time API integration

👨‍💻 Author
Adel Muhammed

📧 Email: adelmuhammed786@gmail.com
🔗 GitHub: https://github.com/dragon486
