"""
Pretvornik enot °F -> °C
"""

# Vprašaj uporabnika za temperaturo
temp_F = input('Vnesi temperaturo v °F: ')
temp_F = float(temp_F)
# Pretvori
temp_C = (temp_F - 32) / 1.8
# Izpiši
izpis = str(temp_F) + '°F je ' + str(round(temp_C)) + '°C.'
print(izpis)
print(temp_F, '°F je ', round(temp_C), '°C.', sep='')
