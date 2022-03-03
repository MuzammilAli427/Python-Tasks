
price=int(input("Enter the number"))
if price >=300:
    print(price*0.3)
elif(price >=300 or price <=200):
    print(price*0.2)
elif(price >=200 or price <=100):
    print(price * 0.1)
elif(price <=100):
    print(price *0.1)
	
	
	
	
tab=int(input('Enter the value'))
for i in range(1,11):
        print ("%d x %d = %d" % (tab,i,tab*i))
		


#=========================================================#		                
#						Function creation:
#=========================================================#
# 
# 
# 	
a=int(input("Enter the value to find the maxiumum"))
b=int(input("Enter the value to find the maxiumum"))
max=0
if a>b:
    max=a
    print("you find the Max value=", a)
elif(b>a):
    max=b
    print("you find the Max value=", b)



a=int(input("Enter the value to find the maxiumum"))
b=int(input("Enter the value to find the maxiumum"))

print(min(a,b))
print(sum(a,b))
print(type(a,b))


list=[1,2,3,4,5,6,7,8,9]
print(sum(list))
print(min(list))





def myfun():
    a=int(input("Enter the value to find the maxiumum"))
    b=int(input("Enter the value to find the maxiumum"))
    print(min(a,b))

    
myfun()




def my_function(a,b):
    sum=a+b
    print("the sum is =",sum)

my_function(1,2)


#===============================#




def find_max(a,b):
    max=0
    if a>b:
        max=a
        #print("you find the Max value=", a)
    elif(b>a):
        max=b
        #print("you find the Max value=", b)
    return max


find_max(3,2)

#===============================#




#========================================Function Scope================================
#Data cycle:
#===========

def fun():
    name = "Muzammil"
      
fun()



#Altering Data:
#==============

a=10

def fun(b):
    b *=2
    x=b
    print("The value inside the function is ",x)
    return x
fun(a)
print("The value outside the function is ",a)

#================================================



list=[1,2,3,4,5]

def fun(mylist):
    mylist[0] *=10
    
fun(list)
print("Value is ",list)


#=================================Built-In String Functions==========================


my="Welcome to developer team"
print(my.find("to"))
print(my.replace("W","w"))
print(my.upper())
print(my.lower())
print('>'.join(my))
print(','.join(my))


string="Python is a high {} language"
print(string.format(234))

string="Python is a high {} language {}"
print(string.format("level"))
