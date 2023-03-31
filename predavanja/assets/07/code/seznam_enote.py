def izpisi_seznam_v1(s, enota, dodaj_indeks, uredi):
    """
    Izpiši elemente seznama `s`. Opcijsko lahko dodamo enoto, indeks
    elementa v seznamu oziroma seznam pred izpisom uredimo.
    
        Argumenti:
            s (list):    seznam
            enota (str): enota, ki jo izpišemo za elementom seznama
            dodaj_indeks (bool): če je True, pred elementom seznama
                         izpišemo njegov indeks, sicer ne
            uredi (int): 0 - ne urejamo, 1 - seznam pred izpisom uredimo
                         naraščajoče, -1 seznam uredimo padajoče
        
        Vrnjena vrednost:
            None
            
    """
    if not s:
        print('Seznam je prazen.')
        return
    
    if uredi == 1:
        s.sort()
    elif uredi == -1:
        s.sort(reverse=True)
    
    for i in range(len(s)):
        if dodaj_indeks:
            indeks = str(i)+': '
        else:
            indeks = ''
        
        print(indeks, s[i], ' ', enota, sep='')
        
def izpisi_seznam_v2(s, enota, dodaj_indeks, uredi):
    """
    Izpiši elemente seznama `s`. Opcijsko lahko dodamo enoto, indeks
    elementa v seznamu oziroma seznam pred izpisom uredimo.
    
        Argumenti:
            s (list):    seznam
            enota (str): enota, ki jo izpišemo za elementom seznama
            dodaj_indeks (bool): če je True, pred elementom seznama
                         izpišemo njegov indeks, sicer ne
            uredi (int): 0 - ne urejamo, 1 - seznam pred izpisom uredimo
                         naraščajoče, -1 seznam uredimo padajoče
        
        Vrnjena vrednost:
            None
            
    """
    if not s:
        print('Seznam je prazen.')
        return
    
    if uredi:
        s_urejen = uredi_seznam(s, uredi)
    else:
        s_urejen = s
    
    for i in range(len(s_urejen)):
        if dodaj_indeks:
            indeks = str(i)+': '
        else:
            indeks = ''
        
        print(indeks, s_urejen[i], ' ', enota, sep='')

def izpisi_seznam_v3(s, enota='', dodaj_indeks=False, uredi=0):
    """
    Izpiši elemente seznama `s`. Opcijsko lahko dodamo enoto, indeks
    elementa v seznamu oziroma seznam pred izpisom uredimo.
    
        Argumenti:
            s (list):    seznam
            enota (str): enota, ki jo izpišemo za elementom seznama
                         privzeto je prazen niz ''
            dodaj_indeks (bool): če je True, pred elementom seznama
                         izpišemo njegov indeks, sicer ne (privzeto)
            uredi (int): 0 - ne urejamo (privzeto),
                         1 - seznam pred izpisom uredimo naraščajoče,
                        -1 - seznam uredimo padajoče
        
        Vrnjena vrednost:
            None
            
    """
    if not s:
        print('Seznam je prazen.')
        return
    
    if uredi:
        s_urejen = uredi_seznam(s, uredi)
    else:
        s_urejen = s
    
    for i in range(len(s_urejen)):
        if dodaj_indeks:
            indeks = str(i)+': '
        else:
            indeks = ''
        
        print(indeks, s_urejen[i], ' ', enota, sep='')

def uredi_seznam(s, smer):
    if smer == -1:
        padajoce = True
    else:
        padajoce = False
    s_kopija = s.copy()
    s_kopija.sort(reverse=padajoce)
    return s_kopija

meti = [20, 40, 30]

izpisi_seznam_v1(meti, '', False, 0)
print('-'*20)
# Argumente lahko poimenujemo in menjamo vrstni red
# Najprej pridejo tisti argumenti, ki jim ne damo imena (položajni),
# sledijo tisti z imeni, ki so lahko v poljubnem vrstnem redu
izpisi_seznam_v1(meti, dodaj_indeks=False, enota='', uredi=0)
# Tole ne gre:
# izpisi_seznam_v1(dodaj_indeks=False, meti, enota='', uredi=0)

izpisi_seznam_v1(meti, 'm', True, 0)
print('-'*20)
izpisi_seznam_v1(meti, 'm', True, 1)
print('-'*20)
izpisi_seznam_v1(meti, 'm', True, -1)
print('-'*20)
print(meti)
# POZOR!!! Funkcija je spremenila vrstni red v seznamu
meti = [20, 40, 30]
izpisi_seznam_v2(meti, 'm', True, -1)
print('-'*20)
print(meti)

# Uporabimo privzete vrednosti
izpisi_seznam_v3(meti)
print('-'*20)
izpisi_seznam_v3(meti, 'm', True)
print('-'*20)
izpisi_seznam_v3(meti, 'm', True, 1)
print('-'*20)
izpisi_seznam_v3(meti, 'm', True, -1)
print('-'*20)
print(meti)

# Uporabimo privzete vrednosti
izpisi_seznam_v3(meti)
print('-'*20)
izpisi_seznam_v3(meti, 'm')
print('-'*20)
izpisi_seznam_v3(meti, 'm', True)
print('-'*20)
izpisi_seznam_v3(meti, 'm', False, -1)
print('-'*20)
print(meti)
