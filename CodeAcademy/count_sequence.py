# функция для подсчета количества вхождений переданного аргумента
# функция должна вернуть ИНТ
# переданные параметры могут быть int, string, float, list
def count(sequence, item):
	count = 0
	item = str(item)
	for i in sequence:
		if str(i) == item:
			count += 1
	return count


count(['bacon', 'eggs', 'cheese', 'eggs'],'eggs')
