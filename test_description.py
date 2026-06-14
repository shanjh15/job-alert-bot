import requests

job_url = "https://www.mongodb.com/careers/jobs/7860071"

response = requests.get(job_url)

print(response.text[:5000])