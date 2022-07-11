# Set union, difference and intersection
# Union: simply concatenates two sets, represented by |
string_set1 = {"City", "Nation", "Country", "Planets", "Galaxies"}
string_set2 = {"Galaxies", "Planets", "Multiverse", "Universe"}
print(string_set1)
print(string_set2)
union = string_set1 | string_set2   # Sets cannot be concatenated by the + operator
print(f"Union is: {union}")

# Intersection: shows similar elements and displays them to the output, represented by &
intersection = string_set1 & string_set2
print(f"Intersection is: {intersection}")

# Difference: removes common elements the displays the result, represented by the -
difference = string_set1 - string_set2  # Shows remainder of elements in the first set only
print(f"The difference of string_set1 is: {difference}")

difference2 = string_set2 - string_set1   # Shows remainder of elements in the second set only
print(f"The difference of string_set2 is: {difference2}")

# Remember sets does not display elements in the order printed during execution