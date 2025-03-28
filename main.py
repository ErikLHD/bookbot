from stats import count_words, char_count
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    path = sys.argv[1]


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    file_contents = get_book_text(path)
    # print(file_contents)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(file_contents)} total words")
    print("--------- Character Count -------")
    sorted_dict = sorted(char_count(file_contents).items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    for key, value in sorted_dict:
        print(key + ": " + str(value))
    print("============= END ===============")

    #print(char_count(file_contents))

main()
