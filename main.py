from stats import count_words, lower_character, sort_letters, print_dictionary_list

import sys


def main():
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    text = get_book_text(path)
    print("----------- Word Count ----------")
    count_words(text)
    print("--------- Character Count -------")
    lowers = lower_character(text)
    sorted_chars = sort_letters(lowers)
    print_dictionary_list(sorted_chars)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()