
set={"a","b","c","d","e",(1,2,3,4,5)}
tuple=(9,8,7,6,5)




print (set)
print (len(set))




set.add("Pakistan")
print(set)



set.update(tuple)
print(set)




list=[]
tuple={1,2,3,4,5,6,7,8,9,10,11,12,13}

for i in tuple:
    if(not i % 2==0):
        list.append(i)

print (list)



#=============================================#
#    Union ,Intersection ,Difference
#=============================================#


set={"a","b","c","d"}
set2={1,2,3,4,5,6,7}
set3={1,3,5,6,8,9,}

print(set2 | set3)
print(set2.union(set3))


print(set2 & set3)
print(set2.intersection(set3))


print(set2-set3)
print(set2.difference(set3))



#========================================
#     Conversion of data staructure
#========================================


set={"a","b","c","d"}
tuple=(1,2,3,4,5)
dict={"a": 5, "b": 9, "c": 10}

list1=list(set)
list2=list(tuple)
list3=list(dict)



print(type(list1))
print(type(list2))
print(type(list3))



