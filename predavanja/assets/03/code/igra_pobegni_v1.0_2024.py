# To je naša super igra pobega
# Verzija 1.0
# FKKT letnik 2024

# Tukaj so moje skrivnosti
PIN_pravilen = '2201'


# Začetek igre

print('''IGRA POBEGA!
Znajdeš se v sobi, ki ima samo ena
modra vrata in mizo na sredi.''')

print('''
AKCIJE:
1: Odpri modra vrata.
2: Poglej, kaj je na mizi.''')

akcija = input('Tvoja izbira? ')

if akcija == '1':
    print('Prideš do modrih vrat, ki pa so zaklenjena.')
    PIN = input('Vnesi PIN: ')
    
    if PIN == PIN_pravilen:
        print('PIN je pravilen! Vrata se odklenejo in stopiš v ....')
        
    else:
        print('PIN je napačen!')    
    
elif akcija == '2':
    print('''Na mizi zagledaš tole:
    "2"*2+str(0//3)+'1' ''')
    
else:
    print('Zadela te je strela, izgubiš vsa življenja, pojdi se solit.')
    
print('KONEC IGRE!')
