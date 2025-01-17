def main():
    book_path = "books/frankenstein.txt" 
    text = get_book_text(book_path)
    number_of_words = get_num_words(text)
    characters = get_num_repeated_characters
    print(f"{number_of_words} words found in the book")
    print(characters)

def get_num_repeated_characters(book):
    lowered_string = book.lower()
    words = lowered_string.split()
    dict = {}
    for word in len(words):
        pass

    return 0

def get_num_words(book):
    words = book.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()