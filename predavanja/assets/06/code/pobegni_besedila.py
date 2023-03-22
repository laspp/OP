
"""Besedila za igro Pobegni!

Imena spremenjlivk se zacnejo brez ''.
"""

# Splošno
izbira_dejanja = '\nIzberi eno od dejanj:'
izbira_input = 'Izbira: '
napacna_izbira = 'Napačna izbira!'
glavni_meni = """----------------------
X: izhod"""
izhod_iz_igre = 'Že konec? Nasvidenje!'
resna_napaka = 'Resna napaka, končujem program.'

# Začetni zaslon - uvod
uvod = """
POBEGNI!

Znajdeš se v neznani sobi.
"Zakaj sem tu?" se sprašuješ.
Hočeš pobegniti."""

# Stopnja 1
s1_opis_sobe = """
Soba ima modra vrata.
Sredi sobe je miza in na njej nekaj."""

# V vsaki vrstici je eno dejanje
s1_dejanja = [
  'Odpri modra vrata.',
  'Poglej, kaj je na mizi.'
  ]

s1_vrata = """
Modra vrata so zaklenjena z elektronsko ključavnico."""

s1_vrata_input = 'Vnesi PIN za odklep: '
s1_vrata_preverjam_pin = 'Preverjam PIN ...'
s1_vrata_pravilen_pin = 'PIN je pravilen! Vrata so odklenjena.'
s1_vrata_napacen_pin = 'Napačen PIN!'

s1_miza = """
Stopiš do mize, na kateri leži kladivo in
zaprašen zvezek. Odpreš zvezek in ven pade listič,
na katerem je zapisano:
      +~~~~~~~~~~~~~~~~~~~~~~~+
      |                       |
      |     !uganka!       |
      |                       |
      +~~~~~~~~~~~~~~~~~~~~~~~+"""

# Stopnja 2
s2_opis_sobe = """
Skozi modra vrata vstopiš v prostorno halo.
Spominja te na grajsko plesno dvorano, v daljavi
celo slišiš pritajeno igranje orkestra.
Tla dvorane so videti kot ogromna šahovnica
z belimi in črnimi polji. Videti je, da so polja
označena s številkami in črkami. Po vseh štirih
stenah dvorane so obešene slavne slike konj,
med drugimi tudi ta: https://rb.gy/groo5t.

Poleg modrih vrat, pred katerim stojiš, ima dvorana
še troje vrat - označena so z 'v'. Tvoj trenutni
položaj je d1 in je prikazan z '×'.
"""

# Seznam dejanj
s2_dejanja = [
    'Vneseš oznako polja, kamor želiš iti.'
    ]

# Napačna poteza
s2_napacna_izbira = """
Ko stopiš na to polje, se ti odprejo tla
in padeš v globino ... Poskusi ponovno.
"""

s2_ponovni_zacetek = 'Pritisni ENTER za ponovni začetek stopnje. '
s2_vrata1 = """
Odpreš vrata in zagledaš leva, ki ni jedel že en mesec.
To je zadnja stvar, ki jo vidiš.
"""
s2_vrata2 = """
Pred tabo so kamnita vrata.
Žal nimaš ničesar, s čimer bi jih razbil.
"""
s2_vrata3 = """
Odpreš vrata in zagledaš leglo kober.
Nato začutiš pekočo bolečino in padeš v nezavest.
"""
