import os
import random
import uuid
from datetime import datetime, timedelta
import pandas as pd

OUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
os.makedirs(OUT_DIR, exist_ok=True)
OUT_PATH = os.path.join(OUT_DIR, 'transactions.csv')

random.seed(42)
NUM_ROWS = 5000
START_DATE = datetime.now() - timedelta(days=90)

products = [
{'sku':'P001','name':'T-Shirt','category':'Apparel','price':299},
{'sku':'P002','name':'Jeans','category':'Apparel','price':899},
{'sku':'P003','name':'Sneakers','category':'Footwear','price':2499},
{'sku':'P004','name':'Cap','category':'Accessories','price':199},
{'sku':'P005','name':'Backpack','category':'Accessories','price':1499},
]

stores = ['Store_A','Store_B','Store_C','Store_D']

rows = []
for i in range(NUM_ROWS):
prod = random.choice(products)
quantity = random.choices([1,2,3], [0.7,0.2,0.1])[0]
txn_date = START_DATE + timedelta(seconds=random.randint(0, 90*24*3600))
row = {
'transaction_id': str(uuid.uuid4()),
'transaction_ts': txn_date.strftime('%Y-%m-%d %H:%M:%S'),
'store': random.choice(stores),
'sku': prod['sku'],
'product_name': prod['name'],
'category': prod['category'],
'price': prod['price'],
'quantity': quantity,
'total_amount': prod['price'] * quantity,
'payment_method': random.choice(['Card','UPI','Cash','Wallet'])
}
rows.append(row)

pdf = pd.DataFrame(rows)
pdf.to_csv(OUT_PATH, index=False)
print(f"Wrote {len(pdf)} rows to {OUT_PATH}")
