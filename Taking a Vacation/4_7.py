def rental_car_cost(day):
    cost = 40 * day
    if day >= 7:
        cost -= 50
        return cost
    elif day >= 3:
        cost -= 20
        return cost
    else:
        return cost
    
