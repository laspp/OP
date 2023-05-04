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
    print(
        ime.ljust(s),
        str(ure).center(s),
        str(placa).rjust(s),
        sep='')
    # Za glavo tabele (indeks 0) pride črta
    if i == 0:
        print('-' * s * len(podatki[0]))
