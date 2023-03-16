"""
Vožnja čez seznam
Uporaba zanke while za izpis seznama
"""

# Vsebino v oklepajih (okroglih, oglatih, zavitih) lahko pišemo
# preko več vrstic brez težav.
postaje = [
    'Konzorcij',
    'Cankarjev dom',
    'Svetčeva',
    'Večna pot',
    'Živalski vrt'
    ]

print('Vožnja tja:')
# Prvo postajališče ima indeks 0, drugo 1,..., do `len(postaje)-1`.
# Potrebujemo števec, ki se vsako iteracijo zanke poveča za 1,
# s pogojem v glavi zanke pa pazimo, da se pravočasno ustavimo.
i = 0
while i < len(postaje):
    postaja = postaje[i]
    print('\t', postaja)
    i = i + 1
    
print('In vožnja nazaj:')
# Števec v zanki oz. indeks seznama pogosto označimo z i
i = len(postaje)-1
while i >= 0:
    print('\t', postaje[i])
    i -= 1
    
print('Vožnja nazaj malo drugače:') 
i = 1
while i <= len(postaje):
    print('\t', postaje[-i])
    i += 1