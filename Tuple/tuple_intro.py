
fruits = ("strawberry","apple","orange","banana","orange")

print(fruits)
print(type(fruits))

print(fruits.index("apple"))

print(fruits.count("orange"))

print(fruits[2])

# Using for loop

for element in fruits:
    print(element)

# fruits = ("strawberry","apple","orange","banana","orange")
# From this tuple print out first name
# that has odd lenght. If there is no fruits with odd lenght
# print odd lenght couldn't be found

for fruit in fruits:
    if len(fruit)%2!=0:

        break

print("First odd lenght fruit is",fruit)









