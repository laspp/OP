def pozdrav_vsem():
    print('Dober dan, vsi!')

def pozdrav(ime):
    # V glavnem programu večkrat kličemo to funkcijo.
    # Če bi rad spremenil pozdrav, to storim samo na enem mestu
    # v programu, kar je super!
    print('Dober dan,', ime)

def pozdrav_ura(ime, ura=12):
    # Upoštevamo del dneva
    if 5 <= ura < 9:
        print('Dobro jutro,', ime)
    elif 9 <= ura <= 17:
        print('Dober dan,', ime)
    else:
        print('Dober večer,', ime)

# Glavni del programa
pozdrav_vsem()

uporabnik = input('Kako ti je ime? ')
# Uporabimo funkcijo, ki izvede eno manjšo nalogo (podproblem)
pozdrav(uporabnik)

uporabnik2 = input('Je s tabo še kdo drug? ')
# Tokrat lahko uporabimo isto funkcijo kot prej, samo z drugimi podatki
pozdrav(uporabnik2)

uporabnik3 = input('Koga naj še pozdravim? ')
pozdrav_ura(uporabnik3)
ura = int(input('Aja, koliko pa je že ura? '))
pozdrav_ura(uporabnik3, ura)
# Ob klicu funkcije, lahko argumente tudi poimenujemo.
# Če uporabljamo imena, lahko vrstni red argumentov tudi mešamo.
pozdrav_ura('Ana')     # Dober dan, Ana
pozdrav_ura(ime='Ana') # Dober dan, Ana
pozdrav_ura('Ana', 7)  # Dobro jutro, Ana
pozdrav_ura(ura='7', ime='Ana') # Dobro jutro, Ana
pozdrav_ura('Ana', ura='23') # Dober večer, Ana