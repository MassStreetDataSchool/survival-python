import os

user = os.getlogin()
print('\nCurrent Logged in User:\n{}'.format(user))

info = os.uname()
print('\nCurrent Operating System Info:\n{}'.format(info))

files = os.listdir()
print('\nFiles in Current Working Directory:\n{}'.format(files))
