import re
import logging

# # Error classes examples

# class APIClientError(Exception):
#     """Base exception for API client failures."""

# class APIResponseError(APIClientError):
#     """Raised when API returns unexpected data."""

def count_words(text):
    words = text.split()
    return print(f"Found {len(words)} total words")

def lower_character(text):
    lower_dictionary = {}
    try:
        for letter in text:
            letter = str.lower(letter)
            if letter in lower_dictionary:
                # Do add the value of the key + 1
                lower_dictionary[letter] = lower_dictionary[letter] + 1
            else:
                # add letter to lower_dictionary
                lower_dictionary[letter] = 1
        # print(lower_dictionary)
        return lower_dictionary
    except:
        raise TypeError(f"text must be a str, got {type(text).__name__}")


# Function that takes a dictionary and returns the key of value
def helper_sorter(items):
    return items["num"]

def sort_letters(lower_dictionary):
    # print(lower_dictionary)
    sorted_list = []

    for key, value in lower_dictionary.items():
        # Append key, value as a lower_dictionary into list "sorted_list"
        if key.isalpha():
            small_dicitonary = {"char": key, "num": value}
            # print(small_dicitonary)
            sorted_list.append(small_dicitonary)
        else:
            continue


    sorted_list.sort(key=helper_sorter, reverse=True)
    # print(sorted_list)
    return sorted_list

# Function to print the value of each char, + ": " + the value of num for each dictionary. 
def print_dictionary_list(sorted_list):
    # for each dictionary in list, print value of char and num
    for item in sorted_list:
        char = item.get("char")
        num = item.get("num")
        print(f"{char}: {num}")
    return True


