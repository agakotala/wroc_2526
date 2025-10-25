import pandas as pd
import random

random.seed(42)

imiona = ["Anna", "Antek", "Jan", "Beata", "Ela", "Jola", "Ewa", "Tomasz", "Julian", "Agata", "Jurek", "Magda", "Ola", "Sylwia", "Klaudia"]
miasta = ["Adamczycha", "Warszawa", "Legnica", "Gdańsk", "Pcim", "Kobyla Góra", "Łódź", "Wrocław", "Gdynia", "Orłowo", "Ełk", "Zielona Góra"]

n = 1000 #liczba rekordow

dane = {
    #kolumna imie - losuje imiona z listy imiona
    "imie": [random.choice(imiona) for _ in range(n)],
    #kolumna miasto - losuje miasta z listy
    "miasto": [random.choice(miasta) for _ in range(n)],
    #kolumna dochód - losuje liczby z okreslionego przedzialu
    "dochód": [random.randint(5800, 25850) for _ in range(n)],

    #puste kolumny, beda uzupelniane petla
    "ma_dzieci": [],
    "liczba_dzieci": [],
    "ma_zwierze": [],
    "jakie_zwierze": []
}
#petla dodajaca wartosci do kolumn dzieci i zwierzeta
for _ in range(n):
    #losowo decyduje czy ma dzieci
    if random.choice([True, False]):
        dane["ma_dzieci"].append("Tak")
        dane["liczba_dzieci"].append(random.randint(1, 4)) #losuje liczbe dzieci od 1 do 4
    else:
        dane["ma_dzieci"].append("Nie") #jesli nie ma dzieci wpisz nie
        dane["liczba_dzieci"].append(0) #wpisz 0

    #losowo przypisal zwierzaki
    if random.choice([True, False]):
        dane["ma_zwierze"].append("Tak")
        dane["jakie_zwierze"].append(random.choice(["pies", "kot", "małpa", "słoń"]))
    else:
        dane["ma_zwierze"].append("Nie")
        dane["jakie_zwierze"].append("brak") #jak nie ma zwierzaka napisz brak

df = pd.DataFrame(dane)

df.to_csv("dane_ludzie.csv", index=False, encoding='utf-8-sig')
print("plik zapisany")