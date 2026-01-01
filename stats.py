def num_words(file_contents):
    words = 0
    for i in file_contents.split():
        words += 1
    return words

def get_num_char(file_contents):
    input_string = file_contents.lower()
    char_counts = {}
    for i in input_string:
        if i not in char_counts:
            char_counts[i] = 1
        else:
            char_counts[i] += 1
    return char_counts

def sort_on(char_counts):
    return char_counts["num"]

def sorted_list(char_counts):   
    charlist = []

    for i in char_counts:
        entry = {"char": i, "num": char_counts[i]}
        charlist.append(entry)

    charlist.sort(reverse=True, key=sort_on)

    return charlist