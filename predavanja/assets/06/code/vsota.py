"""Primer: vsota prvih n pozitivnih števil
Brez uporabe funkcije `sum()`.
"""
n = 20
vsota = 0
for i in range(1,n+1):
    vsota += i

print('Vsota prvih',
      n, 'pozitivnih števil je',
      vsota)
