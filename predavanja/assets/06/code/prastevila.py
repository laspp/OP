"""Praštevila
Praštevilo je naravno število, ki ima točno dva pozitivna delitelja:
število 1 in samega sebe.
"""

# Preverimo, ali je podano število `n` praštevilo.
n = int(input('Vnesi število: '))

if n < 1:
    print('Število mora biti večje od 0.')
else:
    for i in range(2,n):
        # Če je n deljiv z i (ki gre od 2 do n-1),
        # potem n ni praštevilo.
        if n % i == 0:
            print(n, 'ni praštevilo.')
            break
    else:
        print(n, 'je praštevilo.')


print('Vsa praštevila do ', n,': ', end='', sep='')
for m in range(1,n+1):
    for i in range(2,m):
        if m % i == 0:
            break
    else:
        print(m,', ', sep='', end='')
print()

