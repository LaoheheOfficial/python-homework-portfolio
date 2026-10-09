# Parking Garage Ticket System

A parking garage has 6 floors. Each car has a ticket number, and the floor is determined by the ticket number.

Write a Python program that does the following:

1. Create a function called `find_floor(ticket_number)` that returns a floor number from 1 to 6.
2. Use the modulo operator `%` so that ticket numbers repeat through floors 1-6.
3. Create another function called `parking_cost(hours)` that calculates the parking cost. The garage charges $4 per hour.
4. Test both functions using at least five different ticket numbers and parking times.
5. Use variables or constants so that the number of floors and hourly price are not repeated throughout the code.
6. Print the ticket number, assigned floor, number of hours, and total cost for each test case.

## Explanation

This problem is meant to test variables, functions, expressions, the modulo operator, and the DRY principle. The student needs to turn written instructions into Python code and use functions to break the problem into smaller parts.

The hardest part may be using `%` to make the floor numbers repeat from 1 to 6 instead of 0 to 5. Students also need to avoid repeating important values, such as the hourly price and number of floors, which helps practice DRY programming.