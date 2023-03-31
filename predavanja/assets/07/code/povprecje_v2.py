"""
Računanje povprečja števil v seznamu.
Uporaba vgrajenih funkcij. Olajšanje!
"""

seznam = [4, 8, 6]

if not seznam:
    p = None
else:
    p = sum(seznam) / len(seznam)
    
print(p)

