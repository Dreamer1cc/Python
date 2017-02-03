def censor(text, word):
	new_string = ""
	len_word = len(word)
	cen_str = "*" * len_word
	frst_symb = text.find(word)
	if frst_symb != -1:
		new_string = text.replace(word, cen_str)
	else:
		print("No replace!")
	return new_string


censor("Hello world it is fucking shit", "word")