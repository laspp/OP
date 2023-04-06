"""Zamrzovalna omara - združevanje seznamov"""

# Pripravljamo zalogo hrane, ki jo bomo dali v zamrzovalno omaro.
# Hrano iste vrste damo skupaj v vrečko. Zapišemo si tudi količino
# in enoto hrane v vrečki. Pripravimo si tri sezname:

# indeksi:  0                 1        2
opis     = ['sojini polpeti', 'bučke', 'pišč. bedrca']
kolicina = [12,               1,       4]
enota    = ['kos',            'kg',    'kos']

# Izpišimo vsebino zamrzovalnika. Potrebujemo indekse, uporabimo range():
for i in range(len(opis)):
    print(opis[i], kolicina[i], enota[i])

# Kako bi te tri sezname združili v enega?
zamrzovalnik = []
for i in range(len(opis)):
    # Tu se odločimo, da bomo elemente spajali v terke
    zamrzovalnik.append((opis[i], kolicina[i], enota[i]))
print(zamrzovalnik)

# Kaj pa, če seznami niso enako dolgi?
# Recimo, da igubimo podatek o količini piščančjih bedrc
kolicina.pop()

# Pogledamo dolžine seznamov in vzamemo "najmanjši skupni imenovalec"
n = min(len(opis), len(kolicina), len(enota))

zamrzovalnik2 = []
for i in range(n):
    zamrzovalnik2.append(
        (opis[i], kolicina[i], enota[i])
        )
    
print(zamrzovalnik2)

# Nato ugotovimo, da Python pozna funkcijo, ki dela točno to: zip()
zamrzovalnik3 = list(zip(opis, kolicina, enota))
print(zamrzovalnik3)
