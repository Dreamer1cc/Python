"""
9-3 . Пользователи: создайте класс с именем User . Создайте два 
атрибута first_name и last_ name, а затем еще несколько атрибутов, 
которые обычно хранятся в профиле пользователя . 
Напишите метод describe_user(), который выводит сводку с 
информацией о пользователе . Создайте еще один метод greet_user() 
для вывода персонального приветствия для пользователя . 
Создайте несколько экземпляров, представляющих разных пользователей . 
Вызовите оба метода для каждого пользователя .
"""
class Users():
    """классический пользователь"""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print("Имя пользователя " + self.first_name.title() + " " + self.last_name.title())

    def greet_user(self):
        print("Привет " + self.first_name.title() + " " + self.last_name.title())

user1 = Users("иван", "иванов")
user2 = Users("петр", "петров")
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()

