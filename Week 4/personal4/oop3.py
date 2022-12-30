class Employee:
    def __init__(self,sal,ag) -> None: 
        self.salary= sal
        self.age=ag
    def display(self): ## instance method
     print(self.salary,self.age)
    
## self is the memory location of current object
e1 = Employee(20000,20)
e2 = Employee(30000,24)

#c=e1.age #one way of printing the attribute v=
#print(c)
#print(e1.salary) also can print like this

d =e1.display()
print(d)
print(e2.display())


##class Members ==>> attribute and methods inside class

## to access the attribute we write obj_name.variable_name

##like e1.salary

## to access method outside the class 
##obj_name.method_name()
##e1.display()
#To which object we call a function that object works for 

#that particular function 
