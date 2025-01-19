def main():
    book_path = "books/frankenstein.txt" 
    text = get_book_text(book_path)
    number_of_words = get_num_words(text)
    characters = get_num_repeated_characters(text)
    list_from_dict = sort_on(characters)
    #characters.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{number_of_words} words found in the book")
    print("\n")
    for item in list_from_dict:
        if item[0].isalpha():
            print(f"The '{item[0]}' character was found {item[1]} times")
    print("--- End Report ---")

def sort_on(chars):
    chars_sorted =  dict(sorted(chars.items(), key=lambda item: item[1], reverse = True))
    list_from_dict = list(chars_sorted.items())
    return list_from_dict

def get_num_repeated_characters(text):
    chars = {}
    for c in text:
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