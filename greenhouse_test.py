import requests

url = "https://boards-api.greenhouse.io/v1/boards/datadog/jobs"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

print("Keys:", data.keys())

print("Total jobs:", len(data["jobs"]))

for job in data["jobs"][:5]:
    print(job["title"])