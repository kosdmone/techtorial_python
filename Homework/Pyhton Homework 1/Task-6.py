
print("Please enter first word biger than 3 lenght:")
string1 = input()

print("Please enter second word biger than 3 lenght:")
string2 = input()

three_last_string1 = string1[:1:-1]
print(three_last_string1)
three_first_string2 = string2[:3]
print(three_first_string2)
result = (three_first_string2 == three_last_string1)

print(result)















