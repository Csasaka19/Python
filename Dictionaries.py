# Dictionaries: this is a data structure that  stores key value pairs for use later
# Football nominees dictionaries e.g. Best players shortlist for a season
Nominee = {
    "Name": "Player's Name",
    "age": "Player's Age",
    "Current Club": "Where he plays",
    "Club Position": "Position in the league table",
    "G/A contribution": "Goals and assists"
}  # Criteria used in the nomination

Nominee_one = {
    "name_1": "Kamaliza Tena",
    "age": 24,
    "Current Club": "Red Star FC",
    "Club Position": 8,
    "G/A contribution": 31
}
Nominee_two = {
    "name_2": "Clive Sasaka",
    "age": 22,
    "Current Club": "Annihilator's FC",
    "Club Position": 3,
    "G/A contribution": 48
}
Nominee_three = {
    "name_3": "Carlos Miller",
    "age": 32,
    "Current Club": "Dead Devils FC",
    "Club Position": 1,
    "G/A contribution": 28
}
Nominee_four = {
    "name_4": "Braun Mkennie",
    "age": 29,
    "Current Club": "Piemonte Calcio FC",
    "Club Position": 5,
    "G/A contribution": 40
}
Nominee_five = {
    "name_5": "Philip Foden",
    "age": 19,
    "Current Club": "Manchester City FC",
    "Club Position": 4,
    "G/A contribution": 15
}
print("The criteria of nomination is: {}" .format(Nominee.keys()))
# print(f"The criteria of nomination is: {Nominee_two.keys()}")
# if you want to know about the key values print(f"The criteria of the nominees is: {Nominee.values()}")
# or print("The values of the nominees is: {}" .format(Nominee.values()))
print("\nWhat a season it has been!!Though the race was tight the best player this season has been named")

print("\nThe best player this season is {}" .format(Nominee_two.get("name_2")))
print("A quick overview of his profile")
print("His name is: {}".format(Nominee_two["name_2"]))
print("His age is: {}".format(Nominee_two["age"]))
print("He is currently playing for: {}" .format(Nominee_two["Current Club"]))
print("His club is {}rd position in the league table".format(Nominee_two["Club Position"]))
print("He has  {} goal contributions  overally for his club".format(Nominee_two["G/A contribution"]))

print("\nThe second placed player this season is {}" .format(Nominee_four.get("name_4")))
print("A quick overview of his profile")
print("His name is: {}".format(Nominee_four["name_4"]))
print("His age is: {}".format(Nominee_four["age"]))
print("He is currently playing for: {}" .format(Nominee_four["Current Club"]))
print("His club is {}th position in the league table".format(Nominee_four["Club Position"]))
print("He has {} goal contributions overally for his club".format(Nominee_four["G/A contribution"]))


print("\nThe third placed player this season is {}" .format(Nominee_three.get("name_3")))
print("A quick overview of his profile")
print("His name is: {}".format(Nominee_three["name_3"]))
print("His age is: {}".format(Nominee_three["age"]))
print("He is currently playing for: {}" .format(Nominee_three["Current Club"]))
print("His club is {}st position in the league table".format(Nominee_three["Club Position"]))
print("He has {} goal contributions overally for his club".format(Nominee_three["G/A contribution"]))

# Another method: the dict.get() method
# print("\nThe best player this season is {}" .format(Nominee_two.get("Player name")))
# print("A quick overview of his profile")
# print("His name is: {}".format(Nominee_two.get("Player name")))
# print("His age is: {}".format(Nominee_two.get("age")))
# print("He is currently playing for: {}" .format(Nominee_two.get("Current Club")))
# print("His club is {} position in the league table".format(Nominee_two.get("Club Position")))
# print("He has contributed to {} goals overally for his club".format(Nominee_two.get("G/A contribution")))



