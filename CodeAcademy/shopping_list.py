# Write your code below!
def compute_bill(food):
    total = 0
    for x in food:
        if stock[x] !=0:
            total += prices[x]
            stock[x] -= 1
    return total

stock = {
    "banana":   6   ,
    "apple":    0   ,
    "orange":   32  ,
    "pear":     15
}
    
prices = {
    "banana":   4   ,
    "apple":    2   ,
    "orange":   1.5 ,
    "pear":     3
}

shopping_list = ["banana", "orange", "apple"]
print compute_bill(shopping_list)