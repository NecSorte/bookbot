def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    count_words(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return print(f"Found {len(words)} total words")

main()