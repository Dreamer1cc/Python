"""
9-7 . Администратор: администратор — особая разновидность пользователя . 
Напишите класс с именем Admin, наследующий от класса User из упражнения 9-3 
(с . 165) или упражнения 9-5 (с . 170) . Добавьте атрибут privileges для 
хранения списка строк вида «разрешено добавлять сообщения», 
«разрешено удалять пользователей», «разрешено банить пользователей» и т.д. 
Напишите метод show_privileges() для вывода набора привилегий администратора.
 Создайте экземпляр Admin и вызовите свой метод . 
 
9-8 . Привилегии: напишите класс Privileges . Класс должен содержать всего 
один атрибут privileges со списком строк из упражнения 9-7 . 
Переместите метод show_privileges() в этот класс . 
Создайте экземпляр Privileges как атрибут класса Admin . 
Создайте новый экземпляр Admin и используйте свой метод для 
вывода списка привилегий .
"""
class Users():
    """классический пользователь"""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(
            "Имя пользователя " 
            + self.first_name.title() + " " + self.last_name.title()
            )

    def greet_user(self):
        print(
            "Привет " + self.first_name.title() 
            + " " + self.last_name.title()
            )

class Privileges():
    def __init__(self):
        self.privileges = [
            "разрешено добавлять сообщения",
            "разрешено удалять пользователей",
            "разрешено банить пользователей",
            ]

class Admin(Users):
    """Администратор в рамках списка пользователей"""
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = [
            "разрешено добавлять сообщения",
            "разрешено удалять пользователей",
            "разрешено банить пользователей",
            ]

    def show_privileges(self):
        print("Пользователю разрешено: ")
        for privilege in self.privileges:
            print("\n-" + privilege)

    def greet_user(self):
        print(
            "Хвала админу! Приветствуем " + self.first_name.title() 
            + " " + self.last_name.title()
            )


user1 = Users("иван", "иванов")
user2 = Users("петр", "петров")
user3 = Admin("евгений", "евгеньевич")
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
user3.show_privileges()

