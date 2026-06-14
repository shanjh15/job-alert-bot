GOOD_PATTERNS = [
    "0-2 years",
    "0 to 2 years",
    "0-3 years",
    "0 to 3 years",
    "1-3 years",
    "1 to 3 years",
    "entry level",
    "early career",
    "new grad",
    "graduate"
]

BAD_PATTERNS = [
    "5+ years",
    "6+ years",
    "7+ years",
    "8+ years",
    "10+ years",
    "senior",
    "staff engineer",
    "principal engineer"
]


def is_good_experience_level(text):

    text = text.lower()

    if any(pattern in text for pattern in BAD_PATTERNS):
        return False

    if any(pattern in text for pattern in GOOD_PATTERNS):
        return True

    return None