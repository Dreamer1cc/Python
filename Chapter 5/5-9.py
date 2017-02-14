# 5-9 . Без пользователей: добавьте в hello_admin .py команду if, которая
# проверит, что список пользователей не пуст . 
# • Если список пуст, выведите сообщение: «We need to find some users!» 
# • Удалите из списка все имена пользователей и убедитесь в том, что программа 
# выводит правильное сообщение . 
# users_list = ["Andrew", "JOHHNAS", "AdMiN", "FrenchPress", "Dreamer1cc", "XIII"]
users_list = []
if users_list: 
    for user in users_list:
        if user.lower() == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print("Helo " + user.title() + ", thank you for logging in again")
else:
    print("We need to find some users!")