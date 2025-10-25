import pandas as pd

df = pd.read_csv("dane_ludzie_i_nieruchomosci", encoding="utf-8-sig")

#usuwanie jednej kolumny z pliku csv
df = df.drop(columns=["jakie_zwierze"])

df.to_csv("dane_ludzie_i_nieruchomosci.csv", index=False, encoding="utf-8-sig")
print("plik dane_ludzie_i_nieruchomosci.csv został zmodyfikowany i zapisany")