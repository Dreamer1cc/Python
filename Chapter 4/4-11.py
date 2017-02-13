"""
4-11 . Моя пицца, твоя пицца: начните с программы из упражнения 4-1 .
Создайте копию списка с видами пиццы, присвойте ему имя friend_pizzas . Затем сделайте следующее . 
• Добавьте новую пиццу в исходный список . 
• Добавьте другую пиццу в список friend_pizzas . 
• Докажите, что в программе существуют два разных списка . Выведите сообщение «My favorite pizzas are:», а затем первый список в цикле for .
 Выведите сообщение «My friend’s favorite pizzas are:», а затем второй список в цикле for . 
 Убедитесь в том, что каждая новая пицца находится в соответствующем списке . """

pizzas = ["margarita", "bavaria", "truffel", "meat", "pineapple"]
friend_pizzas = pizzas[:]
pizzas.append("strawbery pizza")
friend_pizzas.append("fish pizza")
print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza),
print("My friend’s favorite pizzas are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza),