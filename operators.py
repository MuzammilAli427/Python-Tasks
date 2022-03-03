
#====================================================#
#                       Operators
#====================================================#

'''Arthemetic Opreator'''

from ast import Assign, operator


value1=20
value2=30

print (value1 + value2)
print (value1 - value2)
print (value1 * value2)
print (value1 / value2)
print (value1 % value2)
print (value1 // value2)
print (value1 * value2 / value1)
print ((value1 * value2) - value1)


print ('''Comparison Opreator''')

mylist1=[1,2,3,4,5]
mylist=[6,7,8,9,10]

value1=value2=30
value3=40

print (value1 > value3)
print (value1 >= value3)
print (value1 < value3)
print (value1 <= value3)
print (value1 == value3)
print (value1 != value3)
print (value1 is value3)
print (value1 is not value3)
print (mylist1 + mylist)
print (mylist > mylist)
print (mylist < mylist)
print (mylist is mylist)

#===========================================#


'''Assignment operator'''

value1=20

value1 +=2
print (value1)


value1 -=2
print (value1)

value1 *=2
print (value1)

value1 /=2
print (value1)


value1 **=2
print (value1)


value1 +=2
print (value1)

value1 +=2
print (value1)


'''=================Logical Operator==================='''

value1=True and False
print(value1)


value1= True or False
print(value1)

value1= not False
print(value1)


'''bitwise operator'''
#Let True=1, False=0

a=1
b=0
print(a & b)
print(a | b)
print(~b)
print(a >> b)
print(a >> b)


















