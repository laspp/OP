"""Program za izpis prvih nekaj bajtov datoteke"""

datoteke = [
    'kolokvij-2.txt',
    '../psst/rotating_earth.gif'
    ]

st_bajtov = 12

for datoteka in datoteke:
    print(datoteka + '\n' + '-'*30)
    with open(datoteka, mode='rb') as f:
        vsebina = f.read()[:st_bajtov]
        
        print('Tako je zapisano v shrambi (dvojiško):')
        bin_str = [bin(bajt)[2:].zfill(8) for bajt in vsebina]
        bin_join = ' '.join(bin_str)
        print(bin_join)
        
        print('\nTako je zapisano v shrambi (šestnajstiško):')
        hex_str = [hex(bajt)[2:].zfill(2) for bajt in vsebina]
        hex_join = ' '.join(hex_str)
        print(hex_join)
        
        print('\nTako je zapisano v shrambi (desetiško):')
        dec_str = [str(bajt) for bajt in vsebina]
        dec_join = ' '.join(dec_str)
        print(dec_join)
        
        print('\nPretvorba v znake:')
        print(vsebina)
        
    print()