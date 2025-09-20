def greet():
    x = input("Greetings costumer: ").lower().strip()
    if x == 'hello':
        print("20$ /-")
    elif x[0] == 'h':
        print("50$ /-")
    else:
        print("100$ /-")


def extension():
    # Getting the flie name from the user
    file_name = input("Enter the file name with extension").strip().lower()

    # Determine the file's media type based on its extension
    if file_name.endswith(".txt"):
        print("text/plain")
    elif file_name.endswith(".gif"):
        print("image/gif")
    elif file_name.endswith(".jpg"):
        print("image/jpeg")
    elif file_name.endswith(".png"):
        print("image/png")
    elif file_name.endswith(".pdf"):
        print("application/pdf")
    elif file_name.endswith(".zip"):
        print("application/zip")
    else:
        # For all other file extensions or no extensions at all
        print("application/octet-stream")


def interpret():
    expression = input("Enter the expression: ")
    x, y, z = expression.split(' ')
    x = float(x)
    z = float(z)
    if y == '/' and z == 0:
        print("Invalid expression")
    else:
        if y == '+':
            result = x+z
        elif y == '-':
            result = x-z
        elif y == '*':
            result = x*z
        elif y == '/':
            result = x/z
        else:
            result = "Invalid operator"
        print(result)


def meal():
    time = input("Enter the time as Hrs:Min ")
    hr, mi = time.split(":")
    time1 = int(hr)+(int(mi)/60)
    if time1 >= 7 and time1 < 8:
        print("Breakfast time!!!")
    elif time1 >= 12 and time1 < 13:
        print("Lunch time!!!")
    elif time1 >= 18 and time1 < 19:
        print("Dinner time!!!")
    else:
        print("Just get to work buddy !!!")


meal()
