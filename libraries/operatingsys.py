import os


def create_directory():
    path = input("Enter the path to create a new directory: ")
    try:
        os.mkdir(path)
        print(f"Directory '{path}' created successfully.")
    except FileExistsError:
        print(f"Directory '{path}' already exists.")
    except Exception as e:
        print(f"Error creating directory: {e}")


def rename_directory():
    old = input("Enter the current directory path: ")
    new = input("Enter the new directory path: ")
    try:
        os.rename(old, new)
        print(f"Directory renamed to '{new}' successfully.")
    except Exception as e:
        print(f"Error renaming directory: {e}")


def remove_directory():
    path = input("Enter the directory path to remove: ")
    try:
        os.rmdir(path)
        print(f"Directory '{path}' removed successfully.")
    except OSError:
        print(f"Directory '{path}' is not empty or cannot be removed.")
    except Exception as e:
        print(f"Error removing directory: {e}")


def create_file():
    path = input("Enter the file path to create: ")
    try:
        with open(path, 'w') as f:
            f.write("This is a test file.")
        print(f"File '{path}' created successfully.")
    except Exception as e:
        print(f"Error creating file: {e}")


def rename_file():
    old = input("Enter the current file path: ")
    new = input("Enter the new file path: ")
    try:
        os.rename(old, new)
        print(f"File renamed to '{new}' successfully.")
    except Exception as e:
        print(f"Error renaming file: {e}")


def remove_file():
    path = input("Enter the file path to remove: ")
    try:
        os.remove(path)
        print(f"File '{path}' removed successfully.")
    except Exception as e:
        print(f"Error removing file: {e}")


def main():
    while True:
        print("\nFile/Directory Operations Menu:")
        print("1. Create Directory")
        print("2. Rename Directory")
        print("3. Remove Directory")
        print("4. Create File")
        print("5. Rename File")
        print("6. Remove File")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            create_directory()
        elif choice == '2':
            rename_directory()
        elif choice == '3':
            remove_directory()
        elif choice == '4':
            create_file()
        elif choice == '5':
            rename_file()
        elif choice == '6':
            remove_file()
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
