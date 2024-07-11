# File IO

try:
    with open('mani.txt', 'r') as file:
        print(file.read())
        file.close()

except FileNotFoundError as fnfe:
    print("I am not able find the file, Please add the correct path.")

finally:
    print("Closing the file.")
    file.close()