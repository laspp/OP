"""
Napišimo funkcijo, ki sprejme dva niza in iz prvega izbriše vse
znake, ki se pojavijo v drugem.
"""

def radirka_niz(prvi, drugi):
    # Z zanko gremo čez drugi niz
    for i in drugi:
        # Brišemo vse pojavitve znaka i iz prvega niza
        prvi = prvi.replace(i,'')
    return prvi

def radirka_seznam(prvi, drugi):
    # Z zanko gremo čez drugi seznam
    for i in drugi:
        # Brišemo element i iz prvega, lahko jih je več
        while i in prvi:
            prvi.remove(i)

a = 'brokoli'
b = 'korenje'
r = radirka_niz(a, b)
print(a, b, r)

a = 'brokoli'
b = 'cvetaca'
r = radirka_niz(a, b)
print(a, b, r)

a = [1, 1, 2]
b = [1, 1, 3]
r = radirka_seznam(a, b)
print(a, b, r)
        