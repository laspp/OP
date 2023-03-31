# met krompirja

print("""NAVODILA:
Vnesi dolžino meta
I - izpiši seznam metov
P - povprečje metov
S - uredi seznam metov
N - najdaljši met
M - mediana metov
X - konec
""")

# Seznam metov
meti = [] # ali list()

while True:
    vnos = input('Vnos: ')
    
    if vnos.upper() == 'X':        
        break
    
    elif vnos.upper() == 'I':
        # Izpiši seznam metov
        i = 0
        while i < len(meti):
            print(i+1, ': ', meti[i], ' m', sep='')
            i += 1
    
    elif vnos.upper() == 'P':
        # Izpiši povprečje metov
        if not meti:
            # Seznam je prazen
            print('Seznam metov je prazen.')
            continue
        
        # 1. uporaba sum in len
        povprecje1 = sum(meti)/len(meti)
        
        # 2. uporaba zanke
        i = 0
        vsota = 0
        while i < len(meti):
            vsota += meti[i]
            i += 1
        povprecje2 = vsota/i
        
        assert povprecje1 == povprecje2, 'Napaka!'
        
        print('Povprečje metov:', povprecje1, 'm')
    
    elif vnos.upper() == 'N':
        # Izpiši najdaljši met
        if not meti:
            # Seznam je prazen
            print('Seznam metov je prazen.')
            continue
        
        # najdaljsi = max(meti)            
        
        najdaljsi = meti[0]
        i = 1
        while i < len(meti):
            if meti[i] > najdaljsi:
                najdaljsi = meti[i]
            i += 1
        
        print('Najdaljši met:', najdaljsi, 'm')

    elif vnos.upper() == 'S':
        # Izpiši urejen seznam metov
        kopija = meti.copy()
        kopija.sort(reverse=True)
                
        # Uporaba zanke for (for each)
        for i in range(len(kopija)):
            print(i+1, '. ', kopija[i], ' m', sep='')
            
    elif vnos.upper() == 'M':
        # Izpiši mediano metov
        if not meti:
            # Seznam je prazen
            print('Seznam metov je prazen.')
            continue        
        
        # uredimo po velikosti
        kopija = meti.copy()
        kopija.sort()
        
        # Izbrišemo nevljavne mete (-1), ki
        # so na začetku
        while -1 in kopija:
            del kopija[0]
            # kopija.pop(0)
            # kopija.remove(-1)
        
        # Ali imamo liho število metov
        n = len(kopija)
        if n % 2 == 1:
            a = n // 2
            mediana = kopija[a]
        else:
            a = n // 2
            b = a - 1
            mediana = (kopija[a] + kopija[b]) / 2
        
        print('Mediana:', mediana, 'm')    
        
    else:
        # Predvidevamo, da je vnos število
        dolzina = float(vnos)
        meti.append(dolzina)

print('Konec programa')      