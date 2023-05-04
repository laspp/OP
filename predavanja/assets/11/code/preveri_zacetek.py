def se_zacne(s, p):
    """Vrne True, če se niz s začne s podnizom p."""
    return s[:len(p)] == p

print(se_zacne('Marko skače', 'Marko'))
print(se_zacne('Marko skače', 'Marko skače'))
print(se_zacne('Marko skače', 'marko'))
print(se_zacne('Marko skače', 'Marko  skače'))
print(se_zacne('Marko skače', 'Marko skače in si strga hlače'))
