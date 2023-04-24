"""Uporabimo slovar za slovensko-angleški slovar"""

s = {
    'jabolko': 'apple',
    'hruška': 'pear'
    }

original = 'jabolko'
prevod = s[original]
print(original, 'je', prevod)

original = 'češnja'
if original in s:
    prevod = s[original]
else:
    prevod = None
# ali:
prevod = s.get(original, None)
print(original, 'je', prevod)
