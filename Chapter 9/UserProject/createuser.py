import user
import admin
import privileges


user1 = user.Users("иван", "иванов")
user2 = user.Users("петр", "петров")
user3 = admin.Admin("евгений", "евгеньевич")
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
user3.show_privileges()