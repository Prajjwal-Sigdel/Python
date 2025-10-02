import math


def main():
    x = int(input("Enter a Value: "))
    sqr = math.sqrt(x)
    print("The square toot is: ", sqr)
    print("Decimal only:", math.trunc(sqr))
    print("Floor Value: ", math.floor(sqr))
    print("Ceiling Value: ", math.ceil(sqr))

    y = int(input("Input another Value: "))
    print("To the power 4: ", math.pow(y, 4))
    print("To the log of 10: ", math.log(y, 10))
    print("The greatest common divisor with 36: ", math.gcd(y, 36))

    print("The Value of Pi: ", math.pi)


if __name__ == "__main__":
    main()
