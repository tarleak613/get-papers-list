Great — since Aganitha also wants a **report** summarizing your:

* ✅ Approach
* ✅ Methodology
* ✅ Results

I'll now generate a clean and professional `report.md` file that you can submit or convert to PDF if required.

---

## 📄 `report.md` (You can rename this to `report.pdf` after converting)

````markdown
# 📊 Aganitha Backend Take-home Assignment Report

## 👨‍💻 Project Title
**get-papers-list** — A PubMed research paper filtering tool for non-academic authors

---

## ✅ Objective

The goal of this project was to develop a command-line Python tool that:

- Accepts a **search query** related to biomedical research
- Fetches research papers using the **PubMed API**
- Filters out papers that contain **at least one author affiliated with a pharmaceutical or biotech company**
- Saves the filtered results into a **CSV file** with clean structure and proper metadata

---

## 🧠 Methodology

### 1. **Technology Stack**
- Python 3.10+
- [Poetry](https://python-poetry.org/) for dependency management
- [Typer](https://typer.tiangolo.com/) for CLI support
- [Requests](https://docs.python-requests.org/) for API calls
- Built-in `csv` and `xml.etree.ElementTree` for CSV formatting and XML parsing

### 2. **Workflow**

#### a. User Input
- User runs the CLI:  
  ```bash
  poetry run get-papers-list "cancer therapy" -f result.csv
````

#### b. PubMed Integration

* Uses `esearch` to fetch PubMed IDs based on the query
* Uses `efetch` to retrieve full metadata for those IDs (in XML)

#### c. XML Parsing

* Extracts:

  * Title
  * Pubmed ID
  * Publication year
  * List of authors
  * Affiliations
  * Email addresses

#### d. Author Filtering (Heuristics)

* If an author's affiliation:

  * **Does NOT** contain keywords like `"university"`, `"institute"`, `"college"`
  * **DOES** contain terms like `"pharma"`, `"biotech"`, `"Inc."`, `"Ltd."`, etc.
  * → It is considered **non-academic**

* Also uses regex to extract email addresses.

#### e. Output

* Saves all valid papers (those with at least one non-academic author) in a CSV with six columns:

  * Pubmed ID
  * Title
  * Publication Date
  * Non-academic Author(s)
  * Company Affiliation(s)
  * Corresponding Author Email

---

## 🗃️ Code Structure

```
get_papers/
├── api.py          # Connects to PubMed API
├── cli.py          # Command-line interface
├── filter.py       # Filtering logic for authors
├── main.py         # Main workflow logic
├── models.py       # Typed dataclasses
├── __init__.py     # Package marker
```

---

## 🧪 Results

### Sample Query: `"cancer therapy"`

CSV Output:

| PubmedID | Title                                             | Publication Date | Non-academic Author(s) | Company Affiliation(s) | Corresponding Author Email |
| -------- | ------------------------------------------------- | ---------------- | ---------------------- | ---------------------- | -------------------------- |
| 40622693 | Multiple comorbidities and healing venous ulcers. | 2025             | Sylvie Hampton         | Wound Consultants Ltd. | (email if found)           |

* Successfully filters papers with authors from private organizations
* Output opens cleanly in Excel or any CSV viewer
* Supports queries with hundreds of papers efficiently

---

## 📦 Packaging & CLI

* The CLI command `get-papers-list` is exposed using `pyproject.toml`
* Project can be installed and run via:

  ```bash
  poetry install
  poetry run get-papers-list "query" -f output.csv
  ```

---

## 🧠 Key Design Choices

* **Modular Code**: Logic separated into API, filtering, parsing, and CLI
* **Typed Python**: Uses `dataclasses` and `typing` for clarity and safety
* **CLI Flexibility**: Typer allows quick command-line integration and helps add future flags easily
* **Heuristics-Driven Filtering**: Uses readable, adjustable keyword-based checks for affiliation

---

## 📝 Tools & Libraries

| Tool        | Use Case                              |
| ----------- | ------------------------------------- |
| Poetry      | Dependency management & CLI packaging |
| Typer       | CLI creation                          |
| Requests    | Calling PubMed APIs                   |
| ElementTree | Parsing XML from PubMed               |
| csv         | Writing clean spreadsheet outputs     |

---

## 📌 Conclusion

The project satisfies all functional and non-functional requirements:

* Command-line driven
* Heuristic-based filtering
* PubMed API integration
* CSV output with correct columns and formatting
* Clean, modular code with type annotations

The tool is ready to be extended or published as a standalone utility.

---

## 🔗 GitHub Repository

[👉 GitHub Link Here](https://github.com/your-username/get-papers-list)

```

---

## ✅ What You Should Do Next

1. Save this as `report.md` or paste into a Google Doc / Word file and export as `report.pdf`
2. Add it to your GitHub repo or email zip submission
3. Make sure the GitHub link is added in the README and/or submission form

Would you like me to:

- Convert this to a downloadable `.pdf` version for you?
- Help you write a professional email to submit this to Aganitha?

Let me know — you're almost done and this is looking **very professional** 💼
```
