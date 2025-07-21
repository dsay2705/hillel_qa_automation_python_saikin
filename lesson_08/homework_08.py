"""
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

def sum_list_numbers(list_of_strings):
    for string in list_of_strings:
        print(sum_string_numbers(string))

sum_list_numbers(test_data)