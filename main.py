from stats import count_words, lower_character

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    count_words(text)
    lowers = lower_character(text)
    print(lowers)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    

main()