"""Praštevila
Praštevilo je naravno število, ki ima točno dva pozitivna delitelja:
število 1 in samega sebe.
"""


def je_prastevilo(x):
    """Preverimo, ali je število `x` praštevilo."""
    
    if x < 1:
        print('Število mora biti večje od 0.')
        return False
    
    for i in range(2,x):
        # Če je x deljiv z i (ki gre od 2 do x-1),
        # potem x ni praštevilo.
        if x % i == 0:
            # Ni praštevilo
            return False
    else:
        # Sem pridemo, ko se zanka konča,
        # kar pomeni, da x je praštevilo (sicer bi že prej klicali return)
        return True

def izpisi_prastevila():
    """Izpiše vsa praštevila do n, ki je definiran globalno"""
    print('Vsa praštevila do', n)
    for m in range(1, n+1):
        if je_prastevilo(m):
            print(m)

n = int(input('Vnesi število n: '))
# Funkcija ne sprejme argumentov. Predpostavlja, da je
# meja za izračun praštevil poimenovana `n` in je globalna.
izpisi_prastevila()



