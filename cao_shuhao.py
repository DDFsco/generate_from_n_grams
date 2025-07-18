import re
import random
import collections
import json
import os

# List of books
books = {
    "Great Expectations": "GreatExpectations_nll.txt",
    "Anne of Green Gables": "Anne_of_Green_Gables.txt",
    "Pride and Prejudice": "pride_and_prejudice_nll.txt"
}

def process_text(filename):
    """Processes a text file into a trigram dictionary."""
    with open(filename, 'r') as f:
        lines = f.readlines()

    trigram_dict = collections.defaultdict(lambda: collections.defaultdict(list))

    for line in lines:
        # Remove period after Mr., Mrs., and St.
        line = re.sub(r'\b(Mr|Mrs|St)\.', r'\1', line)
        # Put a space before punctuation so that it will be treated as a separate word.
        line = re.sub(r'([.,!?])', r' \1', line)
        # Put a space after start quotes.
        line = re.sub(r'([“”])', r'\1 ', line)
        # Remove underscores.
        line = re.sub(r'[_]', r' ', line)
        # Surround dashes with spaces.
        line = re.sub(r'[-]', r' - ', line)

        words = line.lower().split()

        # Create trigrams from each line
        for i in range(len(words) - 2):
            w1, w2, w3 = words[i], words[i + 1], words[i + 2]
            trigram_dict[w1][w2].append(w3)

    return trigram_dict

def save_trigram_to_json(trigram_dict, filename):
    """Saves trigram dictionary to a JSON file."""
    json_filename = filename.replace('.txt', '_trigrams.json')
    with open(json_filename, 'w') as f:
        json.dump(trigram_dict, f)

def load_trigram_from_json(filename):
    """Loads trigram dictionary from a JSON file."""
    json_filename = filename.replace('.txt', '_trigrams.json')
    if os.path.exists(json_filename):
        with open(json_filename, 'r') as f:
            return json.load(f)
    return None

def generate_text(trigram_dict):
    """Generates text using a trigram model."""
    iteration = 0
    max_iterations = 200

    # Start with a random key
    current_word = random.choice(list(trigram_dict.keys()))
    next_word = random.choice(list(trigram_dict[current_word].keys()))
    print(current_word, end=' ')
    print(next_word, end=' ')

    while iteration < max_iterations:
        iteration += 1

        # Check if valid sequence exists
        if (current_word in trigram_dict and
            next_word in trigram_dict[current_word] and
            trigram_dict[current_word][next_word]):

            predicted_word = random.choice(trigram_dict[current_word][next_word])
            print(predicted_word, end=' ')
            current_word, next_word = next_word, predicted_word

        elif next_word in trigram_dict:
            predicted_word = random.choice(list(trigram_dict[next_word].keys()))
            print(predicted_word, end=' ')
            current_word, next_word = next_word, predicted_word

        else:
            print("\n")
            break

# Process each book
for book, filename in books.items():
    print(f"\nProcessing {book}...\n")

    # Try loading the trigram dictionary from a JSON file
    trigram_dict = load_trigram_from_json(filename)

    if trigram_dict is None:
        print(f"From {filename} to create trigram dictionary.")
        trigram_dict = process_text(filename)
        save_trigram_to_json(trigram_dict, filename)
        print(f"Saved trigram for {book}.")

    else:
        print(f"Loaded existing trigram dictionary for {book}.")

    # Generate text from the trigram model
    print(f"\nGenerated text from {book}:\n")
    generate_text(trigram_dict)
    print("\n" + "="*50 + "\n")