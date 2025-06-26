# sales_analysis_full.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set plot style
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

# === STEP 1: LOAD AND CLEAN ===

# Load dataset
file_path = "Financials.csv"  # Update if needed
df = pd.read_csv(file_path)

# Strip column name whitespaces
df.columns = df.columns.str.strip()

# Columns to clean
cols_to_clean = [
    'Units Sold', 'Manufacturing Price', 'Sale Price',
    'Gross Sales', 'Discounts', 'Sales', 'COGS', 'Profit'
]

# Currency cleaner function
def clean_currency(x):
    if isinstance(x, str):
        x = x.strip().replace('$', '').replace(',', '')
        if x == '-' or x == '':
            return np.nan
        if x.startswith('(') and x.endswith(')'):
            x = '-' + x[1:-1]
        return float(x)
    return x

# Clean the financial columns
for col in cols_to_clean:
    df[col] = df[col].apply(clean_currency)

# Convert date column
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')

# === STEP 2: EXPLORATORY DATA ANALYSIS ===

print("📊 Summary Statistics:\n", df.describe())
print("\n🧩 Missing Values:\n", df.isna().sum())

# Correlation heatmap
financial_features = [
    'Units Sold', 'Manufacturing Price', 'Sale Price',
    'Gross Sales', 'Discounts', 'Sales', 'COGS', 'Profit'
]

plt.figure(figsize=(10,6))
sns.heatmap(df[financial_features].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# Boxplots
plt.figure(figsize=(15,5))
for i, col in enumerate(['Sales', 'COGS', 'Profit']):
    plt.subplot(1, 3, i+1)
    sns.boxplot(y=df[col])
    plt.title(f"Boxplot: {col}")
plt.tight_layout()
plt.show()

# Histograms
plt.figure(figsize=(15,5))
for i, col in enumerate(['Sales', 'COGS', 'Profit']):
    plt.subplot(1, 3, i+1)
    sns.histplot(df[col], kde=True, bins=30)
    plt.title(f"Distribution: {col}")
plt.tight_layout()
plt.show()

# Time Series Trend
df_sorted = df.sort_values('Date')
plt.figure(figsize=(15,6))
sns.lineplot(data=df_sorted, x='Date', y='Sales', label='Sales')
sns.lineplot(data=df_sorted, x='Date', y='COGS', label='COGS')
sns.lineplot(data=df_sorted, x='Date', y='Profit', label='Profit')
plt.title("Time Series: Sales, COGS, and Profit Over Time")
plt.xlabel("Date")
plt.ylabel("Amount ($)")
plt.legend()
plt.tight_layout()
plt.show()

# === STEP 3: FEATURE ENGINEERING ===

# Profit Margin
df['Profit Margin (%)'] = (df['Profit'] / df['Sales']) * 100

# Fill missing values
df['Discounts'] = df['Discounts'].fillna(0)
df['Profit'] = df['Profit'].fillna(df['Sales'] - df['COGS'])

# Fiscal Year
df['Fiscal Year'] = df['Date'].dt.year

# Profit Margin Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['Profit Margin (%)'], bins=30, kde=True, color='green')
plt.title("Profit Margin Distribution")
plt.xlabel("Profit Margin (%)")
plt.tight_layout()
plt.show()

# Profit vs Manufacturing Price
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='Manufacturing Price', y='Profit', hue='Country')
plt.title("Manufacturing Price vs Profit")
plt.tight_layout()
plt.show()

# === STEP 4: FISCAL YEAR AGGREGATE VIEW ===

fiscal_summary = df.groupby('Fiscal Year')[['Sales', 'COGS', 'Profit']].sum().reset_index()

plt.figure(figsize=(10,6))
sns.lineplot(data=fiscal_summary, x='Fiscal Year', y='Sales', label='Sales')
sns.lineplot(data=fiscal_summary, x='Fiscal Year', y='COGS', label='COGS')
sns.lineplot(data=fiscal_summary, x='Fiscal Year', y='Profit', label='Profit')
plt.title("Fiscal Year-wise Financial Performance")
plt.xlabel("Fiscal Year")
plt.ylabel("Amount ($)")
plt.legend()
plt.tight_layout()
plt.show()

# === OPTIONAL: SAVE CLEANED DATA ===

df.to_csv("Cleaned_Financials.csv", index=False)
print("✅ Cleaned dataset saved as Cleaned_Financials.csv")
