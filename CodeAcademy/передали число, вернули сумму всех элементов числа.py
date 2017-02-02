number = 456 # Входящая переменная типа int
def digit_sum(number): # Объявление функции
	word_ = str(number) # Переводим в строку
	count = 0 # Принимаем переменную для конечного результата как int
	len_word = int(len(word_)) # Посчитали длину строки
	for i in range(len_word): # Для каждого элемента в заданном пределе
		count += int(word_[i]) # Считаем переменная + приведенное к int значение i-того лемента 
	return count

digit_sum(number)