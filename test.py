from string import digits, ascii_lowercase, ascii_uppercase
import os


chars = ascii_lowercase + ascii_uppercase + digits # The chars for checking first element in the string


def check_line(line):
    """ The function for checking first element in the string """
    return True if line[0] in chars else False


def create_file(name_file_with_extension: str):
    """ The function to create a file """
    try:
        with open(os.path.join(os.getcwd(), "result", name_file_with_extension), "w"):
            pass
    except FileNotFoundError:
        print(f"Error to create a file {name_file_with_extension}")


create_file("English.txt")
create_file("Russian.txt")

try:
    with open("PythonTest.txt", "r") as file_handler:
        for line in file_handler:
            if not check_line(line):
                continue
            l = line.split("\t")
            for i in l[0].split(";"):
                for j in range(l[1].count(";") + 1):
                    with open(os.path.join(os.getcwd(), "result", "English.txt"), "a") as english:
                        english.write(i.strip() + "\n")
                    with open(os.path.join(os.getcwd(), "result", "Russian.txt"), "a") as russian:
                        russian.write(l[1].split(";")[j].strip() + "\n")

except FileNotFoundError:
    print("Error to open the file 'PythonTest.txt'")

