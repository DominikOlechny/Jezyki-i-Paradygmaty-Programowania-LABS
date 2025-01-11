import numpy as np

def walidacja_operacji(macierz1, macierz2, operacja):
    """
    Sprawdza poprawność wymiarów macierzy dla wybranej operacji.
    """
    if operacja == "dodawanie":
        return macierz1.shape == macierz2.shape
    elif operacja == "mnożenie":
        return macierz1.shape[1] == macierz2.shape[0]
    elif operacja == "transponowanie":
        return True  # Transpozycja nie wymaga porównania wymiarów
    else:
        raise ValueError("Nieobsługiwana operacja")

def wykonaj_operacje(macierz1, macierz2=None, operacja="dodawanie"):
    """
    Wykonuje wybraną operację na macierzach.
    """
    if operacja == "dodawanie":
        if not walidacja_operacji(macierz1, macierz2, operacja):
            raise ValueError("Macierze muszą mieć te same wymiary do dodawania")
        return eval("macierz1 + macierz2")
    elif operacja == "mnożenie":
        if not walidacja_operacji(macierz1, macierz2, operacja):
            raise ValueError("Liczba kolumn macierzy1 musi być równa liczbie wierszy macierzy2 do mnożenia")
        return eval("macierz1 @ macierz2")
    elif operacja == "transponowanie":
        return eval("macierz1.T")
    else:
        raise ValueError("Nieobsługiwana operacja")

# Przykłady użycia
if __name__ == "__main__":
    # Tworzenie macierzy
    macierz1 = np.array([[1, 2, 3], [4, 5, 6]])
    macierz2 = np.array([[7, 8, 9], [10, 11, 12]])

    try:
        # Operacja dodawania
        wynik_dodawanie = wykonaj_operacje(macierz1, macierz2, operacja="dodawanie")
        print("Dodawanie:\n", wynik_dodawanie)

        # Operacja mnożenia
        macierz3 = np.array([[1, 2], [3, 4], [5, 6]])
        wynik_mnozenie = wykonaj_operacje(macierz1, macierz3, operacja="mnożenie")
        print("Mnożenie:\n", wynik_mnozenie)

        # Operacja transponowania
        wynik_transpozycja = wykonaj_operacje(macierz1, operacja="transponowanie")
        print("Transponowanie:\n", wynik_transpozycja)

    except ValueError as e:
        print("Błąd:", e)