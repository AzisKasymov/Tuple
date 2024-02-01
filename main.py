myfamily = ("mother", "father", "sister", "brother", "sister") 

print(type(myfamily))#First 

print(myfamily[2])#second

y = ("me",)
myfamily += y
print(myfamily)#third

y = list(myfamily)
y.remove("brother")
myfamily = tuple(y)
print(myfamily)#fourth
