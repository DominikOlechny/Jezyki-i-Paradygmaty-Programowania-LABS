class Employee:
    def __init__(self, imie: str, wiek: int, pensja: float):
        self.imie = imie
        self.wiek = wiek
        self.pensja = pensja

    def __repr__(self):
        return f"Pracownik(imie={self.imie}, wiek={self.wiek}, pensja={self.pensja})"

class EmployeesManager:
    def __init__(self, plik="pracownicy.txt"):
        self.plik = plik
        self.pracownicy = self.wczytaj_pracownikow()

    def wczytaj_pracownikow(self):
        pracownicy = []
        try:
            with open(self.plik, "r") as f:
                for linia in f:
                    dane = linia.strip().split(",")
                    if len(dane) == 3:
                        imie, wiek, pensja = dane
                        pracownicy.append(Employee(imie, int(wiek), float(pensja)))
        except FileNotFoundError:
            pass
        return pracownicy

    def zapisz_pracownikow(self):
        with open(self.plik, "w") as f:
            for prac in self.pracownicy:
                f.write(f"{prac.imie},{prac.wiek},{prac.pensja}\n")

    def dodaj_pracownika(self, imie: str, wiek: int, pensja: float):
        if not imie or wiek <= 0 or pensja < 0:
            print("Błąd: Niepoprawne dane.")
            return
        self.pracownicy.append(Employee(imie, wiek, pensja))
        self.zapisz_pracownikow()
        print("Pracownik dodany.")

    def lista_pracownikow(self):
        return self.pracownicy

    def usun_pracownikow_w_wieku(self, min_wiek: int, max_wiek: int):
        self.pracownicy = [prac for prac in self.pracownicy if not (min_wiek <= prac.wiek <= max_wiek)]
        self.zapisz_pracownikow()
        print("Usunięto pracowników.")

    def znajdz_pracownika(self, imie: str):
        return next((prac for prac in self.pracownicy if prac.imie.lower() == imie.lower()), None)

    def zaktualizuj_pensje(self, imie: str, nowa_pensja: float):
        if nowa_pensja < 0:
            print("Błąd: Pensja nie może być ujemna.")
            return False
        pracownik = self.znajdz_pracownika(imie)
        if pracownik:
            pracownik.pensja = nowa_pensja
            self.zapisz_pracownikow()
            print("Pensja zaktualizowana.")
            return True
        print("Nie znaleziono pracownika.")
        return False

class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()

    def logowanie(self):
        for _ in range(3):
            login = input("Podaj login: ")
            haslo = input("Podaj hasło: ")
            if login == "admin" and haslo == "admin":
                return True
            print("Niepoprawne dane logowania!")
        return False

    def menu(self):
        if not self.logowanie():
            print("Zbyt wiele nieudanych prób logowania. Zamykam program.")
            return

        while True:
            print("\nSystem zarządzania pracownikami")
            print("1. Dodaj pracownika")
            print("2. Wyświetl listę pracowników")
            print("3. Usuń pracowników według wieku")
            print("4. Zaktualizuj pensję pracownika")
            print("5. Wyjście")
            wybor = input("Wybierz opcję: ")

            if wybor == "1":
                imie = input("Podaj imię: ")
                try:
                    wiek = int(input("Podaj wiek: "))
                    pensja = float(input("Podaj pensję: "))
                    self.manager.dodaj_pracownika(imie, wiek, pensja)
                except ValueError:
                    print("Błąd: Niepoprawny format danych.")

            elif wybor == "2":
                pracownicy = self.manager.lista_pracownikow()
                if pracownicy:
                    for prac in pracownicy:
                        print(prac)
                else:
                    print("Brak pracowników.")

            elif wybor == "3":
                try:
                    min_wiek = int(input("Podaj minimalny wiek: "))
                    max_wiek = int(input("Podaj maksymalny wiek: "))
                    self.manager.usun_pracownikow_w_wieku(min_wiek, max_wiek)
                except ValueError:
                    print("Błąd: Niepoprawny format danych.")

            elif wybor == "4":
                imie = input("Podaj imię pracownika: ")
                try:
                    nowa_pensja = float(input("Podaj nową pensję: "))
                    self.manager.zaktualizuj_pensje(imie, nowa_pensja)
                except ValueError:
                    print("Błąd: Niepoprawny format danych.")

            elif wybor == "5":
                print("Zamykanie programu...")
                break
            else:
                print("Niepoprawny wybór, spróbuj ponownie.")

if __name__ == "__main__":
    frontend = FrontendManager()
    frontend.menu()
