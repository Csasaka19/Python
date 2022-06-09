string_list1 = ["City", "Nation", "Country", "Planets", "Galaxies"]
string_list2 = ["Galaxies", "Planets", "Multiverse", "Universe"]
print(string_list1)
print(string_list2)
union = string_list1 + string_list2   # Sets cannot be concatenated by the + operator
print(f"Union is: {union}")