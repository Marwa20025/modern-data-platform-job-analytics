import json
import pandas as pd

INPUT_FILE = "data/raw/jobs_raw.json"
OUTPUT_FILE = "data/processed/jobs_clean.csv"


def transform_jobs():

    # Lire les données brutes
    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)

    jobs = data["jobs"]

    # Transformer en DataFrame
    df = pd.DataFrame(jobs)

    # Garder les colonnes utiles
    columns = [
        "id",
        "title",
        "company_name",
        "category",
        "job_type",
        "candidate_required_location",
        "salary",
        "publication_date",
        "tags"
    ]

    df = df[columns]

    # Nettoyage
    df = df.drop_duplicates(subset=["id"])

    # Convertir les tags en texte
    df["tags"] = df["tags"].apply(
        lambda x: ", ".join(x) if isinstance(x, list) else x
    )

    # Sauvegarder
    df.to_csv(
        OUTPUT_FILE,
        index=False,
        encoding="utf-8"
    )

    print(f"{len(df)} offres nettoyées sauvegardées")


if __name__ == "__main__":
    transform_jobs()