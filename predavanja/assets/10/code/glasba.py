"""
Glasbena zbirka
Zgled večnivojske zgradbe slovarja (slovar v slovarju).
V zbirki hranimo izvajalce in za vsakega od njih še albume.
Za vsak album imamo tudi podatek o letu izdaje.
"""

def dodaj_izvajalca(zbirka, izvajalec):
    if izvajalec not in zbirka:
        zbirka[izvajalec] = {}
    else:
        print('Izvajalec', izvajalec, 'je že v zbirki.')

def dodaj_album(zbirka, izvajalec, album, leto=None):
    # Če izvajalca še ni v zbirki, da najprej dodamo
    if izvajalec not in zbirka:
        dodaj_izvajalca(zbirka, izvajalec)  
    # Bodimo pozorni na dvonivojsko sklicevanje
    zbirka[izvajalec][album] = leto

def izbrisi_izvajalca(zbirka, izvajalec):
    r = zbirka.pop(izvajalec, None)
    if not r:
        print('Izvajalec '+ izvajalec + ' ne obstaja')
    
def popravi_leto_albuma(zbirka, izvajalec, album, leto):
    if izvajalec in zbirka and album in zbirka[izvajalec]:
        zbirka[izvajalec][album] = leto

def izpisi_zbirko(zbirka):
    print('Zbirka:')
    for izvajalec in zbirka:
        print(' ', izvajalec)
        izpisi_albume(zbirka, izvajalec)
        
def izpisi_izvajalce(zbirka):
    print('Izvajalci:')
    for izvajalec in zbirka:
        print(' ', izvajalec)
   
def izpisi_albume(zbirka, izvajalec):
    for album, leto in zbirka[izvajalec].items():
        if not leto:
            leto = 'neznano'
        print('    ', album, ' (', leto, ')', sep='')

def izpisi_vse_albume(zbirka, od_leta=float('-inf')):
    """Izpiše vse albume, ki so novejši od_leta"""
    print('Vsi albumi novejši od leta ', od_leta, ': ', sep='')
    for albumi in zbirka.values():
        for album, leto in albumi.items():
            if leto and leto >= od_leta:
                print(' ', album)
        

# Začetna zbirka je prazna
zbirka = {}
# Dodamo prvega izvajalca, njegovi albumi so zaenkrat prazen slovar
zbirka['Vlado Kreslin'] = {}
# Dodamo prvi album in letnico izdaje
zbirka['Vlado Kreslin']['Kreslinčice'] = 2002
print(zbirka)

# Uporaba funkcij
dodaj_izvajalca(zbirka, 'Dua Lipa')
dodaj_album(zbirka, 'Dua Lipa', 'Future Nostalgia', 2020)
dodaj_album(zbirka, 'Vlado Kreslin', 'Drevored')
popravi_leto_albuma(zbirka, 'Vlado Kreslin', 'Drevored', 2010)

izpisi_zbirko(zbirka)
izpisi_izvajalce(zbirka)
izpisi_vse_albume(zbirka)
izpisi_vse_albume(zbirka, 2010)

izbrisi_izvajalca(zbirka, 'Bon Jovi')
izbrisi_izvajalca(zbirka, 'Dua Lipa')
izpisi_zbirko(zbirka)


