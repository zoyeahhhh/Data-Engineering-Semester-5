import os
import pandas as pd

BASE = os.path.join(os.path.dirname(__file__), '..', 'data')
SILVER = os.path.join(BASE, 'lake', 'silver', 'transactions_silver.parquet')
GOLD_DIR = os.path.join(BASE, 'lake', 'gold')
os.makedirs(GOLD_DIR, exist_ok=True)

df = pd.read_parquet(SILVER)
df['date'] = pd.to_datetime(df['transaction_ts']).dt.date

daily = df.groupby('date').agg(
total_revenue = ('total_amount','sum'),
txn_count = ('transaction_id','nunique'),
avg_ticket = ('total_amount','mean')
).reset_index()
daily.to_parquet(os.path.join(GOLD_DIR,'daily_sales.parquet'), index=False)

prod = df.groupby(['sku','product_name','category']).agg(
units_sold=('quantity','sum'),
revenue=('total_amount','sum')
).reset_index()
prod.to_parquet(os.path.join(GOLD_DIR,'product_summary.parquet'), index=False)

store = df.groupby('store').agg(
units_sold=('quantity','sum'),
revenue=('total_amount','sum')
).reset_index()
store.to_parquet(os.path.join(GOLD_DIR,'store_summary.parquet'), index=False)

print('Wrote gold tables to', GOLD_DIR)
