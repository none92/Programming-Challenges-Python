#!/bin/python3  
print("___________              ________           .__  .__          __") 
print("\__    ___/___           \______ \   ____   |  | |__| _______/  |_ ")
print("  |    | /  _ \   ______  |    |  \ /  _ \  |  | |  |/  ___/\   __\ ")
print("  |    |(  <_> ) /_____/  |    `   (  <_> ) |  |_|  |\___ \  |  |  ")
print("  |____| \____/          /_______  /\____/  |____/__/____  > |__|  ")
print("                                 \/                      \/        ")
print(" By Mako ") ### My art work
print ("Welcome to your to-do list") #Very small intro
print("\n")
print ("On your current list you have:") #Show the current list

todo = [] # What we need to do today
with open("E:\Workplace\Programming Challenges\Python\Easy\\todo.txt", "r") as f: # Opening todo.txt file
    todo = [line.rstrip('\n') for line in f]


total_item = len(todo) # The number of items in the list
counter=0 # To keep count the position we are in
i=1 #Filling an empty spot

def list (x,y):  # This function will list always list the items we have in order. If there is nothing, we say nothing
    y = len(todo)
    if y == 0: #Checks if theres anything, if not, then it will say none
        print("You have nothing to do today yet")
        print("")
    else:
        while x < y:
            print('(',x+1,')',todo[x])
            x += 1
        else:
            x = 0
            print("")
def adding ():
    new = input("What would you like to add? ")
    todo.append(new)
    list(counter, total_item)
    with open("E:\Workplace\Programming Challenges\Python\Easy\\todo.txt", "w") as f: # Save it to todo.txt
        for s in todo:
            f.write(str(s)+ '\n')

list (counter, total_item) # Start off what we have

while i > 0:    #Options Options
    print("What would you like to do today?")
    print("(1) Add a new item   (2) Check off item   (3) Edit Item   (4)List  (99)Exit")
    print("\n")
    response = input("What number: ")
    if response == "1":
        adding ()
    elif response == "2":
        print("")
        print("Will delete item one day")
        break
    elif response == "3":
        print("")
        print("Will edit item one day")
        
    elif response == "4":
        print("")
        list (counter, total_item)
    elif response == "99":
        print("")
        print("Bye-bye")
        break
    else:
        print("")
        print("Dude, try again")