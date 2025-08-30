import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title='Retail Sales Dashboard', layout='wide')
BASE = os.path.join(os.path.dirname(__file__), '..', 'data', 'viz')

st.title('Retail Sales — Mini Project')

@st.cache_data
def load_data():
daily = pd.read_csv(os.path.join(BASE, 'daily_sales.csv'), parse_dates=['date'])
prod = pd.read_csv(os.path.join(BASE, 'product_summary.csv'))
store = pd.read_csv(os.path.join(BASE, 'store_summary.csv'))
return daily, prod, store

daily, prod, store = load_data()

st.header('Overall trend')
fig = px.line(daily, x='date', y='total_revenue', title='Daily Revenue')
st.plotly_chart(fig, use_container_width=True)

col1, col2 = st.columns(2)
with col1:
st.header('Top products by revenue')
topn = st.slider('Top N products', 3, 20, 5)
top_products = prod.sort_values('revenue', ascending=False).head(topn)
st.table(top_products[['sku','product_name','category','units_sold','revenue']])
with col2:
st.header('Store performance')
fig2 = px.bar(store.sort_values('revenue',ascending=False), x='store', y='revenue', title='Revenue by Store')
st.plotly_chart(fig2, use_container_width=True)

st.markdown('---')
st.write('This dashboard reads pre-computed gold tables (CSV). For production, connect Power BI or a BI lakehouse.')
