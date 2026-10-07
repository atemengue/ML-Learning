import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


nom = np.random.choice(["Regis", "Simone", "Christelle", "Patrick", "Gaelle"],999)
type = np.random.choice(["Type1", "Type2", "Type3", "Type4", "Type5"],999)

# generation des valeurs

x = np.random.normal(0,1,999)
y = np.random.normal(1,2,999)
z = np.random.choice(range(10),999)

# creation du dataframe par concatenation
df = pd.DataFrame([nom, type, x, y, z]).T # utilisation la transposition
df.columns=['nom','type','a','b','c']

# importance de prendre un echantillon
# print(df.head(10))
# print(df)

# df.info()


#utilisation du casting
df["nom"] = df["nom"].astype(str)
df["type"] = df["type"].apply(str)
df["a"] = pd.to_numeric(df["a"])
df["b"] = df["b"].astype(float)
df["c"] = df["c"].astype(int)


# df.info()


#desribe pour la description de la donnee.
# print(df.describe())

# print(df["a"].describe())

# visualisation partie 01
# plt.hist(df['nom'])
# plt.title("Frequences des noms")
# plt.show()

# creation d'un graphique pour affiche en code
gb = df.groupby("type")["c"].sum()
# print(gb)

df1 = pd.DataFrame({"total": gb})

# print(df1)

plt.pie(df1["total"],labels=df1.index, autopct='%1.1f%%')
plt.title("distribution des types")
plt.savefig("pie.disbribution.png")
plt.close()

# plt.pie(df1)