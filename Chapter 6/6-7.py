# 6-7 . Люди: начните с программы, написанной для упражнения 6-1 (с . 107) . 
# Создайте два новых словаря, представляющих разных людей, и сохраните все три 
# словаря в списке с именем people . Переберите элементы списка людей . 
#  процессе перебора выведите всю имеющуюся информацию о каждом человеке .


kyrylo = {
        "last_name" : "holovchenko",
        "age" : 27,
        "city" : "kyiv",
        },
artur = {
        "last_name" : "arukov",
        "age" : 28,
        "city" : "kyiv",
        },
oleg = {
        "last_name" : "driga",
        "age" : 35,
        "city" : "kyiv",
        },

people = [kyrylo, artur, oleg]
for human in people:
    print(human)



# for human_n, human_inf in people.items():
#     print("Username: " + human_n.title() + " " + human_inf["last_name"].title() 
#         + " is " + str(human_inf["age"]) + " years old. Live in " 
#         + human_inf["city"].title())

