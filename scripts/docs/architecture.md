# Architecture & mapping to marks

- Capture: scripts/generate_sample_data.py simulates POS transactions.
- Ingest/Store: scripts/ingest_and_store.py writes bronze (partitioned parquet) and silver cleaned parquet.
- Transform: scripts/etl_transform.py creates gold tables (daily_sales, product_summary, store_summary).
- Visualize: dashboard/app.py (Streamlit) uses exported CSVs produced by scripts/export_for_viz.py.

This maps capture → ingestion → storage → transformation → visualization and shows where governance, testing or cataloging steps would be added in a real project.
