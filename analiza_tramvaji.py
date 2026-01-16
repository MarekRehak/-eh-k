import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Data tramvají v Praze
# Formát: (typ, maximální_rychlost_km_h, rok_prvního_výroby)
tramvaje_data = [
    ("T3", 50, 1958),
    ("T6A5", 80, 2000),
    ("T4", 60, 1988),
    ("KT8D5", 65, 1994),
    ("27T", 70, 2000),
    ("34T", 75, 2008),
    ("35T", 80, 2010),
]

# Vytvoření DataFrame
df = pd.DataFrame(tramvaje_data, columns=["typ", "max_rychlost_km_h", "rok_prvniho_vyroby"])

print("=" * 50)
print("ANALÝZA TRAMVAJÍ V PRAZE")
print("=" * 50)

# 1. PŘEHLED DAT
print("\n1. PŘEHLED TRAMVAJÍ")
print("-" * 50)
print(df.to_string(index=False))

# 2. STATISTIKA
print("\n2. POPISNÁ STATISTIKA")
print("-" * 50)
print(df.describe())

# 3. FILTROVÁNÍ - Tramvaje s rychlostí > 60 km/h
print("\n3. FILTROVÁNÍ - Tramvaje s rychlostí > 60 km/h")
print("-" * 50)
rychle_tramvaje = df[df["max_rychlost_km_h"] > 60]
print(rychle_tramvaje.to_string(index=False))

# 4. FILTROVÁNÍ - Tramvaje z 21. století (rok >= 2000)
print("\n4. FILTROVÁNÍ - Tramvaje z 21. století (rok >= 2000)")
print("-" * 50)
moderne_tramvaje = df[df["rok_prvniho_vyroby"] >= 2000]
print(moderne_tramvaje.to_string(index=False))

# 5. HISTOGRAM - Maximální rychlost
print("\n5. VYTVÁŘENÍ GRAFŮ...")
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(df["max_rychlost_km_h"], bins=6, color="blue", edgecolor="black", alpha=0.7)
plt.xlabel("Maximální rychlost (km/h)", fontsize=11)
plt.ylabel("Počet typů tramvají", fontsize=11)
plt.title("Distribuce maximální rychlosti tramvají v Praze", fontsize=12, fontweight="bold")
plt.grid(True, alpha=0.3)

# 6. HISTOGRAM - Rok výroby
plt.subplot(1, 2, 2)
plt.hist(df["rok_prvniho_vyroby"], bins=6, color="green", edgecolor="black", alpha=0.7)
plt.xlabel("Rok prvního výroby", fontsize=11)
plt.ylabel("Počet typů", fontsize=11)
plt.title("Distribuce let výroby tramvají", fontsize=12, fontweight="bold")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\n" + "=" * 50)
print("Analýza dokončena!")
print("=" * 50)
