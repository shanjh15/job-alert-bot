import requests


def fetch_greenhouse_jobs(company):

    url = (
        f"https://boards-api.greenhouse.io/"
        f"v1/boards/{company}/jobs"
    )

    response = requests.get(url)

    if response.status_code != 200:
        return []

    data = response.json()

    return data.get("jobs", [])