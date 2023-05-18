'''
Pridobimo podatke o vremenu iz https://open-meteo.com/
Gre za javen in brezplačen strežnik, ki ponuja aktualne in arhivske
vremenske podatke za celoten planet preko svojega aplikacijskega
programskega vmesnika (ang. application programming interface - API).

Podatke pridobimo z uporabo modula `requests`.
'''

import requests
import json
from datetime import datetime

# Končna točka za API
url = 'https://api.open-meteo.com/v1/forecast'
# Parametri naše poizvedbe
params = {
    'latitude': 46.0569,    # zemlj. širina za Ljubljano
    'longitude': 14.5058,   # zemlj. dolžina za Ljubljano
    'hourly': 'temperature_2m,precipitation_probability',
    'forecast_days': 1,     # napoved za toliko dni
    'timezone': 'Europe/Ljubljana'  # časovni pas
}

# Pošljemo zahtevek na strežnik in dobimo odgovor
odgovor = requests.get(url, params=params)

# Preverimo uspešnost odgovora (koda 200 pomeni OK)
if odgovor.status_code == 200:
    # Iz odgovora izluščimo podatke, ki so v obliki JSON
    podatki = odgovor.json()
    # Zapišemo podatke v datoteko
    with open('vreme.json', 'w') as f:
        json.dump(podatki, f, indent=4)
    
    # Izluščimo za nas zanimive podatke
    cas = podatki['hourly']['time']
    temperatura = podatki['hourly']['temperature_2m']
    padavine = podatki['hourly']['precipitation_probability']
    
    # Izpis
    print('Vremenska napoved za Ljubljano')
    for c, t, p in zip(cas, temperatura, padavine):
        casovni_zig = datetime.fromisoformat(c)
        cas_lep = casovni_zig.strftime("%d. %m. %Y, %H:%M")
        print(f'{cas_lep}: {t:>4} °C, padavine: {p:>3} %')
else:
    print('Prišlo je do napake pri pridobivanju podatkov iz {url}.')
