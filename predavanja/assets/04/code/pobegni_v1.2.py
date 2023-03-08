"""
Pobegni!
Pustolovska igra v slogu slavne sobe pobega

Avtor: FKKT letnik 2023
Verzija: 1.2
Spremembe:
    - besedila smo dali v svojo datoteko in jo uvozili 
      kot modul
    - uganka za odklep vrat je lažja, a se naključno spreminja;
      uporabili smo modul `random`
    - merimo čas, ki ga uporabnik potrebuje za posamezno stopnjo;
      uporabimo modul `time`
    - odklep ključavnice traja nekaj časa, uporabimo `time.sleep()`
    - glavni meni: lahko končamo igro, uporabimo `sys.exit(0)`
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
import igra_pobegni_besedila as bes

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
# Pravi PIN
pin_pravi = str(a + b * c)
# Sestavimo niz, ki vsebuje izračun za prikaz.
uganka_niz = str(a) + " + " + str(b) + " * " + str(c)

print(bes.s1_opis_sobe)

cas_zacetek = perf_counter()

stopnja_opravljena = False
while not stopnja_opravljena:

    # Izbira dejanja
    ponovi_izbiro = True
    while ponovi_izbiro:
        # Pri izpisu ne naredimo zaključne nove vrstice
        print(bes.izbira_dejanja, end='')
        print(bes.s1_dejanja)
        print(bes.glavni_meni)
        # Prestejemo dejanja, ki jih je toliko kot znakov \n
        stevilo_dejanj = bes.s1_dejanja.count('\n')
        # Uporabnik vpiše izbiro. Zaradi lažjega primerjanja
        # z dovoljenimi izbirami, jo pretvorimo v število.
        izbira = input(bes.izbira_input)
        # Glavni meni - najprej pogledamo za črke.
        # Pred primerjavo poenotimo velike/male črke.
        if izbira.upper() == 'X':
            # Končajmo igro
            print('Konec igre, nasvidenje!')
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
    print('Resna napaka, končujem program.')
    sys.exit(1)

