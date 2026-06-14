MY_SKILLS = [
    "c++",
    "python",
    "react",
    "javascript",
    "typescript"
]

MY_ROLES = [
    "software engineer",
    "software engineer i",
    "software engineer 1",
    "sde",
    "sde 1",
    "associate software engineer",
    "associate engineer",
    "backend engineer",
    "full stack engineer"
]

MY_INTERESTS = [
    "ai",
    "machine learning",
    "llm",
    "genai",
    "generative ai",
    "agent",
    "rag",
    "langchain",
    "langgraph",
    "vector database"
]


def calculate_score(text):

    score = 0

    for skill in MY_SKILLS:
        if skill in text:
            score += 2

    for interest in MY_INTERESTS:
        if interest in text:
            score += 5

    return score