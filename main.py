def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def num_words(get_book_text):
    words = 0
    for i in get_book_text.split():
        words += 1
    return words

def main():
    print(f"Found {num_words(get_book_text)} total words")

main()