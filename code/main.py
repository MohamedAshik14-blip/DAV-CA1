import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

gdp = pd.read_csv(DATA_DIR / "GDP per capita in PPS.csv")
life = pd.read_csv(DATA_DIR / "Life expectancy at birth by sex.csv")
edu = pd.read_csv(DATA_DIR / "Public expenditure on education in current prices, by education level and programme orientation.csv")
unemp = pd.read_csv(DATA_DIR / "Unemployment rates by citizenship.csv")
happy = pd.read_csv(DATA_DIR / "Overall life satisfaction by level of satisfaction, age and educational attainment.csv")

print("GDP")
print(gdp.head())
print(gdp.columns)

print("Life")
print(life.head())
print(life.columns)

print("Education")
print(edu.head())
print(edu.columns)

print("Unemployment")
print(unemp.head())
print(unemp.columns)

print("Happiness")
print(happy.head())
print(happy.columns)
