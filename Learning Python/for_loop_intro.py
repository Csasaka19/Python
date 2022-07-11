# For loop
my_list = [1, 2, 3, 4, 5]
for i in my_list:
    print("{:^4d}" .format(i))

# If else within a for loop
cities = ["Nairobi", "Cairo", "Sydney", "Malibu", "Sasaka"]
for city in cities:
    print(city if len(city) >= 5 else "Invalid city", end=",")

# Looping through dictionaries
Student = {
    "Name": "Clive Sasaka",
    "Major": "Computer Science",
    "age": 20,
    "Status": "Sina money!!",
    "ID": 23456098765
}
print(f"\nThe items within the list are: {Student.items()}")

for key, value in Student.items():
    print(f"\nKey name is: {key}.\n Value is: {value}")

# The total sum of a list using a loop
digits = [89, 70, 123, 405, -12, -23]
for digit in digits:
    addition = sum(digits)

print("The total sum of the list is {}" .format(addition))
