"""Različni načini pisanja v datoteko"""

pot = 'nekaj-novega.txt'

# Če datoteka še ne obstaja, jo bomo ustvarili,
# če obstaja, jo bomo prepisali.
with open(pot, mode='w', encoding='utf8') as datoteka:
    datoteka.write('Moja nova zgodba')

# Sedaj datoteka gotovo obstaja, prepišimo jo
with open(pot, mode='w', encoding='utf8') as datoteka:
    datoteka.write('Tvoja zgodba')
# Datoteka ima sedaj vsebino:
# Tvoja zgodba

# Dodajmo nekaj na konec datoteke
with open(pot, mode='a', encoding='utf8') as datoteka:
    datoteka.write('\nje super.')
# Datoteka ima sedaj vsebino:
# Tvoja zgodba
# je super.

# Uporaba funkcije print za izpis v datoteko
recenzent = 'Marko Pišmevuh'
ocena_knjige = 4.9999999

with open(pot, mode='a', encoding='utf8') as datoteka:
    # Pišemo samo novo vrstico
    print(file=datoteka)
    # Na koncu tega izpisa je tudi nova vrstica
    print('Recenzent:', recenzent, file=datoteka)
    # U, kaj pa f-niz?
    print(f'Ocena: {ocena_knjige:.1f}.', file=datoteka)