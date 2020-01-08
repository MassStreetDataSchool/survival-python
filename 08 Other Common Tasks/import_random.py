import random

letters = ['a', 'b', 'c', 'd', 'e', 'f']

count = 0
while count < 10:
    random_int = random.randint(0, 9)
    random.shuffle(letters)
    choice = random.choice(letters)
    print('RandInt: {}, Shuffle: {}, Choice: {}'.format(random_int, letters, choice))
    count += 1
