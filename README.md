# 📘 get-papers-list

A Python command-line tool to fetch PubMed research papers based on a user query and extract papers that include **at least one author affiliated with a non-academic (pharmaceutical or biotech) organization**.

---

## 🚀 Features

- Fetches research papers using the PubMed E-utilities API
- Filters papers that include non-academic authors using simple heuristics
- Outputs data in a clean CSV format or prints to console
- Fully typed Python code with modular structure
- CLI interface with Typer (`--help`, `--debug`, `--file` supported)
- Poetry-based project setup and execution

---

## 🗃️ Code Structure

```bash
get_papers/
├── api.py          # Connects to PubMed API to fetch paper data
├── cli.py          # CLI interface (Typer)
├── filter.py       # Logic to filter non-academic authors
├── main.py         # Glue logic to tie everything together
├── models.py       # Typed data models (Author, Paper)
├── __init__.py     # Marks as Python package
README.md           # This file
pyproject.toml      # Poetry config
```

## 💻 Installation & Usage
1. Clone the Repo and Install Poetry (if not already)
<pre> git clone https://github.com/your-username/get-papers-list.git 
 cd get-papers-list 
 poetry install </pre>

2. Run the CLI
<pre> poetry run get-papers-list "your search query" </pre>

To save results to a CSV file:
<pre> poetry run get-papers-list "cancer therapy" -f results.csv </pre>

To see debug information:
<pre> poetry run get-papers-list "cancer therapy" --debug </pre>

## 🔍 Output Format (CSV Columns)
PubmedID – Paper ID

Title – Title of the research paper

Publication Date – Year of publication

Non-academic Author(s) – Author names who work in companies

Company Affiliation(s) – Company names from author affiliation field

Corresponding Author Email – Email address extracted from affiliation text

## 🧠 Heuristics Used
Academic affiliation detection:

Looks for words like "University", "Institute", "College", "Hospital", etc.

Non-academic affiliation detection:

Looks for words like "Pharma", "Biotech", "Inc", "Ltd", "Company"

Emails extracted using regular expressions from affiliation strings

## 🔧 Tools & Libraries Used
Tool	Purpose
Poetry	Dependency & packaging manager
Typer	CLI interface
Requests	PubMed API calls
csv module	Output formatting
ElementTree	XML parsing from PubMed

## 📌 Notes
Only papers with at least one company-affiliated author are included.

Some results may have missing email addresses or affiliations if PubMed data is incomplete.

Strict typing used via dataclasses and typing.

## 🤝 Credits
Made as part of the Aganitha Backend Take-home Assignment.

## ✅ Final Step

Save that as `README.md` in your project root (same level as `pyproject.toml`).  
Now your submission meets all the documented criteria.

Let me know if you want help:
- Hosting this on GitHub (with a good commit message)
- Publishing it to TestPyPI (for bonus points)
- Writing an email reply to send your assignment professionally

You're in great shape!
