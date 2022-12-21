## list comprehension is also sourrounded by brackets
#USe to write code in single line 
##   
g=[]
for i in "range":
    g.append(i)
print(g)

## by list comprehension we can do the same task 
# in oneline 

g=[letter for letter in "letter"]
print(g)
'''
square =[] ##  empty list to generate vvalue from the below exxpressin  
for i in range(1,101):
    square.append(i**2) ## it shows square of number between 1 to 100  
    #=================
    #3# .append() 
    ## method  is used to add element to the last of the list as the 
    ## squares of number are generated the values are added to the last autoamatically 
# in this way list is called as mutable 
    #=====================
    print(square) ## it will print in the list called square=[]
'''
### Doing same above task by list comprehension 

square =[i**2 for i in range(1,101)]
print(square)

## list  of remainder when we divde fist 100 squares by 5
remainder=[x**2%5 for x in range(1,101)] 
print(remainder)
print(2/5)

remainder2 = [x**2%5 for  x in range(1,4)]
print(remainder2)

## Qudratic reciporcity 
## p_remainders =[x**2 %5 for x in range (0,p)]
## len(p_remainders)=p+1/2
###======================
movies =["star wrs", "gandhi", "casablance", "shawank","toystory",
"gone with wild ", "citizen ", "the wizaard"]

gmovies=[title for title in movies if title.startswith("g")]
print(gmovies)


###=====>>>

## find out movies which were released before 2000
## Title with g 

movies2 = [("Citizen Kane", 1941), ("Spirited Away", 2001), 
("It's a Wonderful Life", 1946), ("Gattica",1997), 
("No Country for Old Men",2007),  ("Rear Window",1954), 
("The Lord of the Rings: The Fellowship of the Ring", 2001), 
("Groundhog Day", 1993),    ("Close Encounters of the Third Kind", 1977), 
("The Royal Tenenbaums", 2001), ("The Aviator", 2004), ("Raiders of the Lost Ark", 1981)]

pri = [title for (title,year) in movies2 if year<2000]
print(pri)

 ## cartesian product list comprehesion 

A=[1,3,5,7]
B=[2,4,6]
cartesian_product= [ (a,b)for a  in  A for b in B]
print(cartesian_product)
