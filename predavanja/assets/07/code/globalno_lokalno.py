"""Globalni in lokalni imenski prostor"""

a = 1

def f(x):
    b = 2
    return x + a + b

print('f(1):', f(1))
# f(1): 4

# Spremenimo vrednost globalne spremenljivke
a = 2

# Pokličemo funkcijo z enako vrednostjo argumenta
print('f(1):', f(1))
# Sedaj dobimo drugačen rezultat
# f(1): 5

# Lahko izpišemo vrednost spremenljivke b, ki je
# lokalna spremenljivka funkcije f()?
print(b)
# Dobimo napako:
# Traceback (most recent call last):
#   File "globalno_lokalno.py", line 22, in <module>
#     print(b)
# NameError: name 'b' is not defined