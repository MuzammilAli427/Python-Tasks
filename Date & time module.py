
import datetime
from datetime import date 
import random
import math

list=[1,2,3,4,5,6,7,8,9,10]

d=datetime.datetime.now()
e=datetime.date.today()


random.shuffle(list)

rand=random.uniform(1,10)

fact=math.factorial(5)

print(d)
print(d.time())
print(e)
print(d.strftime("%A"))

print(list)
print(rand)

print(fact)