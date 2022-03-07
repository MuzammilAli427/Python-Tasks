import re

txt = "The rain in pakistan"

x = re.findall("ai", txt)
y = re.search("The", txt)

if y:
    print("Matched")
else:
    print("Not Matched")
print(x)



st="this is a boy @ # abc"
s=re.findall("@",st)
print(s)

txt = "The rain in lahore"
x = re.search("in", txt)
print(x)


txt = "Python is used in webscraping AI Machine learning"
x = re.split("\s", txt)
print(x)