import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv("owid-covid-data.csv", parse_dates=["date"])
print(df[["date", "location", "new_cases", "new_deaths", "total_vaccinations"]].head(3))

print(df.isnull().sum())

df["new_cases"] = df["new_cases"].fillna(df["new_cases"].median())
df["total_cases"] = df["total_cases"].fillna(df["total_cases"].median())
df["new_deaths"] = df["new_deaths"].fillna(df["new_deaths"].median())
df["total_deaths"] = df["total_deaths"].fillna(df["total_deaths"].median())
df= df.dropna(subset=["total_vaccinations", "people_vaccinated"])

location_dummies = pd.get_dummies(df["location"], prefix="location")
df = pd.concat([df, location_dummies], axis=1)

df.to_csv("owid-covid-encoded.csv", index=False)
print(f"\n✅ Збережено у файл: owid-covid-encoded.csv")

print(f"\n✅ One-hot encoding: додано {location_dummies.shape[1]} колонок")
print("\n--- Приклад (перші 3 рядки, 4 країни) ---")
sample_cols = list(location_dummies.columns[:4])
print(df[["date", "location"] + sample_cols].head(3).to_string(index=False))


sns.set_theme(style="darkgrid", palette="muted")
fig, axes = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle("COVID-19 | Огляд даних", fontsize=18, fontweight="bold", y=1.01)

ua = df[df["location"] == "Ukraine"].copy()

ax1 = axes[0, 0]

ax1.fill_between(ua["date"], ua["new_cases"],color="#4C9BE8", alpha=0.5)
ax1.plot(ua["date"], ua["new_cases"],color="#4C9BE8")
ax1.set_title("Нові випадки Україна")

ax2 = axes[0, 1]
ax2.fill_between(ua["date"], ua["new_deaths"],color="#4C9BE8", alpha=0.5)
ax2.plot(ua["date"], ua["new_deaths"],color="#4C9BE8")
ax2.set_title("Нові смерті Україна")

ax3 = axes[1, 0]
ax3.fill_between(ua["date"], ua["total_vaccinations"],color="#4C9BE8", alpha=0.5)
ax3.plot(ua["date"], ua["total_vaccinations"],color="#4C9BE8")
ax3.set_title("Вакцинація Україна")

ax4 = axes[1, 1]
latest = df.sort_values("date").groupby("location").last().reset_index()
top10 = (
    latest.nlargest(10, "total_cases")[["location", "total_cases"]]
    .sort_values("total_cases")
)
colors = sns.color_palette("Blues_d", len(top10))
bars = ax4.barh(top10["location"], top10["total_cases"] / 1e6, color=colors)
ax4.set_title("ТОП-10 по захворюваності")


plt.tight_layout()
plt.show()

CORR_COLS = ["new_cases", "new_deaths", "total_cases", "population"]

corr_matrix = df[CORR_COLS].corr()



# Heatmap
fig, ax = plt.subplots(figsize=(7, 5))
sns.heatmap(
    corr_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    center=0,
    linewidths=0.5,
    ax=ax,
)
ax.set_title("Кореляційна матриця ключових показників", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.show()