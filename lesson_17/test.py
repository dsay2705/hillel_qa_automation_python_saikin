import randominfo
person = randominfo.Person()

print("Full name:", person.full_name)
print("Gender:", person.gender)
print("Hobbies:", ', '.join(person.hobbies))
print("Country:", person.country)
print("Address:")
for key, value in person.address.items():
    print(f"  {key.capitalize()}: {value}")
