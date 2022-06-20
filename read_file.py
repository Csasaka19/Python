# File input output basics
# r: read, w:write, r+:read and write a:append
file = open("first.py")
print(file.readline())  # Reads a file line by line but prints it in one line
for line in file:
    print(line)  # also reads a file line by line
print(file.read())  # reads file randomly
file.close()  # file must be closed once it is opened


    
