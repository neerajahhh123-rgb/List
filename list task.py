fruits=["Apple","Orange","Apple","Banana","Mango"]
print(fruits[1])
print(fruits[3])

print(fruits[2:5])

print(fruits)
print(fruits[-4])

fruits.insert(6,"Cherry")
print(fruits)

fruits.extend(["Banana","Kiwi"])
print(fruits)

fruits.insert(3,"Strawberry")
print(fruits)

fruits.remove("Apple")
print(fruits)

fruits.pop(3)
print(fruits)

del fruits[4]
print(fruits)

print(fruits)
print(fruits.index("Kiwi"))

print(fruits)
print(fruits.count("Apple"))

fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

copy_list=fruits.copy()
print(fruits)

print(len(fruits))
