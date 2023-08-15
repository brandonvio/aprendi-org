"""
This module generates a random sentence from a list of words.
"""
import random


def generate_random_sentence():
    """
    This function generates a random sentence from a list of words.
    """
    # Check if the file has already been loaded
    try:
        if not hasattr(generate_random_sentence, "word_list"):
            # Load the word list from the file
            with open("data/words.txt", "r") as file:
                word_list = file.read().split(",")
                generate_random_sentence.word_list = word_list  # Store the loaded word list
        else:
            word_list = generate_random_sentence.word_list

        # Generate a random sentence length between 10 and 30 words
        sentence_length = random.randint(10, 30)

        # Select random words from the word list
        random_words = random.sample(word_list, sentence_length)

        # Capitalize the first word and create the sentence
        sentence = " ".join(random_words)
        sentence = sentence.capitalize() + "."

        return sentence

    except Exception as e:
        return "An error occurred: " + str(e)
