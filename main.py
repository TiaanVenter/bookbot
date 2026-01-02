import sys
from stats import num_words, get_num_char, sorted_list

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_file = sys.argv[1]

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    sorted_chars = sorted_list(get_num_char(get_book_text(path_to_file)))
    book_text = get_book_text(path_to_file)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {num_words(book_text)} total words")
    print("--------- Character Count -------")

    for i in sorted_chars:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")

main()