import random

random.seed(42)

tajna_liczba = random.randint(1, 200) #komp losuje liczbe od 1 do 200

while True:
    proba = int(input("podaj liczbe od 1 do 200: "))
#dodajemy warunek, ze liczby moga byc tylko z zakresu od 1 do 200
    if proba < 1 or proba > 200:
        print("błąd! mozesz podac tylko liczby od 1 do 200")
        continue
    if proba < tajna_liczba:
        print("ta liczba jest mniejsza niz wylosowana, sprobuj jeszcze raz")
    elif proba > tajna_liczba:
        print("ta liczba jest wieksza niz wylosowana, sprobuj jeszcze raz")
    else:
        print("odgadles wylosowana liczbe")
        break #zatrzymuje petle
