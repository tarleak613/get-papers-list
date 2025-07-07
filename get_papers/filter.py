# get_papers/filter.py
from typing import List
from get_papers.models import Author

def is_non_academic(affiliation: str) -> bool:
    academic_keywords = ["University", "Institute", "College", "School", "Department", "Hospital"]
    return not any(word.lower() in affiliation.lower() for word in academic_keywords)

def is_company(affiliation: str) -> bool:
    company_keywords = ["Pharma", "Biotech", "Inc", "Ltd", "Corp", "Company"]
    return any(word.lower() in affiliation.lower() for word in company_keywords)

def extract_email(affiliation: str) -> str:
    import re
    match = re.search(r"[\w\.-]+@[\w\.-]+", affiliation)
    return match.group(0) if match else ""
