"""
Program za beleženje metov krompirja
- uporabnik vnaša dolžine metov enega po enega
- konča tako, da vpiše znak 'X'
- če vpiše 'I', program izpiše seznam dolžin
"""

# Ustvarimo prazen seznam
meti = []

print("""NAVODILA:
Vnesi dolžino meta
ali I za izpis seznama
ali X za izhod.
""")
    
# V zanki beremo uporabnikove vnose
while True:
    vnos = input('Vnos: ')
    
    if vnos.upper() == 'X':
        print('Konec')
        break
    elif vnos.upper() == 'I':
        if not meti:
            print('Seznam je prazen.')
        else:
            print('Seznam metov:')
            i = 0
            while i < len(meti):
                print(i, ': ', meti[i], ' m', sep='')
                i = i + 1
    else:
        dolzina = float(vnos)
        meti.append(dolzina)
        # Dodajanje elementa drugače:
        # meti.extend([dolzina])
        # meti = meti + [dolzina]
        # meti += [dolzina]
        # meti.insert(len(meti),dolzina)
