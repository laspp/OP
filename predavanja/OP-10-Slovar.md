---
title: Slovar
exportFilename: OP-10-Slovar.pdf
download: false
info: Predavanja pri predmetu Osnove programiranja
theme: default
themeConfig:
  primary: null
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
    publicDir: './assets/10'
   Popravi ProgressBar completed na ustrezno številko predavanja
2. npx slidev OP-10-Slovar.md
3. npx slidev --remote=geslo OP-10-Slovar.md 
  če si presenter, potem uporabi url, ki ima notri ?password=geslo, da te ne gnjavi za vpis gesla
4. npx slidev build --out dist/04 OP-10-Slovar.md
5. npx slidev export OP-10-Slovar.md
pdfinfo OP-10-Slovar.pdf
Pages :---

6. gswin64 -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/printer -dNOPAUSE -dQUIET -dBATCH -dLastPage=12 -sOutputFile=output.pdf OP-10-Slovar.pdf
7. move output.pdf OP-10-Slovar.pdf
-->

<ProgressBar bgcolor="#e54240" completed="10" total="13"/>

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

# Iz množice v slovar
Prejšnji teden smo spoznali množico. Slovar je njen bratranec.

| lastnost | množica | slovar |
| -------- | :-----: | :----: |
| je spremenljiv objekt (iz plastelina) | <div v-click>✓</div> |  <div v-click>✓</div> |
| elementi [^1] morajo biti edinstveni (unikatni) |  <div v-click>✓</div> |  <div v-click>✓</div> |
| elementi so lahko samo nespremenljivi objekti |  <div v-click>✓</div> |  <div v-click>✓</div> |
| elementi niso urejeni, njihov vrstni red je poljuben |  <div v-click>✓</div> |  <div v-click>✘</div> |
| elementov ne označujemo z indeksi |  <div v-click>✓</div> |  <div v-click>✓</div> |

[^1]: Temu, čemur pri množici rečemo element množice, je pri slovarju <Mark>ključ</Mark>.

---
layout: image-right
image: '/img/maria-lin-kim-8RaUEd8zD-U-unsplash.jpg'
caption: 'Fotografija: Maria Lin Kim'
url: 'https://unsplash.com/photos/8RaUEd8zD-UPhoto'
---

# Primer <Marker>shramba</Marker>
Slovar je malo bolj napredna množica.

V svoji shrambi živil (pri nas temu lepo rečemo *špajz*) pogrešamo malo sistematičnosti (in precej čokolade). Začnimo voditi evidenco. Najprej popišimo množico živil:

```python
shramba = {'banana', 'kruh', 'mleko'}
```

Zdaj pa bi radi zabeležili tudi količino živil. Hm, z množico to ne gre zlahka. Gre pa s slovarjem:

```python
shramba = {'banana': 5, 'kruh': 1, 'mleko': 12}
```

Kaj pove zgornji zapis? Enostavno, imamo 5 banan, en hleb kruha in 12 litrov mleka. Nič čokolade 😭 Treba bo v trgovino ...

---
layout: two-cols-title
---

::title::

# Izrazoslovje
Element, ključ, vrednost

::left::

Slovar je zbirka <Mark>elementov</Mark> (ang. *items*), ki so oblike <Mark>ključ: vrednost</Mark> (ang. *key: value*).

Za *ključ* veljajo isti zakoni kot za element množice - biti mora edinstven in nespremenljiv ("kamen").

*Vrednost* je lahko katerikoli objekt.

Slovar si torej lahko predstavljamo takole:

```
slovar = {  ključ_1: vred_1, ključ_2: vred_2, ...}
           └── element 1 ──┘ └── element 2 ──┘
```

```python
shramba = {
  'banana': 5, # element 1
  'kruh':   1, # element 2 
  'mleko': 12  # element 3
  }
```

::right::

## Naslavljanje

Iz slovarja potegnemo vrednost tako, da uporabimo ključ. Slovar nima številčnih indeksov, tako kot niz, seznam, terka in ostala zaporedja. Njegovi indeksi so kar ključi.

```python
>>> shramba['banana']
5
```

Pravkar smo postali hudo lačni, privoščimo si banano. Sedaj moramo popraviti vrednost v shrambi. Zopet uporabimo ključ:

```python
>>> shramba['banana'] = 4
>>> shramba
{'banana': 4, 'kruh': 1, 'mleko': 12}
```

---
layout: two-cols-title
---

::title::

# Ustvarimo slovar

::left::

## Prazen slovar

Če napišemo

```python
a = {}
```

s tem ne ustvarimo prazne množice, kot bi si mislili matematiki, temveč prazen slovar.

```python
>>> type(a)
<class 'dict'>
```

Prav tako lahko pokličemo konstruktor za gradnjo novih objektov tipa slovar (`dict`):

```python
>>> a = dict()
>>> a
{}
```

::right::

## Z začetnimi vrednostmi

To smo že videli:

```python
a = {'konj': 4, 'riba': 0, 'človek': 2}
```

## Slovar iz seznama terk

Če konstruktorju podamo seznam terk, pri čemer so terke pari, bo iz njega naredil slovar. Poglejmo:

```python
seznam_terk = [
    ('konj', 4), 
    ('riba', 0), 
    ('človek', 2)
    ]
a = dict(seznam_terk)

>>> a
{'konj': 4, 'riba': 0, 'človek': 2}
```

---
layout: image-left
image: '/img/nathan-dumlao-wN7Dtu0saNs-unsplash.jpg'
caption: 'Fotografija: Nathan Dumlao'
url: 'https://unsplash.com/photos/wN7Dtu0saNs'
---

# Ključi
Kaj vse je lahko ključ

Ključ je lahko objekt, ki ima nespremenljiv podatkovni tip, torej: `int`, `float`, `str`, `tuple`.

Aha, tudi celo število! Potem lahko slovar napišemo tako:

```python
polica = {0: 'banana', 1: 'mleko'}
```

Pravkar smo naredili nekaj, kar se obnaša podobno kot seznam.

```python
>>> polica[0]
'banana'
>>> polica[1] = 'kruh'
>>> polica
{0: 'banana', 1: 'kruh'}
```

Uporabno? Kaj pa vem. Je pa poučno.

---
layout: two-cols-title
---

::title::

# Ko nimaš pravega ključa ...
Dostop do vrednosti v slovarju gre preko ključa

::left::

```python
>>> shramba
{'banana': 4, 'kruh': 1, 'mleko': 12}
```

<div class="error">

```
>>> shramba['sir']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'sir'
```

</div>

Ključ `'sir'` ne obstaja, zato dobimo napako tipa `KeyError`.

Da se izognemo napaki, najprej preverimo, ali ključ obstaja. Uporabimo <Mark>operator vsebovanosti</Mark> `in`:

```python
>>> 'sir' in shramba
False
```

::right::

Napišimo funkcijo, ki preveri zalogo živila v shrambi:

```python
def preveri_zivilo(shramba, zivilo):
    if zivilo in shramba:
        return shramba[zivilo]
    else:
        return 'Živila ' + zivilo + ' ni v shrambi.'
```

Testirajmo:

```python
>>> preveri_zivilo(shramba, 'banana') 
4
>>> preveri_zivilo(shramba, 'jabolko')
'Živila jabolko ni v shrambi.'
```

Podobno obnašanje dobimo, če uporabimo metodo `get()`, več o tem čez nekaj strani.

---
layout: two-cols-title
---

::title::

# Dodajmo/spremenimo vrednost
Gremo nazaj na naš primer s shrambo.

::left::

Šli smo v trgovino in kupili tablico temne čokolade. Radi bi jo dodali v shrambo. Dodati moramo torej nov par *ključ: vrednost*. To storimo preprosto tako, da naslovimo željeni ključ. Če v slovarju še ne obstaja, se bo ustvaril.

```python
shramba['čokolada'] = 1
```

Če ključ že obstaja, se bo vrednost na tem ključu spremenila/prepisala.

```python
>>> shramba['čokolada'] = 2
>>> shramba['čokolada']
2
>>> shramba['čokolada'] += 1
>>> shramba['čokolada']
3
```

::right::

Napišimo funkcijo za dodajanje živil v shrambo. Sprejme tri argumente: slovar `shramba`, niz z nazivom živila `zivilo` in količino živila `kolicina`, ki pa ni obvezen argument - privzeto je 1. Ker je slovar spremenljiv objekt, bodo vse spremembe na njem vidne tudi, ko se funkcija zaključi.

```python
def dodaj_zivilo(shramba, zivilo, kolicina=1):
    if zivilo in shramba:
        shramba[zivilo] += kolicina
    else:
        shramba[zivilo] = kolicina
```

```python
>>> dodaj_zivilo(shramba, 'čokolada') 
>>> shramba
{'banana': 4, 'kruh': 1, 'mleko': 12, 'čokolada': 1}
>>> dodaj_zivilo(shramba, 'čokolada', 2) 
>>> shramba
{'banana': 4, 'kruh': 1, 'mleko': 12, 'čokolada': 3}
```

---
layout: two-cols-title
---

::title::

# Izbrišimo element slovarja
Uporabimo že poznani stavek `del`

::left::

Element lahko izbrišemo iz slovarja na tri načine. Prvi je z uporabo stavka `del`, druga dva pa sta metodi slovarja `popitem()` oziroma `pop()`. Metodi si bomo ogledali pozneje.

```python
>>> shramba
{'banana': 4, 'kruh': 1, 'mleko': 12, 'čokolada': 3}
>>> del shramba['mleko']
>>> shramba
{'banana': 4, 'kruh': 1, 'čokolada': 3}
```

V naš program za upravljanje s shrambo dodajmo še eno funkcijo, in sicer `porabi_zivilo()`, ki bo pogledala, ali neko živilo je v shrambi in če je, mu bo zmanjšala količino. Če porabimo vso količino živila, ga izbrišemo iz shrambe.

::right::

```python
def porabi_zivilo(shramba, zivilo, kolicina=1):
    # Preverimo zalogo živila. Če ga ni, dobimo niz.
    zaloga = preveri_zivilo(shramba, zivilo)
    if type(zaloga) is not str:
        # Če smo želeli porabiti več kot imamo,
        # se omejimo na toliko, kolikor imamo.
        if kolicina > zaloga:
            kolicina = zaloga
        # Če porabimo vso zalogo, izbrišemo živilo.
        if kolicina == zaloga:
            del shramba[zivilo]
        # Sicer pa zgolj zmanjšamo količino živila.
        else:
            shramba[zivilo] -= kolicina
```

```python
>>> dodaj_zivilo(shramba, 'čokolada') 
>>> shramba
{'banana': 4, 'kruh': 1, 'mleko': 12, 'čokolada': 1}
>>> dodaj_zivilo(shramba, 'čokolada', 2) 
>>> shramba
{'banana': 4, 'kruh': 1, 'mleko': 12, 'čokolada': 3}
```

---
layout: two-cols-title
---

::title::

# Metode slovarja
Najprej si oglejmo metode, ki vračajo *pogled* (*view*) na slovar - to so objekti, ki se dinamično spreminjajo ob spremembi slovarja.

::left::

## `slovar.keys()`

Metoda vrne ključe slovarja.

```python
>>> kljuci = shramba.keys()
>>> kljuci
dict_keys(['banana', 'kruh', 'mleko', 'čokolada'])
```

Vrnjeni objekt `kljuci` se posodobi, ko se posodobi slovar. Izbrišimo ključ `'čokolada'` in preverimo:

```python
>>> del shramba['čokolada']
>>> kljuci
dict_keys(['banana', 'kruh', 'mleko'])
```

::right::

## `slovar.values()`

Vrne vrednosti slovarja, zopet kot *pogled*, ki se ob posodobitvah spreminja.

```python
>>> shramba.values()
dict_values([4, 1, 12])
```

<br/>

## `slovar.items()`

Vrne elemente slovarja, ki so organizirani v seznam terk (nam že poznana oblika).

```python
>>> shramba.items()
dict_items([('banana', 4), ('kruh', 1), ('mleko', 12)])
```

## `slovar.get(k, d=None)`

Metoda `get()` nam vrne vrednost pod ključem `k`, če ta obstaja. Če ne, nam vrne vrednost `d`, ki je privzeto `None`.

```python
>>> shramba.get('mleko', 'Živila ni v shrambi.')
12
>>> shramba.get('sok', 'Živila ni v shrambi.')
'Živila ni v shrambi.'
```

<br/>



## slovar.clear()

## slovar.pop(k)

## slovar.popitem()

## slovar.update(slovar2)

## slovar.fromkeys

## slovar.copy()

---
layout: two-cols
---

# Metode slovarja
Nadaljujmo s pregledom uporabnih metod.

## `slovar.copy()`

Naredi plitvo kopijo slovarja.

```python
>>> klet = shramba.copy()
>>> klet['vino'] = 3
>>> klet
{'banana': 4, 'kruh': 1, 'mleko': 12, 'vino': 3}
>>> shramba
{'banana': 4, 'kruh': 1, 'mleko': 12}
```

<br/>

## `slovar.clear()`

```python
>>> klet.clear()
>>> klet
{}
```

::right::

## `slovar.get(k, d=None)`

Vrne vrednost pod ključem `k`, če ta obstaja. Če ne, nam vrne vrednost `d`, ki je privzeto `None`. Podobno funkciji `preveri_zivilo()`, kajne?

```python
>>> shramba.get('mleko', 'Živila ni v shrambi.')
12
>>> shramba.get('sok', 'Živila ni v shrambi.')
'Živila ni v shrambi.'
```

<br/>

## `slovar.update(slovar2)`

Združi skupaj slovarja `slovar` in `slovar2`.

```python
>>> shramba.update({'sir': 3})
>>> shramba
{'banana': 4, 'kruh': 1, 'mleko': 12, 'sir': 3}
```

---
layout: two-cols
---

# Metode slovarja
Še tri

## `dict.fromkeys(z, v=None)`

Zgradi slovar iz zaporedja `z` (niz, seznam, terka, ...), pri čemer vsi elementi dobijo vrednost `v`.

```python
>>> ocene = dict.fromkeys(['Janko', 'Metka'], 5)
>>> ocene
{'Janko': 5, 'Metka': 5} 
```

## `slovar.popitem()`

Odstrani in vrne zadnji element slovarja (terko):

```python
>>> shramba.popitem()
('sir', 3)
>>> shramba
{'banana': 4, 'kruh': 1, 'mleko': 12}
```

::right::

## `slovar.pop(k, d)`

Če ključ `k` obstaja v slovarju, ta metoda odstrani ključ in vrne vrednost elementa. Če ključ ne obstaja, vrne `d`. Če `d` ni podan in ključ ne obstaja, vrne `KeyError`.

```python
>>> shramba
{'banana': 4, 'kruh': 1, 'mleko': 12}
>>> shramba.pop('kruh')
1
>>> shramba.pop('kruh')
```

<div class="error">

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'kruh'
```

</div>


```python
>>> shramba.pop('kruh', 'Ključ ne obstaja')
'Ključ ne obstaja'
```

---
layout: two-cols-title
---

::title::

# Sprehod čez slovar
Slovar je zaporedje, preko katerega se lahko sprehajamo z zanko `for`

::left::

## Zanka po ključih

Če čisto naivno napišemo zanko `for` takole:

```python
for zivilo in shramba:
    print(zivilo)
```

dobimo sledeči izpis vseh ključev slovarja:

```
banana
mleko
```

Očitno si lahko privoščimo bananin frapé. Izpišimo še količine:

```python
for zivilo in shramba:
    print(zivilo, ': ', shramba[zivilo], sep='')
```

::right::

## Zanka po elementih

Zanko na koncu levega stolpca lahko elegantneje napišemo z uporabo metode `items()` in razpakiranja terke:

```python
for zivilo, kolicina in shramba.items():
    print(zivilo, ': ', kolicina, sep='')
```

Dobimo:

```
banana: 4
mleko: 12
```

---
layout: two-cols-title
---

::title::

# Urejanje elementov slovarja - po ključih
&nbsp;

::left::

Pri seznamih smo spoznali metodo `sort()`, ki uredi objekt, ki je klical to metodo. Obstaja tudi funkcija `sorted()`, ki vrne nov (urejen) objekt. Če mu kot argument podamo slovar, to razume kot seznam ključev. Pred urejanjem v shrambo dodajmo ananas.

```python
>>> shramba['ananas'] = 5
>>> shramba
{'banana': 4, 'mleko': 12, 'ananas': 5}
>>> sorted(shramba)
['ananas', 'banana', 'mleko']
>>> shramba
{'banana': 4, 'mleko': 12, 'ananas': 5}
```

`sorted` je vrnil nov objekt (urejen seznam ključev). Objekt `shramba` se ni spremenil.

::right::

Napišimo funkcijo `uredi()`, ki bo vrnila urejene ključe slovarja. Način urejanja podamo z argumentom `padajoce`.

```python
def uredi(shramba, po_kolicini=False, padajoce=False):
    if po_kolicini:
        # To bomo naredili na naslednji strani
        pass
    else:
        s = sorted(shramba.items(), reverse=padajoce)
    return s
```

```python
>>> uredi(shramba)
[('ananas', 5), ('banana', 4), ('mleko', 12)]
>>> uredi(shramba, padajoce=True)
[('mleko', 12), ('banana', 4), ('ananas', 5)]
```

---
layout: two-cols-title
---

::title::

# Urejanje elementov slovarja - po vrednostih
&nbsp;

::left::

Če želimo shrambo urediti po količinah živil (po vrednosti), moramo biti malo zviti:

1. funkciji `sorted` moramo kot argument podati seznam terk oblike `(kljuc, vrednost)` in
2. definirati moramo funkcijo, ki bo vrnila element terke, po katerem urejamo.

Začnimo s točko 2 in definirajmo preprosto funkcijo, ki sprejme zaporedje in vrne drugi element tega zaporedja:

```python
def dobi_vrednost(item):
    return item[1]
```

::right::

Sedaj dopolnimo funkcijo `uredi()` s prejšnje strani:

```python
def uredi(shramba, po_kolicini=False, padajoce=False):
    if po_kolicini:
        s = sorted(
            shramba.items(), 
            reverse=padajoce, 
            key=dobi_vrednost)
    else:
        s = sorted(
            shramba.items(), 
            reverse=padajoce)
    return s
```

```python
>>> uredi(shramba, po_kolicini=True, padajoce=True)
[('mleko', 12), ('ananas', 5), ('banana', 4)]
```

Pa smo!

---
layout: two-cols-title
---

::title::

# Napredna stopnja <Marker>glasba</Marker>
Radi bi si uredili svojo glasbeno zbirko.

::left::

Napravimo zgled večnivojske zgradbe slovarja. V slovarju bomo kot vrednosti hranili slovarje.
V zbirki hranimo izvajalce in za vsakega od njih še albume.
Za vsak album imamo tudi podatek o letu izdaje.

```python
# Naredimo najprej prazen slovar
zbirka = {}
# Dodamo prvega izvajalca, 
# njegovi albumi so zaenkrat prazen slovar
zbirka['Vlado Kreslin'] = {}
# Dodamo prvi album in letnico izdaje
zbirka['Vlado Kreslin']['Kreslinčice'] = 2002
print(zbirka)
```

Izpis:

```
{'Vlado Kreslin': {'Kreslinčice': 2002}}
```

::right::

Sedaj dodajmo podporne funkcije, ki bodo omogočale:

- dodajanje izvajalca v zbirko,
- dodajanje albuma izvajalcu, leto izdaje ni obvezno,
- popravke v letu izdaje za nek album,
- izbris izvajalca,
- izpis celotne zbirke,
- izpis vseh izvajalcev,
- izpis vseh albumov, pri čemer lahko določimo, od katerega leta izdaje naprej,
- izpis vseh albumov določenega izvajalca.

Glej program <Tag>glasba.py</Tag> z izdelano rešitvijo.
