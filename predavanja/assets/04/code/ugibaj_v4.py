"""Igra ugibanja števil

Program v Scratchu smo prepisali v Python:
https://scratch.mit.edu/projects/815241970
"""

from random import randint
from time import perf_counter

start = 20
stop  = 30
print('Izbral sem si število med ', start, ' in ', stop, '.', sep='')
izbrano_stevilo = randint(start, stop)
tic = perf_counter()
odgovor = int(input('Ajde, ugibaj, katero: '))
poskus = 1
while odgovor != izbrano_stevilo:
    print('Ah, kje pa, nimaš pojma.')
    if poskus >= 5:
        print('Zmanjkalo ti je poskusov :(')
        break
    odgovor = int(input('Poskusi ponovno: '))
    poskus += 1
else:
    print('Bravo!')
print('Izbral sem število', izbrano_stevilo)
toc = perf_counter()
print('Čas igranja:', round(toc-tic), 'sekund.')