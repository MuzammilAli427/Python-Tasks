try:
    prin()
except:
    print("Try not worked fine")


try:
  print(a)
except NameError:
  print("Variable a is not defined")
except:
  print("Something else went wrong")


x = 0
if x < 1:
  raise Exception("Sorry, no numbers below zero")


x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")