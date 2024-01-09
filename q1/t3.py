import csv
import time
from collections import Counter
from transformers import AutoTokenizer

start = time.process_time()

PRE_DIR_NAME = './q1'
INPUT_FILE = PRE_DIR_NAME + '/merged_csv.txt'
CHUNKS_DIRECTORY = PRE_DIR_NAME + '/chunks'
MODEL_NAME = 'dmis-lab/biobert-v1.1'


# # Read the text file
# with open('./q1/merged_csv.txt', 'r') as file:
#     text = file.read()

# # Split the text into words
# words = text.split()

# # Count the occurrences of each word
# word_counts = Counter(words)

# # Get the top 30 most common words
# top_30_words = word_counts.most_common(30)

# # Write the top 30 words and their counts to a CSV file
# with open('./q1/top_30_output.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Word', 'Count'])
#     writer.writerows(top_30_words)


def count_unique_tokens(file_path, model_name, top_n=30, chunk_size=800):
    start = time.process_time()
    # Load the AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Initialize an empty counter for token counts
    token_counts = Counter()

    # Read the text from the file in chunks
    with open(file_path, 'r', encoding='utf-8') as file:
        count = 0
        while True:
            count += 1
            if count % 10000 == 0:
                print(count / 1000, '/ 900', time.process_time() - start, 'seconds ')
            chunk = file.read(chunk_size)
            if not chunk:
                break
            # Tokenize the chunk and update token counts
            tokens = tokenizer.tokenize(tokenizer.decode(tokenizer.encode(chunk)))
            token_counts.update(tokens)

    # Get the top N tokens
    top_tokens = token_counts.most_common(top_n)

    # Print the count of unique tokens
    print(f'Number of unique tokens: {len(token_counts)}')

    # Print the top N tokens
    print(f'\nTop {top_n} tokens:')
    for token, count in top_tokens:
        print(f'{token}: {count}')

    # Export final_counter to CSV
    with open(PRE_DIR_NAME + '/most_common_30_AutoTokenizer.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Unique tokens', len(token_counts)])
        writer.writerow(['Word', 'Count'])
        writer.writerows(top_tokens)


count_unique_tokens(INPUT_FILE, MODEL_NAME)
