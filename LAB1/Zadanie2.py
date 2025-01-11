def znajdz_najkrotsza_sciezke(graf, start, cel):
    # Kolejka przechowująca wierzchołki do odwiedzenia i aktualną ścieżkę.
    kolejka = [(start, [start])]  # Zaczynamy od punktu startowego i ścieżki [start].

    while kolejka:  # Dopóki kolejka nie jest pusta:
        obecny_wierzcholek, sciezka = kolejka.pop(0)  # Pobieramy pierwszy element z kolejki (FIFO).

        # Iterujemy po wszystkich sąsiadach obecnego wierzchołka.
        for sasiad in graf[obecny_wierzcholek]:
            if sasiad not in sciezka:  # Jeśli sąsiad nie był jeszcze odwiedzony:
                nowa_sciezka = sciezka + [sasiad]  # Dodajemy go do aktualnej ścieżki.
                if sasiad == cel:  # Sprawdzamy, czy to jest punkt docelowy.
                    return nowa_sciezka  # Jeśli tak, zwracamy ścieżkę.
                kolejka.append((sasiad, nowa_sciezka))  # Jeśli nie, dodajemy do kolejki.

    return None  # Jeśli nie znaleziono ścieżki, zwracamy None.


# Przykładowy graf jako słownik
graf = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Ustawiamy punkt początkowy i końcowy
punkt_startowy = 'A'
punkt_docelowy = 'F'

# Wywołujemy funkcję
najkrotsza_sciezka = znajdz_najkrotsza_sciezke(graf, punkt_startowy, punkt_docelowy)

# Wyświetlamy wynik
if najkrotsza_sciezka:
    print(f"Najkrótsza ścieżka z {punkt_startowy} do {punkt_docelowy}: {najkrotsza_sciezka}")
else:
    print(f"Nie znaleziono ścieżki z {punkt_startowy} do {punkt_docelowy}.")