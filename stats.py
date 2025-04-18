def count_words(text):

	num_words = 0
	words = text.split()

	for word in words:
		num_words += 1

	return num_words

def letter_dictionary(text):

	character_list = []
	words = text.split()
	letter_dict = {}

	for word in words:
		letters = list(word)
		for letter in letters:
			letter = letter.lower()
			character_list.append(letter)

	for character in character_list:
		letter_dict[character] = letter_dict.get(character, 0) + 1

	return letter_dict




def dictionary_sort(dictionary):
	dictionary = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
#	dictionary = sorted((value,key) for (key,value) in dictionary.items())
	
	return dictionary
