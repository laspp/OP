"""Različni načini branja iz datoteke"""

pot = 'besedilo.txt'
crta = '-'*60

print(crta)

with open(pot, mode='r', encoding='utf8') as datoteka:
    vsebina = datoteka.read()
    # Nočemo dodatne nove vrstice na koncu vsebine datoteke, zato end=''
    print(vsebina, end='')
    
print(crta)

with open(pot, mode='r', encoding='utf8') as datoteka:
    seznam_vrstic = datoteka.readlines()
    for vrstica in seznam_vrstic:
        print(vrstica, end='')

# Ponovimo, da `print()` privzeto doda novo vrstico na konec izpisa.
# Posledično bomo imeli na koncu vsake vrstice, ki jo preberemo iz
# datoteke, dve novi vrstici (ena je zapisana v datoteki,
# eno doda `print()`). Zato z argumentom `end=''` jasno povemo, da
# nočemo dodatne nove vrstice.

print(crta)

with open(pot, mode='r', encoding='utf8') as datoteka:
    prva_vrstica = datoteka.readline()
    vrstica = prva_vrstica
    while vrstica:
        print(vrstica, end='')
        vrstica = datoteka.readline()

print(crta)

with open(pot, mode='r', encoding='utf8') as datoteka:
    for vrstica in datoteka:
        print(vrstica, end='')
        
print(crta)