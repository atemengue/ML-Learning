import pandas as pd
import numpy as np
from pathlib import Path

# dossier data/ situe a cote de src/, peu importe d'ou le script est lance
DATA_DIR = Path(__file__).resolve().parent.parent / "data"

df = pd.read_csv(DATA_DIR / "testfichier.csv")
# print(df) 

print(df["NUM_RUE"])
print(df["NUM_RUE"].isnull())


print(df["NBR_CHAMBRES"])
print(df["NBR_CHAMBRES"].isnull())

valeurs_manquantes = ["na", "-", "n/a"]
df = pd.read_csv(DATA_DIR / "testfichier.csv", na_values=valeurs_manquantes)


print(df["NUM_RUE"])
print(df["NUM_RUE"].isnull())

print(df["NBR_CHAMBRES"])
print(df["NBR_CHAMBRES"].isnull())