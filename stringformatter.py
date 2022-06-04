print("Sammy has {} balloons.".format(5))

open_string = "Sammy loves {}."
print(open_string.format("open source"))

new_open_string = "Sammy loves {} {}."                      # 2 {} placeholders
print(new_open_string.format("open-source", "software"))    # Pass 2 strings into method, separated by a comma

# Indexing
print("Sammy the {1} has a pet {0}!".format("shark", "pilot fish"))

# Keyword eg ke
print("Sammy the {0} {1} a {ke}.".format("shark", "made", ke = "pull request"))

# Specifying type {field_name:conversion}
print("Sammy ate {0:.4f} percent of a {1}!".format(75, "pizza"))

# Alignment <(left) >(right) ^(center)
print("Sammy has {0:<4} red {1:^16}!".format(5, "balloons"))

print("{:*^40s}".format("Sammy"))

print("Sammy ate {0:^5.0f} percent of a pizza!".format(75.765367))

# Using Variables
nBalloons = 8
print("Sammy has {} balloons today!".format(nBalloons))
# sammy = "Sammy has {} balloons today!"
# nBalloons = 8
# print(sammy.format(nBalloons))

# Using Formatters to Organize Data
for i in range(3,13):
    print("{:^3d} {:^4d} {:^5d}".format(i, i*i, i*i*i))

# Conclusion
# Using formatters for variable substitution can be an effective way to concatenate strings and organize values and data