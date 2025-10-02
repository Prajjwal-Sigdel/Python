import math as moo


def main():
    x = int(input("Enter a Value: "))
    sqr = moo.sqrt(x)
    print("The square toot is: ", sqr)
    print("Decimal only:", moo.trunc(sqr))
    print("Floor Value: ", moo.floor(sqr))
    print("Ceiling Value: ", moo.ceil(sqr))

    y = int(input("Input another Value: "))
    print("To the power 4: ", moo.pow(y, 4))
    print("To the log of 10: ", moo.log(y, 10))
    print("The greatest common divisor with 36: ", moo.gcd(y, 36))

    print("The Value of Pi: ", moo.pi)


if __name__ == "__main__":
    main()
