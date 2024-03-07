---
title: Množica
exportFilename: OP-09-Množica.pdf
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
  mono: Fira Mono
---

<!-- 
1. Spremeni `vite.config.ts`, da publicDir kaže na ustrezno mapo gradiva za predavanje 
    publicDir: './assets/09'
   Popravi ProgressBar completed na ustrezno številko predavanja
2. npx slidev OP-09-Množica.md
3. npx slidev --remote=geslo OP-09-Množica.md 
  če si presenter, potem uporabi url, ki ima notri ?password=geslo, da te ne gnjavi za vpis gesla
4. npx slidev build --out dist/04 OP-09-Množica.md
5. npx slidev export OP-09-Množica.md
pdfinfo OP-09-Množica.pdf
Pages :---

6. gswin64 -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/printer -dNOPAUSE -dQUIET -dBATCH -dLastPage=12 -sOutputFile=output.pdf OP-09-Množica.pdf
7. move output.pdf OP-09-Množica.pdf
-->

<ProgressBar bgcolor="#e54240" :completed=9 :total=13 />

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
layout: two-cols-title
---

::title::

# Lastnosti množice
Python temu pravi `set`. Podpira osnovne matematične operacije nad množicami, kot so unija, razlika in presek.

::left::

- Novo množico ustvarimo tako:
  - prazna množica: `set()` ali
  - elementi v zavitih oklepajih:  
    `{'a', 'b', 'c'}` ali ekvivalentno  
    `set(['a', 'b', 'c'])`
  - `{}` ne pomeni prazne množice, ampak prazen *slovar*, ki ga bomo spoznali naslednjič.

- Elementi množice so edinstveni (unikatni) elementi. Torej se elementi v množici ne ponavljajo: `{1, 1, 2}` ➞ `{1, 2}`.

::right::

- Množica je spremenljiv objekt (*plastelin*), elemente lahko dodajamo in brišemo.
- Elementi množice so lahko samo nespremenljivi objekti (*kamen*). Množica ne more vsebovati seznama, slovarja ali druge množice.
- Elementi v množici niso urejeni, njihov vrstni red ni pomemben.

  ```python
  >>> {'b', 'a', 'c', 'd'} 
  {'c', 'd', 'a', 'b'}
  ```

- Elementov v množici ne označujemo z indeksi. Recimo, da imamo `a = {1, 2}`. Naslavljanje `a[0]` sproži napako. Prav tako rezanje `a[1:]`.

---
layout: two-cols-title
---

::title::

# Ustvarjanje množice
Lahko ustvarimo prazno ali neprazno množico ali pa v množico pretvorimo zaporedje.

::left::

Kot smo že omenili, je edini način, da ustvarimo prazno množico ta:

```python
>>> set()
set()
```

Množico z definiranimi elementi ustvarimo tako:

```python
>>> {'sliva', 'češnja', 'jabolko'}
{'sliva', 'češnja', 'jabolko'}
```

ali z uporabo *konstruktorja* objektov:

```python
>>> set(['sliva', 'češnja', 'jabolko'])
{'sliva', 'češnja', 'jabolko'}
```

Konstruktor je posebna funkcija, ki izdela nov objekt.

::right::

V prejšnjem primeru smo v množico pretvorili seznam. V splošnem lahko v množico pretvorimo poljubno drugo zaporedje (seznam, terko, niz, obseg `range`, slovar):

```python
>>> set(('sliva', 'češnja', 'jabolko'))
{'sliva', 'češnja', 'jabolko'}
>>> set('jabolko')  
{'o', 'j', 'a', 'b', 'k', 'l'}
>>> set(range(1,4)) 
{1, 2, 3}
```

Pretvarjanje zaporedja v množico ima pomembno posledico: s tem odstranimo podvojene vrednosti:

```python
>>> set(('sliva', 'češnja', 'jabolko', 'sliva'))
{'sliva', 'češnja', 'jabolko'}
```

---
layout: two-cols
---

# Funkcije nad množico
Stari znanci

Kot pri seznamih in terkah, lahko nad množico kličemo funkcije:

- `len()`: moč množice (število elementov)
- `sum()`: vsota elementov množice; dobimo napako, če elementi množice niso števila
- `min()` in `max()`: podobno kot `sum()`, sta tudi ti dve funkciji definirani za številčne elemente množice

```python
>>> m = {1, 2, 3}  
>>> len(m) 
3
>>> sum(m) - min(m) + max(m)
8
```

::right::

# Sprehod čez množico
Elementov množice ne moremo indeksirati

Za sprehod preko elementov množice lahko uporabimo zanko `for`:

```python
sadje = {'češnja', 'sliva' , 'jabolko'}
for sadez in sadje:
    print(sadez)
```

Če želimo oštevilčiti elemente, lahko uporabimo `enumerate()`:

```python
for i, sadez in enumerate(sadje):
    print(i, sadez)
```

Izpis:

```
0 sliva
1 češnja
2 jabolko
```

---
layout: two-cols-title
---

::title::

# Operatorji nad množico
Definirani so operatorji vsebovanosti in primerjanja

::left::

## Vsebovanost

Z operatorjem `in` (ali `not in`) lahko preverimo pripadnost elementa množici. Torej, ali element $x$ pripada množici $M$: $x \in M$. Lahko trdimo tudi, da element množici ne pripada: $x \notin M$.

```python
>>> M = {'Merkur', 'Venera', 'Zemlja', 'Mars'}
>>> x = 'Pluton'
>>> x in M
False
>>> x not in M
True
```

::right::

## Primerjanje množic

- (Ne)enakost

```python
>>> {1, 2} == {2, 1}
True
>>> {1, 2, 3} != {2, 1, 1}
True
```

- Relacija podmnožice: $A \subset B$

  Množica A je podmnožica množice B, če so vsi elementi množice A vključeni tudi v množico B.

```python
>>> {1, 2} < {0, 1, 2, 3} # {1, 2} ⊂ {0, 1, 2, 3}
True
>>> {1, 2} < {0, 1}       # {1, 2} ⊄ {0, 1}
False
>>> {1, 2} <= {0, 1}
False
```

---
layout: two-cols-title
---

::title::

# Metode množice
Najprej si oglejmo metode, ki dodajo ali odstranijo element.

::left::

## `mnozica.add(x)`

V množico `mnozica` doda element `x`. Če v tej množici že obstaja element z vrednostjo `x`, metoda `add()` nima učinka.

```python
>>> jedilnik = set()
>>> jedilnik.add('juha')
>>> jedilnik.add('glavna jed')
>>> jedilnik
{'glavna jed', 'juha'}
>>> jedilnik.add('juha')
>>> jedilnik
{'glavna jed', 'juha'}
```

::right::

## `mnozica.remove(x)`

Iz množice `mnozica` izbriše element `x`. Če ga ni, javi napako.

```python
>>> jedilnik.remove('juha')
>>> jedilnik
{'glavna jed'}
>>> jedilnik.remove('sladica')
```

<div class="error">

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'sladica'
```

</div>

<br/>

## `mnozica.discard(x)`

Iz množice izbriše element `x`. Če ga ni, je tiho.

---
layout: two-cols-title
---

::title::

# Metode množice: operacije nad množicami
Tako kot pri matematiki

::left::

## Unija

Unija množic A in B je množica, ki vsebuje elemente iz obeh. Matematično to zapišemo kot $A~\cup~B$, v Pythonu pa:

- z uporabo operatorja `A | B` ali
- s klicem metode `A.union(B)`.

Izračunamo lahko tudi unijo več množic, denimo:

- `A | B | C`
- `A.union(B, C)`

::right::

<div class="text-center">

<Image class="m-auto" src="/img/mnozice-unija.png" width="300"/>

$$A \cup B$$

`A | B`

</div>

---
layout: two-cols-title
---

::title::

# Metode množice: operacije nad množicami
Tako kot pri matematiki

::left::

## Presek

Presek množic A in B je množica elementov, ki so hkrati v A in v B. Matematično to zapišemo kot $A~\cap~B$, v Pythonu pa:

- z uporabo operatorja `A & B` ali
- s klicem metode `A.intersection(B)`.

Izračunamo lahko tudi presek med več množicami, recimo:

- `A & B & C`
- `A.intersection(B, C)`

::right::

<div class="text-center">

<Image class="m-auto" src="/img/mnozice-presek.png" width="300"/>

$$A \cap B$$

`A & B`

</div>

---
layout: two-cols-title
---

::title::

# Metode množice: operacije nad množicami
Tako kot pri matematiki

::left::

## Razlika

Razlika množic A in B je množica elementov, ki so v A in niso v B. Matematično to zapišemo kot $A~\backslash~B$, v Pythonu pa:

- z uporabo operatorja `A - B` ali
- s klicem metode `A.difference(B)`.

Izračunamo lahko tudi razliko več množic, npr.:

- `A - B - C`
- `A.difference(B, C)`

<br/>

<mark>Pozor:</mark> $A-B$ ni enako kot $B-A$.

::right::

<div class="text-center">

<Image class="m-auto" src="/img/mnozice-razlika.png" width="300"/>

$$A~\backslash~B$$

`A - B`

</div>

---
layout: two-cols-title
---

::title::

# Metode množice: operacije nad množicami
Tako kot pri matematiki

::left::

## Simetrična razlika

Simetrična razlika množic A in B je množica elementov, ki so v njuni uniji, a niso v njunem preseku. Matematično to zapišemo kot $A~\triangle~B$, v Pythonu pa:

- z uporabo operatorja `A ^ B` ali
- s klicem metode `A.symmetric_difference(B)`.

Izračunamo lahko tudi simetrično razliko več množic, naprimer:

- `A ^ B ^ C = (A ^ B) ^ C`

::right::

<div class="text-center">

<Image class="m-auto" src="/img/mnozice-sim-razlika.png" width="300"/>

$$A~\triangle~B = (A \cup B) \backslash (A \cap B)$$

`A ^ B`

</div>

---
layout: two-cols-title
---

::title::

# Operacije nad množicami: primeri
*"O okusih se ne razpravlja."* - latinski pregovor

::left::

```python
>>> Maja = {'The Weeknd', 'Shakira', 'Joker Out'}
>>> Lara = {'Shakira', 'Vlado Kreslin', 'Joker Out'}
>>> Tomi = {'Newsboys', 'The Weeknd', 'Joker Out'}

# Kakšen okus imata dekleti?
>>> Maja | Lara
{'Vlado Kreslin', 'Shakira', 'Joker Out', 'The Weeknd'}

# Vsi radi poslušajo ...
>>> Maja & Lara & Tomi
{'Joker Out'}

# Kateri izvajalec je skupen samo Tomiju in Lari?
>>> Tomi & Lara - Maja 
set()

# Kateri izvajalci niso v nobenem preseku?
>>> (Tomi ^ Lara ^ Maja) - (Maja & Lara & Tomi)
{'Newsboys', 'Vlado Kreslin'}
```

::right::

<div class="text-center">

<Image class="m-auto" src="/img/mnozice.png" width="300"/>

</div>
