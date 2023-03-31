"""
Računanje povprečja števil v seznamu.
Brez uporabe funkcij.
Tudi funkciji print() smo se odpovedali, čista Šparta!
"""

seznam = [4, 8, 6]

if not seznam:
    p = None
else:
    vsota = 0
    dolzina = 0
    for el in seznam:
        vsota += el
        dolzina += 1
    p = vsota / dolzina
