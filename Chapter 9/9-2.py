# 9-1 . Ресторан: создайте класс с именем Restaurant . 
# Метод __init__() класса Restaurant должен содержать два 
# атрибута: restaurant_name и cuisine_type . Создайте метод 
# describe_restaurant(), который выводит два атрибута, и метод 
# open_restaurant(), который выводит сообщение о том, что ресторан 
# открыт . Создайте на основе своего класса экземпляр с именем restaurant . 
# Выведите два атрибута по отдельности, затем вызовите оба метода . 

class Restaurant():
    """класс ресторан"""
    def __init__(self, restaurant_name, cuisine_type):
        """Инициализирует атрибуты ресторана"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Описываем ресторан"""
        print("Ресторан называется " + self.restaurant_name.title())
        print("Кухня ресторана: " + self.cuisine_type)

    def open_restaurant(self):
        """сообщение об открытии ресторана"""
        print("Ресторан открыт")

new_restaurant = Restaurant("King kongo", "Kongo")
print("Имя ресторана " + new_restaurant.restaurant_name)
print("Кухня ресторана " + new_restaurant.cuisine_type)

print("\nописание ресторана:")
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()

"""9-2 . Три ресторана: начните с класса из упражнения 9-1 . 
Создайте три разных экземпляра, вызовите для каждого экземпляра 
метод describe_restaurant() ."""

new_restaurant2 = Restaurant("МакДак","Бургеры, картошка, кола")
new_restaurant3 = Restaurant("ДонкиКонг","Гигантские обезьяны")

new_restaurant2.describe_restaurant()
new_restaurant3.describe_restaurant()