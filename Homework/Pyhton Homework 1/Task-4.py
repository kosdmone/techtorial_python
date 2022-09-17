
number = 53876

digit_5 = number % 10
number = number // 10
digit_4 = number % 10
number = number // 10
digit_3 = number % 10
number = number // 10
digit_2 = number % 10
number = number // 10
digit_1 = number % 10

print(digit_5,digit_4,digit_3,digit_2,digit_1)

print("Please enter 5 digit number")
numbers = input()

print(numbers[::-1])
