class myclass:
    x=5

p1=myclass()
print(p1.x)


class person:
    def __init__(shelf,name,age,nationality):
        shelf.name=name
        shelf.age=age
        shelf.nationality=nationality

    def myfunc(pnp):
        print("The name is ",pnp.name,"age is ",pnp.age,"nationality",pnp.nationality)


p1=person('rahul',23,'indian')
p2=person('raj',22,'indian')

print(p1.name)
print(p1.age)
print(p1.nationality)


p2.myfunc()

p1.age=40
print(p1.age,p1.name)   #both are of diffrent data types so we can not use +

del p1.age
print(p1.name,p2.age)

del p1

print(p2.age)

class newone(person):             #example of inheritance
    pass

class student(person):
    def __init__(self,name,age,town):   #if we put init then the inheritance will cancell
        self.name=name
        self.age=age
        self.town=town



print("xxxxxxxxxxxxxxxxxxxxxx  \n")

x=student('amit',20,'indian')

print(x.name)
print(x.age)
print(x.town)

print("xxxxxxx  \n")
y=newone('ajay',25,'japan')
y.myfunc()





