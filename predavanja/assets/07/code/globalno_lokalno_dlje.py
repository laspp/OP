"""Globalni in lokalni imenski prostor"""

a = 1

def f(x):
    b = 2
    # Ali lahko spremenimo globalno spremenljivko v funkciji?
    # a = a + 1 # Tole ne bo šlo, napaka.
    # a = 2 # To gre, vendar naredimo novo lokalno spremenljivko
          # z istim imenom, zato tudi izgubimo dostop do globalne
    # Tako je prav, povedati moramo, da mislimo globalno
    global a
    a = a + 1
    return x + a + b

print('f(1):', f(1)) # f(1): 4
print('a: ', a)      # a: 2

a = 2
print('f(1):', f(1)) # f(1): 6
print('a: ', a)      # a: 3