
five_d_n = 54321

digit_n_5 = five_d_n % 10
four_d_n = five_d_n // 10
digit_n_4 = four_d_n % 10
third_d_n = four_d_n // 10
digit_n_3 = third_d_n %10
second_d_n = third_d_n // 10
digit_n_2 = second_d_n % 10
first_d_n = second_d_n // 10
digit_n_1 = first_d_n % 10

print(digit_n_5,digit_n_4,digit_n_3,digit_n_2,digit_n_1)