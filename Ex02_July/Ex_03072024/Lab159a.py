# File IO
import os.path
try:
    file = open('mani.txt', 'r')
    print(file.read())

except FileNotFoundError as fnfe:
    print("I am not able find the file, Please add the correct path.")

finally:
    print("Executed.")
    try:
        file.close()
    except NameError as ne:
        print(ne)