import requests

def fetch_lever_jobs(company):

    url = f"https://api.lever.co/v0/postings/{company}?mode=json"

    response = requests.get(url)

    if response.status_code != 200:
        return []

    return response.json()