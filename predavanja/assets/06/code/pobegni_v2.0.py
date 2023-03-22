"""
Pobegni!
Pustolovska igra v slogu slavne sobe pobega

Avtor: FKKT letnik 2023
Verzija: 2.0
Spremembe:
    - uporabimo eval() za rešitev uganke
    - dejanja so v seznamu
    - dodali smo drugo stopnjo: sobo s šahovnico
"""

# Uvozimo modul za naključna števila
#import random
from random import randint, random
from time import perf_counter, sleep
import sys

###########################################################
# Besedila
###########################################################
# Uvozimo besedila pod imenom 'bes'
import pobegni_besedila as bes

###########################################################
# Uvodni zaslon
###########################################################
print(bes.uvod)

###########################################################
# Stopnja 1
###########################################################

# Rešitve ugank
# Uganko bomo sestavili naključno, vsaka igra bo imela svojo rešitev.
a = randint(100, 300)
b = randint(2, 9)
c = randint(2, 9)

# Sestavimo niz, ki vsebuje izračun za prikaz.
uganka_niz = str(a) + " + " + str(b) + " * " + str(c)
# Pravi PIN
pin_pravi = str(eval(uganka_niz))

print(bes.s1_opis_sobe)

cas_zacetek = perf_counter()

stopnja_opravljena = False
while not stopnja_opravljena:

    # Izbira dejanja
    ponovi_izbiro = True
    while ponovi_izbiro:
        # Pri izpisu ne naredimo zaključne nove vrstice
        print(bes.izbira_dejanja)
        for i in range(len(bes.s1_dejanja)):
            print(i+1, '. ', bes.s1_dejanja[i], sep='')
        print(bes.glavni_meni)
        # Prestejemo dejanja
        stevilo_dejanj = len(bes.s1_dejanja)
        # Uporabnik vpiše izbiro. Zaradi lažjega primerjanja
        # z dovoljenimi izbirami, jo pretvorimo v število.
        izbira = input(bes.izbira_input)
        # Glavni meni - najprej pogledamo za črke.
        # Pred primerjavo poenotimo velike/male črke.
        if izbira.upper() == 'X':
            # Končajmo igro
            print(bes.izhod_iz_igre)
            sys.exit(0)

        # Številčna izbira
        dejanje = int(izbira)
        if 1 <= dejanje <= stevilo_dejanj:
            ponovi_izbiro = False
        else:
            print(bes.napacna_izbira)

    if dejanje == 1:
        # Hočemo odpreti modra vrata, ampak so zaklenjena
        print(bes.s1_vrata)
        pin = input(bes.s1_vrata_input)
        # Čakamo 2.5 sekunde
        print(bes.s1_vrata_preverjam_pin)
        sleep(2.5)
        
        if pin == pin_pravi:
            print(bes.s1_vrata_pravilen_pin)
            stopnja_opravljena = True
        else:
            print(bes.s1_vrata_napacen_pin)

    elif dejanje == 2:
        # Poglej na mizo. Iz zvezka pade listič z uganko.
        # V besedilu uganke nadomestimo rezerviran prostor z novo uganko
        uganka_izpis = bes.s1_miza.replace('!uganka!', uganka_niz)

        print(uganka_izpis)

    else:
        # Napačna izbira dejanja
        # Sem ne bi smeli več priti, razen če ...
        print(bes.napacna_izbira)
        break
        
else:
    # To se izvede, ko pogoj `not stopnja_opravljena` ni več resničen
    cas_konec = perf_counter()
    cas_stopnja = round(cas_konec - cas_zacetek)
    print('Stopnjo ste opravili v', cas_stopnja, 'sekundah.')

if not stopnja_opravljena:
    print(bes.resna_napaka)
    sys.exit(1)


###########################################################
# Stopnja 2
###########################################################

# Nastavitve šahovskega polja
n = 8

# Začetni položaj igralca
konj_polozaj_zacetek = 'd1'
konj_polozaj = konj_polozaj_zacetek
# Položaj vrat predstavimo kar z internimi oznakami - indeksi.
# Napišemo ju kot [vrstica, stolpec], pri čemer dodamo ščepec
# naključnosti.
vrata = [
    [randint(1,n-2), 0],
    [0, randint(1,n-2)],
    [randint(2,n-3), n-1]
    ]

# Oznake polj: simbola za 'belo' in 'črno'
polje_oznaka = ['░░', '██']
konj_oznaka =   ' ×'
vrata_oznaka = 'v '

print(bes.s2_opis_sobe)

cas_zacetek = perf_counter()

stopnja_opravljena = False
while not stopnja_opravljena:
    # Ustvarimo seznam vrstic, vsaka vrstica je seznam posameznih 
    # polj v vrstici.
    plosca = []
    for vrstica in range(n):
        # Prazen seznam za posamezno vrstico
        plosca.append([])
        for stolpec in range(n):
            # Če si zapišemo indekse posameznega polja in pogledamo sodost
            # indeksa vrstice in stolpca, opazimo ta vzorec:
            # če sta indeksa vrstice in stolpca bodisi oba soda
            # bodisi liha, je polje belo, sicer je črno.
            # Velja tudi: sodo + sodo = sodo = liho + liho
            # Torej, če je vsota indeksa vrstice in stolpca soda,
            # je polje belo.
            oznaka_i = (vrstica + stolpec) % 2
            polje = polje_oznaka[oznaka_i]
            plosca[vrstica].append(polje)

    # Dodamo vrata
    for v in vrata:
        plosca[v[0]][v[1]] = vrata_oznaka

    # V seznam sedaj vstavimo konja na želeno pozicijo
    # Poiščimo pravi indeks vrstice in stolpca glede na položaj
    # Stolpec dobimo iz prvega znaka položaja, npr. 'b'. Zdaj moramo 'b'
    # preslikati v indeks drugega elementa v seznamu. Vemo tole:
    # ord('a') = 97
    # ord('b') = 98
    # ...
    # chr(97) = 'a'
    # Indeks 0 se torej preslika na 'a', ki ima vrednost 97.
    # Indeks 1 dobimo kot ord('b') - ord('a') = 98 - 97
    konj_stolpec = ord(konj_polozaj[0]) - ord('a')

    # Vrstico šahovnice pretvorimo v indeks vrstice v seznamu tako, da:
    # se 8 preslika v 0
    # in 1 v 7 (ter vse vmes).
    # Preprosto od n odštejemo oznako vrstice.
    konj_vrstica = n - int(konj_polozaj[1])
    
    # Preverimo, če je igralec prišel na polje z vrati
    konj_na_vratih = False
    nova_oznaka = konj_oznaka
    for i in range(len(vrata)):
        if [konj_vrstica, konj_stolpec] == vrata[i]:
            konj_na_vratih = i+1
            nova_oznaka = vrata_oznaka.strip() + konj_oznaka.strip()
        
    plosca[konj_vrstica][konj_stolpec] = nova_oznaka

    

    # Izris plošče skupaj z oznakami
    print()
    for vrstica in range(n):
        # Najprej pride oznaka vrstice, začnemo z najvišjo:
        # v primeru plošče 8x8 je zgoraj 8. vrstica
        print(n-vrstica,'│', sep='', end='')
        
        for stolpec in range(n):
            print(plosca[vrstica][stolpec], sep='', end='')
        print()
        
    # Najprej ločevalna črta v svoji vrstici
    # Za simbole glej: https://en.wikipedia.org/wiki/Box-drawing_character
    print(' └' + '─'*n*2)
    # Nato zamik
    print(' ', end='')
    # In zatem izpis oznak stolpcev s črkami od 'a' naprej
    for stolpec in range(n):
        print(' ', chr(97+stolpec), sep='', end='')
    print()

    ponovi_izbiro = True
    
    # Če pridemo do vrat, izpišemo eno od besedil
    if konj_na_vratih:   
        
        if konj_na_vratih == 1:
            print(bes.s2_vrata1)
            input(bes.s2_ponovni_zacetek)
            konj_polozaj = konj_polozaj_zacetek
            ponovi_izbiro = False
            
        elif konj_na_vratih == 2:
            print(bes.s2_vrata2)
        
        elif konj_na_vratih == 3:
            print(bes.s2_vrata3)
            input(bes.s2_ponovni_zacetek)
            konj_polozaj = konj_polozaj_zacetek
            ponovi_izbiro = False
    else:
        ponovi_izbiro = True
    
    while ponovi_izbiro:
        # Imamo samo eno dejanje
        print(bes.s2_dejanja[0])
        print(bes.glavni_meni)
                
        # Uporabnik vpiše izbiro.
        izbira = input(bes.izbira_input)
        # Glavni meni - najprej pogledamo za črke.
        # Pred primerjavo poenotimo velike/male črke.
        if izbira.upper() == 'X':
            # Končajmo igro
            print(bes.izhod_iz_igre)
            sys.exit(0)
        
        elif not (len(izbira) == 2 and
                  izbira[0].isalpha() and
                  izbira[1].isnumeric()):
            print(bes.napacna_izbira)
        else:    
            konj_polozaj_nov = izbira
            # Preverimo veljavnost tega premika:
            # veljavni so tisti premiki, pri katerih se:
            # - stolpec spremeni za 1 IN vrstica za 2 ALI
            # - stolpec spremeni za 2 IN vrstica za 1
            konj_stolpec_nov = ord(konj_polozaj_nov[0]) - ord('a')
            konj_vrstica_nov = n - int(konj_polozaj_nov[1])

            sprememba_stolpca = abs(konj_stolpec_nov - konj_stolpec)
            sprememba_vrstice = abs(konj_vrstica_nov - konj_vrstica)
            veljavna_poteza = (
                (sprememba_stolpca == 1 and sprememba_vrstice == 2 or
                sprememba_stolpca == 2 and sprememba_vrstice == 1) and
                0 <= konj_stolpec_nov < n and
                0 <= konj_vrstica_nov < n
                )
            if veljavna_poteza:
                konj_polozaj = konj_polozaj_nov
                ponovi_izbiro = False
            else:
                print(bes.s2_napacna_izbira)
else:
    # To se izvede, ko pogoj `not stopnja_opravljena` ni več resničen
    cas_konec = perf_counter()
    cas_stopnja = round(cas_konec - cas_zacetek)
    print('Stopnjo ste opravili v', cas_stopnja, 'sekundah.')

if not stopnja_opravljena:
    print(bes.resna_napaka)
    sys.exit(1)
