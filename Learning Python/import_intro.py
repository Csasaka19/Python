# Importing modules
from sys import argv  # this module handles arguments

word = "Player is Known"
print(word if len(argv) >= 0 else "The number of arguments are really low")

from functions import add, powe, modu  # person module

print(add(345, 456))
print(powe(34, 7))
print(modu(543, 9))

import datetime  # module deals with dates and time

print(datetime.date.today())
print(datetime.time.max)
print(datetime.datetime.now())
