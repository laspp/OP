# Izpišimo vse šumnike v nizu
niz = 'Železni škafec pušča.'
for znak in niz:
    znak = znak.lower()
    if (znak == 'č' or
        znak == 'š' or
        znak == 'ž'):
        print(znak)