cars=['toyota','hyundai','tata']


x=cars[0]
print(x)

print(len(cars))

for x in cars:
    print(x)

cars.append('honda')

print(cars[3])

print("\n xxxxxx \n")

cars.pop(1)

for x in cars:
    print(x)

cars.remove('honda')

for x in cars:
    print("\n",x)

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxx \n ")


cars.append('honda')
cars.append('maruti')
cars.append('suzuki')



for x in cars:
    print("\n",x)

newlist=cars.sort(reverse=True)
print("...................")
print(newlist)
