from stats import num_words, get_num_char, sorted_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents



def main():
    sorted_chars = sorted_list(get_num_char(get_book_text('books/frankenstein.txt')))
    book_text = get_book_text("books/frankenstein.txt")

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words(book_text)} total words")
    print("--------- Character Count -------")

    for i in sorted_chars:
        if i["char"].isalpha() == True:
            print(f"{i['char']}: {i['num']}")

main()