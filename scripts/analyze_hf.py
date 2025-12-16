import os, datetime
import pandas as pd
from transformers import pipeline

IN_DIR  = "/opt/airflow/data/processed"
OUT_DIR = "/opt/airflow/data/results"
os.makedirs(OUT_DIR, exist_ok=True)

latest = open(f"{IN_DIR}/_latest.txt", "r", encoding="utf-8").read().strip()
df = pd.read_csv(latest)

clf = pipeline("sentiment-analysis")  # modèle HF par défaut (simple)
texts = df["title_clean"].fillna("").tolist()

# limiter si besoin (ex: 50 titres)
texts = texts[:50]
preds = clf(texts)

out = pd.DataFrame(preds)
out["title"] = texts

ts = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
out_path = f"{OUT_DIR}/hn_sentiment_{ts}.csv"
out.to_csv(out_path, index=False)

with open(f"{OUT_DIR}/_latest.txt", "w", encoding="utf-8") as f:
    f.write(out_path)

print("Saved:", out_path)
