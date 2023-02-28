---
title: Spoznavanje okolja
exportFilename: OP-02-Spoznavanje-okolja.pdf
download: false
info: Predavanja pri predmetu Osnove programiranja
theme: default
themeConfig:
  primary: #e11d48
background: false
class: text-center
highlighter: shiki
lineNumbers: false
drawings:
  enabled: true
  persist: false
  presenterOnly: true
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
    publicDir: './assets/02'
   Popravi ProgressBar completed na ustrezno številko predavanja
2. npx slidev OP-02-Spoznavanje-okolja.md
3. npx slidev --remote=geslo OP-02-Spoznavanje-okolja.md 
  če si presenter, potem uporabi url, ki ima notri ?password=geslo, da te ne gnjavi za vpis gesla
4. npx slidev build --out dist/02 OP-02-Spoznavanje-okolja.md
5. npx slidev export OP-02-Spoznavanje-okolja.md
6. gswin64 -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/printer -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf OP-02-Spoznavanje-okolja.pdf
7. move output.pdf OP-02-Spoznavanje-okolja.pdf
-->

<ProgressBar bgcolor="#e54240" completed="2" total="13"/>

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

# Programski jezik Python

Osnove programiranja bomo odkrivali z visokonivojskim jezikom <mdi-language-python/> Python

[https://www.python.org](https://www.python.org)

>"Si moram nanestiti Python?"

Ni nujno, lahko pa. Uporabljali bomo namreč orodje, ki ima Python že vgrajen.

## Zakaj ravno Python?

- Python je eden najbolj priljubljenih programskih jezikov
- Enostaven za začetnike, a hkrati dovolj močan za stare mačke
- Koda je pregledna, čista, berljiva → zelo blizu psevdo kodi
- "Baterije so priložene" → obširna knjižnica razpoložljivih modulov
- Je kdo omenil kemijo? Python se lepo razume z orodji računalniške kemije
  ([PyMOL](https://pymol.org/), [Maestro](https://www.schrodinger.com/products/maestro), [RDkit](https://www.rdkit.org/))

---

# Prvi zmenek

Python je interaktivni <Mark>tolmač</Mark> → ukaze sproti tolmači v jezik računalnika, tj. <Mark>strojni</Mark> jezik

## Zagon ukaznega poziva na Windows

Pritisnite tipko <kbd><mdi-microsoft-windows/></kbd>, vtipkajte `cmd` in pritisnite tipko <kbd>enter</kbd>.

Nato vpišite `python` in pritisnite <kbd>enter</kbd>. To bo seveda delovalo le, če imate nameščen Python.

Začnimo pogovor v slogu osnovnošolske matematike:

```python
>>> 1 + 1
2
>>> 0 - 42
-42
>>> 3.14 * 2
6.28
```

Označba `>>>` predstavlja naš vnos. Ko pritisnemo <kbd>enter</kbd>, se v vrstici nižje izpiše odgovor.

---

# Osnovni operatorji
Matematični operatorji, ostale pogledamo pozneje

| **operator** | **opis** | **primer**|
| :----------: | :------- | --------- |
| `+`  | seštevanje | `1 + 2` → `3` |
| `-`  | odštevanje | `1 - 2` → `-1` |
| `*`  | množenje | `3.14 * 2` → `6.28` |
| `/`  | deljenje | `3 / 2` → `1.5` |
| `//` | celoštevilsko deljenje | `3 // 2` → `1` |
| `%`  | ostanek pri deljenju (modulo) | `8 % 3` → `2` |
| `**` | potenciranje | `2 ** 3` → `8` |
| `()` | oklepaji (določanje prednosti) | `(1 + 2) * 3` → `9` |

---

# Podatkovni tipi
Vsaka vrednost oziroma podatek ima posebno lastnost: <Mark>podatkovni tip</Mark>.

Tip podatka torej govori o tem, kaj podatek predstavlja in kaj lahko z njim počnemo.

## `int`
celo število (ang. *integer*)
  
Primeri: `0`, `1`, `42`, `-273`, `123456789123456789000000000000000000001`

## `float`
necelo število (ang. *floating point number*). Pozor: decimalna pika namesto "naše" decimalne vejice.

Primeri: `0.0`, `-42.33`, `3.141592653589793`

---

# Podatkovni tipi: nadaljevanje

## `str`
niz, zaporedje znakov (ang. *string*). Niz zapišemo v enojne `'`, dvojne `"` ali trojne `'''` narekovaje.

<div class="grid grid-cols-2 gap-x-4">
<div>

`'Živjo, svet!'`

`"Moj program je kot 🚀"`

`'ᚩᛋᚾᚩvᛖ ᛈᚱᚩᚷᚱᚫᛗᛁᚱᚫᚾjᚫ'`

`'42'`

</div>
<div>

`"0.0"`

`"Sean O'Connery"`

`'Vzkliknil je: "Pri moji duši!"'`

 `'''Vzkliknil je: "Pr' méj duš'!"'''`

</div>
</div>
<br/>

## `bool`
logična vrednost (ang. *boolean*), lahko je bodisi *resnično* (`True`) bodisi *neresnično* (`False`).
O tem podatkovnem tipu bomo precej govorili čez teden dni. Oplazili pa smo ga tudi pretekli teden,
ko smo govorili o Evklidovem algoritmu in odločitvah ter zankah.

---

# Podatkovni tipi: igranje
Kateri podatkovni tip dobimo, če ...

<div class="grid grid-cols-2 gap-x-4">

<div>

```python
>>> 1 + 2
3
>>> 1 + 1.5
2.5
>>> 1 * 2
2
>>> 1 * 2.2
2.2
>>> 1 / 2
0.5
>>> 2 / 2
1.0
>>> 10 // 3
3
>>> 10 // 2.5
4.0
>>> 10 // 2.3
4.0
>>> 10 % 3
1
```

</div>
<div>

```python
>>> 'Ana' + 'Jaka'
'AnaJaka'
>>> 'Ana+' + 'Jaka'
'Ana+Jaka'
>>> 'Dober' + ' ' + 'dan' + '!'
'Dober dan!'
>>> '1' + '1'
'11'
>>> '1 + 1'
'1 + 1'
>>> 'bla' * 3
'blablabla'
```

</div>
</div>

---

# Kdor dela, greši

<div class="error">

```
>>> 6 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

</div>

Hm, delili smo z 0, ups. Tega ne prenese niti papir.

<div class="error">

```
>>> 'Ana' * 'Jaka'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
```

</div>

Nismo mislili takšnega razmnoževanja, kajne?

<div class="error">

```
>>> 'bla' * 3.14
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'float'
```

</div>

Nize lahko razmnožujemo samo s celimi števili.

---

# Kdor veliko dela, še bolj greši

<div class="error">

```
>>> 1 + '1'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

</div>

`1` očitno ni isto kot `'1'`, saj to že vemo. Števil in nizov ne znamo seštevati. Kaj pa naj bi dobili?

<div class="error">

```
>>> '1' + 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

</div>

Podobno kot prej. Nizu `'1'` smo želeli prilepiti celo število `1`, kar pa ne gre kar tako zlahka.

<div class="error">

```
>>> 'Dober' + dan
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dan' is not defined
```

</div>

Opa, na nekaj smo pozabili. `dan` bi moral biti niz `'dan'`, pri nas pa je kaj? "name"? Kaj je to?

---

# Funkcije
Funkcije <Mark>sprejemajo argumente</Mark> in (lahko) <Mark>vračajo rezultat</Mark>.

Klic funkcije: `ime_funkcije(argument_1, argument_2, ...)`

- funkcijo vedno kličemo z oklepaji, tudi če ni ničesar v njih
- argumenti funkcije so navedeni v oklepajih in so ločeni z vejicami
- nekaj primerov:

| **funkcija** | **opis** | **primer**|
| :----------: | :------- | --------- |
| `abs`  | absolutna vrednost | `abs(-42)` → `42` |
| `pow`  | potenca (podobno kot `**`) | `pow(2, 3)` → `8` |
| `min`  | najmanjša vrednost | `min(2, -42, 8)` → `-42` |
| `max`  | največja vrednost | `min(2, -42, 8)` → `8` |
| `print`  | izpis v terminal | `print("Rezultat je", 42)` → `Rezultat je 42` |

<!-- 
Funkcija pow ima še tretji argument, ki je modulus, zato ni čisto enako kot **. pow in math.pow sta malo počasnejša od ** za majhna, cela števila.
Za računanje modula pa je pow neprimerno hitrejši, primer:
2**1234567890 % 4
pow(2, 1234567890, 4) 
-->

---

# Vgrajene funkcije
Te funkcije so vedno dostopne. [Seznam za Python 3.11](href="https://docs.python.org/3/library/functions.html").

<a href="https://docs.python.org/3/library/functions.html" target="_blank"><Image width="370" src="/img/python-built-in-functions.png" alt="Vgrajene funkcije"/></a>

---

# Izraz
"Nekaj", kar se da izračunati

```python
1 + 2
1+5 * 8+1
(1+5)*(8+1)
2**3 % 7
pow(2, 3, 7)
((4-2.2)**2 + (-2-1)**2)**0.5
max(min(0.5, 1), 0)
'Rekel je: "' + 'bla'*3 + '".'
```

Ko Pythonovi ukazni vrstici podamo izraz in pritisnemo <kbd>enter</kbd>, dobimo <Mark>rezultat</Mark> izraza.

```python
>>> 1+5 * 8+1
42
```

Si lahko kam shranimo ta rezultat za mrzlo zimo?

---
layout: fact
---
# a = 42
spremenljivka = izraz

<Mark>Spremenljivka</Mark> je na levi, na desni pa je <Mark>izraz</Mark>. Nikoli obratno!

Vmes je `=`, ki je <Mark>operator prirejanja</Mark>. To ni navaden enačaj.

Ta rezultat se nato shrani v spomin, ki ga lahko označimo, poimenujemo.

Namesto `=` bi si lahko prirejanje predstavili tudi s puščico ← :

`a` ← `42`

Namesto `42` bi seveda lahko napisali poljuben izraz, recimo:

`a = 1+5 * 8+1`

Pravkar smo spoznali <Mark>prireditveni stavek</Mark>.

---
layout: image-right
image: '/img/jesse-orrico-h6xNSDlgciU-unsplash.jpg'
caption: 'Fotografija: Jesse Orrico'
url: 'https://unsplash.com/photos/h6xNSDlgciU'
---

# Spremenljivke
Včasih jim bomo rekli tudi preprosto <Mark>imena</Mark>.

Spremenljivko (ang. *variable*) uporabimo za shranjevanje vrednosti izraza.

```python
>>> a = 42
```

Ko želimo uporabiti to shranjeno vrednost, preprosto rečemo `a`, takole:

```python
>>> b = a + 1
>>> b
43
```

Če naslovim spremenljivko, ki ne obstaja:

<div class="error">

```
>>> c * 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'c' is not defined
```

</div>

---

# Spremenljivke in uganke

<!-- TODO: podobno daj v kviz 03! -->
<!-- Nagubajmo možgane in ne pozabimo, da operator prirejanja `=` ni matematični enačaj. -->

<div class="grid grid-cols-2 gap-x-4">

<div>

Kakšno vrednost ima `b` po naslednjem zaporedju stavkov?

```python {monaco}
a = 15
b = a + 2 * a
```

<div v-click>

<span class="solution">Rešitev: `b` postane 45. Prvi stavek spremenljivki `a` priredi celo število 15. Nato se obdela drugi stavek, kjer se najprej izračuna izraz na desni strani: `15 + 2 * 15`, ki ima rezultat 45. Zatem se ta rezultat priredi spremenljivki `b`.</span>

</div>

<div v-click>

Še ena:

```python {monaco}
a = 15
b = a + 30 % a
```

</div>
<div v-click>

<span class="solution">Rešitev: `b` postane 15. Podobno kot prej, `a` najprej postane 15. V izrazu `15 + 30 % 15` se najprej izračuna ostanek pri deljenju 30 s 15, ki je 0, nato se ta 0 prišteje k 15 in rezultat je 15, ki se zatem priredi `b`ju.</span>

</div>
</div>
<div>

<div v-click>

Kaj pa zdaj?

```python {monaco}
a = 15
b = a
b = 'a'
```

</div>
<div v-click>

<span class="solution">Rešitev: `b` postane niz `'a'`. Najprej `a` postane 15. Nato `b`ju priredimo vrednost `a`ja, torej 15. V tretjem stavku pa `b`ju priredimo vrednost `'a'`, ki je mimogrede niz, in s tem povozimo prejšnjo vrednost.</span>

</div>
<div v-click>

Še zadnja! Koliko je `a` na koncu?

```python {monaco}
a = 15
a = a + 1
```

</div>
<div v-click>

<span class="solution">Rešitev: Točno tako, `a` postane 16. Najprej `a` postane 15. Nato v drugi vrstici izračunamo izraz na desni, ki je `a + 1`, torej `15 + 1`. Rezultat, ki je seveda 16, se nato vpiše v `a` in s tem povozi prejšnjo vrednost.</span>

</div>

</div>
</div>

<!-- 
Opomba: v polja za kodo lahko sproti pišeš. Piši komentarje in jim povej, kaj je to.
-->

---

# Imena spremenljivk
Še nekaj bontona, ko spremenljivkam dajemo imena

<div class="grid grid-cols-2 gap-x-4">

<div>

- vsebujejo lahko črke -- najbolje, da samo črke angleške abecede

- vsebujejo lahko številke, vendar ne na prvem mestu
  
  ~~`24kur = 'www.24kur.si'`~~

- začnejo naj se z malo črko
  
  `pi = 3.14` in ne ~~`Pi = 3.14`~~

- ne smejo vsebovati presledkov -- več besed ločimo s podčrtajem

  `novo_geslo` in ne ~~`novo geslo`~~ ali ~~`novogeslo`~~ ali ~~`novoGeslo`~~

</div>
<div>

- majhna ni velika
  
  `novo_geslo` ni niti približno isto kot `Novo_GESLO`

- izogibamo se imenom vgrajenih funkcij
  
  raje rečemo `maks = max(2, 3)`
  
  in ne `max = max(2, 3)`

- ne moremo uporabiti teh (rezerviranih) besed:
  
<!-- 
  import keyword 
  list = keyword.kwlist 
  print("No. of keywords present in current version :", 
  len(list)) 
  print(list)  
-->
  
  `False`, `None`, `True`, `and`, `as`, `assert`, `async`, `await`, `break`, `class`, `continue`, `def`, `del`, `elif`, `else`, `except`, `finally`, `for`, `from`, `global`, `if`, `import`, `in`, `is`, `lambda`, `nonlocal`, `not`, `or`, `pass`, `raise`, `return`, `try`, `while`, `with`, `yield`

</div>
</div>

---
layout: fact
---

# Dovolj!
Napišimo že kakšen program

> Danes bo delno oblačno s temperaturo do 30 stopinj.
>
> Oprostite, pingvini, za paniko, mislil sem 30 °F.
>
> To je udobnih -1 °C.

Napišimo program, ki bo pretvarjal med °C in °F.

---

# Prvi program: pretvornik med °C in °F

Kakšen bo naš algoritem, postopek? Kako ga bomo zakodirali?

1. Imamo številčno vrednost $T_F$, ki pomeni stopinje Fahrenheita.
2. Uporabimo naslednjo enačbo za pretvorbo v stopinje Celzija:

$$
T_C = \frac{(T_F - 32)}{1{, }8}\quad .
$$

3. Izpišemo $T_C$.

<hr/>
<br/>

Programsko kodo lahko napišemo v ukazno vrstico ...

```python
>>> temp_F = 30
>>> temp_C = (temp_F - 32) / 1.8
>>> temp_C
-1.1111111111111112
```

... kar pa je precej neuporabno. Za ponovni izračun pri drugi vrednosti $T_F$, bi morali ponoviti vse ukaze. Bolje?

---

# Prvi program: napišimo ga
Kam? Na papir? Dober začetek. Potem pa v Wordov dokument! Saj te prime, pa te mine ...

<div class="grid grid-cols-3 gap-x-4">

<div>

## Asketsko

![notepad](/img/prvi-notepad-cmd.png)

Ups, program ničesar ne izpiše. V zadnji vrstici dodajmo `print`.

</div>

<div>

## Za silo

![notepad](/img/prvi-IDLE.png)

Razvojno okolje IDLE

</div>

<div>

## Pr' Toniju

![notepad](/img/prvi-Thonny.png)

Razvojno okolje Thonny

</div>

</div>

---

<!-- HERE: Do tukaj prišli 2023 -->

# Urejevalnik kode - razvojno okolje
Programiranje je udobnejše z integriranim razvojnim okoljem
(ang. integrated development environment - IDE)

## [IDLE](https://docs.python.org/3/library/idle.html)

- Zelo preprost (zanimivost: napisan je v Pythonu)
- Ko namestite Python, se privzeto namesti tudi IDLE
- IDLE → Integrated Development and Learning Environment

## [Thonny](https://thonny.org/)

- Nekoliko, khm, "lepši" kot IDLE
- Zasnovan za učenje programiranja
- [Navodila za namestitev](https://ucilnica.fri.uni-lj.si/mod/page/view.php?id=42205)

## Drugo: [Visual Studio Code](https://code.visualstudio.com/), [PyCharm](https://www.jetbrains.com/pycharm/), [Spyder](https://www.spyder-ide.org/)
<!-- [Navodila za namestitev in delo s Pythonom](https://code.visualstudio.com/docs/python/python-tutorial) |
  [navodila v slovenščini](https://www.epf.um.si/fileadmin/user_upload/Izpitni_center/Dokumenti/MLSA_Visual_Studio_Code_2021.pdf) -->

---

# Pogovor z uporabnikom

## `print`
Ko želimo uporabnika našega programa o čem obvestiti, to najlaže storimo s funkcijo `print`, ki izpisuje v terminal (lupina/konzola/ukazni poziv). Pravimo tudi, da izpisuje na <Mark>standardni izhod</Mark>.

```python
>>> print('Odgovor na vprašanje o vesolju, življenju in sploh vsem je:', 1+5*8+1, '!'*3)
Odgovor na vprašanje o vesolju, življenju in sploh vsem je: 42 !!!
```

<br/>

## `input`
Ko želimo od uporabnika našega programa dobiti kakšen podatek, ga zanj prosimo s funkcijo `input`.

```python
>>> najljubsi_okus_sladoleda = input('Tvoj najljubši okus 🍨? ')
Tvoj najljubši okus 🍨? Jogurt z gozdnimi sadeži
>>> print(najljubsi_okus_sladoleda, 'je tvoj najljubši okus, kajne?')
Jogurt z gozdnimi sadeži je tvoj najljubši okus, kajne?
```

Pravimo, da funkcija `input` bere s <Mark>standardnega vhoda</Mark>.

---

# Prvi program: poskus izboljšave
<p></p>

Psihološki profil našega prvega programa (glej tri strani nazaj)

> Ta program je asocialen. Ne zanima ga mnenje drugega. Ima samo svoj prav.
>
> Njegovo vedenje je družbeno nesprejemljivo, ne pozna osnov bontona. Ni vljuden. Je pa matematični genij, to pa.

Dodajmo ščepec komunikacijskih veščin in nekaj osnovne čustvene inteligence.

```python
temp_F = input('Vnesi temperaturo v °F: ')
temp_C = (temp_F - 32) / 1.8
print(temp_F, '°F je', temp_C, '°C.')
```

Ojoj, spet rdeče! Kaj je tu narobe? Kje tiči napaka? Berimo ...

<div class="error">

```
Traceback (most recent call last):
  File "prvi-v2.py", line 2, in <module>
    temp_C = (temp_F - 32) / 1.8
TypeError: unsupported operand type(s) for -: 'str' and 'int'
```

</div>

V katerem grmu torej tiči zajec? No, a je zajec? Zajčki so navadno srčkani. Zato raje recimo ščurek ali kar hrošč. Kje v našem programu torej tiči hrošč?

---

# Razhroščevanje
Podobno kot razkoščičevanje češenj: da si ne polomimo zob, ko jemo češnjev štrudelj.

Navodila za Thonnyja:

1. Imamo programsko kodo v urejevalniku (bodisi jo napišemo na novo bodisi odpremo obstoječo datoteko).
2. Zaženemo razhroščevalnik na enega od načinov:
   - v orodni vrstici kliknemo na gumb <img class="inline w-8" src="/img/thonny-debug.png" /> ali
   - v meniju izberemo `Poženi` → `Razhroščevanje trenutne skripte (lepše)` ali
   - pritisnemo kombinacijo tipk <kbd>Ctrl</kbd> + <kbd>F5</kbd>.
3. Aktivira se razhroščevalnik, ki ustavi izvajanje programa <MArk>pred izvajanjem</Mark> prvega stavka.
   <img class="inline w-100" src="/img/thonny-debug-highlight.png" />
4. Skozi program se sedaj premikamo z ukazi:

  <div class="grid grid-cols-4 gap-x-4">
  <div class="border">
    <img class="inline w-8" src="/img/thonny-step-over.png" /> Stopi čez stavek <kbd>F6</kbd>
  </div>
  <div class="border">
    <img class="inline w-8" src="/img/thonny-step-into.png" /> Stopi v stavek <kbd>F7</kbd>
  </div>
  <div class="border">
    <img class="inline w-8" src="/img/thonny-step-out.png" /> Stopi ven (iz česa?)
  </div>
  <div class="border">
    <img class="inline w-8" src="/img/thonny-continue.png" /> Nadaljuj <kbd>F8</kbd>
  </div>
  </div>

(se nadaljuje)

---

# Razhroščevanje: nadaljujmo

5. Izvedimo prvi stavek tako, da pritisnemo <kbd>F6</kbd>. Pozvani bomo, da vnesemo temperaturo v °F. Ubogajmo in nato pritisnimo <kbd>enter</kbd>.
6. Ko smo v drugi vrstici, pritiskajmo <kbd>F7</kbd> in opazujmo postopno računanje izraza. Kmalu zagledamo tole:
   <img class="inline w-100" src="/img/thonny-debug-found.png" />
7. Spremenljivka `temp_F` očitno vsebuje *niz* `'30'` in ne *števila* `30`. Zahtevamo, da Python od niza odšteje celo število. Preveč smo zahtevni. Pametnejši odneha. Dobimo obvestilo o napaki.

8. Našli smo hrošča! Tiči v drugi vrstici našega programa.

    Kako je prišel tja? Napačno smo predpostavljali, da se bo vpisana temperatura uporabila kot število.

    Pa se ni. Korenine te napake rastejo iz funkcije `input`, ki vrne uporabnikov odgovor in to <Mark>vedno kot niz</Mark>.

9. Kako streti tega hrošča? Vrednost v `temp_F` moramo pretvoriti v število.

---

# Pretvorba podatkovnih tipov
Spomnimo se: podatki (spremenljivke) imajo svoj podatkovni tip. Funkcija `type()` nam vrne podatkovni tip.

<div class="grid grid-cols-2 gap-x-4">
<div>

## niz → število
Uporabimo funkcijo `int()` ali `float()`.

```python
a = '1'
b = '2.2'
a_num = int(a)
b_num = float(b)
print(a_num + b_num)
```

Programček izpiše `3.2`, lepo!

Kaj bi dobili, če bi rekli `float(a)`? `1.0`.

Kaj bi dobili, če bi rekli `int(b)`?

<div class="error">

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10:'2.2'
```

</div>

</div>
<div>

## število → niz
Uporabimo funkcijo `str()`.

```python
a = 1
b = 2.2
a_str = str(a)
b_str = str(b)
print(a_str + b_str)
```

Programček izpiše `12.2`, tudi lepo!

```python
>>> type(a)
<class 'int'>
>>> type(b)
<class 'float'>
>>> type(c)
<class 'str'>
```

</div>
</div>

---
layout: image-right
image: '/img/ilse-orsel-cPiKUJkTWWA-unsplash.jpg'
caption: 'Fotografija: Ilse Orsel'
url: 'https://unsplash.com/photos/cPiKUJkTWWA'
---

# Prvi program: to je to
Na krilih novih spoznanj dokončajmo delo

Našo kodo tudi dokumentirajmo: uporabimo komentarje (znak `#`) ali več-vrstične nize.

```python
"""Pretvornik enot

Program pretvarja vnešeno temperaturo 
iz stopinj Fahrenheita v stopinje Celzija.
"""
temp_F = input('Vnesi temperaturo v °F: ')
temp_F = float(temp_F) # Niz pretvorimo v število
temp_C = (temp_F - 32) / 1.8 # 1.8 = 9/5
print(temp_F, '°F je', temp_C, '°C.') # Izpis
```

Pritisnemo na <kbd>F5</kbd> in zadržimo dih ...

```
Vnesi temperaturo v °F: 30
30.0 °F je -1.1111111111111112 °C.
```

👏⭐🏆💪👌 Juhuhu! 👌💪🏆⭐👏
