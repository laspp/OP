"""
Pobegni!
Pustolovska igra v slogu slavne sobe pobega

Avtor: FKKT letnik 2023
Verzija: 1.0
"""

# Pozdravno sporočilo
print("""
POBEGNI!

Znajdeš se v neznani sobi.
"Zakaj sem tu?" se sprašuješ.
Hočeš pobegniti.
""")

#------------------------------------
# Stopnja 1
pin_pravi = '2201'

print("""
Soba ima modra vrata.
Sredi sobe je miza in na njej nekaj.
""")

# Izbira akcije
print("""
Izberi eno od dejanj:
1. Odpri modra vrata.
2. Poglej, kaj je na mizi.
""")
dejanje = input('Izbira: ')

if dejanje == '1':
    # Hočemo odpreti modra vrata, ampak so zaklenjena
    print(
    """Modra vrata so zaklenjena z elektronsko ključavnico.
    """)
    pin = input('Vnesi PIN za odklep: ')
    if pin == pin_pravi:
        print('PIN je pravilen! Vrata so odklenjena.')
    else:
        print('Napačen PIN!')
    
elif dejanje == '2':
    # Poglej na mizo. Na mizi je kladivo in zvezek.
    print("""
Stopiš do mize, na kateri leži kladivo in
zaprašen zvezek. Odpreš zvezek in ven pade listič,
na katerem je zapisano:
      +~~~~~~~~~~~~~~~~~~~~~~~+
      |                       |
      |  "2"*2+str(0//3)+'1'  |
      |                       |
      +~~~~~~~~~~~~~~~~~~~~~~~+
""")
else:
    # Napačna izbira
    print('Napačna izbira!')
    # TODO: zopet vprašaj za izbiro
    
