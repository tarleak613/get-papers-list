# get_papers/main.py
from typing import List
from xml.etree.ElementTree import Element
from get_papers.api import search_pubmed_ids, fetch_pubmed_details
from get_papers.models import Author, Paper
from get_papers.filter import is_non_academic, is_company, extract_email

def parse_papers(query: str, debug: bool = False) -> List[Paper]:
    ids = search_pubmed_ids(query)
    root = fetch_pubmed_details(ids)

    papers = []

    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID")
        title = article.findtext(".//ArticleTitle")
        pub_date = article.findtext(".//PubDate/Year") or "Unknown"
        
        authors_xml = article.findall(".//Author")
        non_academic_authors = []
        companies = set()
        email = None

        for auth in authors_xml:
            name = f"{auth.findtext('ForeName') or ''} {auth.findtext('LastName') or ''}".strip()
            affiliation = auth.findtext(".//AffiliationInfo/Affiliation") or ""

            if is_non_academic(affiliation) and is_company(affiliation):
                companies.add(affiliation)
                email = extract_email(affiliation)
                non_academic_authors.append(Author(name, affiliation, email))

        if non_academic_authors:
            paper = Paper(
                pubmed_id=pmid,
                title=title,
                publication_date=pub_date,
                non_academic_authors=non_academic_authors,
                company_affiliations=list(companies),
                corresponding_author_email=email
            )
            papers.append(paper)
    
    return papers
