# 7-10 . Отпуск мечты: напишите программу, которая опрашивает пользователей, 
# где бы они хотели провести отпуск . Включите блок кода для 
# вывода результатов опроса .


interview = {}
active = True
while active:
    name = input("\nКак вас зовут? ")
    name = name.strip()
    vacation = input("\nГде бы вы хотели провести отпуск? ")
    interview[name] = vacation
    message = input("\nХотите продолжить опрос? Да\Нет. ").lower()
    if message == "нет":
        active = False
print("\nРезультаты интервью пользователей: ")
for name, vacation in interview.items():
    print(name.title() + " хотел бы побывать во время отпуска в " + vacation.title())
