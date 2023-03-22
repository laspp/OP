"""Šahovnica - premiki belega konja"""

# Velikost igralne plošče = število vrstic in stolpcev
n = int(input('Velikost šahovske plošče: '))

# Začetni položaj konja - izrisujemo samo to figuro
konj_polozaj = 'b1'

# Oznake polj: simbola za 'belo' in 'črno'
# https://en.wikipedia.org/wiki/Block_Elements
polje_oznaka = ['░░', '██']
konj_oznaka =   '× '

konec = False

while not konec:
    # Ustvarimo seznam vrstic, vsaka vrstica je seznam posameznih 
    # polj v vrstici.
    plosca = []
    for vrstica in range(n):
        # Prazen seznam za posamezno vrstico
        plosca.append([])
        for stolpec in range(n):
            # Če si zapišemo indekse posameznega polja in pogledamo sodost
            # indeksa vrstice in stolpca, opazimo ta vzorec:
            # če sta indeksa vrstice in stolpca bodisi oba soda
            # bodisi liha, je polje belo, sicer je črno.
            # Velja tudi: sodo + sodo = sodo = liho + liho
            # Torej, če je vsota indeksa vrstice in stolpca soda,
            # je polje belo.
            oznaka_i = (vrstica + stolpec) % 2
            polje = polje_oznaka[oznaka_i]
            plosca[vrstica].append(polje)

    # V seznam sedaj vstavimo konja na želeno pozicijo
    # Poiščimo pravi indeks vrstice in stolpca glede na položaj
    # Stolpec dobimo iz prvega znaka položaja, npr. 'b'. Zdaj moramo 'b'
    # preslikati v indeks drugega elementa v seznamu. Vemo tole:
    # ord('a') = 97
    # ord('b') = 98
    # ...
    # chr(97) = 'a'
    # Indeks 0 se torej preslika na 'a', ki ima vrednost 97.
    # Indeks 1 dobimo kot ord('b') - ord('a') = 98 - 97
    konj_stolpec = ord(konj_polozaj[0]) - ord('a')

    # Vrstico šahovnice pretvorimo v indeks vrstice v seznamu tako, da:
    # se 8 preslika v 0
    # in 1 v 7 (ter vse vmes).
    # Preprosto od n odštejemo oznako vrstice.
    konj_vrstica = n - int(konj_polozaj[1]) 
    plosca[konj_vrstica][konj_stolpec] = konj_oznaka

    # Izris plošče skupaj z oznakami
    for vrstica in range(n):
        # Najprej pride oznaka vrstice, začnemo z najvišjo:
        # v primeru plošče 8x8 je zgoraj 8. vrstica
        print(n-vrstica,'│', sep='', end='')
        
        for stolpec in range(n):
            print(plosca[vrstica][stolpec], sep='', end='')
        print()
        
    # Najprej ločevalna črta v svoji vrstici
    # Za simbole glej: https://en.wikipedia.org/wiki/Box-drawing_character
    print(' └' + '─'*n*2)
    # Nato zamik
    print(' ', end='')
    # In zatem izpis oznak stolpcev s črkami od 'a' naprej
    for stolpec in range(n):
        print(' ', chr(97+stolpec), sep='', end='')
    print()

    while True:
        konj_polozaj_nov = input('Vnesi nov položaj (npr. a3) ali X za izhod: ')
        if konj_polozaj_nov.upper() == 'X':
            konec = True
            break
        
        # Preverimo veljavnost tega premika:
        # veljavni so tisti premiki, pri katerih se:
        # - stolpec spremeni za 1 IN vrstica za 2 ALI
        # - stolpec spremeni za 2 IN vrstica za 1
        konj_stolpec_nov = ord(konj_polozaj_nov[0]) - ord('a')
        konj_vrstica_nov = n - int(konj_polozaj_nov[1])

        sprememba_stolpca = abs(konj_stolpec_nov - konj_stolpec)
        sprememba_vrstice = abs(konj_vrstica_nov - konj_vrstica)
        veljavna_poteza = (
            (sprememba_stolpca == 1 and sprememba_vrstice == 2 or
            sprememba_stolpca == 2 and sprememba_vrstice == 1) and
            0 <= konj_stolpec_nov < n and
            0 <= konj_vrstica_nov < n
            )
        if veljavna_poteza:
            konj_polozaj = konj_polozaj_nov
            break
        else:
            print('Neveljavna poteza, poskusi ponovno.')
