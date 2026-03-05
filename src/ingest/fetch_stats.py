import sqlite3
import pandas as pd

#For future live NHL tracking
#For now, dats is loaded from csv
df = pd.read_csv("data/raw/skaters.csv")

#print(df.head())

#print(df.columns.tolist())

#print(df["situation"].unique())