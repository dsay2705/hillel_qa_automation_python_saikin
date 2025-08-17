class Student:
    def __init__(self, first_name, last_name, age, avg_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.avg_grade = avg_grade

    def display_info(self):
        print(f"Студент: {self.first_name} {self.last_name}")
        print(f"Вік: {self.age}")
        print(f"Середній бал: {self.avg_grade}")

    def update_avg_grade(self, new_grade):
        self.avg_grade = new_grade

my_student = Student("Данило", "Сайкін", 30, 79)
my_student.display_info()

my_student.update_avg_grade(91)
my_student.display_info()