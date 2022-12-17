a = [2,"shady",4,12.5]
print (a[1])
a[1]= "slim"
print(a[1])
print (a[1])
#Appending in python helps to add new element in list 
 # at  the last of the list 
a.append("hello") 
# list.append() only take one argument at a time
# but  we can add like this 
# a.append([12,23eoe,"go"])

print (a)

a.append([12,"no",[]])
print(a)
 ## Pop method in python ==>> helps to take the data 
a.pop(0) # pop out from specific 
print(a)

#3 swap the first and last value in list 
z = ["facebok","google","microsoft"]
# swap the first and last vaalue from the list 
temp =z[0]
z[0]=z[2]
z[2]=temp
print(z)



