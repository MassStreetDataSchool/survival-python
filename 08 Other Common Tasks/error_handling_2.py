import random
menu = '''What do you want to do?
1) Add a name
2) Select a random name
3) Remove a name
q) quit
'''

names = ['Tony', 'Betsy', 'Peter']

while True:
    print(names)
    choice = input(menu)
    if choice.lower() == 'q':
        break
    elif choice == '1':
        new_name = input('What name do you want to add?')
        names.append(new_name)
    elif choice == '2':
        print('The random name is {}'.format(random.choice(names)))
        input('Press Enter to Continue')
    elif choice == '3':
        name_to_remove = input('What name do you want to remove?')
        try:
            names.remove(name_to_remove)
        except Exception as e:
            print(e)
            input('press Enter to continue')

