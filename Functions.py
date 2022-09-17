def myfunction(country='norway'):
    print("\n I am from",country)     #norway will be the default value

myfunction('sweden')
myfunction('india')
myfunction()
myfunction('japan')

def newfunction(food):
    for x in food:
        print(x)

fruits=('apple','banana','cherry')

newfunction(fruits)

def afunction(x):
    return 5*x

print(afunction(6))
print(afunction(0))
print(afunction(8))

def fun(play):
    pass

fun('happy')

x=lambda a: a-5
print(x(6))

y=lambda a,b,c:a*b*c
print(y(2,2,9))

def myfunc(x):
    return lambda a:a*x

print(myfunc(8))    #adress of the pbject will be printed

bfunc=myfunc(8) #this func will multiply anynumber with 8
cfunc=myfunc(10) #this func will multiply anynumber with 10

print(bfunc(9))
g=bfunc(65)
print(g)
print(cfunc(999))






