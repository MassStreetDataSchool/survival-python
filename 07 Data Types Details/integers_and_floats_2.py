a = int(2.8)
b = int('2')
# Not supported int('2.8') would return an error

c = float('2')
d = float('2.1')
e = float(2)

f = int(float('2.8'))

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))
print(f, type(f))

