"""Primer: samo pozitivna števila v seznamu
Izpišimo tista števila v seznamu, ki so večja od 0.
Seznam preberemo od uporabnika.
"""
seznam = eval(input('Vnesi seznam števil: '))

# Prva možnost: takojšen izpis
print('Pozitivna števila so: ', end='')

for element in seznam:
    if element > 0:
        print(element, end=', ')
print()

# Druga možnost: dodajanje pozitivnih v
# nov seznam in izpis s print
pozitivni = []
for element in seznam:
    if element > 0:
        pozitivni.append(element)
print('Pozitivna števila so:', pozitivni)

# Tretja možnost: brisanje negativnih
# in izpis celega seznama s print
print('Pozitivna števila so: ', end='')
# Naredimo kopijo, v kateri bomo brisali
kopija = seznam.copy()

for element in seznam:
    if not (element > 0):
        kopija.remove(element)
print(kopija)



