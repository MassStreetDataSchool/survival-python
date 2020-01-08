name = 'Tony'
age = 26

# Not so great way
sentence = 'My name is ' + name + ', I am ' + str(age) + ' years old'
print(sentence)

# Fabulous way
sentence_again = 'My name is {}, I am {} years old'.format(name, age)
print(sentence_again)

