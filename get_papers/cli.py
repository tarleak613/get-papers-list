# get_papers/cli.py

import typer
import csv
from get_papers.main import parse_papers
from get_papers.models import Paper

app = typer.Typer()

@app.command()
def get_papers_list(
    query: str,
    file: str = typer.Option(None, "-f", help="Output CSV filename"),
    debug: bool = typer.Option(False, "-d", "--debug", help="Enable debug output")
):
    """Fetch and display or save filtered PubMed papers."""
    papers = parse_papers(query, debug)

    if not papers:
        typer.echo("No papers found.")
        raise typer.Exit()

    if file:
        with open(file, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["PubmedID", "Title", "Publication Date", "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"])
            for paper in papers:
                authors = "; ".join([a.name for a in paper.non_academic_authors])
                companies = "; ".join(paper.company_affiliations)
                writer.writerow([paper.pubmed_id, paper.title, paper.publication_date, authors, companies, paper.corresponding_author_email])
        typer.echo(f"Saved to {file}")
    else:
        for p in papers:
            typer.echo(f"{p.pubmed_id}: {p.title}")

# 👇 Required for Typer to work with the poetry script
def main():
    app()

if __name__ == "__main__":
    main()
