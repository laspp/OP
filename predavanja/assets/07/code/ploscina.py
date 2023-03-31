from math import pi

def ploscina_kvadrat(a):
    s = a*a
    return s

def ploscina_krog(r):
    s = pi * r**2
    return s

def ploscina(x, lik):
    if lik == 'kvadrat':
        return ploscina_kvadrat(x)
    elif lik == 'krog':
        return ploscina_krog(x)
    else:
        print('Ne znam izračunati ploščine za', lik, ':(')

stranica = int(input('Vpiši stranico kvadrata: '))
plosc = ploscina_kvadrat(stranica)
print('Ploščina kvadrata s stranico', stranica, 'je', plosc)

r = int(input('Vpiši polmer kroga: '))
s = ploscina_krog(r)
print('Ploščina kroga s polmerom', r, 'je', s)

# Uporaba bolj splošne funkcije, ki sprejme dva argumenta
print('Ploščina kvadrata s stranico', stranica,
      'je', ploscina(stranica, 'kvadrat'))

print('Ploščina kroga s polmerom', r, 'je', ploscina(r, 'krog'))

print('Ploščina trikotnika s stranico', 5, 'je', ploscina(5, 'trikotnik'))
# Izpis:
# Ne znam izračunati ploščine za trikotnik :(
# Ploščina trikotnika s stranico 5 je None