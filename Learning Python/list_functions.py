# List functions
my_first_list = [120, 99, 7890, 90, -45, -56, 3.42]

# Pop: removes an item from a list
my_first_list.pop(4)  # The fourth item is removed
print(my_first_list)

# Append: adds item to a list
my_first_list.append(134)
print(my_first_list)

# Remove: removes some elements from a list NB pop uses index while remove uses the actual value
my_first_list.remove(99)
print(my_first_list)

# Sort: arranges list in ascending order
my_first_list.sort()
print(my_first_list)

# Reverse: changes the order of the list
my_first_list.reverse()
print(my_first_list)

# Copy: replicates a selected list
copied_list = my_first_list.copy()
print(copied_list)

# Insert: ,adds a certain element to a specified index
my_first_list.insert(4, 20)
print(my_first_list)

# Index: shows the index of an item in the list
index = my_first_list.index(90)
print(index)

# Count: counts the number of times an item appears in a list
count = my_first_list.count(7890)
print(count)

# Checking for values in list using operators
print(3.42 in my_first_list)
print(240 not in my_first_list)

if my_first_list[3] <= 80:
    print("Value is very minimal")
else:
    print("Value in list is the required one")

# Clear: clears the entire list
my_first_list.clear()
print(my_first_list if len(my_first_list) <= 0 else "List is still not cleared")

# Sets are similar to lists, but they do not favour duplicates like lists and use curly braces {} e.g.
lister = [1, 1, 2, 2, 3, 43, 43, 75]
sett = {1, 1, 1, 2, 2, 3, 43, 43, 75}
print(lister)
print(sett)   # The set cancels out the recursion of items in the set and prints only one
# Sets display an unordered output after every execution

# Deleting by a range
# del my_first_list[0:4] deletes the first four elements
