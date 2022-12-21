## Generators ==>> Generators are simple way of creating 
##iterators

## A Python generator is very similar to a regular Python function, but we end it with 
# yield instead of the return keyword

#3 simple way of iteratinng 

## 
def demo_gen():
    yield "this is 1st st"
    yield "this is 2d"
    yield "this is 3rd"
gen = demo_gen()
print(gen)  #3 this show generator object demmo

## different between yield and return 
for  i in gen:
    print(i)
 
## Generator are special function which works on previous 
## work done
## generator rembembers what it has done before 
## while a normal function do work and go out of memory in 
## generator it do work and go out of memory but rembember s
#what it has done before 
## normal function does not do that 
def Square(num): ## a function
    for i in range(num): 
        yield i**2
for i in Square(10): ## we have passed 10 so start from 0 and end at 9
    print(i) ## this print the square of numbers from 0 to 9
        


