# Every math operation between float amd int data type
# will result in float data type

floatNum = 3.0
intNum = 5

print("Type of floatNum is", type(floatNum))
print("Type of intNum is", type(intNum))

addittion = floatNum + intNum
print("Addittion of float int is" ,type(addittion))

subtraction = intNum - floatNum
print("Subtraction bgetween float int is" ,type(subtraction))

multiplication = floatNum * intNum
print("Multiplication bgetween float int is" ,type(multiplication))

division = intNum / floatNum
print("Devision between float and int data type is" ,type(division))

remainder = floatNum % intNum
print("The remainder between float and int data type is" ,type(remainder))

remainder2 = intNum % floatNum
print("The remainder between float and int data type is" ,type(remainder2))

int_division = floatNum // intNum
print("int_devision" ,type(int_division))