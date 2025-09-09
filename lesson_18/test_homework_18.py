from .homework_18 import (
    even_numbers_gen, fibonacci_gen,
    ReverseListIterator, EvenNumberIterator,
    args_results_logger, catch_exception
)

def test_even_numbers_gen():
    assert list(even_numbers_gen(10)) == [0, 2, 4, 6, 8, 10]

def test_fibonacci_gen():
    assert list(fibonacci_gen(21)) == [0, 1, 1, 2, 3, 5, 8, 13, 21]

def test_reverse_iterator():
    items = ['a', 'b', 'c']
    result = [i for i in ReverseListIterator(items)]
    assert result == ['c', 'b', 'a']

def test_range_iterator():
    result = [i for i in EvenNumberIterator(10)]
    assert result == [0, 2, 4, 6, 8, 10]

def test_args_results_logger(capsys):
    @args_results_logger
    def add(a, b):
        return a + b

    result = add(2, 3)
    captured = capsys.readouterr()
    assert result == 5
    assert "Calling add with args=(2, 3)" in captured.out
    assert "add returned 5" in captured.out

def test_catch_exception(capsys):
    @catch_exception
    def divide(a, b):
        return a / b

    assert divide(10, 2) == 5.0
    divide(10, 0)
    captured = capsys.readouterr()
    assert "Error in divide: division by zero" in captured.out