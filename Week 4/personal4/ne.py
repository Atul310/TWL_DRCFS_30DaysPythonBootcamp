## Asking  for name and house and printing 

def main():
    student = get_student()   ## returnun tuple
    #name,house = get_student()
    print (f"{student[0]} from {student[1]}") ##
    ## indexing the value fro tupple at 0 index it is 
    ## name xa 
    ## at 1 it is house 

    #print (f"{name} from {house}")
'''
def get_name():
    name = input("Name")
    return name

def get_house():
    return input("house")
'''
def get_student():
    name = input("name")
    house = input("house")
    return (name, house) ## creating  tupple here 

if __name__ =="__main__":  ## 
    main()


