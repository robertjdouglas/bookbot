import sys
from stats import count_characters
from stats import get_num_words
from stats import sort_characters_by_count

def main():
#    print(f"{sys.argv}")
#    test = len(sys.argv)
#    print(f"{test}")
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    text = get_book_text(book_path)
    words = text.split()
    count = len(words)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    char_count = count_characters(text)
    # print(f"Character count: {char_count}")
    sorted_char_count = sort_characters_by_count(char_count)
    print("--------- Character Count -------")
    for item in sorted_char_count:
        print(f"{item['character']}: {item['count']}")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
