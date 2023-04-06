def plus_1(a, b):
    c = a + b
    return c

def plus_2(a, b):
    a += b
    return a

# Najprej nizi, ki so nespremenljivi
x = 'logo'
y = 'ped'
z = plus_1(x, y)
print('x:', x, ', y:', y, ', z:', z)

z = plus_2(x, y)
print('x:', x, ', y:', y, ', z:', z)

# Poskusimo s spremenljivimi seznami
x = [1, 2, 3]
y = [4, 5]
z = plus_1(x, y)
print('x:', x, ', y:', y, ', z:', z)

z = plus_2(x, y)
print('x:', x, ', y:', y, ', z:', z)