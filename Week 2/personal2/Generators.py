## Generators ==>> Functions that  acts like iterators 
## Generateors generate the element in a loop
## on demand iteration 
def f():
    return 1
    return 2
    return 3
#print(f)
#print(f())

import sys
## ==>> 
## Generators are elegant way for creating a custom iterator 
##


# iterators 
# ###=========
# What is iteration?
# ==>> it is a general term for for taking each item of something
# one after another. Any time we use a loo[p
# explicit or implicit go over a group of items that is 
# itertion .
#   
# 
#  

# Example 
##==>> in loops we take out the item in a data and perform
# some operation 
# ..
'''
num= [1,3,3]
for i in num:
    print(i)
'''
    # here in above example we have list of items and 
    # we are looping each item over that and printing 
    # that item


## iterator ==>> object that allows a programmer 
##to traverse through sequence of data withoout having to
# store the entire data in memory

## when we use loop and iterator objct is createdd
##all data are not loaded at once 
## it loads one by one in memory which saves memory

## Example of numbers to be multipled by 2 
#from 1 to 1 lakhs
x = range(1,1000000)
print("size = ",sys.getsizeof(x))

## iterable 
## It is an object which we can iterate  over(or loop over)
## ITeranle generate when passed to iter method
L = [2,3,5]
print(type(iter(L)))

## points to remeber 
#Every iterator is also a iterable 
##2) Not all iterable are iterators 


## to check iterable or nor 
a =1,2,3 ## integer is not iterable 
for i in a:
    print(i)
print(dir(a)) ## it gives __iter__ while printing then it is iterable

## it is iterable 
aa = "ahady"
for i in aa:
    print(aa) 
print(dir(aa))
# if there is __iter__ and __next__ while printing

#  making own for loop
def looP_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except:
            StopIteration
            break
a = "aady"
b = [1,2,4]
c = {1,3,4,5}
looP_for(a)
looP_for(b)

