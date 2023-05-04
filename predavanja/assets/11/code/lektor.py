def lektor(vhod):
    # 1. Odpravimo dvojne presledke.
    # Dvojni presledek nadomestimo z enojnim.
    # To ponavljamo, dokler ni več dvojnih presledkov.
    
    while vhod.find('  ') != -1:
        vhod = vhod.replace('  ', ' ')

    # 2. Popravimo veliko začetnico.
    # Niz razdelimo na povedi (uporabimo piko).
    povedi = vhod.split('.')
    # Pozor! Povedi sedaj nimajo več pike.

    for i, poved in enumerate(povedi):
        # Vsako poved najprej obtešemo z obeh strani
        poved = poved.strip()
        # Nato popravimo veliko začetnico.
        poved = poved.capitalize()
        povedi[i] = poved
    
    # Dodamo nazaj piko med povedi.
    izhod = '. '.join(povedi)

    # 3. Zamenjamo vse pojavitve podniza 'čuk' z 'veliki skovik'.
    # Kaj pa različni skloni? Lahko uporabimo slovar!
    # Kaj pa različne velikosti črk? Pazimo na to.
    slovar = {
        'čuk': 'veliki skovik',
        'čuka': 'velikega skovika',
        'čuku': 'velikemu skoviku',
        'čuka': 'velikega skovika',
        'čuku': 'velikem skoviku',
        'čukom': 'velikim skovikom'
    }

    for k, v in slovar.items():
        i = 0
        while True:

            i = izhod.lower().find(k, i)
            
            if i == -1:
                break
            
            vel_zac = False
            if izhod[i].isupper():
                vel_zac = True
        
            # Ali smo našli ujemanje cele beseda ali samo delno?
            # Preverimo znak, ki sledi besedi, če je znak abecede
            if izhod[i+len(k)].isalpha():
                # Iščemo sedaj od tu naprej
                i += 1
                continue

            # Preverimo še veliko začetnico
            if vel_zac:
                zamenjava = v.capitalize()
            else:
                zamenjava = v           
        
            # Vrinemo zamenjavo v niz
            izhod = izhod[:i] + zamenjava + izhod[i+len(k):]

            # Iščemo sedaj od tu naprej
            i += 1
      
    return izhod

besedilo = ' čuk je nočna ptica iz družine sov.\
med parjenjem slišimo čuka, kako spušča zvok \
»kiuh«,  ki se pojavlja    v kratkih intervalih. '

print(lektor(besedilo))

