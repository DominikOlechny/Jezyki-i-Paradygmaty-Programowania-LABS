from functools import reduce


def optymalizacja_funkcyjna(zadania):
    # Sortuj zadania funkcjonalnie po czasie wykonania (rosnąco), a potem po nagrodzie (malejąco)
    posortowane_zadania = sorted(zadania, key=lambda x: (x[1], -x[2]))

    # Redukcja dla obliczenia czasu oczekiwania i kolekcji zadań
    def redukuj_czas_ocz_kolejnosc(akumulator, zadanie):
        czas_calkowity, czas_oczekiwania, kolejnosc = akumulator
        czas_calkowity += zadanie[1]
        czas_oczekiwania += czas_calkowity
        kolejnosc.append(zadanie)
        return czas_calkowity, czas_oczekiwania, kolejnosc

    _, czas_oczekiwania, optymalna_kolejnosc = reduce(
        redukuj_czas_ocz_kolejnosc,
        posortowane_zadania,
        (0, 0, [])
    )

    return optymalna_kolejnosc, czas_oczekiwania


# Przykład danych wejściowych: (nazwa_zadania, czas_wykonania, nagroda)
zadania = [("Zad1", 3, 50), ("Zad2", 1, 40), ("Zad3", 2, 60)]
optymalna_kolejnosc, czas_oczekiwania = optymalizacja_funkcyjna(zadania)

print("Funkcyjnie - Kolejność:", optymalna_kolejnosc)
print("Funkcyjnie - Czas oczekiwania:", czas_oczekiwania)