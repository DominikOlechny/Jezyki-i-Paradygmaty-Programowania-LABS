def podzial_paczek(paczki, max_waga): #Zadeklarowanie funkcji dzielenia paczek na kursy
    paczki.sort(reverse=True) #sortowanie wag paczek
    kursy=[] #pusta tablica z kursami
    for paczka in paczki: #petla wykonuje sie tyle razy ile jest paczek
        dodano = False #ustawiamy flage dodano na false

        for kurs in kursy: #petla odpowiedzialna za dodawanie kursow
            if sum(kurs) + paczka <= max_waga: #jesli suma kursow + paczka miesci lub jest rowna maksymalnej wadzet to:
                kurs.append(paczka) #dodaj do kursu
                dodano = True #ustaw flage o tym ze dodano
                break #przerwij petle
        if not dodano: #jesli nie miesci sie
            kursy.append([paczka]) #zwroc do kursow

    return len(kursy), kursy #zróć ilość kursów, i zawartość kursów

paczki = [10, 8, 7, 4, 2, 1] #listapaczek
max_waga = 15 #max waga kursu

liczba_kursow, rozklad_kursow = podzial_paczek(paczki, max_waga)

print(f"Liczba kursów: {liczba_kursow}") #liczba kursow
print("Rozkład paczek w kursach:")
for i, kurs in enumerate(rozklad_kursow, 1): #petla wypisujaca kursy
    print(f"Kurs {i}: {kurs}")