class Employee:
    def __init__(self, imie: str, wiek: int, pensja: float):
        self.imie = imie
        self.wiek = wiek
        self.pensja = pensja

    def __repr__(self):
        return f"Pracownik(imie={self.imie}, wiek={self.wiek}, pensja={self.pensja})"

class EmployeesManager:
    def __init__(self):
        self.pracownicy = []

    def dodaj_pracownika(self, imie: str, wiek: int, pensja: float):
        self.pracownicy.append(Employee(imie, wiek, pensja))

    def lista_pracownikow(self):
        return self.pracownicy

    def usun_pracownikow_w_wieku(self, min_wiek: int, max_wiek: int):
        self.pracownicy = [prac for prac in self.pracownicy if not (min_wiek <= prac.wiek <= max_wiek)]

    def znajdz_pracownika(self, imie: str):
        return next((prac for prac in self.pracownicy if prac.imie.lower() == imie.lower()), None)

    def zaktualizuj_pensje(self, imie: str, nowa_pensja: float):
        pracownik = self.znajdz_pracownika(imie)
        if pracownik:
            pracownik.pensja = nowa_pensja
            return True
        return False

class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()

    def menu(self):
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
                wiek = int(input("Podaj wiek: "))
                pensja = float(input("Podaj pensję: "))
                self.manager.dodaj_pracownika(imie, wiek, pensja)
                print("Dodano pracownika.")

            elif wybor == "2":
                pracownicy = self.manager.lista_pracownikow()
                for prac in pracownicy:
                    print(prac)

            elif wybor == "3":
                min_wiek = int(input("Podaj minimalny wiek: "))
                max_wiek = int(input("Podaj maksymalny wiek: "))
                self.manager.usun_pracownikow_w_wieku(min_wiek, max_wiek)
                print("Usunięto pracowników.")

            elif wybor == "4":
                imie = input("Podaj imię pracownika: ")
                nowa_pensja = float(input("Podaj nową pensję: "))
                if self.manager.zaktualizuj_pensje(imie, nowa_pensja):
                    print("Zaktualizowano pensję.")
                else:
                    print("Nie znaleziono pracownika.")

            elif wybor == "5":
                print("Zamykanie programu...")
                break
            else:
                print("Niepoprawny wybór, spróbuj ponownie.")

if __name__ == "__main__":
    frontend = FrontendManager()
    frontend.menu()
