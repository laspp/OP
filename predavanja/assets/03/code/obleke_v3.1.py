videz = 'navaden'
odgovor = input('Koliko stopinj je zunaj? ')
odgovor = float(odgovor)
if odgovor < 5:
    print('Zima! Rabim kapo in tople škornje.')
    videz = 'kapa in škornji'
elif odgovor > 25:
    print('Vroče! Vzamem pokrivalo in pijačo.')
    videz = 'pijača in pokrivalo'
else:
    print('Prijetno toplo, obujem superge.')
    videz = 'superge'
print('Zdaj grem lahko ven! Moj videz:', videz)
