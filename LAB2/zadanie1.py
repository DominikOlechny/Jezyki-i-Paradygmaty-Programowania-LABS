def analizuj_tekst(tekst, stop_words):
    # Podział tekstu na słowa i linie
    slowa = tekst.replace('.', '').replace(',', '').replace('!', '').replace('?', '').replace('\n', ' ').split()
    linie = tekst.split('\n')

    # Zliczanie słów, zdań i akapitów
    liczba_slow = len(slowa)
    liczba_zdan = tekst.count('.') + tekst.count('!') + tekst.count('?')
    liczba_akapitow = len([linia for linia in linie if linia.strip() != ''])

    # Usuwanie stop words i zliczanie częstości słów
    slowa_bez_stop = [slowo.lower() for slowo in slowa if slowo.lower() not in stop_words]
    czestosc_slow = {}
    for slowo in slowa_bez_stop:
        if slowo in czestosc_slow:
            czestosc_slow[slowo] += 1
        else:
            czestosc_slow[slowo] = 1
    najczestsze_slowa = sorted(czestosc_slow.items(), key=lambda x: x[1], reverse=True)[:5]

    # Transformacja słów zaczynających się na "a" lub "A"
    transformed_words = [
        slowo[::-1] if slowo.lower().startswith('a') else slowo
        for slowo in slowa
    ]
    tekst_po_transformacji = " ".join(transformed_words)

    # Wynik analizy
    wynik = {
        "liczba_slow": liczba_slow,
        "liczba_zdan": liczba_zdan,
        "liczba_akapitow": liczba_akapitow,
        "najczestsze_slowa": najczestsze_slowa,
        "tekst_po_transformacji": tekst_po_transformacji
    }
    return wynik


# Przykładowy tekst i lista stop words
tekst = """
Apple and apricot are amazing fruits. They are loved by many. 
An adventure awaits those who travel across the Amazon river. 
Art is also a form of expression.
"""

stop_words = {"and", "are", "by", "the", "a", "is", "of", "who", "an"}

# Uruchomienie analizy
wynik = analizuj_tekst(tekst, stop_words)

# Wyświetlenie wyników
print("Liczba słów:", wynik["liczba_slow"])
print("Liczba zdań:", wynik["liczba_zdan"])
print("Liczba akapitów:", wynik["liczba_akapitow"])
print("Najczęściej występujące słowa (bez stop words):", wynik["najczestsze_slowa"])
print("Tekst po transformacji:\n", wynik["tekst_po_transformacji"])