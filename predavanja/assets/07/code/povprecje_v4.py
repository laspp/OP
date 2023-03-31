"""
Računanje povprečja števil v seznamu.
Dodamo še funkcijo za računanje prostornine in jo uporabimo na seznamu
premerov prodnatih kamenčkov.
"""

from random import choices
from math import pi

def povprecje(seznam):
    """
    Sprejme seznam števil in vrne njihovo povprečje.
    
        Argumenti:
            seznam (list): seznam števil
        
        Vrnjena vrednost:
            povprecje (float): povprečje števil v seznamu `seznam`
    """
    # Zgoraj smo med tremi narekovaji napisali dokumentacijo funkcije,
    # torej, navodila za uporabo (t. i. docstring).
    # Do teh navodil pridemo tako:
    # help(povprecje)
    # ali
    # print(povprecje.__doc__)
    
    if not seznam:
        # return pomeni 'vrni' in tukaj se izvajanje funkcije konča
        return None
    
    vsota = 0
    dolzina = 0
    for el in seznam:
        vsota += el
        dolzina += 1
    # Lahko damo tako ime? Lahko, ker je lokalno - vidno samo v okviru
    # te funkcije. Navzven (globalno) ime 'povprecje' pomeni funkcijo.
    povprecje = vsota / dolzina
    return povprecje

def prostornina(premer):
    # Uporabnik lahko kot vhod da eno samo število ali pa seznam
    # Če je premer tipa int ali float, ga pretvorimo v seznam
    samo_en = False
    if type(premer) is int or type(premer) is float:
        premer = [premer]
        samo_en = True
    if type(premer) is not list:
        print('Vhodni argument premer je lahko število ali seznam števil.')
        return None
    
    # Računanje prostornine
    # V = (4/3)*π*r**3 = (4/3)*π*(d**3/8) = (π*d**3)/6
    V = []
    for d in premer:
        vol = (pi * d**3) / 6
        V.append(vol)
    # Če je bil vhodni argument samo število, vrnemo tudi samo število
    if samo_en:
        return V[0]
    else:
        return V

# Uporabimo funkcijo še enkrat, tokrat na drugih podatkih
# Ustvarimo seznam 100 naključnih števil, ki nam predstavljajo premere
# prodnatih kamenčkov. Imamo granulacijo 4-8 mm.
premer = choices(range(4,9), k=100)

# Izračunamo povprečen premer zrn peska
povpr_premer = povprecje(premer)
print('Povprečni premer zrna peska:', povpr_premer, 'mm')

# Izračunamo povprečno prostornino zrnc peska
povpr_prostor_zrna = povprecje(prostornina(premer))
print('Povprečna prostornina zrna peska:', povpr_prostor_zrna, 'mm3')

premer_maks = max(premer)
print('Največji premer zrna peska:', premer_maks, 'mm')
print('Prostornina zrna z največjim premerom:', prostornina(premer_maks), 'mm3')

