def get_word_count(book):
    words = book.split()
    return words

def get_character_count(book):
    char_count = {}
    for char in book.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count