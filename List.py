
list=[1,2,3,4,5,6,7]
print(sum(list))



list=[10,2,3,4,5,6,7]
list.sort()
print (list)


list=[10,2,3,4,5,6,7]
list1=min(list) #Also max()
print (list1)


list=[10,2,3,4,5,6,7]
list.pop(0)
print (list)



list2=['ali','ain','maam zoya','sir waqas']
list1=[1,2,3,4,5,6,7,10]

print(list1 + list2)


list=[1,2,3,4,5,6]
if 1 in list:
    print("present")


list=[1,2,3,4,5,6,7,8,909]
list [1:2]=[22,33]
print(list)


list=[1,2,3,4,5,6,7,8,909]
list.insert(2,"muzzi")
print(list)




list=[1,2,3,4,5,6,7,8,909]
if 1 in list:
    list.append("ali")
    print (list)
	
	
	
list = ["apple", "banana", "cherry"]
new=[]
for i in list:
    if "b" in i:
        new.append(i)
print(new)


my="Welcome to developer team"
print(my.find("to"))
print(my.replace("W","w"))
print(my.upper())
print(my.lower())
print('>'.join(my))
print(','.join(my))







list=[1,2,3,4,5,6,7,8,909]
max=0
for i in list:
    if(i>max):
        max=i
    elif():
        break
print ("congrants! you are greater = " ,max)



mylist=["Muzzi", 1,0.2,True,]
print (mylist[0])
print (len(mylist))
print (len(mylist[0]))



list=["Python","java","C++","cSharp"]
if 'Python' in list:
    print("Character is avaliable in list")


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



