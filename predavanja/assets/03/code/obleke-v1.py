videz = 'navaden'
odgovor = input('Koliko stopinj je zunaj? ')
odgovor = float(odgovor)
if odgovor < 5:
    print('Zima! Rabim kapo in tople škornje.')
    videz = 'kapa in škornji'
print('Zdaj grem lahko ven! Moj videz:', videz)