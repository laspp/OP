"""Evklidov algoritem

Prikaz delovanja `while` + `else` + `break`.
"""

A = int(input('Vnesi A: '))
B = int(input('Vnesi B: '))
while A != B:
    if A < 0 or B < 0:
        print('Ne znam z negativnimi števili.')
        break
    if A > B:
        A -= B
    else:
        B -= A
else:
    print('Največji skupni delitelj:', A)