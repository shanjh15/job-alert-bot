from config import (
    GREENHOUSE_COMPANIES,
    INCLUDE_KEYWORDS,
    EXCLUDE_KEYWORDS
)

from scrapers.greenhouse import fetch_greenhouse_jobs
from filters.role_filter import is_matching_role


for company in GREENHOUSE_COMPANIES:

    jobs = fetch_greenhouse_jobs(company)

    print(f"\n===== {company.upper()} =====")

    count = 0

    for job in jobs:

        if is_matching_role(
            job["title"],
            INCLUDE_KEYWORDS,
            EXCLUDE_KEYWORDS
        ):

            print(job["title"])

            count += 1

    print(f"\nMatches: {count}")