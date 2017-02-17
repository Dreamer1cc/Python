# 8-9 . Фокусники: создайте список с именами фокусников . Передайте 
# список функции show_magicians(), которая выводит имя 
# каждого фокусника в списке .


# 8-10 . Великие фокусники: начните с копии вашей программы из упражнения 8-9 . 
# Напишите функцию make_great(), которая изменяет список фокусников, добавляя 
# к имени каждого фокусника приставку «Great» . Вызовите функцию 
# show_magicians() и убедитесь в том, что список был успешно изменен .

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

show_magicians(make_great(magicians))
