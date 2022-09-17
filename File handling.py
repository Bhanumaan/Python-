

f=open("new.txt")
print(f.read(),"  \n \n xxxxxxx \n ")

f=open("new.txt",'rt')
print(f.read() ,"\n\n\n")

f=open("new2.txt",'w')
f.write("Hello there ")
f=open("new2.txt",'r')
print(f.read())

f=open("new.txt")
print(f.read(7))        #Return the first 7 characters from the file
print(f.readline())              #willl read line by line

print("\n \n \n")
f=open("new.txt")
print(f.readline())
print(f.readline())
print(f.readline())

print("xxxxxxxxxxxxxxxxxxxx","\n \n ")
f=open("new.txt",'r')                   #Have to open the file again to start from begining
for x in f:
    print(x)
f.close()


f=open("new.txt",'a')
 # f.write("   This line has been added on monday ")   #Everytime we run the program it will add the line
f=open("new.txt",'r')
print(f.read())

print(" \n \n \n \n xxxxxxxxxxxxxxxxxxxxx \n \n \n ")

import os

os.remove("new2.txt")

if os.path.exists("new2.txt"):
    os.remove("ewn2.txt")
else:
    print("The file does not exist")


os.rmdir("new folder")      #will delete the specified folder