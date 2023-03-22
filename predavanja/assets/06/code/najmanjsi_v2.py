"""Primer: najmanjši
Izpišemo najmanjši element v seznamu naključnih števil
brez uporabe funkcij min() ali sort().
Izpišimo tudi indeks najmanjšega elementa.
"""
from random import sample

od = -100
do = 100
n  = 5

seznam = sample(range(od, do+1), n)

print('Seznam:', seznam)

# Trenutni najmanjši element mora biti nekaj zelo velikega! Neskončno?
najmanjsi = float('inf')
najmanjsi_indeks = 0

for i in range(len(seznam)):
    el = seznam[i]
    if el < najmanjsi:
        najmanjsi = el
        najmanjsi_indeks = i
print('Najmanjši element je', najmanjsi,
      'na indeksu', najmanjsi_indeks)