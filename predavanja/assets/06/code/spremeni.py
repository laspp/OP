"""Vsem nizom v seznamu dajmo veliko začetnico"""

imena = ['Ana', 'ida', 'eva', 'ada']

for ime in imena:
    ime.capitalize()
print(imena)

# Hm, ni šlo :( 
# Spremembo moramo še shraniti nazaj v seznam.
for i in range(len(imena)):
    imena[i] = imena[i].capitalize()
print(imena)

"""Kvadrirajmo vsa števila v seznamu"""

stevila = list(range(10))
print(stevila)
for i in range(len(stevila)):
    stevila[i] **=2
print(stevila)