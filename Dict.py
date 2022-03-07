dict={
    "a":"Muzammil",
    "b":10,
    "c":True,
    "d":[1,2,3,4,5,6],
    "e":{"m":23},
    1:2
}


print(dict["a"])
dict["b"]=[20]       
print(dict["b"])

print(dict.keys())

print(dict.values())


print(dict.items())

p=dict.pop("b")
print (p)



#==========================#


updatedict={
    "Pyhton":"Developer"
}

dict.update(updatedict)
print(dict)


print(dict.get("b"))
print(dict["a"])


#delete keys wiht values:

del dict["b"]
print(dict)


#==========================#


#========================================
#     Conversion of data staructure
#========================================


set={("a",1),("b",2),("c",3),("d",4)}
list=[[1,2],[3,4],[5,6]]
tuple=((12,22),(34,75),(96,7))

list1=dict(set)
list2=dict(list)
list3=dict(tuple)



print(type(list1))
print(type(list2))
print(type(list3))