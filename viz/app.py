import os, glob
import pandas as pd
import streamlit as st

RESULTS = "/data/results"
files = sorted(glob.glob(os.path.join(RESULTS, "hn_sentiment_*.csv")))
st.title("Hacker News — Sentiment (HuggingFace)")

if not files:
    st.warning("Aucun résultat pour le moment. Lance le pipeline.")
else:
    df = pd.read_csv(files[-1])
    st.write("Dernier fichier:", os.path.basename(files[-1]))
    st.dataframe(df)

    st.subheader("Distribution des labels")
    st.bar_chart(df["label"].value_counts())
