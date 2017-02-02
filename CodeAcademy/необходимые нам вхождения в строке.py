# Write your function below!
# функция для подсчета количества необходимых вхождений
def fizz_count(x):
    count = 0
    for item in x:
        if item == "fizz":
            count += 1
    return count
all_them = fizz_count(["fizz","cat","fizz"])
print all_them
