"""Primer: najmanjši
Izpišemo najmanjši element v seznamu naključnih števil
brez uporabe funkcij min() ali sort().
"""

import random
import math

od = -100
do = 100
n  = 5

seznam = []
for i in range(n):
   seznam.append(random.randint(od,do))

# Namesto zanke bi lahko uporabili funkcijo random.sample().
# Funkcija sample iz seznama (prvi argument) izbere toliko naključnih
# elementov, kolikor je njen drugi argument.
# seznam = random.sample(range(od, do+1), n)

print('Seznam:', seznam)

# Trenutni najmanjši element mora biti nekaj zelo velikega! Neskončno?
najmanjsi = math.inf
# Namesto uvoza modula `math` bi lahko uporabili tudi float('inf')

for el in seznam:
    if el < najmanjsi:
        najmanjsi = el
print('Najmanjši element je', najmanjsi)