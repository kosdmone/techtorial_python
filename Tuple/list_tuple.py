
t = (1,2,3,4,5,6)
t = list(t)
for number in t:
    if number ** 2 < 20:
        t.remove(number)

t = tuple(t)
print(type(t))




















