from stats import get_word_count, get_character_count

def main():
    num_words = get_word_count(get_book_text("./books/frankenstein.txt"))
    print(f"{len(num_words)} words found in the document")
    print(get_character_count(get_book_text("./books/frankenstein.txt")))

def get_book_text(filepath=""):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

main()