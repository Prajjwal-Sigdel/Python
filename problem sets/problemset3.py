
# In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is a positive integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

def fuel_gauge():

    while True:

        try:
            fract = input("Enter a fraction: ")
            x, y = fract.split("/")
            x = int(x)
            y = int(y)

            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError

            percentage = round((x/y)*100)

            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break

        except (ZeroDivisionError, ValueError):
            pass


if __name__ == "__main__":
    fuel_gauge()
