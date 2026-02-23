# zadanie 1
print("zadanie 1")
import math

ID = 71673

print("ID =", ID)

def cube(x):
    return x ** 3

print("cube(ID % 3) =", cube(ID % 3))

suma = sum(range(ID))
print("suma range(ID) =", suma)

liczba_cyfr = len(str(abs(suma)))
print("liczba cyfr =", liczba_cyfr)

print("sqrt(suma) =", math.sqrt(suma))

# zadanie 2
print("zadanie 2")

nazwisko = "Bondariev"
imie = "Maksym"
ID = "71673"

ja = f"{nazwisko} {imie} {ID}"
print("ja =", ja)

print("liczba spacji =", ja.count(" "))

print("nazwisko =", nazwisko)
print("imie =", imie)
print("ID =", ID)

jaLista = list(ja)
print("jaLista =", jaLista)

ja2 = ja.replace(" ", "-")
print("ja2 =", ja2)

for i, ch in enumerate(jaLista):
    if ch == " ":
        jaLista[i] = "*"

print("jaLista po zmianie =", jaLista)

ja3 = "".join(jaLista)
print("ja3 =", ja3)

# zadanie 3
print("zadanie 3")

import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
df1 = iris.frame

df2 = pd.DataFrame(iris.data)
df2["target"] = iris.target

df1.to_csv("iris.csv", index=False)
df3 = pd.read_csv("iris.csv")

dfs = [("df1", df1), ("df2", df2), ("df3", df3)]

for name, df in dfs:
    print("\n===", name, "===")
    print(df.head(3))
    print("wiersze, kolumny:", df.shape)
    print(df.describe())

    arr = df.to_numpy()
    print("numpy shape:", arr.shape, "dtype:", arr.dtype)

# zadanie 4
print("zadanie 4")
import numpy as np

dataMB = np.genfromtxt("iris.csv", delimiter=",", skip_header=1)

print("shape:", dataMB.shape)
print("dtype:", dataMB.dtype)
print("pierwsze 5 wierszy:\n", dataMB[:5])

sepal_len = dataMB[:, 0]

print("min:", np.min(sepal_len))
print("max:", np.max(sepal_len))
print("mean:", np.mean(sepal_len))

drugi = dataMB[50:100]
mean_petal_len = np.mean(drugi[:, 2])

print("średnia długość płatka (kol 2) dla wierszy 50-99:", mean_petal_len)