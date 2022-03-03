#====================================================#
#       Insert String,Integer,Float using Slicing
#====================================================#

Muzammil="I am a Future %s"
Prod="Developer"
print(Muzammil % Prod)
print (Muzammil + Prod)

# output=I am a Future Developer


Muzammil="I am a %s Developer"
Prod="Future"
print(Muzammil % Prod)

# output=I am a Future Developer

Muzammil="I %s a Future %s"
Prod=("am","Developer")
print(Muzammil % Prod)

# output=I am a Future Developer



#====================================================#

'''Insert Integer into String'''

Muzammil="I am a Future Developer for the Year of %i"
Prod=2022
print(Muzammil % Prod)

#output = I am a Future Developer for the Year of 2022

Muzammil="%i + %i=%i"
Prod=(4,5,7)
print(Muzammil % Prod)

# output =4 + 5=7


'''Insert float into String'''

Muzammil="This is a float %f"
Prod=2.022
print(Muzammil % Prod)


# output =This is a float 2.022000
