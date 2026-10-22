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

df["price_per_sqm"] = df["resale_price"] / df["floor_area_sqm"]