var=[1,2,3,4]
var2=['a','b','c','d']
print(var)
print(var[1])  #index value

print(var[-2])    #-1 will be the last

fruits=['apple','banana','cherry']
fruits.append('orange')  #append means add to last position
print(fruits)

thistuple=('apple','banana','cheery','2566')
print(thistuple)

print(len(thistuple))
print(len(fruits))
print(thistuple[1])
print(thistuple[0])
print(thistuple[-3])

thistuple=('apple','banana','cherry','kiwi','melon','orange','mango')
print(thistuple[2:5])  #5 will be excluded

print(len(thistuple))
print(thistuple[-4:-1]) #-1 will be excluded

print('0')
print(thistuple[-4:2])

if "apple" in thistuple:
    print("yes 'apple'  is in thistuple")
    print("eqweqew")

x=('apple','banana','cherry')
y=list(x)
y[1]='kiwi'
x=tuple(y)

print(x)

varr=('apple','banana','cheery')
y=list(varr)
y.append('orange')  #append means add to end
varr=tuple(y)
print(varr)

c=('grapes',)   #there is only one string constant so we have to give a comma at last to make it a tuple
varr += c
print(varr)















