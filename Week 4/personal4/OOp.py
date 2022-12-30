## class ==>> 
#3 everything in python is object 
##object =>> object are instance of class 
##class and object are synonomous to some extend 
a = "str" ## interpreter convert everthing in object
 ## python is alsoo compiled language also 
 ## ww have _pycache_file  in a .py file  :: ==>> which have .cpython #
'''==>>> 
the .cpython  is also the byte code 
the code dosent run directly it get converted into bytecode which is .cpython 
## and then it runs 
## ##before converting to .cpython code get converted into abstract syntax tree
## and then it converted into .cpython and then it get compiled 
and run 
and surface level it is interpreted but deep down we got it is both interepreted and compiled
'''
## we can create our own data type in oop 

class MyClass: ## class keywored ## Myclass class
 def __init__(self) -> None:                          ## self is constructor
      pass
var =int("1")   
print(type(var)) 



## use of init function==>> method is  __init__

## in class we can write once  and reuse 
## encapsulate all other function and use it at once
## one class is used  for one task
## function can to a specific taskk

'''
  Class has  attribute and methods 
  when a variable created inside the class then it is called 
  attribute 


  ## when a class is called it is initializer or inatilized 



'''


class animal:
  name = "maxThepuppy"
  age = 3

print(animal.name) #3 class is  being inatalized and attribute is being called

## the above is same as we are doing in local variable 


class Animal :
  name = "Ok"
  age =6
  def __init__(self) -> None:
     pass

 ##object is are of class .
 ##class is the blueprint 
 #  


l = [2,5,4]
print(l)
so = l.reverse()


print(so)
