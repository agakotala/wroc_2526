import pandas as pd

df = pd.read_csv("klienci.csv")
wyniki = {"duże miasto": 0, "średnie miasto":0, "male miasto":0}

for i in range(len(df)):
    miasto = df.loc[i, "miasto"]
    dl = len(miasto)

    if dl <= 5:
        kat = "male miasto"
    elif dl <= 8:
        kat = "średnie miasto"
    else:
        kat = "duże miasto"

    wyniki[kat] +=  1

print("podsumowanie wg kategorii")
print(wyniki)
