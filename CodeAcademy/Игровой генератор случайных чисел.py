import random

print("Счастливые номер, три номера будет сгенерировано.")
print("Если один из них '5', ты проиграл!")

count = 0
while count < 3:
    num = random.randint(1, 6)
    print(num)
    if num == 5:
        print("Ты проиграл, очень жаль!")
        break
    count += 1
else:
    print("И вот наш победитель!")