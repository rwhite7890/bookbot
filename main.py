from stats import get_num_words , get_num_char, sort_dict
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    file_contents = get_book_text(path)
  
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    get_num_words(file_contents)
    print("--------- Character Count -------")
    counts = get_num_char(file_contents)
    sorted_dict = sort_dict(counts)
    for dict in sorted_dict:
        print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

main()