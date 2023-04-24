def izpisi_shrambo(s):
    print('Shramba:')
    if not s:
        print('prazna')
        return
    for zivilo, kolicina in s.items():
        print('  ', zivilo, ': ', kolicina, 'x', sep='')

def preveri_zivilo(shramba, zivilo):
    if zivilo in shramba:
        return shramba[zivilo]
    else:
        return 'Živila ' + zivilo + ' ni v shrambi.'
    
    # Z uporabo metode get():
    # return shramba.get(zivilo, 'Živila ' + zivilo + ' ni v shrambi.')

def dodaj_zivilo(shramba, zivilo, kolicina=1):
    if zivilo in shramba:
        # kljuc zivilo že obstaja
        shramba[zivilo] += kolicina
    else:
        # kljuc se ne obstaja
        shramba[zivilo] = kolicina

def porabi_zivilo(shramba, zivilo, kolicina=1):
    # Preverimo zalogo živila. Če ga ni, dobimo niz.
    zaloga = preveri_zivilo(shramba, zivilo)
    if type(zaloga) is not str:
        # Če smo želeli porabiti več kot imamo,
        # se omejimo na toliko, kolikor imamo.
        if kolicina > zaloga:
            kolicina = zaloga
        # Če porabimo vso zalogo, izbrišemo živilo.
        if kolicina == zaloga:
            del shramba[zivilo]
        # Sicer pa zgolj zmanjšamo količino živila.
        else:
            shramba[zivilo] -= kolicina

def dodaj_zivila(shramba, zivila, kolicine=None):
    if kolicine == None:
        kolicine = [1]*len(zivila)
        
    for z,k in zip(zivila,kolicine):
        dodaj_zivilo(shramba, z, k)
    
def dobi_vrednost(item):
    return item[1]

def uredi(shramba, po_kolicini=False, padajoce=False):
    if po_kolicini:
        s = sorted(shramba.items(), key=dobi_vrednost, reverse=padajoce)
    else:
        s = sorted(shramba.items(), reverse=padajoce)
    return s



shramba = {}
izpisi_shrambo(shramba)

dodaj_zivilo(shramba, 'banana')
izpisi_shrambo(shramba)
dodaj_zivilo(shramba, 'banana', 3)
izpisi_shrambo(shramba)

zivila = ['banana', 'sir', 'kruh']
kolicine = [10, 3, 5]
dodaj_zivila(shramba, zivila, kolicine)
izpisi_shrambo(shramba)

porabi_zivilo(shramba, 'kruh')
izpisi_shrambo(shramba)
porabi_zivilo(shramba, 'kruh', 10)
izpisi_shrambo(shramba)

shramba = {'banana': 4, 'mleko': 12, 'ananas': 5}
print(uredi(shramba))
print(uredi(shramba, po_kolicini=True))
print(uredi(shramba, po_kolicini=True, padajoce=True))