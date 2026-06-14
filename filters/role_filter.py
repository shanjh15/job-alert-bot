def is_matching_role(
        title,
        include_keywords,
        exclude_keywords):

    title_lower = title.lower()

    # Exclusions
    if any(word in title_lower for word in exclude_keywords):
        return False

    # Reject higher levels
    bad_patterns = [
        "engineer ii",
        "engineer iii",
        "engineer iv",
        "software engineer 2",
        "software engineer 3",
        "software engineer 4",
        "senior",
        "staff",
        "principal",
        "lead",
        "manager"
    ]

    if any(pattern in title_lower for pattern in bad_patterns):
        return False

    # Accept desired roles
    if any(keyword in title_lower for keyword in include_keywords):
        return True

    return False