person = {
    'first_name': 'Tony',
    'last_name': 'Macaroni',
    'age': 26,
    'job': 'Python Developer'
}

del person['age']
print(person)

person.pop('job')
print(person)

