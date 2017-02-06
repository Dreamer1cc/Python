def product (number): # Объявление функции
	count = 1
	for i in number:
		count *= int(i)
	return count
product([1,2])