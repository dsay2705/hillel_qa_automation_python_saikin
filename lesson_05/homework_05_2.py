# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record to the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

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

# 1 - Add your new record to the beginning of the given list

my_record = ('Danylo', 'Saikin', 30, 'QA Engineer', 'Kharkiv')
people_records.insert(0, my_record)

# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result

print("After swapping indexes 1 and 5:")
people_records[1], people_records[5] = people_records[5], people_records[1]
for person in people_records:
    print(person)

# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

indexes_to_check = [6, 10, 13]
ages = [people_records[i][2] for i in indexes_to_check]
all_above_30 = all(age >= 30 for age in ages)
print(f"\nAll people at indexes {indexes_to_check} have age >= 30: {all_above_30}")

