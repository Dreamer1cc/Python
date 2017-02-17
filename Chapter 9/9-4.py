"""9-4 . Посетители: начните с программы из упражнения 9-1 (с . 165) . 
Добавьте атрибут number_served со значением по умолчанию 0; он 
представляет количество обслуженных посетителей . Создайте экземпляр с 
именем restaurant . Выведите значение number_served, потом измените и 
выведите снова . Добавьте метод с именем set_number_served(), 
позволяющий задать количество обслуженных посетителей . Вызовите метод с 
новым числом, снова выведите значение .Добавьте метод с именем 
increment_number_served(), который увеличивает количество обслуженных 
посетителей на заданную величину . Вызовите этот метод с любым числом, 
которое могло бы представлять количество обслуженных клиентов — скажем, 
за один день ."""
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


restaurant = Restaurant("Доннер Кебаб","турецкая")
restaurant.read_number_served()
restaurant.set_number_served(15)
restaurant.read_number_served()
restaurant.increment_number_served(35)
restaurant.read_number_served()

