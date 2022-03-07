tuple1=(1,2,3,4,5,6,7,8,9,10)
tuple2=("python","odoo")

print(tuple1[:])
print(len(tuple1))
print(tuple1[::-1])


#convert tuple into list:

tuple3=list(tuple1 + tuple2)

print (tuple1 + tuple2)
print (tuple3)

print("python" in tuple2)

print(tuple1.index(9))
print(tuple2.index("odoo"))





#========================================
#     Conversion of data staructure
#========================================


set={"a","b","c","d"}
list=[1,2,3,4,5]
dict={"a": 5, "b": 9, "c": 10}

list1=tuple(set)
list2=tuple(list)
list3=tuple(dict)



print(type(list1))
print(type(list2))
print(type(list3))


