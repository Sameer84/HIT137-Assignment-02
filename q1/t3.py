import csv
from collections import Counter

# Read the text file
with open('./q1/merged_csv.txt', 'r') as file:
    text = file.read()

# Split the text into words
words = text.split()

# Count the occurrences of each word
word_counts = Counter(words)

# Get the top 30 most common words
top_30_words = word_counts.most_common(30)

# Write the top 30 words and their counts to a CSV file
with open('./q1/top_30_output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Word', 'Count'])
    writer.writerows(top_30_words)
