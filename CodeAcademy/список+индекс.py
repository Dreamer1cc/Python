# Работа со списком значений
choices = ['pizza', 'pasta', 'salad', 'nachos']
# Печатаем 
print('Your choices are:')
# Для каждого индекса с элементом
for index, item in enumerate(choices):
# Печатаем индекс в удобоваримом виде (не с 0) и элемент ему соответствующий
    print(index + 1, item)