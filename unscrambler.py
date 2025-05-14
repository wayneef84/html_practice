import itertools
from collections import defaultdict
import os

def load_dictionary():
    """Load English dictionary words from a file."""
    # Common English words dictionary
    dictionary = set()
    try:
        with open('/usr/share/dict/words', 'r') as f:
            for word in f:
                word = word.strip().lower()
                if word.isalpha():  # Only include words with letters
                    dictionary.add(word)
    except FileNotFoundError:
        print("Dictionary file not found. Using a small built-in dictionary.")
        # Fallback to a small dictionary if system dictionary is not available
        dictionary = {
            'cat', 'dog', 'bird', 'fish', 'tree', 'house', 'book', 'computer',
            'python', 'program', 'code', 'algorithm', 'data', 'science'
        }
    return dictionary

def find_words(letters, dictionary):
    """Find all possible words that can be made from the given letters."""
    words = defaultdict(set)
    letters = letters.lower()
    
    # Try all possible lengths from the length of input letters down to 2
    for length in range(len(letters), 1, -1):
        # Generate all possible combinations of the given length
        for combo in itertools.permutations(letters, length):
            word = ''.join(combo)
            if word in dictionary:
                words[length].add(word)
    
    return words

def main():
    dictionary = load_dictionary()
    
    while True:
        print("\nWord Unscrambler")
        print("Enter 'q' to quit")
        letters = input("Enter scrambled letters: ").strip()
        
        if letters.lower() == 'q':
            break
            
        if not letters.isalpha():
            print("Please enter only letters!")
            continue
            
        words = find_words(letters, dictionary)
        
        if not words:
            print("No valid words found!")
            continue
            
        print("\nPossible words:")
        for length in sorted(words.keys(), reverse=True):
            print(f"\n{length} letters:")
            print(', '.join(sorted(words[length])))

if __name__ == "__main__":
    main() 