from stats import count_words

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    count_words(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()