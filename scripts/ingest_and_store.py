import os
import pandas as pd

BASE = os.path.join(os.path.dirname(__file__), '..', 'data', 'lake')
RAW = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw', 'transactions.csv')
BRONZE = os.path.join(BASE, 'bronze')
SILVER = os.path.join(BASE, 'silver')

os.makedirs(BRONZE, exist_ok=True)
os.makedirs(SILVER, exist_ok=True)

df = pd.read_csv(RAW, parse_dates=['transaction_ts'])

df['date'] = df['transaction_ts'].dt.date
for date, group in df.groupby('date'):
path = os.path.join(BRONZE, f'date={date}.parquet')
group.to_parquet(path, index=False)

df_silver = df.copy()
df_silver = df_silver.drop_duplicates(['transaction_id'])
cols = ['price','quantity','total_amount']
for c in cols:
df_silver[c] = pd.to_numeric(df_silver[c], errors='coerce').fillna(0)

silver_path = os.path.join(SILVER, 'transactions_silver.parquet')
df_silver.to_parquet(silver_path, index=False)
print("Ingested and wrote bronze + silver files")
