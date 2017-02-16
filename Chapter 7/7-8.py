# 7-8 . Сэндвичи: создайте список с именем sandwich_orders, 
# заполните его названиями различных видов сэндвичей . Создайте пустой список с 
# именем finished_sandwiches . В цикле переберите элементы первого списка и 
# выведите сообщение для каждого элемента (например, «I made your tuna sandwich»)
#  . После этого каждый сэндвич из первого списка перемещается в список 
#  finished_sandwiches . После того как все элементы первого списка будут 
#  обработаны, выведите сообщение с перечислением всех изготовленных сэндвичей .

sandwich_orders = [
    "Крок-месье", "Крок-мадам", 
    "Горячий бутерброд с сыром на гриле", "Муффулетта",
    ]
finished_sandwiches = []
while sandwich_orders:
    maiden_san = sandwich_orders.pop()
    print("Я сделал твой " + maiden_san + " сэндвич")
    finished_sandwiches.append(maiden_san)
print(finished_sandwiches)
print("Изготовлены следующие сэндавичи: ")
for finish_sandwich in finished_sandwiches:
    print(finish_sandwich)
