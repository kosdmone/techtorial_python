
print("Please enter your balance. (exemple 2.36)")
balance = float(input())

balance_full = int(balance * 100)

quater_value = 25
dime_value = 10
nickel_value = 5
pennie_value = 1

quaters_in = balance_full // quater_value
dime_in = ((balance_full - quaters_in * quater_value) // dime_value)
nickel_in = ((balance_full - (quaters_in * quater_value + dime_in * dime_value)) // nickel_value)
pennie_in = ((balance_full - (quaters_in * quater_value + dime_in * dime_value + nickel_value * nickel_in)) // pennie_value)

print("$", balance, "will make", quaters_in, "quarters,", dime_in, "dime,", nickel_in, "nickels and", pennie_in, "pennies.")
