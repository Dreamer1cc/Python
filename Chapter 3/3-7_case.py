'''
3-7 . 
Сокращение списка гостей: только что выяснилось, что новый обеденный стол привезти вовремя не успеют, и места хватит только для двух гостей . 
• Начните с программы из упражнения 3-6 . Добавьте команду для вывода сообщения о том, что на обед приглашаются всего два гостя . 
• Используйте метод pop() для последовательного удаления гостей из списка до тех пор, пока в списке не останутся только два человека . 
Каждый раз, когда из списка удаляется очередное имя, выведите для этого человека сообщение о том, что вы сожалеете об отмене приглашения . 
• Выведите сообщение для каждого из двух человек, остающихся в списке . Сообщение должно подтверждать, что более раннее приглашение остается в силе . 
• Используйте команду del для удаления двух последних имен, чтобы список остался  пустым . 
Выведите список, чтобы убедиться в том, что в конце работы программы список действительно не содержит ни одного элемента .
'''
guests = ["Лена", "Виктория", "Ирина", "Александр", "Анастасия"]
invitation = ", приглашаю тебя на обед!"
print(guests[0] + invitation)
print(guests[1] + invitation)
print(guests[2] + invitation)
print(guests[3] + invitation)
print(guests[4] + invitation)
print("В связи с покупкой нового стола - список гостей расширен! Новый список приглашенных:")
guests.insert(3, "Алексей")
guests.insert(0, "Анастасия")
guests.append("Артур")
print(guests[0] + invitation)
print(guests[1] + invitation)
print(guests[2] + invitation)
print(guests[3] + invitation)
print(guests[4] + invitation)
print(guests[5] + invitation)
print(guests[6] + invitation)
print(guests[7] + invitation)
print("В связи с тем, что стол привезти не успевают - на обед приглашается только двое гостей")
del_guest1 = guests.pop(-1)
print(del_guest1 + ", сожалею об отмене приглашения!")
del_guest2 = guests.pop(-1)
print(del_guest2 + ", сожалею об отмене приглашения!")
del_guest3 = guests.pop(-1)
print(del_guest3 + ", сожалею об отмене приглашения!")
del_guest4 = guests.pop(-1)
print(del_guest4 + ", сожалею об отмене приглашения!")
del_guest5 = guests.pop(-1)
print(del_guest5 + ", сожалею об отмене приглашения!")
del_guest6 = guests.pop(-1)
print(del_guest6 + ", сожалею об отмене приглашения!")
print(guests[0] + ", более раннее приглашение остаётся в силе, жду тебя")
print(guests[1] + ", более раннее приглашение остаётся в силе, жду тебя")
del guests[0]
del guests[0]
print(guests)
#del guests[0]
