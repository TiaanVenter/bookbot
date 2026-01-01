from stats import num_words, get_num_char

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    print(f"Found {num_words(get_book_text('books/frankenstein.txt'))} total words")
    print(f"{get_num_char(get_book_text('books/frankenstein.txt'))}")

main()