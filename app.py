import analysis
import pandas as pd

print("\nLinkedIn Growth Analyzer Started...\n")

# Load post analysis output
post_df = pd.read_csv("data/post_analysis.csv")

print("📊 Post Performance Analysis Result:\n")
print(post_df)

print("\nAnalysis Completed Successfully!")
