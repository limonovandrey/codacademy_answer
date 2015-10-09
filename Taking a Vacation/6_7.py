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

def hotel_cost(days):
    return 140 * days
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
def trip_cost(city,days,spending_money):
    spending_money = rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
    return spending_money
