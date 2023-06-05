import os
import shutil
# Namesti modul pillow
from PIL import Image

"""
# 1. Rešimo problem sortiranja datotek po imenu.
Na Windows imamo sortiranje po abecedi rešeno tako, da upošteva numerično vrednost.
slika_1.jpg
slika_2.jpg
slika_10.jpg
slika_11.jpg
slika_100.jpg
slika_111.jpg

Na večini ostalih sistemov (medijski predvajalniki, ...), ki so tipa UNIX je privzeto drugače:
slika_1.jpg
slika_10.jpg
slika_100.jpg
slika_11.jpg
slika_111.jpg
slika_2.jpg

Kakorkoli, imamo problem, če števila zapisujemo z različnim številom števk. Preimenujmo datoteke, 
da bodo imele števila zapisana na 3 mesta.
slika_001.jpg
slika_002.jpg
slika_010.jpg
slika_011.jpg
slika_100.jpg
slika_111.jpg

2. Zmanjšamo/povečamo slike za nek faktor

TODO: 3. Slike razporedimo po mapah glede na leto in mesec nastanka.
"""

# Dobimo pot do tega programa
pot_program = os.path.dirname(os.path.realpath(__file__))

# Povemo, kje so originali slik
pot_mapa_slike = os.path.join(pot_program, 'slike-stevilke')

# Če želimo kopijo v drugo mapo, jo definiramo tukaj. 
# Če pustimo prazno, bomo delali na datotekah direktno.
pot_mapa_izhod = os.path.join(pot_program, 'slike-stevilke-bolje')
#pot_mapa_izhod = ''

# Končnica datoteke za obdelavo (velikost črk ni pomembna)
koncnica = '.JPG'

# Ali želimo preimenovanje datotek? Daj False, če ne želiš.
preimenuj_datoteke = True

# Hočemo tudi spremeniti velikost slik? Daj False, če ne želiš.
spremeni_velikost = 0.5 # faktor

ustvari_kopijo = pot_mapa_izhod != ''

# Ustvarimo mapo za izhod; ne jamramo, če že obstaja (argument exist_ok).
if ustvari_kopijo:
    os.makedirs(pot_mapa_izhod, exist_ok=True)

datoteke = os.listdir(pot_mapa_slike)
datoteke_slike = []
for datoteka in datoteke:
    if datoteka.upper().endswith(koncnica.upper()):
        datoteke_slike.append(datoteka)
print(f'Našel sem te datoteke s končnico {koncnica}:')
for datoteka in datoteke_slike:
    print(f'  - {datoteka}')

# Preimenujemo tako, da v številko v imenu zapišemo na več mest
for datoteka in datoteke_slike:
    # Pot do originala
    pot_staro = os.path.join(pot_mapa_slike, datoteka)
    
    novo_ime = datoteka
    if preimenuj_datoteke:
        # Pričakujemo obliko imena: predpona_stevilo.jpg
        ime, koncnica = os.path.splitext(datoteka)
        predpona, stevilka = ime.split('_')
        stevilka = int(stevilka)
        novo_ime = f'{predpona}_{stevilka:03}{koncnica}'
    
    if ustvari_kopijo:
        # Naredimo kopijo v pot_mapa_izhod
        pot_novo = os.path.join(pot_mapa_izhod, novo_ime)
        shutil.copyfile(pot_staro, pot_novo)
        print(f'\nKopiral:\n  {pot_staro} →\n  {pot_novo}')
    else:
        # Preimenujemo na mestu
        pot_novo = os.path.join(pot_mapa_slike, novo_ime)
        os.rename(pot_staro, pot_novo)
        print(f'Preimenoval: {pot_staro} → {pot_novo}')
    
    # Spremenimo velikost
    if spremeni_velikost != False:
        slika = Image.open(pot_novo)
        
        # Nova velikost
        sirina, visina = slika.size
        sirina_nova = int(sirina * spremeni_velikost)
        visina_nova = int(visina * spremeni_velikost)
        
        # Spremenimo velikost
        slika_nova = slika.resize((sirina_nova, visina_nova))
        
        # Želimo ohraniti meta podatke o sliki (t.i. podatke EXIF)
        exif = slika.info.get("exif")
        # Shranimo sliko
        slika_nova.save(pot_novo, exif=exif)
        
        print(f'Spremenil velikost slike za {spremeni_velikost}: {sirina}×{visina} px → {sirina_nova}×{visina_nova} px')
    
    