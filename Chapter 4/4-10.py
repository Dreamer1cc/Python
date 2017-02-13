"""
4-10 . Срезы: добавьте в конец одной из программ, написанных в этой главе, фрагмент, который делает следующее .

• Выводит сообщение «The first three items in the list are:», а затем использует срез для вывода первых трех элементов из списка . 
• Выводит сообщение «Three items from the middle of the list are:», а затем использует срез для вывода первых трех элементов из середины списка . 
• Выводит сообщение «The last three items in the list are:», а затем использует срез для вывода последних трех элементов из списка .
"""
pizzaz = ["margarita", "bavaria", "truffel", "meat", "pineapple"]
for pizza in pizzaz:
	print("I like " + pizza + " pizza")
print("I really love pizza!")
print("The first three items in the list are:")
print(pizzaz[:3])
print("Three items from the middle of the list are:")
print(pizzaz[2:])
print("The last three items in the list are:")
print(pizzaz[-3:])