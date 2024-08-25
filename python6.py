"""
#
# part Python Function
#
"""
def myFunction():
    i = 1
    while i <= 3 :
        print("Hello World" ,i)
        i+=1

myFunction()
myFunction()

def myName(name):
    print("My name is " +name)
myName("Anya")
myName("Loid")

def myFullname(first_name ="Unknown",last_name = "Forger"):
    print("my name is " + first_name + "  "+ last_name)
myFullname("Anya")
myFullname("Bond" , "Forger")
myFullname("Yor" ,"Forger")
myFullname(last_name = "Forger",first_name="Loid")

def myFruit(fruit):
    for fruit in fruits:
        print(fruit)
fruits = ["Apple","Banana","Coconut"]
myFruit(fruits)

def redPotion(hp):
    return hp +50
print("Hp: ", redPotion(100))
print("Hp: ", redPotion(30))