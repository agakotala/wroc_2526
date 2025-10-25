import pandas as pd
import random

random.seed(42)

df = pd.read_csv("dane_ludzie.csv", encoding="utf-8-sig")

nieruchomosci = ["kamienica", "blok", "dom"]

df["nieruchomosc"] = [random.choice(nieruchomosci) for _ in range(len(df))]

df.to_csv("dane_ludzie_i_nieruchomosci", index=False, encoding="utf-8-sig")

