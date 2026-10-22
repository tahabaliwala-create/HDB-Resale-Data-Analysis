import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("HDB Resale Price Data .csv")

# print(df.columns.tolist())
# print(df.head())
df = pd.read_csv("HDB Resale Price Data .csv", header=1)  # account for title 
df = df.dropna(how="all")                                  

df["month"] = pd.to_datetime(df["month"])

df["year"] = df["month"].dt.year
'''
print(df.isnull().sum())       
print(df.duplicated().sum())   
print(df.dtypes)               
print(df["town"].nunique())   
print(df["flat_type"].unique())
'''
df["month"] = pd.to_datetime(df["month"], format="%Y-%m")
df["year"] = df["month"].dt.year
df["price_per_sqm"] = df["resale_price"] / df["floor_area_sqm"]
df["floor_area_sqm"] = pd.to_numeric(df["floor_area_sqm"], errors="coerce")
df["resale_price"] = pd.to_numeric(df["resale_price"].astype(str), errors="coerce")

# Average price by town (most to least expensive)
town_group = df.groupby("town")
town_prices = town_group["resale_price"]
avg_by_town = town_prices.mean().sort_values(ascending=False)


# Average price by year
year_group = df.groupby("year")
avg_by_year = year_group["resale_price"].mean()


# Average price by flat type
avg_by_type = df.groupby("flat_type")["resale_price"].mean().sort_values()


#plotting

x = avg_by_year.index
y = avg_by_year.values

plt.plot(x, y, marker="o")
plt.show()

trend_group = df.groupby(["year", "flat_type"])
trend_prices = trend_group["resale_price"]
trend_mean = trend_prices.mean()
trend_table = trend_mean.unstack()


x = trend_table.index




for flat_type in trend_table.columns:
    y = trend_table[flat_type]
    plt.plot(x, y, marker="o", label=flat_type)

# Prepare the data
town_group = df.groupby("town")
town_prices = town_group["resale_price"]
avg_by_town = town_prices.mean()
avg_by_town = avg_by_town.sort_values(ascending=False)
top_towns = avg_by_town.head(10)

# Define x and y
x = top_towns.index
y = top_towns.values

plt.figure(figsize=(10, 6))
plt.bar(x, y)

plt.title("Top 10 Most Expensive HDB Towns (Average Resale Price)")
plt.xlabel("Town")
plt.ylabel("Average resale price (S$)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
