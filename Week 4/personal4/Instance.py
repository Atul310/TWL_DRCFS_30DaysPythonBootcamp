## instance variable and methods 


class Student:
    def __init__(self,nm ,ag):
     self.name= nm   ## instanc variable are name and age
     self.age =ag
     
s1= Student('at',21)
s2 = Student('s',47)


# creation of  instance variable outside the class ==>>

s1.contact=984100000
print(s1.__dict__)
print(s2.__dict__)

'''
##output
{'name': 'at', 'age': 21, 'contact': 984100000}
{'name': 's', 'age': 47}
'''