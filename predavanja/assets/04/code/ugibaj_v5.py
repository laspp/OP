"""Igra ugibanja števil

Uporabimo svoj modul.
"""

from random import randint
from time import perf_counter
import ugibaj_modul as ug

print(ug.bes_uvod)
izbrano_stevilo = randint(ug.start, ug.stop)
tic = perf_counter()
odgovor = int(input(ug.bes_poziv))
poskus = 1
while odgovor != izbrano_stevilo:
    print(ug.bes_napacno)
    if poskus >= ug.maks_poskusov:
        print(ug.bes_konec_poskusov)
        break
    odgovor = int(input(ug.bes_poziv_spet))
    poskus += 1
else:
    print(ug.bes_bravo)
print(ug.bes_resitev, izbrano_stevilo)
cas = str(round(perf_counter() - tic))
cas_izpis = ug.bes_cas.replace('???', cas)
print(cas_izpis)