# 6-1 . Человек: используйте словарь для сохранения информации об известном вам 
# человеке . Сохраните имя, фамилию, возраст и город, в котором живет этот 
# человек. Словарь должен содержать ключи с такими именами, 
# как first_name, last_name, age и city . 
# Выведите каждый фрагмент информации, хранящийся в словаре .

human = {}
frst_name = "kyrylo"
last_name = "holovchenko"
age = 27
city = "kyiv"

human[frst_name] = frst_name
human[last_name] = last_name
human[age] = age
human[city] = city

print(human[frst_name].title())
print(human[last_name].title())
print(human[age])
print(human[city].title())

print("My name is " + human[frst_name].title() + " " + human[last_name].title() 
    + ". I am " + str(human[age]) + " years old." + " I live in " + 
    human[city].title())