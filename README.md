# Devoir 3 — Airflow : Scraping → Preprocess → Analyse HuggingFace → Visualisation

## Objectif

Mettre en place un pipeline distribué avec **plusieurs DAGs Airflow** :

1. **Scraping** de données (simple)
2. **Préprocessing** (nettoyage / transformation)
3. **Analyse** avec **au moins un modèle HuggingFace** (ici : sentiment-analysis)
4. **Conteneur de visualisation** en fin de pipeline (Streamlit)

Dataset choisi (facile, sans clé API) : **Hacker News (RSS)**.

---

## Structure du projet

```
.
├── docker-compose.yaml
├── Dockerfile
├── dags/
│   ├── dag_scrape.py
│   ├── dag_preprocess.py
│   └── dag_analyze.py
├── scripts/
│   ├── scrape.py
│   ├── preprocess.py
│   └── analyze_hf.py
├── data/
│   ├── raw/
│   ├── processed/
│   └── results/
└── viz/
    ├── Dockerfile
    └── app.py
```

---

## Prérequis

- Docker + Docker Compose v2 installés

---

## Modifications apportées au `docker-compose.yaml`

1. **Construction d’une image Airflow custom** (au lieu d’utiliser uniquement `image:`) via `build: .`
2. Ajout de volumes :
   - `./scripts -> /opt/airflow/scripts`
   - `./data -> /opt/airflow/data`
3. Ajout d’un service **viz** (Streamlit) lisant `./data`

---

## Installation / Lancement

### 1) Construire et initialiser Airflow

Dans le dossier du projet :

```bash
docker compose down
docker compose up --build airflow-init
docker compose up --build
```

### 2) Accès Airflow

Ouvrir :

- [http://localhost:8080](http://localhost:8080)

(Identifiants par défaut si inchangés : `airflow` / `airflow`)

---

## Exécution du pipeline (Airflow UI)

### 1) Activer les DAGs

Dans la page **DAGs**, activer :

- `hn_scrape`
- `hn_preprocess`
- `hn_analyze_hf`

### 2) Lancer le pipeline

- Ouvrir `hn_scrape`
- Cliquer **Trigger DAG ▶**
- Les DAGs suivants se déclenchent automatiquement via **Datasets**.

### 3) Vérifier succès

Dans **Grid/Graph**, vérifier que les tâches passent en **success**.

---

## Sorties attendues (fichiers)

### A) Scraping (données brutes)

Le scraping sauvegarde **localement** un dataset avec **datetime dans le nom** :

- `data/raw/hn_raw_YYYYMMDD_HHMMSS.csv`

### B) Preprocessing

- `data/processed/hn_processed_YYYYMMDD_HHMMSS.csv`

### C) Analyse HuggingFace (sentiment)

- `data/results/hn_sentiment_YYYYMMDD_HHMMSS.csv`

---

## Visualisation (conteneur Streamlit)

Le service `viz` tourne via docker-compose.

Ouvrir :

- [http://localhost:8501](http://localhost:8501)

La page affiche :

- le dernier fichier `hn_sentiment_*.csv`
- un tableau + un graphique simple de distribution des labels.

---

## Tests rapides (optionnel)

### Vérifier les conteneurs

```bash
docker compose ps
```

### Vérifier les derniers fichiers générés

```bash
ls -lt data/raw | head
ls -lt data/processed | head
ls -lt data/results | head
```

---

## Captures d’écran à inclure (recommandé)

Pour prouver l’exécution :

- Page des DAGs (les 3 DAGs visibles/activés)
- Grid/Graph montrant une exécution **success**
- Page Streamlit avec résultats affichés

---

## Arrêt / Nettoyage

Arrêter :

- `Ctrl + C` dans le terminal docker-compose

Puis :

```bash
docker compose down
```

---

## Contenu du rendu (zip)

À remettre sur Teams : un zip contenant au minimum :

- `docker-compose.yaml`
- `Dockerfile` (Airflow custom)
- `dags/`
- `scripts/`
- `viz/`
- `README.md`
- (Optionnel) un exemple de résultats dans `data/results/` + captures d’écran

