"""
Izris grafa temperature in verjetnosti za padavine na podlagi podatkov 
o vremenu, pridobljenih s programom `vreme.py`
"""

import json
from matplotlib import pyplot as plt
from datetime import datetime
import locale

# Pot do datoteke JSON z vremenskimi podatki
pot = '../2-API-JSON/vreme.json'

with open(pot, mode='r', encoding='utf8') as datoteka:
    podatki = json.load(datoteka)

locale.setlocale(locale.LC_ALL, 'sl_SI.UTF-8')

cas = podatki['hourly']['time']
cas_lepse = [datetime.fromisoformat(t).strftime("%A %H:%M") for t in cas]
temp = podatki['hourly']['temperature_2m']
padavine = podatki['hourly']['precipitation_probability']


# Enojna y-os
# plt.plot(cas_lepse, temp, linestyle='-', marker='o')
# plt.xlabel('čas')
# plt.ylabel('temperatura (°C)')
# plt.title(f'Napoved temperatur')
# fig.autofmt_xdate(rotation=45)
# plt.tight_layout()
# plt.show()

# Dvojna y-os: temperatura in padavine
fig, ax1 = plt.subplots()

# Narišemo temperaturo na prvo (levo) y-os
ax1.plot(cas_lepse, temp, marker='o', linestyle='-', color='tab:red')
ax1.set_xlabel('čas')
ax1.set_ylabel('temperatura [°C]', color='tab:red')

# Naredimo drugo y-os (desno) za padavine
ax2 = ax1.twinx()
ax2.bar(cas_lepse, padavine, color='tab:blue', alpha=0.4)
ax2.set_ylabel('padavine [%]', color='tab:blue')

# Skupne lastnosti grafa
plt.title(f'Napoved temperature in padavin')
fig.autofmt_xdate(rotation=45)
fig.legend(['Temp.', 'Verj. padavin'])

# Shranimo v datoteko
plt.savefig("vreme.pdf", format="pdf")

# Prikažemo
plt.show()


