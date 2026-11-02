#!/usr/bin/env python3
from datetime import date
import matplotlib.pyplot as plt
import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# Remove Weighted_Price column
df = df.drop(columns=['Weighted_Price'])

# Rename Timestamp to Date
df = df.rename(columns={'Timestamp': 'Date'})

# Convert timestamps to date values
df['Date'] = pd.to_datetime(df['Date'], unit='s').dt.date

# Index the DataFrame on Date
df = df.set_index('Date')

# Fill missing values
df['Close'] = df['Close'].ffill()
df['High'] = df['High'].fillna(df['Close'])
df['Low'] = df['Low'].fillna(df['Close'])
df['Open'] = df['Open'].fillna(df['Close'])
df['Volume_(BTC)'] = df['Volume_(BTC)'].fillna(0)
df['Volume_(Currency)'] = df['Volume_(Currency)'].fillna(0)

# Filter from 2017 and beyond
df = df.loc[df.index >= date(2017, 1, 1)]

# Group by day with specified aggregations
daily = df.groupby('Date').agg({
    'High': 'max',
    'Low': 'min',
    'Open': 'mean',
    'Close': 'mean',
    'Volume_(BTC)': 'sum',
    'Volume_(Currency)': 'sum'
})

# Plot the daily interval data
daily.plot()
plt.show()
