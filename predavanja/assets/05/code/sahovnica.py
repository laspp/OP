"""
Sprehod čez seznam seznamov
Primer šahovnice 4x4
"""

plosca = [
    ['█','░','█','░'],
    ['░','█','░','█'],
    ['█','░','█','░'],
    ['░','█','░','█'],
    ]

st_vrstic = len(plosca)
st_stolpcev = len(plosca[0])

vrstica = 0
while vrstica < st_vrstic:
    stolpec = 0
    while stolpec < st_stolpcev:
        # Izpišemo vsebino polja brez nove vrstice
        print(plosca[vrstica][stolpec], end='')
        stolpec += 1
    print()
    vrstica += 1
    

