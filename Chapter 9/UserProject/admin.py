from user import Users

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