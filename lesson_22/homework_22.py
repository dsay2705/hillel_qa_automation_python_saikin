from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import random

SQLITE_SQL = 'sqlite:///students_and_courses.db'
engine = create_engine(SQLITE_SQL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

enrollment_table = Table(
    'enrollment', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship('Course', secondary=enrollment_table, back_populates='students')

    def __repr__(self):
        return f"Student(id={self.id}, name='{self.name}')"

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    students = relationship('Student', secondary=enrollment_table, back_populates='courses')

    def __repr__(self):
        return f"Course(id={self.id}, name='{self.name}')"

Base.metadata.create_all(engine)

def create_data(session):
    courses = [Course(name=f"Course {i}") for i in range(1, 6)]
    session.add_all(courses)
    session.commit()
    for i in range(1, 21):
        student = Student(name=f"Student {i}")
        student.courses = random.sample(courses, random.randint(1, 3))
        session.add(student)
    session.commit()

def show_students_in_course(name):
    course = session.query(Course).filter_by(name=name).first()
    print(f"\nStudents in {name}:")
    if course:
        for student in course.students:
            print(student)
    else:
        print(f"Course {name} not found.")

def get_student_id_by_name(name):
    student = session.query(Student).filter_by(name=name).first()
    if student:
        return student.id
    else:
        print(f"\nStudent '{name}' not found.")
        return None

def update_student(old_name=None, student_id=None, new_name=None, course_ids=None):
    if student_id:
        student = session.get(Student, student_id)
    elif old_name:
        student = session.query(Student).filter_by(name=old_name).first()
    else:
        print("\nNo identifier provided for student.")
        return
    if student:
        if new_name:
            student.name = new_name
            print(f"\nUpdated name to {new_name}.")
        if course_ids:
            new_courses = session.query(Course).filter(Course.id.in_(course_ids)).all()
            student.courses = new_courses
            print(f"Updated courses to {[c.name for c in new_courses]}.")
        session.commit()
    else:
        if old_name:
            print(f"\nStudent {old_name} not found.")
        else:
            print(f"\nStudent {student_id} not found.")

def add_user(name):
    student = Student(name=name)
    all_courses = session.query(Course).all()
    student.courses = random.sample(all_courses, random.randint(1, 3))
    session.add(student)
    session.commit()
    print(f"\nAdded student: {student}")

def show_courses_of_student(name):
    student = session.query(Student).filter_by(name=name).first()
    if student:
        print(f"\nCourses of {name}:")
        for course in student.courses:
            print(course)
    else:
        print(f"\nStudent {name} not found.")

def update_course(course_id, new_name=None, student_ids=None):
    course = session.get(Course, course_id)
    if course:
        if new_name:
            course.name = new_name
            print(f"\nUpdated course name to {new_name}.")
        if student_ids:
            new_students = session.query(Student).filter(Student.id.in_(student_ids)).all()
            course.students = new_students
            print(f"Updated students to {[s.name for s in new_students]}.")
        session.commit()
    else:
        print(f"\nCourse {course_id} not found.")

def delete_student_by_id(student_id):
    student = session.get(Student, student_id)
    if student:
        session.delete(student)
        session.commit()
        print(f"\nStudent {student_id} deleted.")
    else:
        print(f"\nStudent {student_id} not found.")


print("\n--- Creating Initial Data ---")
create_data(session)

print("\n--- Students in Course 1 ---")
show_students_in_course("Course 1")

print("\n--- Adding a New User ---")
add_user("New Student")

print("\n--- Courses of New Student ---")
show_courses_of_student("New Student")

print("\n--- ID of 'New Student' ---")
new_student_id = get_student_id_by_name("New Student")
print(f"ID of 'New Student': {new_student_id}")

print("\n--- Updating 'New Student' ---")
update_student(student_id=new_student_id, new_name="Updated Student", course_ids=[1, 2])

print("\n--- Courses of Updated Student ---")
show_courses_of_student("Updated Student")

print("\n--- Updating Course 1 ---")
update_course(course_id=1, new_name="Advanced Course 1", student_ids=[new_student_id])

print("\n--- Students in Updated Course ---")
show_students_in_course("Advanced Course 1")

print("\n--- Deleting Updated Student ---")
delete_student_by_id(new_student_id)
