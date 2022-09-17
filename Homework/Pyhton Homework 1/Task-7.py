

print("Please input number of minutes that need to be converted in years and days:")
minutes = int(input())

day = 60 * 24
year = day * 365

years_in = minutes // year
days_in = (minutes - (years_in * year)) / day

print(minutes, "minutes is approximately", years_in ,"years and", days_in ,"days.")
