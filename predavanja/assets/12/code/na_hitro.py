"""Program prebere datoteko in izpiše njeno vsebino."""

# Pot do datoteke (relativna glede na pot programa)
pot = 'skrivnost/tajna/kolokvij-2.txt'
# Funkcija open vrne objekt, ki predstavlja tok podatkov.
# Če ne podamo drugih argumentov, bo datoteka odprta za branje.
datoteka = open(pot)
# Z metodo read() preberemo celotno vsebino datoteke v niz.
vsebina = datoteka.read()
# Izpišemo vsebino
print(vsebina)
# Zapremo datoteko
datoteka.close()