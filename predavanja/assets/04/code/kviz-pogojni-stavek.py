# Kako to lepše napišemo? y = x > 2

x = 5 // 2
y = False
if x > 2:
    y = True


# Težji primer. Izpiše 'Vreme bo.'
# Kaj bi morali prirediti `vreme`, da se izvede else?

vreme = 'dez'
if vreme:
    print('Vreme bo.')
    if vreme == 'sonce':
        print('Piknik!')
elif vreme == 'dez':
    print('Deznik!')
else:
    print('Nema vremena.')

