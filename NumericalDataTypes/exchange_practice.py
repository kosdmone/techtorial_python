
# Create a python program to give
# most efficient exchange possible using only
# coins
# quaters 25 cent
# nickel 5 cents
# dime 10 cents
# penny 1 cent
# you have to give 2 dollars 34 centts for exchenge
# 9 quaters
# 0 dimes
# 1 nickels
# pennies

# $1.89 
# 7 quaters
# 1 dimes
# 0 nickels

amount = 4.35



quaters = amount /.25
amount = amount // 10
dimes = amount %10
amount = amount // 10
nickels = amount %10


print("We need to give:" ,quaters , "quaters")

dollar = 2.36
dollar_amount = dollar * 100

quater_value = 25
dime_value = 10
nickel_value = 5
penny = 1

count_of_q = dollar_amount // quater_value
print("We need to give back" ,count_of_q, "quaters")

remaining_exchenge_after_q = dollar_amount % quater_value

count_of_d = remaining_exchenge_after_q // dime_value
print("We need to give back" ,count_of_d, "dimes")
remaining_exchenge_after_d = remaining_exchenge_after_q % dime_value
# print("We need to give back" ,count_of_pennies, "pennies")
count_of_nickel = remaining_exchenge_after_d // nickel_value
remaining_after_nickel = remaining_exchenge_after_d % nickel_value
print("We need to give back" ,count_of_nickel, "nickels")
count_of_pennies = remaining_after_nickel // penny

print("")





# Create a python program to give 
# most efficient exchange possible using only 
# coins 
# quarter 25 cent
# nickel 5 cents
# dime is 10 cents
# penny 1 cent
# $2.34 exchange
# 9 quarters 
# 0 dimes 
# 1 nickel 
# 4 pennies
# $1.89
# 7 quarters 1 dimes and 0 nickels 4 pennies
dollar = 2.96
print(type(dollar))
dollar_amount = dollar * 100
print(type(dollar_amount))
quarter_value = 25
dime_value = 10
nickel_value = 5
penny = 1
            
# count_of_q = dollar_amount // quarter_value 

# print("We need to give back",count_of_q, "quarters") 
                          
# remaining_exchange_after_q = dollar_amount % quarter_value

# count_of_d = remaining_exchange_after_q // dime_value
# print(count_of_d , "dimes")
# remaining_exchange_after_d = remaining_exchange_after_q % dime_value
# count_of_nickel = remaining_exchange_after_d // nickel_value
# print(count_of_nickel, "nickels")
# remaining_after_nickel = remaining_exchange_after_d % nickel_value

# count_of_pennies = remaining_after_nickel // penny

# print(count_of_pennies,"pennies")














