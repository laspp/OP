"""Program prebere datoteko in izpiše njeno vsebino."""

pot = 'skrivnost/tajna/kolokvij-2.txt'

# Uporabimo stavek with
with open(pot) as datoteka:
    vsebina = datoteka.read()
    print(vsebina)
# Ko se konča zgornji blok, se datoteka samodejno zapre