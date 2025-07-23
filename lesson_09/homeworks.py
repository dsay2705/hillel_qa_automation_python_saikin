"""
Homework_09
Оберіть від 3 до 5 різних домашніх завдань
перетворюєте їх у функції (якщо це потрібно)
створіть в папці файл homeworks.py куди вставте ваші функції з дз
та покрийте їх не менш ніж 10 тестами (це загальна к-сть на все ДЗ).
імпорт та самі тести помістіть в окремому файлі - test_homeworks08.py
На оцінку впливає як якість тестів так і розмір тестового покриття.
Мінімум на 10 балів - 1 правильно задизайнений позитивний тест на функцію.
"""

"""
Homework_08_1:
Створіть масив зі строками, які будуть складатися з чисел, які розділені комою. Наприклад:
[”1,2,3,4”, ”1,2,3,4,50” ”qwerty1,2,3”]
Для кожного елементу списку виведіть суму всіх чисел (створіть нову функцію для цього).
Якщо є символи, що не є числами (”qwerty1,2,3” у прикладі),
вам потрібно зловити вийняток і вивести “Не можу це зробити!”
Використовуйте блок try\\except, щоб уникнути інших символів, окрім чисел у списку.
Для цього прикладу правильний вивід буде - 10, 60, “Не можу це зробити”
"""

test_data = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

def sum_string_numbers(string_of_numbers):
    try:
        numbers = [int(n) for n in string_of_numbers.split(',')]
        return sum(numbers)
    except ValueError:
        return "Не можу це зробити"

# def sum_list_numbers(list_of_strings):
#     for string in list_of_strings:
#         print(sum_string_numbers(string))
#
# sum_list_numbers(test_data)


""" 
Homework_07_1 task 6:
Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка.
"""
def find_substring(str1, str2):
    return str1.find(str2)

#print("\nTask 6:")

str1 = "Hello, world!"
str2 = "world"
#print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
#print(find_substring(str1, str2)) # поверне -1

"""
Homework_06_3:
Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
Данні в лісті можуть бути будь якими
"""

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']

def get_strings(input_list: list) -> list[str]:
    return [variable for variable in input_list if isinstance(variable, str)]

lst2 = get_strings(lst1)

#print(lst1)
#print(lst2)