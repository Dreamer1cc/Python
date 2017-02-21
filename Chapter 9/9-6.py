"""
9-6 . Киоск с мороженым: киоск с мороженым — особая разновидность ресторана . 
Напишите класс IceCreamStand, наследующий от класса Restaurant из 
упражнения 9-1 (с . 165) или упражнения 9-4 (с . 169) . 
Подойдет любая версия класса; просто выберите ту, которая вам больше 
нравится . Добавьте атрибут с именем flavors для хранения списка 
сортов мороженого . Напишите метод, который выводит этот список . 
Создайте экземпляр IceCreamStand и вызовите этот метод .
"""


class Restaurant():
    """класс ресторан"""
    def __init__(self, restaurant_name, cuisine_type):
        """Инициализирует атрибуты ресторана"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Описываем ресторан"""
        print("Ресторан называется " + self.restaurant_name.title())
        print("Кухня ресторана: " + self.cuisine_type)

    def open_restaurant(self):
        """сообщение об открытии ресторана"""
        print("Ресторан открыт")

    def read_number_served(self):
        print("Посетителей обслужено: " + str(self.number_served))

    def set_number_served(self, served):
        self.number_served = served

    def increment_number_served(self, served):
        self.number_served += served

class IceCreamStand(Restaurant):
    """параметры специфичные для кафе-мороженного"""
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["пломбир", "шоколадное", "банановое", "ванильное",]

    def flavors_types(self):
        print("\nДля заказа доступны такие виды мороженного: ")
        for flavor in self.flavors:
            print("-" + flavor)

icecreamstand = IceCreamStand("SubZero", "IceCream")
icecreamstand.describe_restaurant()
icecreamstand.flavors_types()