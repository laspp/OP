"""Odštevajmo do vzleta

Želimo izpis:
3, 2, 1, vzlet!
"""

import time

sekund_do_vzleta = 3
while sekund_do_vzleta:
    print(
        sekund_do_vzleta,
        ', ',
        sep='',
        end=''
        )
    time.sleep(1)
    sekund_do_vzleta -= 1
print('vzlet!')