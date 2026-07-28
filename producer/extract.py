import requests
import json
from datetime import datetime


API_URL = "https://remotive.com/api/remote-jobs"


def extract_jobs():
    response = requests.get(API_URL)

    if response.status_code == 200:
        data = response.json()
        return data["jobs"]

    raise Exception("API request failed")


def save_raw_data(jobs):
    output = {
        "extraction_date": datetime.now().isoformat(),
        "count": len(jobs),
        "jobs": jobs
    }

    with open("producer/data/jobs_raw.json", "w", encoding="utf-8") as file:
        json.dump(output, file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    jobs = extract_jobs()

    save_raw_data(jobs)

    print(f"{len(jobs)} offres sauvegardées dans jobs_raw.json")