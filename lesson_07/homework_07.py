# task 1
""" 
Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

print("Task 1:")
multiplication_table(3)

# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

# task 2
""" 
Написати функцію, яка обчислює суму двох чисел.
"""
def sum_of_two_numbers(a, b):
    return a + b
print("\nTask 2:", sum_of_two_numbers(2, 3))

# task 3
"""
Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def average_in_list(list_of_numbers): 
    return sum(list_of_numbers) / len(list_of_numbers)
print("\nTask 3 with list:", average_in_list([1, 2, 3, 4, 5]))

#OR with *args
def average_of_numbers(*args):
    return sum(args) / len(args)
print("Task 3 with args:", average_of_numbers(1, 2, 3, 4, 5))

# task 4
""" 
Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(string):
    return string[::-1]
print("\nTask 4:", reverse_string("Якась строка."))

# task 5
""" 
Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_list_word(list_of_words):
    return max(list_of_words, key=len)
print("\nTask 5 with list:", longest_list_word(["коротке", "найдовше_слово", "дуже_довге"]))

#OR with *args
def longest_word(*args):
    return max(args, key=len)
print("Task 5 with args:", longest_word("коротке", "найдовше_слово", "дуже_довге"))

# task 6
""" 
Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка.
"""
def find_substring(str1, str2):
    return str1.find(str2)

print("\nTask 6:")

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
print("\nTask 7:")

#HW 05_1
# TEST DATA:
car_data = {
    'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
    'Audi': ('black', 2020, 2.0, 'sedan', 55000),
    'BMW': ('white', 2018, 3.0, 'suv', 70000),
    'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
    'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
    'Honda': ('red', 2017, 1.5, 'sedan', 30000),
    'Ford': ('green', 2019, 2.3, 'suv', 40000),
    'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
    'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
    'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
    'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
    'Kia': ('white', 2020, 2.0, 'sedan', 28000),
    'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
    'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
    'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
    'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
    'Jeep': ('green', 2021, 3.0, 'suv', 50000),
    'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
    'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
    'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
    'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
    'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
    'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
    'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
    'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
    'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
    'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
    'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
    'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
    'Acura': ('white', 2017, 2.4, 'suv', 40000),
    'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
    'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
    'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
    'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
    'Ram': ('black', 2019, 5.7, 'pickup', 40000),
    'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
    'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
    'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
    'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}

#BEFORE:
# search_criteria = (2017, 1.6, 36000)

# min_year, min_engine_volume, max_price = search_criteria

# filtered_cars = [
#     (name, data)
#     for name, data in car_data.items()
#     if data[1] >= min_year and data[2] >= min_engine_volume and data[4] <= max_price
# ]
# print(f"Found {len(filtered_cars)} cars matching the criteria.")

# filtered_cars.sort(key = lambda x: x[1][4])

# print("5 cars with the lowest price:")

# for name, data in filtered_cars[:5]:
#     print(f"{name}: color={data[0]}, year={data[1]}, engine_volume={data[2]}, type={data[3]}, price={data[4]}")

#AFTER:
def find_cars(cars_list, criterias, max_results=5):
    min_year, min_engine_volume, max_price = criterias

    filtered_cars = [
        (name, data)
        for name, data in cars_list.items()
        if data[1] >= min_year and data[2] >= min_engine_volume and data[4] <= max_price
    ]
    print(f"Found {len(filtered_cars)} cars matching the criteria.")

    filtered_cars.sort(key=lambda x: x[1][4])

    print(f"{max_results} cars with the lowest price:")
    for name, data in filtered_cars[:max_results]:
        print(f"{name}: color={data[0]}, year={data[1]}, engine_volume={data[2]}, type={data[3]}, price={data[4]}")

search_criteria = (2017, 1.6, 36000)
find_cars(car_data, search_criteria)

# task 8
print("\nTask 8:")

#HW 05_2
# TEST DATA:
people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

my_record = ('Danylo', 'Saikin', 30, 'QA Engineer', 'Kharkiv')

#BEFORE:
# # 1 - Add your new record to the beginning of the given list

# my_record = ('Danylo', 'Saikin', 30, 'QA Engineer', 'Kharkiv')
# people_records.insert(0, my_record)

# # 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result

# print("After swapping indexes 1 and 5:")
# people_records[1], people_records[5] = people_records[5], people_records[1]
# for person in people_records:
#     print(person)

# # 3 - check that all people in modified list with records indexes 6, 10, 13
# #   have age >=30. Print condition check result

# indexes_to_check = [6, 10, 13]
# ages = [people_records[i][2] for i in indexes_to_check]
# all_above_30 = all(age >= 30 for age in ages)
# print(f"\nAll people at indexes {indexes_to_check} have age >= 30: {all_above_30}")

#AFTER:
def process_people_records(peoples_list, add_record):
    # 1 - Add your new record to the beginning of the given list
    peoples_list.insert(0, add_record)

    # 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
    print("After swapping indexes 1 and 5:")
    peoples_list[1], peoples_list[5] = peoples_list[5], peoples_list[1]
    for person in peoples_list:
        print(person)

    # 3 - check that all people in modified list with records indexes 6, 10, 13
    #   have age >=30. Print condition check result
    indexes_to_check = [6, 10, 13]
    ages = [peoples_list[i][2] for i in indexes_to_check]
    all_above_30 = all(age >= 30 for age in ages)
    print(f"\nAll people at indexes {indexes_to_check} have age >= 30: {all_above_30}")

process_people_records(people_records, my_record)

# task 9
print("\nTask 9:")

#HW 06_1
# TEST DATA:
user_input = input("Введіть рядок: ")

#BEFORE:
# input_string = input("Введіть рядок: ")
# unique_chars = set(input_string)
# count_unique_chars = len(unique_chars)
# print(f'Кількість унікальних символів:', count_unique_chars)
# print(f'Символів більше 10 :', count_unique_chars > 10)

#AFTER:
def count_unique_characters(input_string):
    unique_chars = set(input_string)
    count_unique_chars = len(unique_chars)
    print(f'Кількість унікальних символів:', count_unique_chars)
    print(f'Символів більше 10 :', count_unique_chars > 10)

count_unique_characters(user_input)

# task 10
print("\nTask 10:")

#HW 06_1
# TEST DATA:
import random
my_list = random.sample(range(1, 100), 5)

#BEFORE:
# import random
#
# my_list = random.sample(range(1, 100), 5)
# print(f'Мій список: {my_list}')
#
# numbers_sum = sum(number for number in my_list if number % 2 == 0)
# print(f'Сума парних: {numbers_sum}')

#AFTER:
def sum_even_numbers(numbers):
    return sum(number for number in numbers if number % 2 == 0)

numbers_sum = sum_even_numbers(my_list)
print(f'Сума парних: {numbers_sum}')

"""
Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""