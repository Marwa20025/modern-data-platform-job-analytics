import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import json
import pandas as pd

from config.logger import logger

INPUT_FILE = "data/raw/jobs_raw.json"
OUTPUT_FILE = "data/processed/jobs_clean.csv"


def transform_jobs():

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    jobs = pd.DataFrame(data["jobs"])

    columns = [
        "id",
        "title",
        "company_name",
        "category",
        "job_type",
        "candidate_required_location",
        "salary",
        "publication_date",
        "tags",
    ]

    jobs = jobs[columns]

    jobs["publication_date"] = pd.to_datetime(jobs["publication_date"])
    jobs["tags"] = jobs["tags"].apply(
        lambda x: ", ".join(x) if isinstance(x, list) else x
    )

    jobs.to_csv(OUTPUT_FILE, index=False)

    logger.info(f"{len(jobs)} offres transformées.")


if __name__ == "__main__":
    transform_jobs()