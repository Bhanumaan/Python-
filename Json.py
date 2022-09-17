print("hi")

import json

x='{"name":"John","age":30,"city":"New york"}'  #some JSON

y=json.loads(x)          #parse x   - parse means process
print(y["city"])           #The result is now a python dictionary and can be accesed easily


a={
    "Name":"Rahul",
    "Age":23,
    "State":"Delhi"
}

b=json.dumps(a)  #dictionary converted into a JSON

print(b)

print(json.dumps({"name":"Raj","Age":23}))        #Dictionary Converted
print(json.dumps(["rohan",23,"malhotra"]))        #List converted
print(json.dumps(("apple","Banana",'cherry ')))   #Tuple converted
print(json.dumps("Hello"))                        #String converted
print(json.dumps(31.76))                          #float converted
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

print("xxxxxxxxxxxxxxxx \n \n ")
b={
    "name":"AJay",
    "Age":24,
    "Married":False,
    "Unmarried":True,
    "Friends":("Maninder","Parmar"),
    "Pets":None,
    "Cars":[
        {"Model":"Swift","MPG":24},
        {"Model":"Brezza","MPG":21}
    ]



}

print(json.dumps(b))

print("\n \n ")
print(json.dumps(b,indent=10))  #one intend means 4 spaces

print(json.dumps(b,indent=3,separators=(".","=")))  #':'will be replaced with '=' and ',' will be replaced with '.'

print(" \n \n \n xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \n ")
print(json.dumps(b,indent=4,separators=('-','='),sort_keys=True))  #sort_keys arrange data alphabetically
