#======================Conditional statment===================#

#if 
#if-else 
#if-elif-else 


from msvcrt import putch


oracle=35
mysql=25

if oracle > mysql:
    print("Oracle is the World Largest Database")

if oracle == mysql:
    print("Oracle is the World Largest Database")

if oracle is mysql:
    print("Oracle is the World Largest Database")

if oracle is not mysql:
    print("Oracle is the World Largest Database")


if oracle >= mysql:
    print("Oracle is the World Largest Database")


if oracle <= mysql:
    print("Oracle is the World Largest Database")

if oracle < mysql:
    print("Oracle is the World Largest Database")


#=================================================#

odoo=10
dgango=15
if odoo > dgango:
    print("Hi, Welcome to onboard")
else:
    print("Sorry")


#=================================================#
#                 Even & odd number
#=================================================#
odoo=3

if (odoo % 2==0):
    print("Hi, You enter a even number")
else:
    print("Hi, You enter a odd number")





odoo=90
if (odoo <= 90 and odoo >= 80):
    print("Your children is pass with A+")
elif(odoo >=70 and odoo <= 80):
    print("pass with B+")
elif(odoo >=40 and odoo <= 60):
    print("satisfactory")


'''Nested if'''

# python=input("Enter the values")
# python=int(python)
# if(python > 70 or python < 99 ):
#     if(python >50 or python <70):       
#         print("Pyhton is an interpreter language")



list=["Python","java","C++","cSharp"]
if 'Python' in list:
    print("Character is avaliable in list")
else:
    print ("Can't see this in list")




a=[1,2,3,4,5,6,7,8,9]
for i in a:
    if 1==1 :
        print("Yes is it avaliable")
    else:
        print("Not avaliable")



w=input("Enter the color = ")

if w=="green":
    print("GO")
elif w=="red":
    print("Stop")
elif w=="yellow":
    print("Wait")


