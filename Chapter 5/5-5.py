# 5-3 . Цвета 1: представьте, что в вашей компьютерной игре только что был подбит 
# корабль пришельцев . Создайте переменную с именем alien_color и присвойте ей 
# значение ‘green’, ‘yellow’ или ‘red’ . • Напишите команду if для проверки того, 
# что переменная содержит значение ‘green’ . Если условие истинно, выведите 
# сообщение о том, что игрок только что заработал 5 очков . 
# • Напишите одну версию программы, в которой условие if выполняется, и другую 
# версию, в которой оно не выполняется . 
# (Во второй версии никакое сообщение выводиться не должно .) 
alien_color = "green"
if alien_color == "green":
    print("Вы только что заработало 5 очков!")

alien_color = "red"
if alien_color == "green":
    print("Вы только что заработало 5 очков!")

# 5-4 . Цвета 2: выберите цвет, как это было сделано в упражнении 5-3, и напишите 
# цепочку if-else . 
# • Напишите команду if для проверки того, что переменная 
# содержит значение ‘green’ . Если условие истинно, выведите сообщение о том, что 
# игрок только что заработал 5 очков . 
# • Если переменная содержит любое другое 
# значение, выведите сообщение о том, что игрок только что заработал 10 очков . 
# • Напишите одну версию программы, в которой выполняется блок if, и другую 
# версию, в которой выполняется блок else . 

alien_color = "green"
if alien_color == "green":
    print("Вы только что заработало 5 очков!")
else:
    print("Вы только что заработали 10 очков!")

alien_color = "red"
if alien_color == "green":
    print("Вы только что заработало 5 очков!")
else:
    print("Вы только что заработали 10 очков!")

# 5-5 . Цвета 3: преобразуйте цепочку if-else из упражнения 5-4 в цепочку 
# if-elif-else . 
# • Если переменная содержит значение 'green', выведите сообщение о том, что игрок
# только что заработал 5 очков . 
# • Если переменная содержит значение 'yellow', 
# выведите сообщение о том, что игрок только что заработал 10 очков . 
# • Если переменная содержит значение 'red’, выведите сообщение о том, что игрок 
# только что заработал 15 очков . 
# • Напишите три версии программы и проследите за тем, чтобы для каждого цвета 
# пришельца выводилось соответствующее сообщение .

alien_color = "green"
if alien_color == "green":
    print("Вы только что заработали 5 очков!")
elif alien_color == "yellow":
    print("Вы только что заработали 10 очков!")
elif alien_color =="red":
    print("Вы только что заработали 15 очков")

alien_color = "yellow"
if alien_color == "green":
    print("Вы только что заработало 5 очков!")
elif alien_color == "yellow":
    print("Вы только что заработали 10 очков!")
elif alien_color =="red":
    print("Вы только что заработали 15 очков")

alien_color = "red"
if alien_color == "green":
    print("Вы только что заработало 5 очков!")
elif alien_color == "yellow":
    print("Вы только что заработали 10 очков!")
elif alien_color =="red":
    print("Вы только что заработали 15 очков")