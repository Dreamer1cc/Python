#УПРАЖНЕНИЯ 
'''
3-9 . Количество гостей: в одной из программ из упражнений с 3-4 по 3-7 используйте len() для вывода сообщения с количеством людей, приглашенных на обед .
'''
guests = ["Лена", "Виктория", "Ирина", "Александр", "Анастасия"]
invitation = ", приглашаю тебя на обед!"
print(guests[0] + invitation)
print(guests[1] + invitation)
print(guests[2] + invitation)
print(guests[3] + invitation)
print(guests[4] + invitation)
print(guests[4] + ", к сожалению, не сможет прийти")
guests[4] = "Андрей"
print(guests[0] + invitation)
print(guests[1] + invitation)
print(guests[2] + invitation)
print(guests[3] + invitation)
print(guests[4] + invitation)
print("Всего гостей: " + str(len(guests)))