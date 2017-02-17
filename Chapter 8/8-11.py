# 8-9 . Фокусники: создайте список с именами фокусников . Передайте 
# список функции show_magicians(), которая выводит имя 
# каждого фокусника в списке .

# 8-10 . Великие фокусники: начните с копии вашей программы из упражнения 8-9 . 
# Напишите функцию make_great(), которая изменяет список фокусников, добавляя 
# к имени каждого фокусника приставку «Great» . Вызовите функцию 
# show_magicians() и убедитесь в том, что список был успешно изменен .

# 8-11 . Фокусники без изменений: начните с программы из упражнения 8-10 . 
# Вызовите функцию make_great() и передайте ей копию списка имен фокусников . 
# Поскольку исходный список остался неизменным, верните новый список и сохраните 
# его в отдельном списке . Вызовите функцию show_magicians() с каждым 
# списком, чтобы показать, что в одном списке остались исходные имена, а 
# в другом к имени каждого фокусника добавилась приставка «Great» .

magicians = ["alicIa", "dAvid", "jOhn"]
def make_great(names):
    great_magician = []
    while names:
        gret_m = "Great " + names.pop()
        great_magician.append(gret_m)
    return great_magician

def show_magicians(names):
    for name in names:
        print(name.title())

great_magicians = make_great(magicians[:])
show_magicians(magicians)
show_magicians(great_magicians)