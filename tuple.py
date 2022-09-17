thistuple=('apple','banana','orange')
y=list(thistuple)
y.remove('orange')
thistuple=tuple(y)

print(thistuple)

del thistuple  #delete the tuple


catt=('apple','banana','grapes')

for i in catt:                                #loop to empty tuple
    catt=list(catt)
    catt.remove(i)
    catt=tuple(catt)

    print(catt)


r=('apple','banana','grapes')
print(r)
t=list(r)
t.append('pineapple')
r=tuple(t)

print(r)

p=list(r)
print(p)

p.remove('banana')
r=tuple(p)

print(r)

for i in r:
    r=list(r)
    r.remove(i)
    r=tuple(r)

print(r)
del r




thistuple=('apple','banana','cheery')
(green,red,blue) = thistuple
print(green)
print(red)
print(blue)

print("this is an example for complex tuple unpacking ")

newtuple=('apple','banana','cherry','orange','raspberry')
(yellow,black,*white)=newtuple    #'*'is important to add with the last variable to make it asterisk
print(yellow)
print(black)
print(white)   #this will print as a list

print("                               ")


for i in newtuple:
    print(i)
print(" \n using range in for loop  now ")
for i in range(len(newtuple)):
    print(newtuple[i])

print(" \n now using while loop ")
i=0
while i<len(newtuple):
    print(i+1)
    print(newtuple[i])
    i=i+1
print("\n")
tuple1=('a','b','c')
tuple2=(1,2,3)
tuple3=tuple1+tuple2
print(tuple3,'\n')

fruits=('apple','banana','cheery')
mytuple=fruits*2
print(mytuple,"\n")

print(fruits.count('apple'))
x=mytuple.count('cheery')
print(x)

print('xxxxxxxxxxxxxx \n')

mytuple=('apple','banana','cheery','apple','banana','cheery')

print(fruits.index('apple'),"\n")

print(mytuple.index('banana'),"\n")

print('xxxxxxxxxx')









