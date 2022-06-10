# While loop,break and continue
# Continue: checks if the condition is true and continues within the loop
# Break: escapes a certain loop
numeral = 0
while numeral <= 100:
    numeral += 1
    if numeral < 2:
        continue  # Continue checks for 0, 1 and 100 then excludes them and continues with the rest of the loop
    elif numeral == 100:
        break  # Break escapes the loop
    elif numeral % 6 == 0:
        print("FizzBuzz")  # Numbers that are both divisible by 2 and 3
    elif numeral % 2 == 0:
        print("Fizz")
    elif numeral % 3 == 0:
        print("Buzz")
    else:
        print(numeral)