inventory = {
			'gold' 		: 500,
			'pouch' 	: ['flint', 'twine', 'gemstone'], # Можем в словаре добавить ключу список
			'backpack' 	: ['xylophone','dagger', 'bedroll','bread loaf']
			}

# добавляем новый ключ и присваиваем ему список
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
# Сортируем список принадлежащий ключу
inventory['pouch'].sort() 
# Добавляем новый элемент в словарь и присваиваем ему список
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
# сортируем список по ключу
inventory['backpack'].sort()
# удаляем одно из значений списка принадлежащего ключу
inventory['backpack'].remove('dagger')
# +50 к текущему значению поля
inventory['gold'] += 50