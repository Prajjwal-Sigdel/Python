def lists():
    def students():

        # Defining the list student with 2 elements
        student = ["Ram", "Hari"]

        # Copying list,(Shallow copy)
        temp = student.copy()

        print("Just two: ", student)
        student.append("Sita")
        student.insert(1, "Shyam")
        print("Added Sita and Shyam: ", student)
        student.remove("Hari")
        student.insert(2, "Ram")
        print("Removed hari and added Ram : ", student)

        # Found the index and count to respective elements
        print("Index of Sita: ", student.index("Sita"))
        print("Count of Ram: ", student.count("Ram"))

        # Reversed the order of elements in the list
        student.reverse()
        print("Reversed list of students: ", student)

        # Sorted the elements in the list
        student.sort()
        print("Initial list: ", temp)
        print("Sorted list: ", student)

        # Clearing the list
        student.clear()
        print("Cleared student: ", student, end="\n\n")
    # calling student
    students()


# calling lists
# lists()


def dictionaries():

    # Defining a dictionary
    student_info = {
        "name": "Ram",
        "age": 18,
        "subjects": ["Phy", "Chem", "Calculus"],
        "school": "GBS"
    }
    print("Initial Dictionary: ", student_info)

    # Copying a dict
    student_info1 = student_info.copy()

    # Accessing elements with keys of the dict
    print("Accessing name:", student_info["name"])

    # Adding and modifying the dict
    student_info["address"] = "Pokhara"
    student_info["age"] = 17
    print("Insertion & modification:", student_info)

    # Addinga and updating keys in dict
    student_info.update({"age": 19, "Gender": "Male"})
    print("Update and new key: ", student_info)

    # Removing a Key-Value pair
    del student_info["subjects"]
    print("Deletion of Key-Value pair: ", student_info)

    # Accessing the value from the dict
    # Default output for missing key: None
    print("The Subjects: ", student_info.get("Subject"))
    # Altered output for missing key
    print("The age: ", student_info.get("age", "Not Available"))
    # USing loop and keys() func
    for val in student_info.keys():
        print(val, ": ", student_info[val], sep="")

    # Clearing everything from student_info
    student_info.clear()
    print("Initial Dictionary: ", student_info1)
    print("Cleared Dictionary: ", student_info)


dictionaries()
