import requests
from os import getcwd

url = "https://raw.githubusercontent.com/riceboypeter/CMPUT-404-lab-1/main/myScript.py"
d = getcwd()
filename = d + "myScript.py"
r = requests.get(url)

f = open(filename,'w')
f.write(r.text)
f.close()

f = open(filename, 'r')
print(f.read())