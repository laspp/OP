"""Evklidov algoritem

Vpeljava kompaktnega zapisa -=
"""

A = int(input('Vnesi A: '))
B = int(input('Vnesi B: '))
while A != B:
    if A > B:
        A -= B
    else:
        B -= A
print('Največji skupni delitelj:', A)