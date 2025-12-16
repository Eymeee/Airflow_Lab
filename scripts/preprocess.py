import os, datetime
import pandas as pd

RAW_DIR = "/opt/airflow/data/raw"
OUT_DIR = "/opt/airflow/data/processed"
os.makedirs(OUT_DIR, exist_ok=True)

latest = open(f"{RAW_DIR}/_latest.txt", "r", encoding="utf-8").read().strip()
df = pd.read_csv(latest)

df["title_clean"] = (
    df["title"].fillna("")
      .str.strip()
      .str.lower()
)
df["title_len"] = df["title_clean"].str.len()

ts = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
out_path = f"{OUT_DIR}/hn_processed_{ts}.csv"
df.to_csv(out_path, index=False)

with open(f"{OUT_DIR}/_latest.txt", "w", encoding="utf-8") as f:
    f.write(out_path)

print("Saved:", out_path)
