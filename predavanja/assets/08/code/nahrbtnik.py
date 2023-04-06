"""Evidenca predmetov v nahrbtniku z njihovimi količinami"""

nahrbtnik = [
    ('signalna raketa', 2),
    ('mačeta', 1),
    ('proteinska ploščica', 5),
    ('zavoj robčkov', 1),
    ('rezervne nogavice', 0) # pravkar smo jih obuli
    ]

for predmet in nahrbtnik:
    print(predmet[0], ' (', predmet[1], '×)', sep='')
    
# Razpakiramo terko
for predmet in nahrbtnik:
    opis, kolicina = predmet
    print(opis, ' (', kolicina, '×)', sep='')

# Razpakiranje lahko naredimo že kar v glavi zanke `for`
for opis, kolicina in nahrbtnik:
    print(opis, ' (', kolicina, '×)', sep='')