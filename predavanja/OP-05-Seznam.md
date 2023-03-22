---
title: Seznam
exportFilename: OP-05-Seznam.pdf
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
    publicDir: './assets/05'
   Popravi ProgressBar completed na ustrezno številko predavanja
2. npx slidev OP-05-Seznam.md
3. npx slidev --remote=geslo OP-05-Seznam.md 
  če si presenter, potem uporabi url, ki ima notri ?password=geslo, da te ne gnjavi za vpis gesla
4. npx slidev build --out dist/05 OP-05-Seznam.md
5. npx slidev export OP-05-Seznam.md
6. gswin64 -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/printer -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf OP-05-Seznam.pdf
7. move output.pdf OP-05-Seznam.pdf
-->

<ProgressBar bgcolor="#e54240" completed="5" total="13"/>

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

<!--
Zapiski predavatelja
-->

---
layout: image-right
image: '/img/lukasz-rawa-QHWxPcrpBB0-unsplash-2.jpg'
url: 'https://unsplash.com/photos/QHWxPcrpBB0'
caption: 'Fotografija: Łukasz Rawa'
---

# Met krompirja
Bodoča olimpijska disciplina, Praskež se uri za zapisnikarja. Svetovni rekord je 101,9 m.

- Tekmovalci lučajo krompir. Kdor ga vrže najdlje, je zmagovalec.

- Praskež mora beležiti dolžine metov in nato razglasiti najdaljši met.

- Organizatorji želijo od njega tudi statistiko - povprečje vseh metov.

Pomagajmo mu pri vodenju seznama metov in izračunih.

<!-- 
Nemška vas –  Družba fantov in deklet iz Nemške vasi, je prejšnjo soboto, 22. avgusta 2015, pred cerkvijo sv. Lenarta organizirala že deveti družabni dogodek, tekmovanje v metu krompirja. Ideja zanj se je rodila leta 2007, ko so sosedje: Matjaž, Miran in Uroš, ki je bil letos vodja prireditve, v bližnji okrepčevalnici stavili, kdo bo določeno stvar vrgel najdlje. Naslednji dan so »stvar« izbrali in se odločili za krompir. Fantje so imeli celo dve gledalki, ki sta na sosednji njivi kopali krompir.
Že naslednje leto je tekmovanje postalo zanimivo za širšo javnost. Sedaj tekmovanje poteka v treh kategorijah, in sicer člani, članice in otroci, v dveh serijah. Letos je krompir metalo 82 tekmovalcev (36 moških, 7 žensk, 39 otrok) s širšega ribniško-kočevskega konca. Po tekmovanju so vsega pobrali, spekli in s spoštovanjem pojedli.

Med člani je zmagal Denis Sevenšek iz Kočevja, ki je krompir zalučal 97 m. Drugi je bil z 92,4 m Goran Zorič iz Kočevja, ki se tekmovanja udeležuje redno in je vsakič v vrhu, tretje mesto pa je osvojil Jošt Vesel z Brega pri Ribnici z dolžino meta 86,4 m. Nosilec rekorda tako ostaja Peter Gradišar, ki je leta 2012 krompir vrgel 101,9 m daleč.

Pri ženskah je zmagala Iva Cilenšek iz Kočevja, ki je krompir vrgla 63,0 m, drugo mesto je osvojila Alja Vrček iz Kamenč s 55,9 m in tretje Brina Obranovič iz Kočevja s 53,8 m. V otroški konkurenci je zmago slavil Luka Dejak iz Dolenje vasi, najdaljši od dveh metov je znašal 62,3 m. Vsi tekmovalci so imeli na voljo dva meta, v prvi in drugi seriji. Drugi je bil Gal Košir iz Ribnice z 48,1 m in tretji Miha Šilc iz Nemške vasi s 46,5 m.

Prvih pet najboljših v vsaki kategoriji je prejelo praktične nagrade, prvi trije tudi pokale, nagrade pa so prejeli tudi tekmovalci v izboru za največji krompir. Tega je letos prinesel Tone Bojc iz Dolenje vasi. Njegov krompir je tehtal kar 823 g. Drugi najtežji krompir je prinesla Milka Bojc, prav tako iz Dolenje vasi. Pri njej oz. njem se je tehtnica ustavila pri 731 g. Tretja je bila Ota Blatnik iz Nemške vasi, njen krompir pa je tehtal 661 g.
-->

---
layout: two-cols-title
---

::title::

# Programski paket za podporo tekmovanja
Napavimo to najprej v Scratchu

::left::

## Zastonj <Marker>[met_krompirja_v1.sb3](https://scratch.mit.edu/projects/818442094/)</Marker>

Neorganizirani Praskež, ki vse dolžine metov krompirja nosi v svoji kosmati pameti.
Zatakne se mu že pri drugi seriji tekmovanja.

## Premium <Marker>[met_krompirja_v2.sb3](https://scratch.mit.edu/projects/818300109/)</Marker>

Praskež si omisli <Mark>seznam</Mark>, v katerega beleži dolžine. Ko se mu zahoče,
izvede del programa za izračun najdaljšega meta oziroma povprečja vseh metov.

::right::

[![https://scratch.mit.edu/projects/818300109/](/img/met_krompirja_v3.png)](https://scratch.mit.edu/projects/818300109/)

---

# Seznam
Zaporedje vrednosti

Python ima precej vgrajenih podatkovnih tipov. Do sedaj smo spoznali:

- nični tip `NoneType`, ki ima samo vrednost `None` in pomeni "nič",
- Booleov tip `bool`, ki zavzame vrednosti `True` ali `False`,
- številčna tipa `int` in `float` ter
- niz znakov `str`.

Slednji, niz znakov torej, je že prvi predstavnik podatkovnih tipov,
ki opisujejo zaporedje podatkov, denimo:

`abeceda = 'ABCČDEFGHIJKLMNOPRSŠTUVZŽ'`.

## Spoznajmo sedaj <Mark>seznam</Mark> (v pythonščini je to `list`).

Gre za <Mark>zaporedje elementov, ki so lahko poljubnega podatkovnega tipa</Mark>.

---

# Kako definiramo seznam
<br/>

Uporabimo oglate oklepaje `[ ]`

- znak `[` dobimo, če na tipkovnici pritisnemo <kbd>Alt Gr</kbd> + <kbd>F</kbd> oziroma <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>F</kbd>
- znak `]` dobimo, če na tipkovnici pritisnemo <kbd>Alt Gr</kbd> + <kbd>G</kbd> oziroma <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>G</kbd>

Elemente seznama ločimo z vejico

`[57, 32, 99, 98, 57]`

Seznamu seveda lahko damo ime z uporabo operatorja prirejanja `=`

`moja_najljubsa_stevila = [7, 12, 22, 42, 3.14]`

Aha, zgornji seznam vsebuje tako cela kot tudi necela števila. Lahko notri stlačimo še kaj?

---

# Kaj lahko seznam vsebuje
<br/>

Vsebuje lahko vrednosti ali imena (spremenljivke) poljubnih podatkovnih tipov.

Pazi tole:

<div class="code-lg">

```python
import math
a = 22
moja_najljubsa_stevila = [7, 'dvanajst', a, 7*6, math.pi]
```

</div>

Seznam lahko vsebuje tudi sezname (in še veliko drugega, kot bomo videli do poletja).

<div class="code-lg">

```python
vreca = [None, True, False, 42, 3.14, 3+2j, 'niz', ['in', ['seznam','v'], 'seznamu']]
```

</div>

<br/>

*PS. Mimogrede sem notri vrgel še kompleksno število $3+2i$, ki je tipa `complex`, imaginarna enota pa je `j`.*

---
layout: image-right
image: '/img/elena-mozhvilo-fXf6H8yxCqM-unsplash.jpg'
url: 'https://unsplash.com/photos/fXf6H8yxCqM'
caption: 'Fotografija: Elena Mozhvilo'
---
# Hišne številke
Vsak element v seznamu ima svoj naslov

Praskež in navadni smrtniki začenjajo štetje z 1.

Programerji začnemo z 0. Vsaj v Pythonu[^1].

Naslovu elementa v seznamu pravimo <Mark>indeks</Mark>. Seznami so torej oštevilčeni oziroma indeksirani.

## Koliko je hiš v kraju?
Dolžino seznama dobimo s funkcijo `len()`.

[^1]: Nekateri, redki, programski jeziki začenjajo sezname z naslovom 1, npr. Fortran, Julia, Lua, MATLAB, R, Scratch.

---
layout: two-cols-title
---

::title::
# Indeksi in dostop do elementov
Vsak element seznama ima svoj indeks, preko katerega ga lahko dosežemo.

Imamo seznam imen študentov. Nad elemente seznama napišimo njihove indekse.

<div class="code-xl code-no-ligatures">

```python
# indeksi:     0         1         2         3
studenti = ['Sofija', 'Lenart', 'Patrik', 'Erazem']
```

</div>

::left::

- Do elementov dostopamo z oglatimi oklepaji. Študentka Sofija je prva v seznamu in ima indeks 0. Njeno ime dobimo tako:
  
  `studenti[0]`

- Drugi element ima indeks 1.
  
  `>>> studenti[1]`
  
  `Lenart`

::right::

- Zadnji element ima indeks 3, ki ga lahko izračunamo tako: "dolžina seznama minus ena":
  
  `len(studenti) - 1`

  torej

  `studenti[len(studenti) - 1]`

  V Pythonu obstaja tudi lažji način, da pridemo do zadnjega, predzadnjega itd. Obrni stran.

---

# Negativni indeksi
Olajšajo nam dostop do elementov na koncu seznama.

Da se bomo v nadaljevanju lažje razumeli, si predstavljajmo, da so indeksi elementov seznama napisani pred samim elementom. Indeksom od 0 do `len(studenti)-1`, ki so napisani nad elementi, dodajmo pod seznam še negativne indekse. Poleg tega smo dodali še indeks 4, razlog povemo na čez nekaj strani 😄

<div class="code-xl code-no-ligatures">

```python
 0        1        2        3        4
 |        |        |        |        |
 | Sofija | Lenart | Patrik | Erazem |
 |        |        |        |        |      
-4       -3       -2       -1        

```

</div>

<div class="grid grid-cols-3 gap-x-6">
<div>

```python
>>> studenti[3]
'Erazem'
>>> studenti[len(studenti)-1]
'Erazem'
>>> studenti[-1]
'Erazem'
```

</div>
<div>

```python
>>> studenti[0]
'Sofija'
>>> studenti[-4]
'Sofija'
>>> studenti[-len(studenti)]
'Sofija'
```

</div>
<div>

```python
>>> studenti[4]
```

<div class="error">

```
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

</div>

</div>
</div>

---
layout: two-cols-title
class: code-lg
---

::title::
# Vožnja čez seznam <Marker>postaje</Marker>
Uporabimo zanko, da se premikamo po indeksih seznama

Kot primer vzemimo postajališča LPP linije 18 (od centra proti Stožicam):

`postaje = ['Konzorcij', 'Cankarjev dom', 'Svetčeva', 'Večna pot', 'Živalski vrt']`

::left::

## Vožnja tja ...
Prvo postajališče ima indeks 0, drugo 1,..., do `len(postaje)-1`. Potrebujemo števec, ki se vsako iteracijo zanke poveča za 1, s pogojem v glavi zanke pa pazimo, da se pravočasno ustavimo. Števec v zanki oz. indeks seznama pogosto označimo z `i`.

```python
i = 0
while i < len(postaje):
    postaja = postaje[i]
    print(postaja)
    i += 1
```

::right::

## ... in spet nazaj

```python
i = len(postaje)-1
while i >= 0:
    print(postaje[i])
    i -= 1
```

Za hec uporabimo še negativne indekse:

```python
i = 1
while i <= len(postaje):
    print(postaje[-i])
    i += 1
```

---

# Rezanje seznamov
Seznam je kot čajna klobasa - lahko ga režemo na rezine.

Navpične črtice na spodnji sliki označujejo mesta, kjer lahko zarežemo v seznam. Recimo, da želimo razdeliti seznam študentov na dve rezini (manjša seznama) tako, da bo v prvem samo prvi element, v drugem pa vsi ostali. Kje bomo zarezali? Zakaj smo dodali indeks 4?

<div class="code-xl code-no-ligatures">

```python
 0        1        2        3        4
 |        |        |        |        |
 | Sofija | Lenart | Patrik | Erazem |
 |        |        |        |        |      
-4       -3       -2       -1        
          ✂

```

</div>

<arrow x1="95" y1="260" x2="175" y2="260" color="#e54240" width="2" />
<arrow x1="200" y1="260" x2="505" y2="260" color="#e54240" width="2" />

Rezino v Pythonu določimo tako, da povemo njen začetni in končni indeks (lahko tudi korak, počakajmo).

<div class="code-lg">

</div>

<div class="grid grid-cols-3 gap-x-6">
<div>

```python
>>> studenti[0:1]
['Sofija']
```

</div>
<div>

```python
>>> studenti[1:4]
['Lenart', 'Patrik', 'Erazem']
```

</div>
<div>

```python
>>> studenti[1:-1]
['Lenart', 'Patrik']
```

</div>
</div>

---

# Rezine
Pravila za oblikovanje rezin

Splošna oblika rezine je:

<div class="code-xl">

```python
seznam[zacetek:konec:korak]
```

</div>

**Iz seznama `seznam` izrežemo rezino, ki vsebuje elemente z indeksi od vključno `zacetek` do <Mark>ne vključno</Mark> `konec` (torej do `konec-1`), pri čemer se indeksi povečujejo s korakom `korak`.**

Števila `zacetek`, `konec` in `korak` so opcijski - lahko katerega od njih tudi izpustimo. Pri tem velja:

- če izpustimo `zacetek`, je isto, kot bi rekli, da je `zacetek` enak 0. Torej se rezina začne na začetku seznama;
- če izpustimo `konec` pomeni, da se rezina konča na koncu seznama, torej je `konec` enak `len(seznam)`;
- če izpustimo `korak`, se razume, da je korak 1.

---

# Rezine - primeri

Spomnimo se spet na Praskeža in prvenstvo v metu krompirja. Praskež je v svoj seznam zabeležil tole:

`meti = [57, 32, 99, 98, 57, 101, 48]`

```python
>>> meti[0:3]           # Od ničtega do ne vključno tretjega, torej od 0 do 2. To so prvi trije meti.
[57, 32, 99]
>>> meti[:3]            # Če začnemo rezino na začetku, lahko indeks 0 izpustimo. Dobimo isto kot prej.
[57, 32, 99]
>>> meti[3:len(meti)]   # Meti od vključno četrtega (ki ima indeks 3) do zadnjega, torej do ne vključno len(meti).
[98, 57, 101, 48]
>>> meti[3:]            # Indeks konca lahko v tem primeru izpustimo.
[98, 57, 101, 48]
>>> meti[:]             # Če zamolčimo tako začetek kot konec, dobimo cel seznam (od 0 do len(meti)).
[57, 32, 99, 98, 57, 101, 48]
>>> meti[0:len(meti):2] # Do sedaj je bil korak privzeto 1. Spremenimo ga na 2 in sedaj skačemo po 2 naprej.
[57, 99, 57, 48]
>>> meti[::2]           # Izpustimo začetek in konec, korak pustimo na 2.
[57, 99, 57, 48]
>>> meti[1::2]          # Začnemo pri drugem elementu in skačemo po 2 naprej vse do konca
[32, 98, 101]
>>> meti[4::-1]         # Korak je lahko negativen - gremo od desne proti levi! 
[57, 98, 99, 32]        # Konec smo tukaj izpustili, torej gremo do začetka.
```

---

# `range()`
Funkcija, ki generira sezname števil v podanem obsegu

Izkoristimo zagon, ki nam ga je dalo spoznanje rezin, in odkrijmo generator obsegov. Obnaša se namreč zelo podobno kot to določajo pravila rezin.

Splošni klic funkcije `range()` je:

<div class="code-lg">

```python
range(zacetek, konec, korak)
```

</div>

Funkcija vrne seznam zaporednih celih števil (`int`) od vključno `zacetek` do ne vključno `konec` s korakom `korak`. Če izpustimo argument `korak`, se privzame korak 1.

<div class="code-lg">

<div class="grid grid-cols-2 gap-x-10">
<div>

Funkcija `range()` vrne nekaj, čemur rečemo <Mark>generator</Mark> - to pomeni, da nam izroči elemente seznama šele tedaj, ko jih zares potrebujemo.

```python
>>> range(1, 20, 2)
range(1, 20, 2)
```

</div>
<div>

Če želimo vse elemente zdaj in takoj, to zahtevamo tako, da generator pretvorimo v seznam. Uporabimo funkcijo `list()`:

```python
>>> list(range(1, 20, 2))
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
```

</div>
</div>
</div>

---
layout: two-cols-title
---

::title::

# `range()` - primeri

::left::

**Prvih 10 naravnih števil**, vključimo tudi 0:

```python
>>> list(range(10))   # Izpustili smo konec in korak
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Prvih 10 pozitivnih števil**:

```python
>>> list(range(1, 11))  # Izpustili smo korak
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

**Liha števila**:
izdelajmo seznam vseh lihih števil od `a` do `b`, vendar brez slednjega. Uporabnik zagotovi, da je `a` lih.
Primer za `a = 1` in `b = 20`:

```python
>>> list(range(a, b, 2))
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
```

::right::

**Seznam večkratnikov**, ki vsebuje večkratnike števila `a` od `a` do vključno `b`. Primer za `a = 3` in `b = 21`:

```python
>>> list(range(a, b+1, a))
[3, 6, 9, 12, 15, 18, 21]
```

**Soda števila**:
izdelajmo seznam vseh sodih števil od `a` do vključno `b`. Ni nujno, da je `a` sod. Primer za `a = 1` in `b = 20`:

```python
>>> list(range(a+a%2, b+1, 2)) # a%2 je 1, če je a lih
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

**Odštevalnik** od 5 do vključno 0:

```python
>>> list(range(5, -1, -1))  # korak je lahko negativen
[5, 4, 3, 2, 1, 0]
```

---
layout: two-cols-title
---

::title::
# Operatorji nad seznami

::left::

## Vsebovanost
Z operatorjema `in` in `not in` lahko preverimo, ali seznam vsebuje določen element ali ne.

```python
>>> 101 in [57, 32, 99, 98, 57, 101, 48]
True
>>> 'Ana' not in ['Sofija', 'Lara', 'Marija']
True
```

## Seštevanje in množenje
Operator `+` lepi skupaj dva seznama, operator `*` naredi več kopij vsebine seznama.

```python
>>> [1, 2, 3, 4] + [5, 6]
[1, 2, 3, 4, 5, 6]
>>> [0]*5
[0, 0, 0, 0, 0]
```

::right::

## Primerjanje
Kdaj je nek seznam večji/manjši od drugega? Gledamo istoležne elemente in jih primerjamo. Uporabimo lahko tudi `>=` in `<=`.

```python
>>> [1, 2, 3] > [5, 6]     # Ni res, 1 ni večja od 5
False
>>> [1, 2, 3] > [1, 2, 2]  # Res je, 3 je več kot 2
True
```

Enakost?

```python
>>> [1, 2, 3] == [3, 2, 1]
False
>>> ['jabolko', 'kivi'] != ['jabolko', 'kivi']
False
```

---
layout: two-cols-title
---

::title::
# Funkcije nad seznami
Vgrajene funkcije, ki sprejmejo seznam kot argument (razen prve)

::left::

## `list()`

```python
>>> list()      # Ustvarimo prazen seznam, isto kot []
[]
>>> list('ABC') # Niz znakov pretvorimo v seznam znakov
['A', 'B', 'C']
```

<br/>

## `bool()`
Vrne `True`, če seznam ni prazen, sicer `False`.

```python
>>> bool([])
False
>>> bool([1, 2])
True
```

::right::

## `len()`, `sum()`, `min()`, `max()`

```python
>>> meti = [57, 32, 99, 98, 57, 101, 48]
>>> len(meti) # Že poznamo: dolžina seznama
7
>>> sum(meti) # Vsota vseh elementov seznama
492
>>> min(meti) # Najmanjši element
32
>>> max(meti) # Največji element
101
>>> max(['Rob', 'Rok']) # Isto kot max('Rob', 'Rok')
'Rok'
```

Znamo izračunati povprečno dolžino meta?

```python
>>> sum(meti) / len(meti) # vsota / dolžina
70.28571428571429
```

---
layout: two-cols-title
---

::title::
# Objekti - zelo na hitro

V Pythonu so vse *stvari* v resnici <Mark>objekti</Mark>. Objekti imajo svoje lastnosti in funkcije, ki jim pravimo metode. Do njih pridemo s piko, recimo:

`ime_objekta.ime_metode(argumenti)`

Seznam vseh lastnosti/funkcij objekta dobimo s funkcijo `dir()`. Lahko pa v Thonnyju odpremo `Pogled`→`Pregledovalnik objektov`. Nato izberemo spremenljivko v oknu *Spremenljivke*.

::left::

To nam je znano od prejšnjič, ko smo uvažali module. Uvoženi modul je tudi objekt in do njegovih konstant in funkcij pridemo s piko.

```python
>>> import math as m
>>> m.pi         # Dostopamo do konstante
3.141592653589793
>>> m.sin(m.pi)  # Dostopamo do funkcije
1.2246467991473532e-16  # To je praktično 0
```

::right::

Tudi nizi so objekti. Ko uporabimo funkcijo `str()`, v resnici izdelamo nov objekt tipa `str`.

```python
>>> a = str(42)
>>> a
'42'
>>> a.isnumeric()  # Pokličemo metodo niza, ki pove,
True               # ali niz vsebuje samo števke.
```

---
layout: two-cols-title
---

::title::
# Metode seznama
Seznam je objekt ... poglejmo njegove najbolj uporabne metode

::left::

| **metoda** | **opis**  |
| -----------| --------  |
| `seznam.clear()`   | čiščenje seznama  |
| `seznam.copy()`    | kopiranje seznama |
| `seznam.sort()`    | urejanje seznama  |
| `seznam.append(x)` | na konec dodamo element `x` |
| `seznam.insert(i,x)` | na indeks `i` vrinemo element `x`  |
| `s1.extend(s2)` | Seznam `s1` razširimo s `s2` (to naredi tudi  `+`) |

::right::

| **metoda** | **opis**  |
| -----------| --------  |
| `seznam.reverse()` | obračanje seznama |
| `seznam.count(x)`  | štetje pojavitev elementa `x`|
| `seznam.index(x)`  | indeks elementa `x` |
| `seznam.pop()` | ven vzamemo zadnji element |
| `seznam.pop(i)` | ven vzamemo element z indeksom `i` |
| `seznam.remove(x)` | izbrišemo element `x` |

---
layout: two-cols
---

## `seznam.clear()`

```python
# Počistimo vsebino seznama, postane prazen
>>> seznam = [1, 2, 3]
>>> seznam
[1, 2, 3]
>>> seznam.clear()
>>> seznam
[]
```

## `seznam.copy()`

```python
# Naredimo "pravo" kopijo seznama, ne zgolj "povezave"
>>> seznam = [1, 2, 3]
>>> ni_prava_kopija = seznam
>>> ni_prava_kopija[0] = 0 # Spremenimo prvi element
>>> seznam  # Ups, s tem smo spremenili tudi seznam!
[0, 2, 3]
>>> kopija = seznam.copy()
>>> kopija[0] = 1
>>> kopija
[1, 2, 3]
>>> seznam
[0, 2, 3]
```

::right::

## `seznam.sort()`

```python
# Urejanje seznama po velikosti / abecedi ...
>>> seznam = [3, 1, 2, 3]
>>> seznam.sort()
>>> seznam
[1, 2, 3, 3]
>>> seznam.sort(reverse=True)
>>> seznam
[3, 3, 2, 1]
>>> seznam = ['Robnik', 'Rok', 'Rob']
>>> seznam.sort()
>>> seznam
['Rob', 'Robnik', 'Rok']
>>>
```

---
layout: two-cols
---

## `seznam.append(x)`

```python
# Dodamo element `x` na konec seznama.
>>> seznam = [1, 2, 3]
>>> seznam.append(4)
>>> seznam
[1, 2, 3, 4]
>>> seznam.append([5, 6]) # Če dodamo seznam,
>>> seznam                # dobimo seznam v seznamu.
[1, 2, 3, 4, [5, 6]]
```

<br/>

## `seznam.insert(i, x)`

```python
# V seznam na indeks `i` vstavimo nov element `x`.
>>> seznam = [1, 2, 3]
>>> seznam.insert(1, 0)
>>> seznam
[1, 0, 2, 3]
>>> seznam.insert(1000, 4)
>>> seznam
[1, 0, 2, 3, 4]
```

::right::

## `seznam1.extend(seznam2)`

```python
# Seznam `seznam1` razširimo s seznamom `seznam2`.
# Zlepimo ju skupaj. To dela tudi `+` oziroma `+=`.
>>> seznam1 = [1, 2, 3]
>>> seznam2 = [4, 5, 6]
>>> seznam1.extend(seznam2)
>>> seznam1
[1, 2, 3, 4, 5, 6]
>>> seznam1 = seznam1 + [7, 8]
>>> seznam1
[1, 2, 3, 4, 5, 6, 7, 8]
>>> seznam1 += [9]
>>> seznam1
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> seznam1[:3] + [0, 0, 0] + seznam1[3:]
[1, 2, 3, 0, 0, 0, 4, 5, 6, 7, 8, 9]
```

---
layout: two-cols
---

## `seznam.reverse()`

```python
# Obrnemo seznam, od desne proti levi
>>> seznam = [1, 2, 3]
>>> seznam.reverse()
>>> seznam
[3, 2, 1]
```

<br/>

## `seznam.count(x)`

```python
# Preštejemo, kolikokrat se pojavi element `x`.
>>> seznam = [1, 2, 3, 3]
>>> seznam.count(2)
1
>>> seznam.count(3)
2
>>> seznam.count(4)
0
```

::right::

## `seznam.index(x)`

```python
# Vrne indeks prve pojavitve elementa `x`
>>> seznam = [1, 2, 3, 3]
>>> seznam.index(2)
1
>>> seznam.index(3) 
2
>>> seznam.index(4)
```

<div class="error">

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 4 is not in list
```

</div>

---
layout: two-cols
---

## `seznam.pop()`

```python
# Iz seznama brišemo zadnji element in ga vrnemo
>>> seznam = [1, 2, 3]
>>> seznam.pop()
3
>>> seznam
[1, 2]
```

<br/>

## `seznam.pop(i)`

```python
# Iz seznama vzamemo element z indeksom `i`
>>> seznam = [1, 2, 3]
>>> seznam.pop(1)
2
>>> seznam
[1, 3]
```

::right::

## `seznam.remove(x)`

```python
# Iz seznama brišemo element `x` (prvo pojavitev)
>>> seznam = [1, 3, 2, 3]
>>> seznam.remove(3)
>>> seznam 
[1, 2, 3]
>>> seznam.remove(3)
>>> seznam
[1, 2]
>>> seznam.remove(3)
```

<div class="error">

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
```

</div>

Brisanje elementov je mogoče tudi s stavkom `del`:

```python
>>> seznam = [1, 3, 2, 3]
>>> del seznam[1]
>>> seznam 
[1, 2, 3]
>>> del seznam[0:2]
>>> seznam
[3]
```

---
layout: two-cols-title
---

<!-- 2023: do tukaj smo prišli, nismo še naredili programa -->

::title::

# Program za beleženje metov krompirja
Pomagajmo zapisnikarju Praskežu, tokrat v Pythonu

::left::

## Beležka <Marker>met_krompirja_v1</Marker>

- uporabnik vnaša dolžine metov enega po enega
- konča tako, da vpiše znak `'X'`
- če vpiše `'I'`, program izpiše seznam dolžin

## Tablica <Marker>met_krompirja_v2</Marker>

- če uporabnik vpiše `'S'`, program izpiše padajoče urejen seznam
- če uporabnik vpiše `'N'`, program izpiše najdaljšo dolžino meta
- če uporabnik vpiše `'P'`, program izpiše povprečno dolžino meta

::right::

## Superračunalnik <Marker>met_krompirja_v3</Marker>

- če uporabnik vpiše `'M'`, program izpiše mediano dolžine meta
- uporabnik vpiše -1, če je bil met neveljaven; ta met se ne upošteva
  pri izračunih povprečja in mediane, tudi se ne izpiše pri opciji `'S'`

---

# `eval()`
Funkcija, ki ovrednoti (ang. evaluate) podani niz

Rezultat funkcije `eval()` je ovrednoten vhodni niz: kot če bi ga vnesli v interaktivno lupino Pyhona.

<div class="code-lg">

```python
>>> eval('"2"*2+str(0//3)+"1"')
'2201'
>>> vnos = input('Vnesi izraz: ') # Vnesemo: 2**8
>>> eval(vnos)
256
>>> eval('[1, 2, 3]')
[1, 2, 3]
>>> vnos = input('Vnesi seznam: ') # Vnesemo: [1, 2, 3]
>>> eval(vnos)
[1, 2, 3]
>>> vnos = input('Vnesi seznam števil, ločenih z vejico: ') # Vnesemo: 57, 32, 99
>>> eval('[' + vnos + ']') # Dodamo oglate oklepaje, da je to res seznam
[57, 32, 99]
```

</div>

---
layout: two-cols-title
---

::title::
# Nizi so v sorodu s seznami
Oba podatkovna tipa opisujeta zaporedje

Kar smo tu povedali za sezname, velja tudi za nize. No, precej metod sicer manjka ... Lahko pa na enak način indeksiramo elemente, delamo rezine, seštevamo in množimo nize, uporabljamo funkcijo `len`, operatorja `in` in `not in`, ...

::left::

```python
>>> niz = 'ABC'
>>> len(niz)
3
>>> niz[0]
'A'
>>> niz[len(niz)-1] 
'C'
>>> niz[-1] 
'C'
>>> niz[0:2]
'AB'
>>> niz[1:]
'BC'
>>> niz[::-1]   
'CBA'
```

::right::

```python
>>> 'Rad imam '+ niz + ' sirček'
'Rad imam ABC sirček'
>>> niz * 3
'ABCABCABC'
>>> niz += ' sirček'
>>> niz
'ABC sirček'
>>> 'sir' in niz 
True
>>> niz.count('s')
1
>>> niz.index('s')
4
>>> palindrom = 'potop'           # palindrom se bere
>>> palindrom == palindrom[::-1]  # z obeh strani enako
True
```

---

# Vgnezdeni seznam *aka.* seznam v seznamu
Element seznama je lahko drug seznam

Poleg dolžine meta krompirja si zapomnimo tudi ime tekmovalca

<div class="code-lg">

```python
>>> rezultati = [[101.9, 'Peter'], [99, 'Janez'], [95, 'Metka']] 
>>> rezultati[0]    # Dobimo podatke prvega meta - to je seznam oblike [dolžina, ime]
[101.9, 'Peter']
>>> rezultati[0][0] # Uporabimo še en nivo naslavljanja
101.9
>>> rezultati[0][1] 
'Peter'
>>> prvi = rezultati[0] # Lahko pa si vgnezdeni seznam zapomnimo v novi spremenljivki
>>> prvi[0]             # in dostopamo do vsebine z enonivojskim indeksom
101.9
>>> rezultati.sort(reverse=True) # Kaj se zgodi, če seznam uredimo?
>>> rezultati
[[101.9, 'Peter'], [99, 'Janez'], [95, 'Metka']]
```

</div>

---
layout: two-cols-title
---
::title::
# Sprehod čez seznam seznamov <Marker>sahovnica</Marker>
Tokrat potrebujemo dve zanki, za vsak nivo eno

::left::

Za primer vzemimo majhno šahovnico 4 x 4 polj. Ima torej 4 vrstice in 4 stolpce. Vsaka vrstica naj bo seznam štirih polj. Imamo tudi seznam vseh vrstic, ki predstavlja celo šahovnico.

<Image src="/img/board_4x4.png" width="250" />

::right::

```python
plosca = [
    ['█','░','█','░'],
    ['░','█','░','█'],
    ['█','░','█','░'],
    ['░','█','░','█'],
    ]

st_vrstic = len(plosca)
st_stolpcev = len(plosca[0])

vrstica = 0
while vrstica < st_vrstic:
    stolpec = 0
    while stolpec < st_stolpcev:
        # Izpišemo vsebino polja brez nove vrstice
        print(plosca[vrstica][stolpec], end='')
        stolpec += 1
    print() # Izpišemo novo vrstico
    vrstica += 1
```

<!-- 
# TODO:

- Pobegni inventar (dodajanje/brisanje/izpis/iskanje elementov)
- Pobegni 2. stopnja šahovnica - premik konja
- uporabi two-cols-title 

-->
