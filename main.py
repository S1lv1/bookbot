def main():
    book_path = "books/frankenstein.txt" 
    text = get_book_text(book_path)
    number_of_words = get_num_words(text)
    characters = get_num_repeated_characters(text)
    # print(f"{number_of_words} words found in the book")
    print(characters)

def get_num_repeated_characters(book):
    chars = {}
    for c in book:
        lowered_char = c.lower()
        if lowered_char in chars:
            chars[lowered_char] +=1
        else:
            chars[lowered_char] = 1

    return chars

def get_num_words(book):
    words = book.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()