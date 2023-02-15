"""Pretvornik enot

Program pretvarja vnešeno temperaturo 
iz stopinj Fahrenheita v stopinje Celzija.
"""
temp_F = input('Vnesi temperaturo v °F: ')
temp_F = float(temp_F) # Niz pretvorimo v število
temp_C = (temp_F - 32) / 1.8 # 1.8 = 9/5
print(temp_F,  '°F je',  temp_C,  '°C.') # Izpis