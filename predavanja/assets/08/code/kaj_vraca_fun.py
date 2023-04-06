"""Nekaj primerov, kaj vse lahko vrača funkcija"""

def povprecje_1(seznam):
    p = sum(seznam)/len(seznam)
    print('Povprečje je', p)

def povprecje_2(seznam):
    p = sum(seznam)/len(seznam)
    return p

def povprecje_3(seznam):
    p = sum(seznam)/len(seznam)
    return 'Povprečje je '+ str(p)

def povprecje_4(seznam):
    v = sum(seznam)
    d = len(seznam)
    p = v/d
    n = 'Povprečje je '+ str(p)
    # Vrnemo terko, v kateri sta seznam in niz
    return [v, d, p], n
    # Lahko zapišemo tudi z oklepaji
    #return ([v, d, p], n)

s = [20, 50, 3, -4]
povprecje_1(s)
p = povprecje_2(s)
print(p)
p = povprecje_3(s)
print(p)
p = povprecje_4(s)
print(p)