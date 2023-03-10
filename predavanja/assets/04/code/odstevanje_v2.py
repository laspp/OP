"""Odštevalnik za rakete
Izbere naključno začetno število.
Uporablja modul, ki smo ga sami napisali.

Hočemo izpis oblike:
3, 2, 1, vzlet!
"""
import time
from random import randint
from odstevanje_modul import *

stevec = randint(izbira_od, izbira_do)

while stevec > 0:
    print(stevec, ', ', sep='', end='')
    stevec -= 1
    time.sleep(cas_spanja)
    
print('vzlet!')
