
# 1:
#===
# class num:
#     x=10

# obj=num

# print(obj.x)


# 2:
#===

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def fun(self):
        print("Good Mornng " + self.name)



p=student("Muzammil",22)
print(p.age)
print(p.name)
p.fun()