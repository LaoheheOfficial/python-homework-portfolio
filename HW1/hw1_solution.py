number_of_floors = 6
price_per_hour = 4

def find_floor(ticket_number):
    floor = (ticket_number - 1) % number_of_floors + 1
    return floor

def parking_cost(hours):
    cost = hours * price_per_hour
    return cost

print(find_floor(1))
print(find_floor(6))
print(find_floor(7))
print(find_floor(8))
print(find_floor(15))

print(parking_cost(1))
print(parking_cost(2))
print(parking_cost(3))
print(parking_cost(4))
print(parking_cost(5))