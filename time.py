# Formatting dates:
from datetime import datetime

now = datetime.now()

print(now.strftime("%d/%B/%Y "))  # %B prints the name of the month while %b prints the short form of the month
# %m prints the  number of the month
print(now.strftime("%H:%M:%S"))

# Another way
from datetime import date
print(date.today().strftime("\n%d/%B/%Y"))
print(date.today().strftime("%H:%M:%S"))



    
