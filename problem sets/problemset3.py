
# In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is a positive integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.


def fuel_gauge():
    while True:
        try:
            x, y = input("Enter a Fraction: ").split("/")
            x = int(x)
            y = int(y)
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError

            # Calculating Percentage
            percentage = round((x/y)*100)

            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(percentage, "%")

        except (ZeroDivisionError, ValueError):
            pass


# implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. Treat the user’s input case insensitively. Ignore any input that isn’t an item.


menu = {
    "momo": 120,
    "chowmein": 100,
    "ice peach tea": 200,
    "pizza": 300,
    "burger": 140,
    "fries": 100
}


def food_menu():
    total = 0
    while True:
        try:
            food = input("Enter your order: ").lower()
            if food == "":
                break
            if food in menu:
                total += menu[food]
                print(total, "$")
        except EOFError:
            break


# Implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.

def groceries():
    # Defining an dictionary to store all the grocery items
    item = {}

    # initilizing try
    try:
        # Running loop until a KeyboardInterrupt
        while True:
            food = input("Enter a value: ").upper()
            if food in item:
                item[food] += 1  # Increasing value for repeated keys
            else:
                item[food] = 1

    # Defining the exception in try
    except KeyboardInterrupt:
        print("\n\n")
        # Providing the list of Groceries
        for key, value in item.items():
            print(value, key)


# implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein all the months are included


def outdated():
    # Storing all the months
    month = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    # Taking input date
    date = input("Date: ").strip()
    try:
        mm, dd, yy = date.split("/")  # First case of date formatt
    except ValueError:
        mm, rem = date.split(" ", 1)
        dd, yy = rem.split(",")
        mm = str(month.index(mm) + 1)  # Converting month to its number
    # Displaying date in desired formatt
    print(yy, mm, dd, sep="-")


fuel_gauge()
food_menu()
groceries()
outdated()
