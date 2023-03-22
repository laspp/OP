"""Vsi šumniki v nizu"""

niz = 'Železni škafec pušča.'

for znak in niz:
    znak_mali = znak.lower()
    
    # Kar je v oklepajih,
    # gre lahko preko več vrstic
    if (znak_mali == 'č' or
        znak_mali == 'š' or
        znak_mali == 'ž'):
        print(znak)