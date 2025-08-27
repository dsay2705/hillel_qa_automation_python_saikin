import json
from abc import ABC, abstractmethod
import math

#Task_1:

class Employee:
    def __init__(self, name: str, salary: float, **kwargs):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name: str, salary: float, department: str, **kwargs):
        super().__init__(name, salary, **kwargs)
        self.department = department

class Developer(Employee):
    def __init__(self, name: str, salary: float, programming_language: str, **kwargs):
        super().__init__(name, salary, **kwargs)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name: str, salary: float, department: str, programming_language: str, team_size: int, **kwargs):
        super().__init__(name, salary, department=department, programming_language=programming_language, **kwargs)
        self.team_size = team_size

team_lead = TeamLead("Danylo", 9999, "Development", "Python", 9)
print(json.dumps(vars(team_lead)))

#Task_2:

class Figure(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

class Triangle(Figure):
    def __init__(self, side_a: float, side_b: float, side_c: float):
        self.__a = side_a
        self.__b = side_b
        self.__c = side_c

    def area(self) -> float:
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c))

    def perimeter(self) -> float:
        return self.__a + self.__b + self.__c

class Circle(Figure):
    def __init__(self, radius: float):
        self.__radius = radius

    def area(self) -> float:
        return math.pi * self.__radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.__radius

class Square(Figure):
    def __init__(self, side: float):
        self.__side = side

    def area(self) -> float:
        return self.__side * self.__side

    def perimeter(self) -> float:
        return 4 * self.__side

all_figures = [
    Triangle(3, 4, 5),
    Circle(5),
    Square(4)
]

for figure in all_figures:
    print(f"{figure.__class__.__name__}: Area = {figure.area():.1f}, Perimeter = {figure.perimeter():.1f}")
