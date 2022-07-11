# Weight convertor
weight = float(input("What is your weight? "))
unit = input("K(g) or P(d): ")
if weight < 0:
    print("Error")
elif unit.upper() == "K":
    convertor = weight * 0.45
    print("Kilogram: {} " .format(convertor))

elif unit.upper() == "P":
    convertor = weight / 0.45
    print("Pounds: {}" .format(convertor))

else:
    print("Invalid input!!Try again")

