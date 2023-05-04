"""Podobno kot v preglednica.py, tokrat z uporabo f-niza"""

podatki = [
    ('ime', 'št. ur', 'plačilo (€)'),
    ('Lojze', 40, 320),
    ('Elizabeta', 20, 160),
    ('Ana', 440, 3520)
]
# Širina enega stolpca v preglednici
s = 12
# Gremo po terkah v seznamu in jih odpakiramo
for i, (ime, ure, placa) in enumerate(podatki):
        
    # Za glavo tabele (indeks 0) pride črta
    if i == 0:
        niz = f'{ime:<{s}}{ure:^{s}}{placa:>{s}}'
        niz += '\n' + '-' * s * len(podatki[0])
    else:
        niz = f'{ime:<{s}}{ure:^{s}}{placa:>{s},.2f}'
    print(niz)
