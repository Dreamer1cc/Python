# 7-4 . Дополнения для пиццы: напишите цикл, который предлагает пользователю 
# вводить дополнения для пиццы до тех пор, пока не будет введено значение 
# 'quit’ . При вводе каждого дополнения выведите сообщение о том, что это 
# дополнение включено в заказ .

ingr = "\nВведите дополнение, которое вы хотите добавить в пиццу."
ingr += "\nКогда закончите введите 'quite': "

active = True
while active:
    message = input(ingr)
    if message == "quite":
        active = False
    else:
        print("Вы решили добавить к заказу: " + message)



