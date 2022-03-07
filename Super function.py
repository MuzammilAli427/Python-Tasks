from typing_extensions import Self


class Prof:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Prof):
  def __init__(self, fname, lname,month):
    super().__init__(fname, lname)
    self.month=month
  def statment():
      print("Welcome",Self.firstname,Self.lastname)

x = Student("Muzammil", "is a developer")
x.printname()
x.statment()