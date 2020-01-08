"""
string slicing

<string>[0] returns the character at index zero in the string
<string>[-1] returns the last character in the string
<string>[:3] returns the first 3 characters in the string, from index 0 to index 2
<string>[3:] returns all but the first 3 characters in the string, from index 3 on
<string>[3:5] returns all from index 3 to index 5 of the string
<string>[3:-2] returns all from index 3, to the second to last index of the string
"""

numbers = '1234567890'

print('numbers[0]', numbers[0])
print('numbers[-1]', numbers[-1])
print('numbers[:3]', numbers[:3])
print('numbers[3:]', numbers[3:])
print('numbers[3:5]', numbers[3:5])
print('numbers[3:-2]', numbers[3:-2])

