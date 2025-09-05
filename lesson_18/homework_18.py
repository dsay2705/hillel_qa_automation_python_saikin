#Генератори:

#1. Напишіть генератор, який повертає послідовність парних чисел від 0 до N.
def even_numbers_gen(n):
    for i in range(0, n + 1, 2):
        yield i

#2. Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.
def fibonacci_gen(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

#Ітератори:

#1. Реалізуйте ітератор для зворотного виведення елементів списку.
class ReverseListIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

#2. Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.
class EvenNumberIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.current <= self.n:
            if self.current % 2 == 0:
                result = self.current
                self.current += 1
                return result
            self.current += 1
        raise StopIteration

#Декоратори:

#1. Напишіть декоратор, який логує аргументи та результати викликаної функції.
def args_results_logger(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

#2. Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.
def catch_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in {func.__name__}: {e}")
    return wrapper
