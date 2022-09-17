
a = 754

# find the multiplication of digits of the number a
# number a will always have the three digit number
# When we find remainder with 10, it will give use
# the last digit of the number
last_digit = a %10
print(last_digit)
a = a // 10
middle_digit = a %10
print(middle_digit)
a = a // 10
first_digit = a %10
print(first_digit)
multiplication = last_digit * middle_digit * first_digit

print("Multiplication result of all digit is", multiplication)


# b = 34
# print(b%10)

# c = 67
# print(c % 10)

# d = 105
# print(d%10)

# e = 1273
# print(e%10)