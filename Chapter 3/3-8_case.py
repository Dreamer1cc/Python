#УПРАЖНЕНИЯ 
#3-8 . Повидать мир: вспомните хотя бы пять стран, в которых вам хотелось бы побывать . 
#• Сохраните названия стран в списке . Проследите за тем, чтобы список не хранился в алфавитном порядке . 
countries = ["Вьетнам", "Соединенные штаты Америки", "Англия", "Швейцария", "Тайланд"]
#• Выведите список в исходном порядке . Не беспокойтесь об оформлении списка, просто выведите его как обычный список Python . 
print(countries)
#• Используйте функцию sorted() для вывода списка в алфавитном порядке без изменения списка . 
print(sorted(countries))
#• Снова выведите список, чтобы показать, что он по-прежнему хранится в исходном порядке . 
print(countries)
#• Используйте функцию sorted() для вывода списка в обратном алфавитном порядке без изменения порядка исходного списка .
print(sorted(countries, reverse = True))
#• Снова выведите список, чтобы показать, что исходный порядок не изменился .
print(countries)
#• Измените порядок элементов вызовом reverse() . Выведите список, чтобы показать, что элементы следуют в другом порядке . 
countries.reverse()
print(countries)
#• Измените порядок элементов повторным вызовом reverse() . Выведите список, чтобы показать, что список вернулся к исходному порядку . 
countries.reverse()
print(countries)
#• Отсортируйте список в алфавитном порядке вызовом sort() . Выведите список, чтобы показать, что элементы следуют в другом порядке . 
countries.sort()
print(countries)
#• Вызовите sort() для перестановки элементов списка в обратном алфавитном порядке . Выведите список, чтобы показать, что порядок элементов изменился . 
countries.sort(reverse = True)
print(countries)




