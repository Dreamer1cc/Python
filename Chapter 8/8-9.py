# 8-9 . Фокусники: создайте список с именами фокусников . Передайте 
# список функции show_magicians(), которая выводит имя 
# каждого фокусника в списке .

magicians = ["alicIa", "dAvid", "jOhn"]
def show_magicians(names):
    for magician in magicians:
        print(magician.title())

show_magicians(magicians)