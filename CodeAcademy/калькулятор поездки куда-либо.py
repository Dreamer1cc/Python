def hotel_cost(nights):
    return 140 * nights
    
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
        
def rental_car_cost(days):
    car_costs = days * 40
    if days >= 7:
         car_costs -= 50
    elif days >= 3:
         car_costs -= 20
    return car_costs
    
def trip_cost(city, days, spending_money):
    all_cost = rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
    return all_cost
    
print trip_cost("Los Angeles", 5, 600) # All Costs 1955$