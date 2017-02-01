'''3-6 . Больше гостей: вы решили купить обеденный стол большего размера . 
Дополнительные места позволяют пригласить на обед еще трех гостей . 
• Начните с программы из упражнения 3-4 или 3-5 . Добавьте в конец программы команду print, которая выводит сообщение о расширении списка гостей . 
• Добавьте вызов insert() для добавления одного гостя в начало списка . 
• Добавьте вызов insert() для добавления одного гостя в середину списка . 
• Добавьте вызов append() для добавления одного гостя в конец списка . 
• Выведите новый набор сообщений с приглашениями – по одному для каждого участника, входящего в список . '''
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