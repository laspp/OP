"""Indeks najmanjšega znaka v nizu"""

niz = '0123!čšž.ﻺ'
najmanjsi = niz[0]  # Dober trik! Ni nam potrebno izumljati
                    # "neskončno velikega znaka".
najmanjsi_indeks = 0

for i in range(len(niz)):
    if niz[i] < najmanjsi:
        najmanjsi = niz[i]
        najmanjsi_indeks = i

print('Najmanjši znak je "', najmanjsi,
      '" na indeksu ', najmanjsi_indeks, 
      '.', sep='')