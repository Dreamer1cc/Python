def reverse(text):
	new_word = ""
	for i in range((len(text) -1), -1, -1):
		new_word += text[i]
	return new_word

reverse("hello")