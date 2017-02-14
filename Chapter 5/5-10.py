# 5-10 . Проверка имен пользователей: выполните следующие действия для создания 
# программы, моделирующей проверку уникальности имен пользователей . 
#• Создайте список current_users, содержащий пять и более имен пользователей . 
#• Создайте другой список new_users, содержащий пять и более имен пользователей .
#  Убедитесь в том, что одно или два новых имени также присутствуют в списке 
#  current_ users . 
#• Переберите список new_users и для каждого имени в этом 
#  списке проверьте, было ли оно использовано ранее . Если имя уже использовалось,
#   выведите сообщение о том, что пользователь должен выбрать новое имя . 
#   Если имя не использовалось, выведите сообщение о его доступности . 
#• Проследите за тем, чтобы сравнение выполнялось без учета регистра символов . 
#   Если имя 'John’ уже используется, в регистрации имени ‘JOHN’ следует отказать.

current_users = ["Andrew", "JOHHNAS", "AdMiN", "FrenchPress", 
                "Dreamer1cc", "XIII"]
new_users = ["AnDrEw", "Apple", "xiii", "frenchpress", "NewUser", "CurrentUser",
            "NotCurrentUser"
            ]
lower_current_users = []
for cr_user in current_users.lower():
    lower_current_users.append(cr_user.lower())
for user in new_users:
    if user.lower() in lower_current_users:
        print("You must change name. Name " + user + " is already exist!")
    else:
        print("Registration availeble. Pls input your e-mail.")



current_users = ["Andrew", "JOHHNAS", "AdMiN", "FrenchPress", 
                "Dreamer1cc", "XIII"]
new_users = ["AnDrEw", "Apple", "xiii", "frenchpress", "NewUser", "CurrentUser",
            "NotCurrentUser"]
for user in new_users:
    if user.lower() in [cr_user.lower() for cr_user in current_users]:
        print("You must change name. Name " + user + " is already exist!")
    else:
        print("Registration availeble. Pls input your e-mail.")


