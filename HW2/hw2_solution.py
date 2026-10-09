def calculate_parking_cost(hours):
    if hours <= 2:
        cost = 5
    elif hours <= 6:
        cost = 10
    else:
        cost = 15

    return cost


hours = int(input("How many hours did you park?"))
day_type = input("Is it a weekday or weekend?")

if hours <= 0 or hours > 24:
    print("That is not a valid number of hours.")

else:
    parking_cost = calculate_parking_cost(hours)

    if day_type == "weekend":
        parking_cost = parking_cost * 0.8

    print(f"Your parking cost is ${parking_cost:.2f}.")