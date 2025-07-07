# get_papers/api.py
import requests
from typing import List
import xml.etree.ElementTree as ET

PUBMED_SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

def search_pubmed_ids(query: str, retmax: int = 20) -> List[str]:
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": retmax,
        "retmode": "json"
    }
    resp = requests.get(PUBMED_SEARCH_URL, params=params)
    resp.raise_for_status()
    return resp.json()["esearchresult"]["idlist"]

def fetch_pubmed_details(ids: List[str]) -> ET.Element:
    params = {
        "db": "pubmed",
        "id": ",".join(ids),
        "retmode": "xml"
    }
    resp = requests.get(PUBMED_FETCH_URL, params=params)
    resp.raise_for_status()
    return ET.fromstring(resp.content)
