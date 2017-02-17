# 8-6 . Названия городов: напишите функцию city_country(), которая получает 
# название города и страну . Функция должна возвращать строку в 
# формате “Santiago, Chile” . Вызовите свою функцию по крайней мере для 3
# трех пар «город—страна» и выведите возвращенное значение .
def city_country(city, country):
    return(city.title() + ", " + country.title())

full_address = city_country("Kyiv", "ukraine")
print(full_address)
