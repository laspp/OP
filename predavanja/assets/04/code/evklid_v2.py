"""Evklidov algoritem

Prikaz delovanja `while True` in `break`.
"""

A = int(input('Vnesi A: '))
B = int(input('Vnesi B: '))
while True:
    if A == B:
        break
    if A > B:
        A -= B
    else:
        B -= A
print('Največji skupni delitelj:', A)