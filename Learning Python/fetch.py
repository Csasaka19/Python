# Fetch from internet intro
from urllib import request
req = request.urlopen("https://www.bleepingcomputer.com/")
print(req.getcode())
print(req.read)
    
