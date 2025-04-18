def get_book_text(path):
	with open(path) as file:
		return file.read()
