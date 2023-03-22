"""Izpišimo indekse vseh pojavitev iskanega elementa v seznamu."""

seznam = ['Ana', 'Ida', 'Ana', 'Eva']
iskan_el = 'Ana'

for i in range(len(seznam)):
    if iskan_el == seznam[i]:
        print(i)
        break
else:
    print('Elementa', iskan_el, 'ni v seznamu.')