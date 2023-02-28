"""
Pobegni!
Pustolovska igra v slogu sobe pobega

Verzija: 1.0
"""

# Uvodno sporočilo
print('''Znajdeš se v neznani sobi. 
Boli te glava, pogled je meglen. 
Ne veš, kaj počneš tu. Veš pa, da je pobeg tvoja edina rešitev.''')

# Stopnja 1
print('''
Soba nima oken, ima pa modro pobarvana vrata.
Sredi sobe je miza in nekaj na njej.''')

vrata_PIN_pravi = '2201'

# Izbira dejanja
dejanje_1 = 'Odpri modra vrata.'
dejanje_2 = 'Poglej, kaj je na mizi.'
print('')
print('Izberi eno od možnosti:')
print('1:', dejanje_1)
print('2:', dejanje_2)
dejanje = input('Izbira: ')

if dejanje == '1':
    # Novo vrstico lahko naredimo tudi z \n
    print('\nModra vrata so zaklenjena z elektronsko ključavnico.')
    vrata_PIN = input('Vnesi PIN za odklep: ')
    if vrata_PIN == vrata_PIN_pravi:
        print('Vneseni PIN je pravilen! Vrata so odklenjena.')
        # TODO: naslednja stopnja!
    else:
        print('Napačen PIN!')
        # TODO: ponovno prikaži seznam izbir
if dejanje == '2':
    print('''
Stopiš do mize, na kateri leži zaprašen zvezek.
Odpreš ga in na tvoje presenečenje iz njega pade listič z napisom:
            +~~~~~~~~~~~~~~~~~~~~~~+
            |                      |
            | "2"*2+str(0//3)+'1'  |
            |                      |
            +~~~~~~~~~~~~~~~~~~~~~~+
''')

# Namesto tega raje narediš if-elif-else:
# if dejanje == '1':
# elif dejanje == '2':
# else:
if dejanje != '1' and dejanje != '2':
    print('Napačna izbira!')
    #TODO: omogočiti ponovni vnos izbire dokler ni veljavna
        
    