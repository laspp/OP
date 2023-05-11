"""
Program za pretvorbo oblike zapisa jedilnika:
izvorna datoteka je v formatu CSV in
ima za vsako jed v dnevu svojo vrstico.
Želimo imeti bolj berljiv jedilnik, primeren za objavo.
"""

def polepsaj_datum(datum):
    """Odstranimo ničle in naredimo presledek za piko"""
    # 02.05.2023 -> 2. 5. 2023
    dan, mesec, leto = datum.split('.')
    dan = int(dan)
    mesec = int(mesec)
    
    return f'{dan}. {mesec}. {leto}'
    

def dodaj_jed_dnevu(jedilnik, datum, jed):
    if datum in jedilnik:
        jedilnik[datum].append(jed)
    else:
        jedilnik[datum] = [jed]

def preberi_jedilnik(pot):
    """Preberemo meni iz datoteke in ga vrnemo kot slovar"""
    jedilnik = {}
    with open(pot, mode='r', encoding='utf8') as datoteka:
        for vrstica in datoteka:
            # Obtešemo vrstico z obeh strani
            vrstica = vrstica.strip()
            # vrstica je sestavljena iz dveh podatkov, ločenih z vejico
            # datum,jed
            datum, jed = vrstica.split(',')
            dodaj_jed_dnevu(jedilnik, datum, jed)
    
    return jedilnik
            
def zapisi_jedilnik(jedilnik, pot, prepisi=False):
    """V datoteko zapisemo jedilnik, ki je podan kot slovar"""
    nacin = 'a'
    if prepisi:
        nacin = 'w'
    
    datum_od = min(jedilnik.keys())
    datum_do = max(jedilnik.keys())
    
    niz = f'Jedilnik od {polepsaj_datum(datum_od)} \
do {polepsaj_datum(datum_do)}\n\n'
        
    for datum, seznam_jedi in jedilnik.items():
        niz += f'{polepsaj_datum(datum)}\n'
        for jed in seznam_jedi:
            niz += f'  - {jed}\n'
        niz += '\n'
    
    with open(pot, mode=nacin, encoding='utf8') as datoteka:
        
        
            datoteka.write(niz)

pot_meni_vhod = 'jedilnik.csv'
pot_meni_izhod = 'jedilnik.txt'
jedilnik = preberi_jedilnik(pot_meni_vhod)
zapisi_jedilnik(jedilnik, pot_meni_izhod, prepisi=True)

