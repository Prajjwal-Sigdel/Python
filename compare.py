def con():
    # Request two values from user
    x = int(input("Enter the first value: "))
    y = int(input("Enter the second value: "))

    # Comparing the two values
    if x > y:
        print(x, "is greater than", y)
    elif y > x:
        print(y, "is greater than", x)
    else:
        print("They are both equal.")


def mulitcon():

    # Get total marks from the user
    total = int(input("Enter your total score: "))

    # Compare and continue to print
    if total > 90:
        print("Distinction.")
    elif total <= 90 and total > 80:
        print("First Division.")
    elif total <= 80 and total > 70:
        print("Second Division.")
    else:
        print("You failed miserably fam!!!")


def is_even(n):         # To return a bool for even or odd stature of the passed value
    if n % 2 == 0:
        return True
    else:
        return False


def is_even1(n):        # Single line return statement
    return n % 2 == 0


def is_even2(n):        # Pythonic code whose format is unique to python only
    return True if n % 2 == 0 else False


def main():             # Main function that does the job
    x = int(input("Enter a number: "))
    if is_even2(x):
        print("The number is even...")
    else:
        print("The number is odd...")


def mat():              # Match function to know the day of the week
    a = int(input("Enter the day number: "))
    match a:
        case 1:
            print("Sunday")
        case 2:
            print("Monday")
        case 3:
            print("Tuesday")
        case 4:
            print("Wednesday")
        case 5:
            print("Thrusday")
        case 6:
            print("Friday")
        case 7:
            print("Saturday")
        case _:
            print("Invalid day number")


mat()
