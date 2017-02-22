# 7-5 . Билеты в кино: кинотеатр установил несколько вариантов цены на билеты 
# в зависимости от возраста посетителя . Для посетителей младше 3 лет билет 
# бесплатный; в возрасте от 3 до 12 билет стоит $10; наконец, если возраст 
# посетителя больше 12, билет стоит $15 . Напишите цикл, который предлагает 
# пользователю ввести возраст и выводит цену билета .

message = "\nВведите свой возраст для определения стоимости билета."
message += " Для выхода нажмите 'q': "
active = True
end_message = "Для посетителей в возрасте "
while active:
    age = input(message)
    if age == "q":
        active = False
    else:
        age = int(age)
        if age < 3:
            print(end_message + str(age) + " Стоимость билета 0$")
        elif age < 13:
            print(end_message + str(age) + " Стоимость билета 10$")
        else:
            print(end_message + str(age) + " Стоимость билета 15$")