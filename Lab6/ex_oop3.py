"""
Name: {}
ID: {}
Group: {}
"""

class Teacher:
    def __init__(self,name):
        self.name = name
    def introduce(self):
        print(f'My name is {self.name}, I am Teacher.')

class Student:
    def __init__(self,name):
        self.name = name
    def introduce(self):
        print(f'My name is {self.name}, I am Student.')

mylist = []
t = Teacher('Puriwat Lertkrai')
s = Student('orrasa jomchana')

mylist.append(t)
mylist.append(s)

#print(len(mylist))

for x in mylist:
    x.introduce()