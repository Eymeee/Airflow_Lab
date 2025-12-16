import os, datetime, csv, requests
import xml.etree.ElementTree as ET

RAW_DIR = "/opt/airflow/data/raw"
os.makedirs(RAW_DIR, exist_ok=True)

url = "https://hnrss.org/frontpage"
xml = requests.get(url, timeout=30).text
root = ET.fromstring(xml)

ts = datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
out_path = f"{RAW_DIR}/hn_raw_{ts}.csv"

items = root.findall(".//item")
with open(out_path, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["title", "link", "pubDate"])
    for it in items:
        title = (it.findtext("title") or "").strip()
        link = (it.findtext("link") or "").strip()
        pub  = (it.findtext("pubDate") or "").strip()
        w.writerow([title, link, pub])

# pointeur vers le dernier fichier (pratique pour preprocess)
with open(f"{RAW_DIR}/_latest.txt", "w", encoding="utf-8") as f:
    f.write(out_path)

print("Saved:", out_path)
