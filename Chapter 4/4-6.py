"""
4-6 . Нечетные числа: воспользуйтесь третьим аргументом функции range() для создания списка нечетных чисел от 1 до 20 . Выведите все числа в цикле for .
"""
million = [x for x in range(1, 21, 2)]
for n in million:
	print(n)