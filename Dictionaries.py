print('xxx')

thisdict={
    'brand':('ford','audi'),
    'model':'mustang',
    'year' :'1964' ,
    'speed':'190',
    'colour':['red','blue','black']


}
print(thisdict['brand'])
print(thisdict['year'])
print(thisdict.keys())
print(thisdict.values())

print(len(thisdict))    #4keysandvalues
print('\n',type(thisdict))

mydict=thisdict.copy() #copy the whole dictionary
mydict=dict(thisdict)   #same copy

a=('bhanumaan')
print(type(a))

x=thisdict.get('colour')
print(x)
y=thisdict['brand']
print(y)

a=thisdict.keys()
print(a)
thisdict['owner']='raj'
print(a)

thisdict['speed']=220,240
print(thisdict.values())

p=thisdict.items()   #print whole dict
print(p)

for i in p:
    print(i)     #print all one by one

if 'model' in thisdict:
    print('yes','this key exists')
else:
    print('no , the key not found')


thisdict.update({'year':2020})
print(thisdict.items())



thisdict.pop('model')    #removed the item model
print(thisdict)

thisdict.popitem()    #removed the last item i.e owner
print(thisdict)


del thisdict['year']
print(thisdict)

print("\n \n \n ")
for x in thisdict.keys():
    print(x)

for x in thisdict.values():
    print(x)

print("\n \n \n \n")

for x,y in thisdict.items():
    print(x,y)

print("\n \n")
print(mydict)


thisdict.clear()
print(thisdict)


myfamily={
    'child1':{
        'name':'happy',
        'age':'5'
    },
    'child2':{
        'name':'peter',
        'age':'3'

    },
    'child3':{
        'name':'jack',
        'age':'1'

    }
}
print(myfamily.items())
print("\n \n" )
for i in myfamily.items():
    print(i)

print("\n \n ")

x=('key1','key2','key3')
y=0
thisdict=dict.fromkeys(x,y)
print(thisdict)

