import os


def main():
    print("Current Working Directory: ", os.getcwd())
    path = input("Enter a path to create a new directory: ")
    try:
        os.mkdir(path)
        print(f"Directory '{path}' created successfully.")
    except FileExistsError:
        print(f"Directory '{path}' already exists.")
    except Exception as e:
        print(f"Error creating directory '{path}': {e}")

    new_path = input("Enter a new path to rename the directory: ")
    try:
        os.rename(path, new_path)
        print(f"Directory renamed to '{new_path}' successfully.")
    except FileNotFoundError:
        print(f"Directory '{path}' does not exist.")
    except Exception as e:
        print(f"Error renaming directory '{path}': {e}")

    try:
        os.rmdir(new_path)
        print(f"Directory '{new_path}' removed successfully.")
    except FileNotFoundError:
        print(f"Directory '{new_path}' does not exist.")
    except OSError:
        print(f"Directory '{new_path}' is not empty or cannot be removed.")
    except Exception as e:
        print(f"Error removing directory '{new_path}': {e}")

    file_path = input("Enter a file path to create a new file: ")
    try:
        with open(file_path, 'w') as f:
            f.write("This is a test file.")
        print(f"File '{file_path}' created successfully.")
    except Exception as e:
        print(f"Error creating file '{file_path}': {e}")

    new_file_path = input("Enter a new file path to rename the file: ")
    try:
        os.rename(file_path, new_file_path)
        print(f"File renamed to '{new_file_path}' successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' does not exist.")
    except Exception as e:
        print(f"Error renaming file '{file_path}': {e}")

    try:
        os.remove(new_file_path)
        print(f"File '{new_file_path}' removed successfully.")
    except FileNotFoundError:
        print(f"File '{new_file_path}' does not exist.")
    except Exception as e:
        print(f"Error removing file '{new_file_path}': {e}")


if __name__ == "__main__":
    main()
