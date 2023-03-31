"""
Računanje povprečja števil v seznamu.
Napišemo lastno funkcijo. Razodetje!
Uvozimo tudi funkcijo iz modula `random`.
"""

from random import choices

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

# Izpišimo dokumentacijo funkcije
help(povprecje)
# Lahko tudi tako, da izpišemo lastnost __doc__, ki jo
# ima objekt z imenom `povprecje`
print(povprecje.__doc__)

# Uporabimo našo funkcijo
p = povprecje([1,2,3])
print(p)

# Uporabimo funkcijo še enkrat, tokrat na drugih podatkih
# Ustvarimo seznam 100 naključnih števil, ki nam predstavljajo premere
# prodnatih kamenčkov. Imamo granulacijo 4-8 mm.
premer = choices(range(4,9), k=100)

# Izračunamo povprečen premer zrn peska
print('Povprečni premer zrna peska:', povprecje(premer), 'mm')

