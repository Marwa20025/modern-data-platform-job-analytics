import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

FILE = "data/processed/jobs_clean.csv"
# Charger les variables d'environnement
load_dotenv()

# Connexion PostgreSQL
engine = create_engine(
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}"
    f"/{os.getenv('DB_NAME')}"
)

# Lire le fichier CSV
df = pd.read_csv(FILE)

# Convertir la date
df["publication_date"] = pd.to_datetime(df["publication_date"])

# Charger les données
df.to_sql(
    "jobs",
    con=engine,
    if_exists="append",
    index=False
)

print(f"{len(df)} offres chargées dans PostgreSQL.")