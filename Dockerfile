FROM apache/airflow:2.10.3

USER root
RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*
USER airflow

RUN pip install --no-cache-dir pandas==2.2.2 transformers==4.44.2 torch==2.4.0
