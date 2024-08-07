lisit = []
def reading(lisit):
    file = open("customers.txt","r")
    lisit = file.readlines()
    for i in range(len(lisit)):
        lisit[i] = lisit[i].split(", ")
        lisit[i][2] = int(lisit[i][2][:-1])
    file.close()        
    return lisit

def check(id:str):
    for i in lisit:
        if i[0] == id:
            return False
    return True
def add(id,name,balance):
    file = open("customers.txt",'a')
    file.writelines([f"{id}, {name}, {str(balance)}"])
    file.close()
def credit(id,amount):
    file = open("customers.txt","w")
    
    for i in range(len(lisit)):
        if lisit[i][0] == id:
            lisit[i][2] = str(int(lisit[i][2]) + amount)
    print(lisit)        
    for i in lisit:
        file.write(f"{id}, {name}, {balance}\n")    
    file.close()
def transfer(id1,id2,amount):
    file = open("customers.txt","w")
    
    for i in range(len(lisit)):
        if lisit[i][0] == id1:
            lisit[i][2] = str(int(lisit[i][2]) - amount)
        if lisit[i][0] == id2:
            lisit[i][2] = str(int(lisit[i][2]) + amount)    
    print(lisit)        
    for i in lisit:
        file.write(f"{i[0]}, {i[1]}, {i[2]}\n")    
    file.close()   
