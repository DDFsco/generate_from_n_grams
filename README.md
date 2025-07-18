# Trigram-Based Text Generator

This Python script generates new text sequences in the style of classic novels using a **trigram language model**. It processes books, builds probabilistic models of word sequences, and then uses those models to generate pseudo-literary text.

---

## What Is a Trigram Model?

A **trigram** is a group of three consecutive words. This model learns how frequently each pair of words (e.g., "it was") is followed by a third word (e.g., "dark"). It can then generate new text by chaining these word triples together.

---

## Project Structure

- `books`:  
  A dictionary mapping book titles to their `.txt` files.
  
- `process_text(filename)`:  
  Cleans and tokenizes text, builds the nested trigram dictionary:  
  `dict[word1][word2] = [word3, word3, ...]`

- `save_trigram_to_json(...)`:  
  Saves the trigram dictionary to a JSON file for reuse.

- `load_trigram_from_json(...)`:  
  Loads previously saved trigram dictionary if available.

- `generate_text(...)`:  
  Starts from a random word pair and generates up to 200 words of text using the trigram model.

---

## Input Texts

The script processes the following classic books:

- *Great Expectations*
- *Anne of Green Gables*
- *Pride and Prejudice*

You can replace or add to the `books` dictionary with any plain `.txt` file.

---

## How to Run

1. Place `.txt` files of books in the same directory.
2. Run the Python script.
3. It will:
   - Clean and parse the text
   - Save a trigram model as a `.json` file (if not already saved)
   - Generate sample text from each book
