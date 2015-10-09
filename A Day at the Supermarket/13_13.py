groceries = [
    "banana",
    "pear",
    "apple"
    ]

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

def computeBill(groceries, total=0):
    for item in groceries:
        if item in prices:
            if int(stock[item]) >= 1:
                itemPrice = prices[item]
                print 'Item is: ' + item
                print 'Item price is: $' + str(itemPrice) + '\n'
                total = itemPrice + total
                stock[item] = int(stock[item])
            else:
                print 'This item ' + item + ' is not in stock. \n'

        print 'Running total is: $' + str(total) + '\n'
    return total

computeBill(groceries)
