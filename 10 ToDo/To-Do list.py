#!/bin/python3  
import os.path
from os import path
print(" ___________              ________           .__  .__          __") 
print(" \__    ___/___           \______ \   ____   |  | |__| _______/  |_ ")
print("   |    | /  _ \   ______  |    |  \ /  _ \  |  | |  |/  ___/\   __\ ")
print("   |    |(  <_> ) /_____/  |    `   (  <_> ) |  |_|  |\___ \  |  |  ")
print("   |____| \____/          /_______  /\____/  |____/__/____  > |__|  ")
print("                                  \/                      \/        ")
print(" By none92 ") ### My art work
print ("Welcome to your to-do list") #Very small intro
print("\n")
print ("On your current list you have:") #Show the current list
counter=0 # To keep count the position we are in
i=1 #Filling an empty spot
if path.exists("todo.txt") == False: #Check if the text file exist or not
    while i > 0 :
        response = input("todo.txt does not exist, would you like to create a new todo.txt file?: ")
        if response == "y":
            f = open("todo.txt","w+")
            print ("Created a new file")
            break
        elif response == "n":
            print ("Can't run, peace out")
            exit()
        else:
            print("Don't know this answer")           
else:
    pass
todo = [] # What we need to do today
with open("todo.txt", "r") as f: # Opening todo.txt file
    todo = [line.rstrip('\n') for line in f]


total_item = len(todo) # The number of items in the list

def list (x,y):  # This function will list always list the items we have in order. If there is nothing, we say nothing
    y = len(todo)
    if y == 0: #Checks if theres anything, if not, then it will say none
        print("You have nothing to do today")
        print("")
    else:
        while x < y:
            print('(',x+1,')',todo[x])
            x += 1
        else:
            x = 0
            print("")
def adding (): #Adding new item to the list, writing then asking again
    new = "yike"
    while i>0 :
        new = input("What would you like to add or 99 back to menu: ")
        if new == "99":
            print("Back to Menu")
            break
        else:
            todo.append(new)
            list(counter, total_item)
            with open("todo.txt", "w") as f: # Save it to todo.txt
                for s in todo:
                    f.write(str(s)+ '\n')
def delete ():
    num = "yike"
    while i>0 :
        list(counter, total_item)
        num = input("What would item number would you like to check off? or 99 to exit back to the menu: ")
        num = int(num)
        if num == 99:
            print("Back to Menu")
            break
        else:
            if num > total_item:
                print("no such number")
            else:
                del todo[num-1]
                print("Item removed")
                with open("todo.txt", "w") as f: # Save it to todo.txt
                    for s in todo:
                        f.write(str(s)+ '\n')
def edit():
    num = "yike"
    while i>0:
        list(counter, total_item)
        num = input("What would item number would you like to edit? or 99 to exit back to the menu: ")
        num = int(num)
        if num == 99:
            print("Back to Menu")
            break
        else:
            while i > 0:
                if num > total_item:
                    print("no such number")
                else: 
                    print('(',num,')',todo[num-1])
                    ans="n"
                    while ans == "n":
                        answer=input("What would you like to change it to? or 99 to go back: ")
                        if answer == "99":
                            break
                        else:
                            ans=input("Are you sure you want to make this change? ")  
                    if answer == "99":
                        break
                    else:
                        while i>0:         
                            if ans == "y":
                                break
                            else:
                                print("Try again")
                        print( todo[num-1]," changed to ", answer)
                        del todo[num-1]
                        todo.insert(num-1,answer)
                        with open("todo.txt", "w") as f: # Save it to todo.txt
                            for s in todo:
                                f.write(str(s)+ '\n')
                        break
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
        delete()

    elif response == "3":
        print("")
        edit()
        
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