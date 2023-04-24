"""Napravimo slovensko-angleški slovar, uporabimo seznam terk."""

s = [
    ('jabolko', 'apple'),
    ('hruška', 'pear')
    ]

original = 'jabolko'
prevod = None
for slo, eng in s:
    if original == slo:
        prevod = eng

print(prevod)
