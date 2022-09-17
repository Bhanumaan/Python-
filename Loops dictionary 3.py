a=33
b=33
if a>b:
    print('a is greater then b ')
elif a==b:
    print('a and b are equal')
else:
    print('b is greater than a  \n')

x=3
y=11
print('X and Y are equal') if x==y  else print('x and y are unequal')

print('x') if x>y else print('=') if x==y else print('y')

if x>2 and y<7: print('X and Y are fine')

if x>9 or y<9:
    print('acceptable')
else:
    print('unacceptable')

if y<x:
    pass
    print('hello')

i=1
while i<9 :
    print('\n ',i)
    if i==3 :
        break
    i+=1

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx \n")

i=0
while i<6:
    i+=1
    if(i==3):
       continue
    print(i)

def fuction():
    print('hello from a function')
    print('xxxxxxxxxxxx')

fuction()

def function2(fname,gname):
    print(fname+'refnes',gname)   #if put "," space will come if put "+" space won't come

function2('happy','asdf')
function2('12313','abc')
function2('./,;;','defg')

def family(*kids):                 #*will shore the data in list format
    print('The name of the youngest child is',kids[0])

family('jack','ross','joey')


def newfamily(child3,child2,child1):
    print('\n name of the childred r as follows',child1,child2,child3)

newfamily(child1="emma",child2="ross",child3="jack")

def afamily(**kid):
    print('his last name is ',kid['lname'])
    print('and his first name is ',kid['fname'])

afamily(lname='potter',fname='harry',age='15')


