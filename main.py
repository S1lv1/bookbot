def main():
    book_path = "books/frankenstein.txt" 
    text = get_book_text(book_path)
    number_of_words = get_num_words(text)
    print(f"{number_of_words} words found in the book")

def get_num_words(book):
    words = book.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()