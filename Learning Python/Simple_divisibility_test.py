# Simple divisibility test
numeral = 0
for numeral in range(2, 100):
    if numeral < 2 and numeral == 100:
        continue  # Continue checks for 0, 1 and 100 then excludes them and continues with the rest of the loop
    elif numeral % 2 == 0:
        print("Fizz")
    elif numeral % 3 == 0:
        print("Buzz")
    else:
        print(numeral)