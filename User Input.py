



# username=input("exter the name")
# print("username is ", username)

count=536
itemno=3
rate=59
txt=("the price of the goods is {}")
print(txt.format(rate))

#in the curly brackets we can specify how to convert value
trt=("the revised price is {0:.2f} for item number {2:.1f} for {1:.2f} number of  goods,which is a very less price for {1} things")
#print(trt.format(rate))
print(trt.format(rate,count,itemno))

#in curly brackets before ":" we give postion and after ":" converison

txt=("I have a {carname}, it is a {year} model ")
print(txt.format(year=1972,carname="Mustang"))

