# Kviz

"""
1. Imamo seznam seznamov. Kako naslovimo belega konja?
Odgovori:
 ✓ plosca[3][1]
    plosca[1][3]
    plosca[3,1]
    'b1'
"""

plosca = [
    ['♜','♞','♝','♛'],
    ['♟','♟','♟','♟'],
    ['♙','♙','♙','♙'],
    ['♖','♘','♗','♕'],
    ]

# print(plosca[3][1])

"""
2. Isti seznam kot prej. Radi bi dobili seznam vseh črnih kmetov? Kateri izraz NI pravilen?
Odgovori:
    plosca[1]
    plosca[1][:]
    plosca[1][:4]
 ✓ plosca[1][1:4]
"""

print(plosca[1])
print(plosca[1][:])
print(plosca[1][:4])
print(plosca[1][1:4])

"""
3. Kaj izpiše program?
Odgovori:
    Črne kmete
    Bele kmete
    Črne in bele kmete
 ✓ Vse figure razen kmetov
"""

plosca = [
    ['♜','♞','♝','♛'],
    ['♟','♟','♟','♟'],
    ['♙','♙','♙','♙'],
    ['♖','♘','♗','♕'],
    ]

for i in range(len(plosca)):
    if 0 < i < 3:
        continue
    print(plosca[i])
    

"""
4. Kaj vrne funkcija na sliki?
Odgovori:
    Niz 'Hej!'
 ✓ None
    True
"""

def pozdrav():
    print('Hej!')
    
"""
5. Kaj izpiše program na sliki?
Odgovori:
    2
 ✓ 4
    6
    pride do napake
"""

def xyz(x, y=2, z=3):
    r = x + y + z
    return r

a = xyz(y=0, x=1)
print(a)
