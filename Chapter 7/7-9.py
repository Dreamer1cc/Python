# 7-9 . Без пастрами: используя список sandwich_orders из упражнения 7-8, 
# проследите за тем, чтобы значение ‘pastrami’ встречалось в списке как 
# минимум три раза . Добавьте в начало программы код для вывода сообщения 
# о том, что пастрами больше нет, и напишите цикл while для удаления всех 
# вхождений ‘pastrami’ из sandwich_orders . Убедитесь в том, что в 
# finished_sandwiches значение ‘pastrami’ не встречается ни одного раза .

sandwich_orders = [
    "Крок-месье", "Крок-мадам", 
    "Горячий бутерброд с сыром на гриле", "Муффулетта", "pastrami",
    "pastrami", "pastrami",
    ]
finished_sandwiches = []
print("Pastrami is over")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    maiden_san = sandwich_orders.pop()
    print("Я сделал твой " + maiden_san + " сэндвич")
    finished_sandwiches.append(maiden_san)

if "pastrami" not in finished_sandwiches:
    print("Изготовлены следующие сэндавичи: ")
    for finish_sandwich in finished_sandwiches:
        print(finish_sandwich)

