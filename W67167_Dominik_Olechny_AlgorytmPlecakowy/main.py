def zachlanny_plecak(przedmioty, maks_waga):
    #Sortowanie według stosunku malejąco wg stosunku "wartość / waga"
    przedmioty.sort(key=lambda x: x[2] / x[1], reverse=True)

    aktualna_waga = 0.0
    laczna_wartosc = 0.0
    wybrane = []
    pominiete = []

    #iteracja po tablicy
    for nazwa, waga, wartosc in przedmioty:
        if aktualna_waga + waga <= maks_waga:
            #Jeśli przedmiot się mieści, to go dodajemy do wybranych
            wybrane.append((nazwa, waga, wartosc))
            aktualna_waga += waga
            laczna_wartosc += wartosc
        else:
            #Jeśli nie ma już miejsca, to dodajemy do listy pominietych
            pominiete.append((nazwa, waga, wartosc))

    return laczna_wartosc, wybrane, pominiete



#Pobieranie danych od użytkownika
liczba_przedmiotow = int(input("Podaj liczbę przedmiotów: "))
przedmioty = []

for i in range(liczba_przedmiotow):
    nazwa = input(f"Podaj nazwę przedmiotu {i + 1}: ")
    waga = float(input(f"Podaj wagę przedmiotu {i + 1}: "))
    wartosc = float(input(f"Podaj wartość przedmiotu {i + 1}: "))
    przedmioty.append((nazwa, waga, wartosc))

maks_waga = float(input("Podaj maksymalną wagę plecaka: "))

#Wywołanie zachłannego algorytmu
laczna_wartosc, wybrane_przedmioty, pominiete_przedmioty = zachlanny_plecak(przedmioty, maks_waga)

# Wyświetlenie wyników
print(f"\nMaksymalna wartość, jaką udało się spakować do plecaka: {laczna_wartosc:}")
print("Wybrane przedmioty:")
for nazwa, waga, wartosc in wybrane_przedmioty:
    print(f"  - Nazwa: {nazwa}, Waga: {waga:}, Wartość: {wartosc:}")

print("\nPominięte przedmioty:")
for nazwa, waga, wartosc in pominiete_przedmioty:
    print(f"  - Nazwa: {nazwa}, Waga: {waga:}, Wartość: {wartosc:}")

