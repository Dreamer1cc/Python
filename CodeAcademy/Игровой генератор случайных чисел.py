import random

<<<<<<< HEAD
print("Счастливые номер, три номера будет сгенерировано.")
=======
print("Lucky Numbers! 3 numbers will be generated.")
>>>>>>> refs/remotes/origin/next
print("If one of them is a '5', you lose!")

count = 0
while count < 3:
    num = random.randint(1, 6)
    print(num)
    if num == 5:
        print("Sorry, you lose!")
        break
    count += 1
else:
    print("You win!")