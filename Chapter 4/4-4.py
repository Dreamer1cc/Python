"""4-4 . Миллион: создайте список чисел от 1 до 1 000 000, затем воспользуйтесь циклом for для вывода чисел . 
(Если вывод занимает слишком много времени, остановите его нажатием Ctrl+C или закройте окно вывода .)"""
million = [x for x in range(1, 1000000)]
for x in million:
	print(x)
