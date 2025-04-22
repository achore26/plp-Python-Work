def modify_line(line):
    return line.upper()

def read_and_modify_file():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        modified_lines = [modify_line(line) for line in lines]

        new_filename = "modified_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.writelines(modified_lines)

        print(f"File successfully modified and saved as '{new_filename}'.")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

read_and_modify_file()
