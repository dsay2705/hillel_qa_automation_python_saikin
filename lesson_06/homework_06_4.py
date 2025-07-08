# Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
import random

my_list = random.sample(range(1, 100), 5)
print(f'Мій список: {my_list}')

numbers_sum = sum(number for number in my_list if number % 2 == 0)
print(f'Сума парних: {numbers_sum}')
