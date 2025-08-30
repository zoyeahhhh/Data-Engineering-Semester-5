import os
import pandas as pd

BASE = os.path.join(os.path.dirname(__file__), '..', 'data')
GOLD = os.path.join(BASE, 'lake', 'gold')
OUT = os.path.join(BASE, 'viz')
os.makedirs(OUT, exist_ok=True)

for fname in ['daily_sales.parquet','product_summary.parquet','store_summary.parquet']:
df = pd.read_parquet(os.path.join(GOLD, fname))
df.to_csv(os.path.join(OUT, fname.replace('.parquet','.csv')), index=False)

print('Exported CSVs for viz in', OUT)
