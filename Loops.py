
#================Loops==============#

# Looping Through a Range
# Looping Through a List/String

n=int(input("How many time you want to print ="))
for i in range(0,n):
    print("Write a Code")

'''
Output:
How many time you want to print =5
Write a Code
Write a Code
Write a Code
Write a Code
Write a Code
'''



n=int(input("How many time you want to print counting ="))
for i in range(0,n):
        print(i)



n=int(input("How many time you want to print Even/Odd ="))
for i in range(1,n):
    if i % 2==0:
        print("Numer is Even",i)
    else:
        print("Numer is Odd",i)


mylist=[1,2,3,4,5,6,7,8,9,10]
for i in mylist:
    if i % 2==0:
        print("Numer is Even",i)
    else:
        print("Numer is Odd",i)


n=int(input("Enter the number to print Table  "))
for i in range(1,11):
    print (str(n) + "x" + str(i) + "=",n*i)


from math import factorial


n=int(input("Enter the number to print Table "))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print(f"The factorial number is ={factorial}")



n=1
while(n<=10):
    print("Hi, Developer")
    n+=1


n=6
for i in range(1,n+1):
    print ("*" * (n-1))




mylist=[1,2,-2,4,5,6,7,8,9,10]

for i in range(len(mylist)):
    for j in range(i+1,len(mylist)):
        if mylist[i] + mylist[j] ==0:
            print("Right")
        else:
            print("Wrong")