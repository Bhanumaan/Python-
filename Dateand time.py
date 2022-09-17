import datetime

x=datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"))    #String Format time  %A is the string identifier for day
print(x.strftime("%j"))


y=datetime.datetime(2022,9,22,16,12,22)
print(y)
print(y.strftime("%B"))

a=min(5,3,7,3)
b=max(5,3,7,3)
print(a,"and",b)

x=abs(-23.99)
print(x)
y=(-x)
print(y)
c=abs(y)          #have a take a new varibale to use abs function
print(c)

x=pow(a,b)   #3 to the power of 7
print(x)
y=pow(9,9)
print(y)

import math

x=math.sqrt(64)   #square root of 64
print(x)

x=math.ceil(1.01)    #rounds up to the upper integer
y=math.floor(1.49)      #rounds up to the lower integer
print(x,"and",y)

x=(math.pi*9)      #math.pi returns the value of pie
print(x)
c=2
y=pow(c,math.pi)
print(y)






