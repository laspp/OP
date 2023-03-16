"""
Program za beleženje metov krompirja
- uporabnik vnaša dolžine metov enega po enega
- konča tako, da vpiše znak 'X'
- če vpiše 'I', program izpiše seznam dolžin
- če vpiše 'S', program izpiše padajoče urejen seznam
- če vpiše 'N', program izpiše najdaljšo dolžino meta
- če vpiše 'P', program izpiše povprečno dolžino meta
- če vpiše 'M', program izpiše mediano dolžine meta
- uporabnik vpiše -1, če je bil met neveljaven; ta met se ne upošteva
  pri izračunih povprečja in mediane, tudi se ne izpiše pri opciji 'S' 
"""

# Ustvarimo prazen seznam
meti = []

print("""NAVODILA:
Vnesi dolžino meta ali
-1, če je bil met neveljaven ali
I: izpis seznama metov
S: izpis urejenega seznama
N: izpis najdaljšega meta
P: izpis povprečja metov
M: izpis mediane metov
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
            # Najprej preverimo, ali so morda v seznamu sami neveljavni
            # meti (imajo vrednost -1)
            if meti.count(-1) == len(meti):
                print('Ni veljavnih metov')
                # Gremo na naslednji obhod zanke
                continue
            
            # Seznam uredimo padajoče in vzamemo prvega.
            # S tem porušimo vrstni red metov!
            # Zato raje prej naredimo kopijo in delamo na njej
            kopija = meti.copy()
            kopija.sort(reverse=True)
            print('Urejen seznam:')
            i = 0
            while i < len(kopija):
                if kopija[i] < 0:
                    # Od tu naprej so negativna števila, končamo izpis
                    break
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
            
            # Pred računanjem, bomo:
            # 1. Kopirali seznam
            # 2. uredili seznam naraščajoče
            # 3. v zanki izbrisali elemente z vrednostjo -1 (na začetku)
            kopija = meti.copy()
            kopija.sort()
            while kopija and kopija[0] < 0:
                # Brisanje elementa na več načinov:
                #del kopija[0]
                kopija.pop(0)
                #kopija.remove(kopija[0])
            
            if not kopija:
                print('Ni veljavnih metov.')
                # Gremo na naslednji obhod zanke
                continue
            
            i = 0
            vsota = 0
            n = len(kopija)
            while i < n:
                vsota += kopija[i]
                i = i + 1            
            povprecje = vsota / n
            
            # Vsoto lahko dobimo tudi s funkcijo sum()
            povprecje = sum(kopija) / n
            
            print('Povprečna dolžina meta: ', povprecje, ' m', sep='')
    
    elif vnos.upper() == 'M':
        # Izračun mediane - to je sredinski element
        # Glej https://eucbeniki.sio.si/vega1/65/index1.html
        # 1. Seznam uredimo
        # 2. Odstranimo neveljavne mete
        # 3. Izračunamo indeks sredinskega elementa
        #    a.) Če je seznam lihe dolžine, je to en sam element
        #    b.) Če je sode dolžine, vzamemo povprečje sredinskih dveh
        kopija = meti.copy()
        kopija.sort()
        while kopija and kopija[0] < 0:
            kopija.pop(0)
        
        if not kopija:
            print('Ni veljavnih metov.')
            # Gremo na naslednji obhod zanke
            continue
        n = len(kopija)
        if n%2 == 1:
            # Liha dolžina
            mediana = kopija[n//2]
        else:
            # Soda dolžina
            mediana = (kopija[n//2] + kopija[n//2 - 1]) / 2
        print('Mediana dolžine meta: ', mediana, ' m', sep='')
    
    else:
        dolzina = float(vnos)
        meti.append(dolzina)
        # Dodajanje elementa drugače:
        # meti.extend([dolzina])
        # meti = meti + [dolzina]
        # meti += [dolzina]
        # meti.insert(len(meti),dolzina)


