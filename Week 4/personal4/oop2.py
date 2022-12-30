a = 2
print(type(a)) ## result <class 'int'> here a is the object
##of class Integer 

## Class has two 

## function vs method 
## method are function written inside class
##function are outside the class 
## and normal function are called by fucntion_name() 
##method are called by using object 
"""
class Employee:
    def __init__(self) -> None:
        self.salary= 2000
        self.age=20

## __init__()  is called  autonmatically    
#When object are created
 # IT intaialized thhe above varialble for each object
 # salary and age are inatilaized for each method      
## here this value are hard coded 
 ## When object are created the above salary value 
 ## and age value are same for all object

e1=Employee()
e2 =Employee()
#print(e1.__dict__)
print(e2.__dict__)

"""
## We can dynamically set the attribute  
class Employee:
    def __init__(self,sal,ag) -> None: 
        self.salary= sal
        self.age=ag
## self is the memory location of current object
e1 = Employee(20000,20)
e2 = Employee(30000,24)

#c=e1.age #one way of printing the attribute v=
#print(c)
#print(e1.salary) also can print like this




''' 
   sal and ag in above are parameter 

   ## salary and age are the attribute or variable 

##=================
self.salary means memory address of particular object
## for e1
# self gives the memory location of e1

memory location of e1.salary(20000,20)
## self helps to reconinze the particular object memory 
##address so we can provide parameter and value and access 
##them in correct order


##(.) notation helps to access the particular object

#when we create objects for a class 
#copy of varible methods are made for each objects
##above has 2 objects 
## here salary and age also given to e1 in heap memory 
##and also to the salary and age is given to e2
        

'''



