

# User want to deposit his money in to his bank account
# He already has $200 in his account
# He has three different paychecks (400, 600, and 350)
# He can only deposit one paycheck at the time
# After he deposit all the money in the account
# He bough a phone for 599, and headphones for $299
# Create a python progam to calculate his final money in the account.
# Use input function to get all the values.

bank_acct = 200

print("Please enter the first paycheck amount you want to deposit") # This is the same as doing bank_acct = first_deposit + bank_acct
first_deposit = int(input())
bank_acct += first_deposit

print("Please enter the second paycheck amount you want to deposit")
second_deposit = int(input())
bank_acct += second_deposit

print("Please enter the thurd paycheck amount you want to deposit")
thurd_deposit = int(input())
bank_acct += thurd_deposit

print("Please enter the headphones amount you want to buy")
headphones = int(input())
bank_acct -= headphones

print("Please enter the phone amount you want to buy")
phone = int(input())
bank_acct -= phone

print("His final money in the bank is", bank_acct)

























