class Prof:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    
    def fun(self):
        print("Good Mornng " + self.fname)
        print("Good Mornng " + self.lname)
        


class student(Prof):
    pass




s=student("Muzammil","Ali")
s.fun()


p=Prof("Muzammil",22)
print(p.age)
print(p.name)
p.fun()