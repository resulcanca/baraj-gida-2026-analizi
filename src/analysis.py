import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
df = pd.read_csv("data/processed/dataset_final.csv", parse_dates=["tarih"])
df["baraj_lag1"] = df["baraj_doluluk_yuzde"].shift(1)
corr = df["baraj_lag1"].corr(df["gida_tufe_aylik_yuzde"])
corr0 = df["baraj_doluluk_yuzde"].corr(df["gida_tufe_aylik_yuzde"])
print(f"Korelasyon lag0: {corr0:.3f}")
print(f"Korelasyon lag1: {corr:.3f}")
tmp = df.dropna(subset=["baraj_lag1", "gida_tufe_aylik_yuzde"])
X = tmp[["baraj_lag1"]].values
y = tmp["gida_tufe_aylik_yuzde"].values
model = LinearRegression().fit(X, y)
print(f"Model: y = {model.coef_[0]:.3f} * x + {model.intercept_:.3f}")
print(f"R2: {model.score(X, y):.3f}")
plt.figure()
plt.scatter(df["baraj_doluluk_yuzde"], df["gida_tufe_aylik_yuzde"])
plt.xlabel("Baraj Doluluk %")
plt.ylabel("Gida TUFE Aylik %")
plt.title("Baraj vs Gida Enflasyonu 2026")
plt.savefig("baraj_gida_scatter.png", dpi=200, bbox_inches="tight")
print("Grafik kaydedildi: baraj_gida_scatter.png")
