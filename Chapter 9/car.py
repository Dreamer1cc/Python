class Car():
    """Простая модель автомобиля.""" 
    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Нельзя скручивать пробег")

    def increment_odometer(self, miles):
        """Увеличивает показания одометра с заданным приращением.""" 
        self.odometer_reading += miles

    def read_odometer(self):
        """выводить пробег машины в милях"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")


my_used_car = Car('subaru', 'outback', 2013) 
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500) 
my_used_car.read_odometer()
my_used_car.increment_odometer(100) 
my_used_car.read_odometer() 