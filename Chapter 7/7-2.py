# 7-2 . Заказ стола: напишите программу, которая спрашивает у пользователя, 
# на сколько мест он хочет забронировать стол в ресторане . Если введенное 
# число больше 8, выведите сообщение о том, что пользователю придется 
# подождать . В противном случае сообщите, что стол готов . 

table = input("На какое количество мест вы бы хотели забронировать стол? ")
table = int(table)
if table > 8:
    print("Вам придётся подождать, все столы заняты")
else:
    print("Стол готов")