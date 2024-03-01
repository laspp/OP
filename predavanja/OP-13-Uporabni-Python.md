---
title: Uporabni Python
exportFilename: OP-13-Uporabni-Python.pdf
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
    publicDir: './assets/13'
   Popravi ProgressBar completed na ustrezno številko predavanja
2. npx slidev OP-13-Uporabni-Python.md
3. npx slidev --remote=geslo OP-13-Uporabni-Python.md 
  če si presenter, potem uporabi url, ki ima notri ?password=geslo, da te ne gnjavi za vpis gesla
4. npx slidev build --out dist/13 OP-13-Uporabni-Python.md
5. npx slidev export OP-13-Uporabni-Python.md
pdfinfo OP-13-Uporabni-Python.pdf
Pages :---

6. gswin64 -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/printer -dNOPAUSE -dQUIET -dBATCH -dLastPage=5 -sOutputFile=output.pdf OP-13-Uporabni-Python.pdf
7. move output.pdf OP-13-Uporabni-Python.pdf
-->

<ProgressBar bgcolor="#e54240" :completed=13 :total=13 />

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

# Uporabimo Python za ... obdelavo slik <Marker>obdelava-slik.py</Marker>

::left::

## Motivacija

Denimo, da imamo kup datotek s fotografijami. Radi bi zmanjšali/povečali dimenzije fotografij, poleg tega pa bi radi tudi poenotili imena datotek.

Imena datotek so trenutno zapisana tako: `slika_1.jpg`. Radi bi, da je številka, ki sledi znaku `_`, zapisana s tremi mesti, torej: `slika_001.jpg`. Na ta način bomo na različnih operacijskih sistemih datoteke uredili po imenu na isti način.

## Uporabljeni moduli

- `os` za delo z imeniki, za preimenovanje
- `shutil` za kopiranje datotek
- `PIL` (`pillow`) za skaliranje slike

::right::

## Rešitev

Napišimo program, ki:

- v podanem imeniku poišče vse datoteke z določeno končnico, npr. `jpg`,
- iz njihovega imena izlušči posamezne sestavine (`predpona`, `_`, `številka`, `končnica`),
- sestavi novo ime in v ciljnem imeniku ustvari kopijo datoteke s tem imenom,
- kopijo še obdela tako, da sliko poveča/zmanjša za poljuben faktor.

---
layout: two-cols-title
---

::title::

# Uporabimo Python za ... vremensko napoved <Marker>vreme.py</Marker>

::left::

## Motivacija

Radi bi pridobili vremenske podatke za prihodnje dni. Spletni portal [Open-Meteo](https://open-meteo.com/) je odprtokodna in prosta platforma, ki ponuja podatke o vremenu po celem svetu. Ponujajo aplikacijski programski vmesnik (ang. *application programming interface*, API), preko katerega dostopamo do podatkov.

## Uporabljeni moduli

- `requests` za pridobivanje podatkov s strežnika
- `json` za delo z datotekami JSON
- `datetime` za delo z datumi

::right::

## Rešitev

Napišimo program, ki:

- pošlje zahtevek na končno točko `https://api.open-meteo.com/v1/forecast`,
- sprejme odgovor strežnika v formatu JSON,
- izlušči podatke o temperaturi in verjetnosti padavin za prihodnje dni ter
- jih izpiše na zaslon v obliki urejene preglednice.

---
layout: two-cols-title
---

::title::

# Uporabimo Python za ... izris grafa <Marker>graf_vreme.py</Marker>

::left::

## Motivacija

Vremensko napoved bi radi prikazali v obliki grafa.

![Graf vreme](/img/graf_vreme.png)

::right::

## Uporabljeni moduli

- `json` za delo z datotekami JSON
- `matplotlib` za izris grafa
- `datetime` in `locale` za delo z datumi v slovenščini

## Rešitev

Napišimo program, ki:

- naloži podatke, ki jih je v formatu JSON shranil program <Tag>vreme.py</Tag>,
- ustvari grafikon z dvema ločenima *y*-osema,
- ga prikaže na zaslonu in shrani v datoteko PDF.

---
layout: two-cols-title
---

::title::

# Namestitev modulov v Thonnyju
Kako namestimo module, ki niso del standardne knjižnice

::left::

1. V glavnem meniju Thonnyja izberemo **Orodja** → **Upravljanje paketov**.
2. Odpre se okno, prikazano spodaj.

![Thonny - moduli](/img/thonny-paketi-matplotlib-2.png)

::right::

3. V iskalno okno napišemo ime modula (npr. `matplotlib`) in pritisnemo gumb **Išči na PyPl**.
4. Izberemo ustrezen modul in kliknemo na gumb **Namestitev**.
5. Tako, nameščeni modul lahko uporabljamo v svojem programu.
