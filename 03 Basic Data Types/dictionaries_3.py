person_1 = {
    'first_name': 'Tony',
    'last_name': 'Macaroni',
    'age': 26,
    'state': 'PA',
}

person_2 = {
    'first_name': 'Betsy',
    'last_name': 'Bolognese',
    'age': 34,
    'state': 'KS',
}

person_3 = {
    'first_name': 'Peter',
    'last_name': 'Pepperoni',
    'age': 24,
    'state': 'NY',
}

friends = [
    person_1,
    person_2,
    person_3
]

print(friends)

peter = friends[2]
print(peter['last_name'])
