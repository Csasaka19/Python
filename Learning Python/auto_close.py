# opening file with automatic close; (with as method)
import os.path

filename = "JR.py"

if os.path.isfile(filename):  # Checks if file exists in the current path
    with open(filename, "r") as file:
        print(file.readlines())
else:  # if file does not exist this is printed
    print(f"\nThe file {filename},is non-existent.")


    
