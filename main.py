import sys
from stats import count_words, letter_dictionary, dictionary_sort
from get_book_text import get_book_text

def main ():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	book_path = sys.argv[1]
	text = get_book_text(book_path)
	num_words = count_words(text)
	dictionary = letter_dictionary(text)
	sorted_dictionary = dictionary_sort(dictionary)



	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("---------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("-------- Character Count -------")

	for i in sorted_dictionary:
		if i[0].isalpha():
			print(f"{i[0]}: {i[1]}")

	print("============ END ============")

main()
