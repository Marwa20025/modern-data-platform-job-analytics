import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

from config.logger import logger

FILE = "data/processed/jobs_clean.csv"

load_dotenv()

engine = create_engine(
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}"
    f"/{os.getenv('DB_NAME')}"
)

df = pd.read_csv(FILE)

df["publication_date"] = pd.to_datetime(df["publication_date"])

df.to_sql(
    "jobs",
    con=engine,
    if_exists="append",
    index=False,
)

logger.info(f"{len(df)} offres chargées dans PostgreSQL.")

print(f"{len(df)} offres chargées dans PostgreSQL.")