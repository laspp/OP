---
title: Funkcije
exportFilename: OP-07-Funkcije.pdf
download: false
info: Predavanja pri predmetu Osnove programiranja
theme: default
themeConfig:
  primary: #e54240
background: false
class: text-center
highlighter: shiki
lineNumbers: false
drawings:
  enabled: true
  persist: false
  presenterOnly: false
  syncAll: false
transition: fade-out
css: unocss
favicon: favicon.png
layout: cover
fonts:
  sans: Roboto
  serif: Roboto Slab
  mono: Fira Code
---

<!-- 
1. Spremeni `vite.config.ts`, da publicDir kaže na ustrezno mapo gradiva za predavanje 
    publicDir: './assets/06'
   Popravi ProgressBar completed na ustrezno številko predavanja
2. npx slidev OP-07-Funkcije.md
3. npx slidev --remote=geslo OP-07-Funkcije.md 
  če si presenter, potem uporabi url, ki ima notri ?password=geslo, da te ne gnjavi za vpis gesla
4. npx slidev build --out dist/04 OP-07-Funkcije.md
5. npx slidev export OP-07-Funkcije.md
6. gswin64 -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/printer -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf OP-07-Funkcije.pdf
7. move output.pdf OP-07-Funkcije.pdf
-->

<ProgressBar bgcolor="#e54240" completed="7" total="13"/>

# {{ $slidev.configs.title }}

Osnove programiranja

Nejc Ilc

<div class="abs-b m-6 flex gap-1 items-center justify-end text-red-500">
  <div><mdi-map-marker/> R2.41</div>
  <a class="text-2xl icon-btn !border-none !hover:text-gray"
  href="https://fri.uni-lj.si/sl/o-fakulteti/osebje/nejc-ilc">
    <mdi-web-box/>
  </a>
  <a class="text-2xl icon-btn !border-none !hover:text-gray"
  href="mailto:nejc.ilc@fri.uni-lj.si?subject=[OP-FKKT] ">
    <mdi-email/>
  </a>
  <a href="https://github.com/laspp/OP/tree/master/predavanja" target="_blank"
    alt="OP GitHub repository"
    class="text-2xl icon-btn !border-none !hover:text-gray">
    <carbon-logo-github />
  </a>
</div>

---
layout: image
image: '/img/ula-kuzma-LpBFnmP0A_s-unsplash.jpg'
caption: 'Fotografija: Ula Kuźma'
url: 'https://unsplash.com/photos/LpBFnmP0A_s'
---

<div class="text-shadow-xl">

<div v-click>

# Eleganca kode
Zakaj potrebujemo funkcije?

- razkosanje kompleksnega problema na lažje odvladljive podprobleme
- ponovna uporaba delov kode na različnih mestih programa
- del kode zapremo v "črno škatlo" in jo ponudimo drugim za uporabo
- preglednost, eleganca programa

</div>
</div>

---
layout: two-cols
class: code-lg
---

# Sintaksa <mdi-signal-cellular1/>
Osnovna definicija funkcije

```python
def ime_funkcije():
    stavek_1
    ...
    stavek_n
```

- Funkcijo definiramo z rezervirano besedo `def`.
- Funkciji damo kakšno lepo ime. Gotovo kaj bolj spevnega kot `ime_funkcije`.
- Okrogli oklepaji za imenom so obvezni.
- Prav tako dvopičje.
- V telesu funkcije napišemo zaporedje stavkov, ki naj se izvedejo, ko to funkcijo pokličemo.

::right::

# Primer
Pozdravimo publiko

```python
def pozdrav_vsem():
    print('Dober dan, vsi!')

# Glavni del programa
pozdrav_vsem()
```

Kaj se dogaja ob zagonu programa?

1. Python prebere definicijo funkcije (prvi dve vrstici), vendar je ne izvede.
2. Preskoči komentar in izvede stavek, ki pokliče funkcijo `pozdrav_vsem()`.
3. Vstopimo v funkcijo, ki izpiše `Dober dan, vsi!`. 
4. Funkcija se zaključi in prav tako program.

---
layout: two-cols
class: code-lg
---

# Sintaksa <mdi-signal-cellular2/>
V definicijo funkcije dodajmo argumente

```python
def ime_funkcije(arg1,..., argN):
    stavek_1
    ...
    stavek_n
```

- Funkcija lahko sprejme argumente. To so spremenljivke, ki smo jih zgoraj poimenovali `arg1` do `argN`.
- Argumente lahko uporabimo v stavkih znotraj funkcije.

::right::

# Primer <Marker>pozdravcek</Marker>
Pozdravimo konkretno osebo

```python
def pozdrav(ime):
    print('Dober dan,', ime)

pozdrav('Ana')
```

1. Definicija funkcije `pozdrav()` pravi, da funkcija potrebuje en argument, ki ima splošno ime `ime`.
2. Ob klicu funkcije moramo zato določiti ta argument. Odločili smo se za vrednost `'Ana'`.
3. Ko vstopimo v funkcijo, spremenljivka `ime` dobi vrednost `'Ana'` in izpiše:  
   `Dober dan, Ana`.

---
layout: two-cols
class: code-lg
---

# Sintaksa <mdi-signal-cellular3/>
Argumenti imajo lahko privzete vrednosti.

```python
def ime_funkcije(arg1, arg2=dfl):
    stavek_1
    ...
    stavek_n
```

- Argumenti funkcije so lahko opcijski, se pravi, da imajo že neko privzeto vrednost. Če pri klicu funkcije določimo vrednost argumenta, se privzeta vrednost ne upošteva.
- Zgoraj je argument `arg1` obvezen - ob klicu funkcije ga moramo določiti.
- Argument `arg2` je opcijski, ob klicu dobi vrednost `dfl`, razen, če smo v klicu funkcije določili drugače.

::right::

# Primer <Marker>pozdravcek</Marker>
Pozdrav prilagodimo uri

```python
def pozdrav_ura(ime, ura=12):
    if 5 <= ura < 9:
        print('Dobro jutro,', ime)
    elif 9 <= ura <= 17:
        print('Dober dan,', ime)
    else:
        print('Dober večer,', ime)

pozdrav_ura('Ana')    # Dober dan, Ana
pozdrav_ura(ime='Ana')
pozdrav_ura('Ana', 7) # Dobro jutro, Ana
pozdrav_ura(ura='7', ime='Ana')


```

Ob klicu funkcije lahko argumente poimenujemo. Če uporabljamo imena, lahko vrstni red argumentov tudi mešamo.

---
layout: two-cols
---

# Sintaksa <mdi-signal-cellular3/>+
Funkcija vrne rezultat

<div class="code-lg">

```python
def ime_funkcije(arg1, arg2=dfl):
    stavek_1
    ...
    stavek_n
    return <vrednost>
```

</div>

- Funkcija se konča, ko:
  - izvede vse stavke v telesu ali
  - ko pride do stavka `return`.
- `return` je podoben `break`, ki prekine zanko
- Funkcija vedno nekaj vrne.
- Če napišemo samo `return` ali če ga sploh ne omenjamo, bo funkcija vrnila `None`. Če napišemo `return vrednost`, bo vrnila `vrednost`.

::right::

# Primer <Marker>ploscina</Marker>
Izračunajmo ploščino likov

```python
from math import pi

def ploscina_kvadrat(a):
    s = a*a
    return s

def ploscina_krog(r):
    s = pi * r**2
    return s

def ploscina(x, lik):
    if lik == 'kvadrat':
        # U, funkcija kliče drugo funkcijo!
        return ploscina_kvadrat(x)
    elif lik == 'krog':
        return ploscina_krog(x)
    else:
        print('Ne znam za', lik, ':(')
        # Tu ni stavka `return` in funkcija vrne `None`
```

---
layout: image
image: '/img/wc-one-way-mirror.jpg'
url: 'https://i.imgur.com/zUz45Cl.jpg'
caption: 'Enosmerno steklo: ko si zunaj, ne vidiš noter; ko si notri, vidiš tudi ven.'
---

<div v-click class="text-shadow-xl text-center">

<div class="grid grid-cols-2 gap-x-10">

<div>

# Globalno

</div>

<div>

# Lokalno

</div>
</div>
</div>

---
layout: two-cols-title
---

::title::

# Globalno in lokalno <Marker>globalno_lokalno</Marker>
"Razmišljaj globalno, deluj lokalno" :)

::left::

"Prostor" zunaj funkcije se imenuje <Mark>globalni imenski prostor</Mark>. Funkcija ima svoj imenski prostor, ki mu pravimo <Mark>lokalni imenski prostor</Mark>.

```python
a = 1

def f(x):
    b = 2
    return x + a + b

print(f(1)) # izpiše 4

a = 2
print(f(1)) # izpiše 5

print(b)    # Napaka: NameError: name 'b' is not defined
```

[Vizualizacija s Python Tutor](https://pythontutor.com/visualize.html#code=a%20%3D%201%0A%0Adef%20f%28x%29%3A%0A%20%20%20%20b%20%3D%202%0A%20%20%20%20return%20x%20%2B%20a%20%2B%20b%0A%0Aprint%28f%281%29%29%0Aa%20%3D%202%0A%0Aprint%28f%281%29%29%0A%0Aprint%28b%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

::right::

## Enosmerno ogledalo
Funkcija je kot stranišče sredi ulice na prejšnji strani. Obdano je s posebnim steklom, ki prepušča svetlobo samo v eni smeri.

- Ko si **zunaj** funkcije, ne vidiš njenih lokalnih spremenljivk. Vidiš pa globalne spremenljivke.
- Ko si **znotraj** funkcije, vidiš njene lokalne spremenljivke in tudi vse, kar je zunaj, torej ves globalni imenski prostor.
- Znotraj funkcije lahko spreminjaš lokalne (itak) in globalne spremenljivke (uau!).

---
layout: image
image: '/img/globalno_lokalno_pythontutor.png'
caption: 'Vizualizacija s Python Tutor'
url: 'https://pythontutor.com/visualize.html#code=a%20%3D%201%0A%0Adef%20f%28x%29%3A%0A%20%20%20%20b%20%3D%202%0A%20%20%20%20return%20x%20%2B%20a%20%2B%20b%0A%0Aprint%28f%281%29%29%0Aa%20%3D%202%0A%0Aprint%28f%281%29%29%0A%0Aprint%28b%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false'
---

---

# Spreminjanje globalne spremenljivke v funkciji

```python
a = 1

def f(x):
    b = 2
    # Ali lahko spremenimo globalno spremenljivko v funkciji?
    # a = a + 1 # Tole ne bo šlo, napaka.
    # a = 2 # To gre, vendar naredimo novo lokalno spremenljivko
          # z istim imenom, zato tudi izgubimo dostop do globalne
    # Tako je prav, povedati moramo, da mislimo globalno
    global a
    a = a + 1
    return x + a + b

print('f(1):', f(1)) # f(1): 4
print('a: ', a)      # a: 2

a = 2
print('f(1):', f(1)) # f(1): 6
print('a: ', a)      # a: 3

```

---
layout: two-cols-title
---
::title::

# Praštevila <Marker>prastevila_funkcija</Marker>
Povadimo koncepte

::left::

```python
def je_prastevilo(x):
    """Preverimo, ali je število `x` praštevilo."""
    
    if x < 1:
        print('Število mora biti večje od 0.')
        return False
    
    for i in range(2,x):
        # Če je x deljiv z i (ki gre od 2 do x-1),
        # potem x ni praštevilo.
        if x % i == 0:
            # Ni praštevilo
            return False
    else:
        # Sem pridemo, ko se zanka konča,
        # kar pomeni, da x je praštevilo 
        # (sicer bi že prej klicali return)
        return True
```

::right::

```python
def izpisi_prastevila():
    """
    Izpiše vsa praštevila do n.
    Število n je definirano globalno
    """
    
    print('Vsa praštevila do', n)
    for m in range(1, n+1):
        if je_prastevilo(m):
            print(m)

n = int(input('Vnesi število n: '))
izpisi_prastevila()
```

---
layout: image-left
image: '/img/farzan-lelinwalla-79WiPFzJrtY-unsplash.jpg'
caption: 'Fotografija: Farzan Lelinwalla'
url: 'https://unsplash.com/photos/79WiPFzJrtY'
---

# Otroško igrišče
Ko se otroci zabavajo na toboganu, mi merimo kamenčke ...

Primer postopne nadgradnje programa:

- <Tag>povprecje_v1</Tag>: program za računanje povprečja brez ene same funkcije. Šparta!
- <Tag>povprecje_v2</Tag>: program za računanje povprečja z vgrajenimi funkcijami. Olajšanje!
- <Tag>povprecje_v3</Tag>: napišemo lastno funkcijo za računanje povprečja. Razodetje!
- <Tag>povprecje_v4</Tag>: dodamo funkcijo za računanje prostornine kamenčkov in ta dela tudi na seznamih. Hudo!
