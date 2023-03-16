"""
Program za beleženje metov krompirja
- uporabnik vnaša dolžine metov enega po enega
- konča tako, da vpiše znak 'X'
- če vpiše 'I', program izpiše seznam dolžin
- če vpiše 'S', program izpiše padajoče urejen seznam
- če vpiše 'N', program izpiše najdaljšo dolžino meta
- če vpiše 'P', program izpiše povprečno dolžino meta
"""

# Ustvarimo prazen seznam
meti = []

print("""NAVODILA:
Vnesi dolžino meta ali
I: izpis seznama metov
S: izpis urejenega seznama
N: izpis najdaljšega meta
P: izpis povprečja metov
X: izhod iz programa
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
                
    elif vnos.upper() == 'S':
        if not meti:
            print('Seznam je prazen.')
        else:                        
            # Seznam uredimo padajoče in vzamemo prvega.
            # S tem porušimo vrstni red metov!
            # Zato raje prej naredimo kopijo in delamo na njej
            kopija = meti.copy()
            kopija.sort(reverse=True)
            print('Urejen seznam:')
            i = 0
            while i < len(meti):
                print(i+1, '. mesto: ', kopija[i], ' m', sep='')
                i = i + 1            
            
    elif vnos.upper() == 'N':
        if not meti:
            print('Seznam je prazen.')
        else:
            # Uporaba zanke za iskanje največjega elementa
            i = 0
            najdaljsi = 0
            while i < len(meti):
                if meti[i] > najdaljsi:
                    najdaljsi = meti[i]
                i = i + 1            
            
            # To lahko storimo tudi s funkcijo max()
            najdaljsi = max(meti)
            
            # Lahko tudi uredimo seznam padajoče in vzamemo prvega.
            # S tem porušimo vrstni red metov!
            # meti.sort(reverse=True)
            # Zato raje prej naredimo kopijo in delamo na njej
            kopija = meti.copy()
            kopija.sort(reverse=True)
            najdaljsi = kopija[0]
            print('Najdaljši met: ', najdaljsi, ' m', sep='')
    
    elif vnos.upper() == 'P':
        if not meti:
            print('Seznam je prazen.')
        else:
            # Uporaba zanke za racunanje vsote elementov
            i = 0
            vsota = 0
            n = len(meti)
            while i < n:
                vsota += meti[i]
                i = i + 1            
            povprecje = vsota / n
            
            # Vsoto lahko dobimo tudi s funkcijo sum()
            povprecje = sum(meti) / n
            
            print('Povprečna dolžina meta: ', povprecje, ' m', sep='')
    else:
        dolzina = float(vnos)
        meti.append(dolzina)
        # Dodajanje elementa drugače:
        # meti.extend([dolzina])
        # meti = meti + [dolzina]
        # meti += [dolzina]
        # meti.insert(len(meti),dolzina)

