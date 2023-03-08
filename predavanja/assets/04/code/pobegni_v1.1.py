"""
Pobegni!
Pustolovska igra v slogu slavne sobe pobega

Avtor: FKKT letnik 2023
Verzija: 1.1
Spremembe:
    - dodali smo zanke
        - ponovni vnos pri napačni izbiri, 
        - ponavljanje stopnje
    - preglednost kode: besedila smo zbrali na enem mestu
"""

###########################################################
# Besedila
###########################################################

# Splošno
bes_izbira_dejanja = '\nIzberi eno od dejanj:'
bes_izbira_input = 'Izbira: '
bes_napacna_izbira = 'Napačna izbira!'

# Začetni zaslon - uvod
bes_uvod = """
POBEGNI!

Znajdeš se v neznani sobi.
"Zakaj sem tu?" se sprašuješ.
Hočeš pobegniti."""

# Stopnja 1
bes_s1_opis_sobe = """
Soba ima modra vrata.
Sredi sobe je miza in na njej nekaj."""

# V vsaki vrstici je eno dejanje
bes_s1_dejanja = """
  1. Odpri modra vrata.
  2. Poglej, kaj je na mizi."""

bes_s1_vrata = """
Modra vrata so zaklenjena z elektronsko ključavnico."""

bes_s1_vrata_input = 'Vnesi PIN za odklep: '

bes_s1_vrata_pravilen_pin = 'PIN je pravilen! Vrata so odklenjena.'

bes_s1_vrata_napacen_pin = 'Napačen PIN!'

bes_s1_miza = """
Stopiš do mize, na kateri leži kladivo in
zaprašen zvezek. Odpreš zvezek in ven pade listič,
na katerem je zapisano:
      +~~~~~~~~~~~~~~~~~~~~~~~+
      |                       |
      |  "2"*2+str(0//3)+'1'  |
      |                       |
      +~~~~~~~~~~~~~~~~~~~~~~~+"""

###########################################################
# Uvodni zaslon
###########################################################
print(bes_uvod)

###########################################################
# Stopnja 1
###########################################################

# Rešitve ugank
pin_pravi = '2201'

print(bes_s1_opis_sobe)

stopnja_opravljena = False 
while not stopnja_opravljena:

    # Izbira dejanja
    ponovi_izbiro = True
    while ponovi_izbiro:
        # Pri izpisu ne naredimo zaključne nove vrstice
        print(bes_izbira_dejanja, end='')
        print(bes_s1_dejanja)
        # Prestejemo dejanja, ki jih je toliko kot vrstic.
        # Prištejemo +1, ker na koncu niza ni znaka \n
        stevilo_dejanj = bes_s1_dejanja.count('\n')
        # Uporabnik vpiše izbiro. Zaradi lažjega primerjanja
        # z dovoljenimi izbirami, jo pretvorimo v število.
        dejanje = int(input(bes_izbira_input))
        
        if 1 <= dejanje <= stevilo_dejanj:
            ponovi_izbiro = False
        else:
            print(bes_napacna_izbira)

    if dejanje == 1:
        # Hočemo odpreti modra vrata, ampak so zaklenjena
        print(bes_s1_vrata)
        pin = input(bes_s1_vrata_input)
        if pin == pin_pravi:
            print(bes_s1_vrata_pravilen_pin)
            stopnja_opravljena = True
        else:
            print(bes_s1_vrata_napacen_pin)
        
    elif dejanje == 2:
        # Poglej na mizo. Na mizi je kladivo in zvezek.
        print(bes_s1_miza)

    else:
        # Napačna izbira dejanja
        # Sem ne bi smeli več priti
        print(bes_napacna_izbira)
        print('Resna napaka, končujem program.')
        break
