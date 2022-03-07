
from re import I


fact=1
n=int(input("Enter the number for Factorial "))
for i in range(1,n+1):
    fact=fact*i
    
print (fact)



def factorial(a):
    if a==0 :
        return 1
    return a * factorial(a-1)

print(factorial(5))





def maxi(n1,n2,n3):
    m=max(n1,n2,n3)
    return m

max_num=maxi(1,2,4)
print("The Maximum Values is : ",max_num)



n=int(input("Number"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("Sum is ",sum)