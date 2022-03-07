from modulefinder import Module
import selfmodule as sm
from selfmodule import addition


a=sm.person1["name"]
b=sm.person1[list]
c=sm.person1[tuple]
d=sm.person1["age"]
print(a)
print(b)
print(c)
print(d)


print(addition(2,3))
