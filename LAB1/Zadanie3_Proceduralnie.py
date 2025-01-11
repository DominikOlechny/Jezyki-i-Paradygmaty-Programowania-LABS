def optymalizacja_proceduralna(zadania):
    # Sortuj zadania po czasie wykonania (rosnąco), a w przypadku remisu po nagrodzie (malejąco)
    zadania.sort(key=lambda x: (x[1], -x[2]))

    czas_calkowity = 0
    czas_oczekiwania = 0
    optymalna_kolejnosc = []

    for zadanie in zadania:
        optymalna_kolejnosc.append(zadanie)
        czas_calkowity += zadanie[1]
        czas_oczekiwania += czas_calkowity  # Dodajemy czas oczekiwania dla bieżącego zadania

    return optymalna_kolejnosc, czas_oczekiwania

# Przykład danych wejściowych: (nazwa_zadania, czas_wykonania, nagroda)
zadania = [("Zad1", 3, 50), ("Zad2", 1, 40), ("Zad3", 2, 60)]
optymalna_kolejnosc, czas_oczekiwania = optymalizacja_proceduralna(zadania)

print("Proceduralnie - Kolejność:", optymalna_kolejnosc)
print("Proceduralnie - Czas oczekiwania:", czas_oczekiwania)