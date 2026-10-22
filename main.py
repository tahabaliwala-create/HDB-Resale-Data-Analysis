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


