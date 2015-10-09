def compute_bill(food):
    total = 0
    for key in food:
        total += prices[key]
    return total

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
b = [1, 2, 3, 32, 8, 12]
print compute_bill(prices)
