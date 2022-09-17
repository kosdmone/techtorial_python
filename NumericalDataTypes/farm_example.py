# In the farm we have 35 cow, 23 chikens and 40 ducks
#Create a program to calculate total legs in the farm

from itertools import count
from unittest import result


cow = 4
chick = 2
duck = 2

print("We have, cow*35 + chick * 23 + duck * 40 legs in the farm ")
print(cow*35 + chick*23 + duck * 40)

result = cow*35 + chick*23 + duck * 40
print("We have", result ,"legs in the farm")

count_of_cows = 35
count_of_chickens = 23
count_of_ducks = 40
legs_of_a_cow = 4
legs_of_a_birds = 2
total_number_of_legs = count_of_cows*legs_of_a_cow + count_of_chickens*legs_of_a_birds + count_of_ducks*legs_of_a_birds

print("We have", total_number_of_legs ,"legs in the farm")