#!/usr/bin/env python
"""
This sample script illustrates a basic arXiv api call
followed by parsing of the results using the
feedparser python module.

Please see the documentation at
http://export.arxiv.org/api_help/docs/user-manual.html for more information

feedparser can be downloaded from http://feedparser.org/ .

Author: Tralah M. Brian

"""

import feedparser
import requests
import logging
from argparse import ArgumentParser
from coloring import colored

# Opensearch metadata such as totalResults, startIndex,
# and itemsPerPage live in the opensearch namespase.
# Some entry metadata lives in the arXiv namespace.
# This is a hack to expose both of these namespaces in
# feedparser v4.1
feedparser.mixin._FeedParserMixin.namespaces["http://a9.com/-/spec/opensearch/1.1/"] = (
    "opensearch"
)
feedparser.mixin._FeedParserMixin.namespaces["http://arxiv.org/schemas/atom"] = "arxiv"

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s",
)

# Categories
math_categories: list[str] = [
    "math.AC",
    "math.AG",
    "math.AP",
    "math.AT",
    "math.CA",
    "math.CO",
    "math.CT",
    "math.CV",
    "math.DG",
    "math.DS",
    "math.FA",
    "math.GM",
    "math.GN",
    "math.GR",
    "math.GT",
    "math.HO",
    "math.IT",
    "math.KT",
    "math.LO",
    "math.MG",
    "math.MP",
    "math.NA",
    "math.NT",
    "math.OA",
    "math.OC",
    "math.PR",
    "math.QA",
    "math.RA",
    "math.RT",
    "math.SG",
    "math.SP",
    "math.ST",
]

stat_categories: list[str] = [
    "stat.AP",
    "stat.CO",
    "stat.ME",
    "stat.ML",
    "stat.OT",
    "stat.TH",
]

eess_categories: list[str] = [
    "eess.AS",
    "eess.IV",
    "eess.SP",
    "eess.SY",
]

physics_categories: list[str] = [
    "physics.acc-ph",
    "physics.ao-ph",
    "physics.app-ph",
    "physics.atm-clus",
    "physics.atom-ph",
    "physics.bio-ph",
    "physics.chem-ph",
    "physics.class-ph",
    "physics.comp-ph",
    "physics.data-an",
    "physics.ed-ph",
    "physics.flu-dyn",
    "physics.gen-ph",
    "physics.geo-ph",
    "physics.hist-ph",
    "physics.ins-det",
    "physics.med-ph",
    "physics.optics",
    "physics.plasm-ph",
    "physics.pop-ph",
    "physics.soc-ph",
    "physics.space-ph",
]

cs_categories: list[str] = [
    "cs.AI",
    "cs.AR",
    "cs.CC",
    "cs.CE",
    "cs.CG",
    "cs.CL",
    "cs.CR",
    "cs.CV",
    "cs.CY",
    "cs.DB",
    "cs.DC",
    "cs.DL",
    "cs.DM",
    "cs.DS",
    "cs.ET",
    "cs.FL",
    "cs.GL",
    "cs.GR",
    "cs.GT",
    "cs.HC",
    "cs.IR",
    "cs.IT",
    "cs.LG",
    "cs.LO",
    "cs.MA",
    "cs.MM",
    "cs.MS",
    "cs.NA",
    "cs.NE",
    "cs.NI",
    "cs.OH",
    "cs.OS",
    "cs.PF",
    "cs.PL",
    "cs.RO",
    "cs.SC",
    "cs.SD",
    "cs.SE",
    "cs.SI",
    "cs.SY",
]

cat_prefixes = {
    "cs": "Computer Science",
    "econ": "Economics",
    "eess": "Electrical Engineering and Systems Science",
    "math": "Mathematics",
    "astro-ph": "Astrophysics",
    "cond-mat": "Condensed Matter",
    "gr-qc": "General Relativity and Quantum Cosmology",
    "hep-ex": "High Energy Physics - Experiment",
    "hep-lat": "High Energy Physics - Lattice",
    "hep-ph": "High Energy Physics - Phenomenology",
    "hep-th": "High Energy Physics - Theory",
    "math-ph": "Mathematical Physics",
    "nlin": "Nonlinear Sciences",
    "nucl-ex": "Nuclear Experiment",
    "nucl-th": "Nuclear Theory",
    "physics": "Physics",
    "quant-ph": "Quantum Physics",
    "q-bio": "Quantitative Biology",
    "q-fin": "Quantitative Finance",
    "stat": "Statistics",
}

cat_descs = {
    "cs.AI": "Artificial Intelligence",
    "cs.AR": "Hardware Architecture",
    "cs.CC": "Computational Complexity",
    "cs.CE": "Computational Engineering, Finance, and Science",
    "cs.CG": "Computational Geometry",
    "cs.CL": "Computation and Language",
    "cs.CR": "Cryptography and Security",
    "cs.CV": "Computer Vision and Pattern Recognition",
    "cs.CY": "Computers and Society",
    "cs.DB": "Databases",
    "cs.DC": "Distributed, Parallel, and Cluster Computing",
    "cs.DL": "Digital Libraries",
    "cs.DM": "Discrete Mathematics",
    "cs.DS": "Data Structures and Algorithms",
    "cs.ET": "Emerging Technologies",
    "cs.FL": "Formal Languages and Automata Theory",
    "cs.GL": "General Literature",
    "cs.GR": "Graphics",
    "cs.GT": "Computer Science and Game Theory",
    "cs.HC": "Human-Computer Interaction",
    "cs.IR": "Information Retrieval",
    "cs.IT": "Information Theory",
    "cs.LG": "Machine Learning",
    "cs.LO": "Logic in Computer Science",
    "cs.MA": "Multiagent Systems",
    "cs.MM": "Multimedia",
    "cs.MS": "Mathematical Software",
    "cs.NA": "Numerical Analysis",
    "cs.NE": "Neural and Evolutionary Computing",
    "cs.NI": "Networking and Internet Architecture",
    "cs.OH": "Other Computer Science",
    "cs.OS": "Operating Systems",
    "cs.PF": "Performance",
    "cs.PL": "Programming Languages",
    "cs.RO": "Robotics",
    "cs.SC": "Symbolic Computation",
    "cs.SD": "Sound",
    "cs.SE": "Software Engineering",
    "cs.SI": "Social and Information Networks",
    "cs.SY": "Systems and Control",
    "econ.EM": "Econometrics",
    "econ.GN": "General Economics",
    "econ.TH": "Theoretical Economics",
    "eess.AS": "Audio and Speech Processing",
    "eess.IV": "Image and Video Processing",
    "eess.SP": "Signal Processing",
    "eess.SY": "Systems and Control",
    "math.AC": "Commutative Algebra",
    "math.AG": "Algebraic Geometry",
    "math.AP": "Analysis of PDEs",
    "math.AT": "Algebraic Topology",
    "math.CA": "Classical Analysis and ODEs",
    "math.CO": "Combinatorics",
    "math.CT": "Category Theory",
    "math.CV": "Complex Variables",
    "math.DG": "Differential Geometry",
    "math.DS": "Dynamical Systems",
    "math.FA": "Functional Analysis",
    "math.GM": "General Mathematics",
    "math.GN": "General Topology",
    "math.GR": "Group Theory",
    "math.GT": "Geometric Topology",
    "math.HO": "History and Overview",
    "math.IT": "Information Theory",
    "math.KT": "K-Theory and Homology",
    "math.LO": "Logic",
    "math.MG": "Metric Geometry",
    "math.MP": "Mathematical Physics",
    "math.NA": "Numerical Analysis",
    "math.NT": "Number Theory",
    "math.OA": "Operator Algebras",
    "math.OC": "Optimization and Control",
    "math.PR": "Probability",
    "math.QA": "Quantum Algebra",
    "math.RA": "Rings and Algebras",
    "math.RT": "Representation Theory",
    "math.SG": "Symplectic Geometry",
    "math.SP": "Spectral Theory",
    "math.ST": "Statistics Theory",
    "astro-ph.CO": "Cosmology and Nongalactic Astrophysics",
    "astro-ph.EP": "Earth and Planetary Astrophysics",
    "astro-ph.GA": "Astrophysics of Galaxies",
    "astro-ph.HE": "High Energy Astrophysical Phenomena",
    "astro-ph.IM": "Instrumentation and Methods for Astrophysics",
    "astro-ph.SR": "Solar and Stellar Astrophysics",
    "cond-mat.dis-nn": "Disordered Systems and Neural Networks",
    "cond-mat.mes-hall": "Mesoscale and Nanoscale Physics",
    "cond-mat.mtrl-sci": "Materials Science",
    "cond-mat.other": "Other Condensed Matter",
    "cond-mat.quant-gas": "Quantum Gases",
    "cond-mat.soft": "Soft Condensed Matter",
    "cond-mat.stat-mech": "Statistical Mechanics",
    "cond-mat.str-el": "Strongly Correlated Electrons",
    "cond-mat.supr-con": "Superconductivity",
    "gr-qc": "General Relativity and Quantum Cosmology",
    "hep-ex": "High Energy Physics - Experiment",
    "hep-lat": "High Energy Physics - Lattice",
    "hep-ph": "High Energy Physics - Phenomenology",
    "hep-th": "High Energy Physics - Theory",
    "math-ph": "Mathematical Physics",
    "nlin.AO": "Adaptation and Self-Organizing Systems",
    "nlin.CD": "Chaotic Dynamics",
    "nlin.CG": "Cellular Automata and Lattice Gases",
    "nlin.PS": "Pattern Formation and Solitons",
    "nlin.SI": "Exactly Solvable and Integrable Systems",
    "nucl-ex": "Nuclear Experiment",
    "nucl-th": "Nuclear Theory",
    "physics.acc-ph": "Accelerator Physics",
    "physics.ao-ph": "Atmospheric and Oceanic Physics",
    "physics.app-ph": "Applied Physics",
    "physics.atm-clus": "Atomic and Molecular Clusters",
    "physics.atom-ph": "Atomic Physics",
    "physics.bio-ph": "Biological Physics",
    "physics.chem-ph": "Chemical Physics",
    "physics.class-ph": "Classical Physics",
    "physics.comp-ph": "Computational Physics",
    "physics.data-an": "Data Analysis, Statistics and Probability",
    "physics.ed-ph": "Physics Education",
    "physics.flu-dyn": "Fluid Dynamics",
    "physics.gen-ph": "General Physics",
    "physics.geo-ph": "Geophysics",
    "physics.hist-ph": "History and Philosophy of Physics",
    "physics.ins-det": "Instrumentation and Detectors",
    "physics.med-ph": "Medical Physics",
    "physics.optics": "Optics",
    "physics.plasm-ph": "Plasma Physics",
    "physics.pop-ph": "Popular Physics",
    "physics.soc-ph": "Physics and Society",
    "physics.space-ph": "Space Physics",
    "quant-ph": "Quantum Physics",
    "q-bio.BM": "Biomolecules",
    "q-bio.CB": "Cell Behavior",
    "q-bio.GN": "Genomics",
    "q-bio.MN": "Molecular Networks",
    "q-bio.NC": "Neurons and Cognition",
    "q-bio.OT": "Other Quantitative Biology",
    "q-bio.PE": "Populations and Evolution",
    "q-bio.QM": "Quantitative Methods",
    "q-bio.SC": "Subcellular Processes",
    "q-bio.TO": "Tissues and Organs",
    "q-fin.CP": "Computational Finance",
    "q-fin.EC": "Economics",
    "q-fin.GN": "General Finance",
    "q-fin.MF": "Mathematical Finance",
    "q-fin.PM": "Portfolio Management",
    "q-fin.PR": "Pricing of Securities",
    "q-fin.RM": "Risk Management",
    "q-fin.ST": "Statistical Finance",
    "q-fin.TR": "Trading and Market Microstructure",
    "stat.AP": "Statistics Applications",
    "stat.CO": "Statistics Computation",
    "stat.ME": "Statistics Methodology",
    "stat.ML": "Statistics Machine Learning",
    "stat.OT": "Other Statistics",
    "stat.TH": "Statistics Theory",
}

fields = [
    "ti",
    "au",
    "abs",
    "co",
    "jr",
    "cat",
    "rn",
    "id",
    "all",
]

field_descs = {
    "ti": "Title",
    "au": "Author",
    "abs": "Abstract",
    "co": "Comment",
    "jr": "Journal Reference",
    "cat": "Subject Category",
    "rn": "Report Number",
    "id": "Arxiv id (use id_list instead)",
    "all": "All of the above",
}


# Base api query url
base_url = "http://export.arxiv.org/api/query"
MAX_RESULTS = 30000
MAX_PER_CALL = 2000
Seconds_Between_Calls = 3

# for i in range(start,total_results,results_per_iteration):
# Remember to play nice and sleep a bit before you call the api again!


class ArxivEntry:
    def __init__(
        self,
        arxiv_id,
        title,
        published,
        abstract,
        abstract_url=None,
        author=None,
        authors=[],
        doi_id=None,
        doi_url=None,
        pdf_url=None,
        primary_category=None,
        categories=[],
        affiliation=None,
        comment=None,
        journal_ref=None,
    ):
        self.arxiv_id = arxiv_id
        self.title = title
        self.published = published
        self.abstract = abstract
        self.abstract_url = abstract_url
        self.author = author
        self.authors = authors
        self.doi_id = doi_id
        self.doi_url = doi_url
        self.pdf_url = pdf_url
        self.primary_category = primary_category
        self.categories = categories
        self.affiliation = affiliation
        self.comment = comment
        self.journal_ref = journal_ref

    def debug_print(self):
        print(
            "Arxiv-id: %s"
            % colored(
                self.arxiv_id,
                attrs=["underline"],
            )
        )
        print(
            "Title: %s"
            % colored(
                self.title,
                color="green",
            )
        )
        if self.published is not None:
            print("Published: %s" % colored(self.published, attrs=["dark"]))
        author_string = self.author
        if self.affiliation is not None:
            author_string += " (%s)" % self.affiliation
        print("Last Author: %s" % author_string)
        print(
            "Authors: %s"
            % ", ".join(
                colored(
                    author,
                    color="red",
                    attrs=["dark"],
                )
                for author in self.authors
            )
        )
        if self.affiliation is not None:
            print(
                "Affiliation: %s"
                % colored(
                    self.affiliation,
                    attrs=["dark"],
                ),
            )
        if self.journal_ref is not None:
            print(
                "Journal reference: %s"
                % colored(
                    self.journal_ref,
                    attrs=["bold", "dark"],
                )
            )
        if self.pdf_url is not None:
            print("PDF link: %s" % colored(self.pdf_url, color="cyan"))
        if self.doi_id is not None or self.doi_url is not None:
            print(
                (
                    "DOI: %s    %s"
                    % (
                        colored(self.doi_id, color="blue"),
                        colored(self.doi_url),
                    )
                ).strip()
            )
        if self.comment is not None:
            print("Comments: %s" % colored(self.comment, attrs=["dark"]))
        words = self.abstract.split()
        primary_category_description = cat_descs.get(self.primary_category)
        all_colored_categories = [
            colored(t, attrs=["bold", "dark"]) for t in self.categories
        ]
        print(
            "Primary Category: %s - %s"
            % (
                colored(self.primary_category, attrs=["bold"]),
                colored(primary_category_description, color="magenta"),
            )
        )
        print("All Categories: %s" % (", ").join(all_colored_categories))

        if self.abstract_url is not None:
            absurl = colored(self.abstract_url, color="yellow")
        else:
            absurl = ""
        print(("Abstract: %d words %s" % (len(words), absurl)).strip())


def extract_arxiv_entry(entry):
    arxiv_id = entry.id.split("/abs/")[-1]
    title = (
        entry.title.replace(" \n", "")
        .replace("\n ", "")
        .replace("\n", " ")
        .replace("  ", " ")
    )
    # The abstract is in the <summary> element
    summary = (
        entry.summary.replace(" \n", "")
        .replace("\n ", "")
        .replace("\n", " ")
        .replace("  ", " ")
    )
    # feedparser v4.1 only grabs the first author
    author = entry.author
    authors = [author]
    published = entry.published
    # grab the affiliation in <arxiv:affiliation> if present
    # - this will only grab the first affiliation encountered
    #   (the first affiliation for the first author)
    # Please email the list with a way to get all of this information!
    if hasattr(entry, "arxiv_affiliation"):
        affiliation = entry.arxiv_affiliation
        affiliation = (
            affiliation.replace(" \n", "")
            .replace("\n ", "")
            .replace("\n", " ")
            .replace("  ", " ")
        )
    else:
        affiliation = None
    # feedparser v5.0.1 correctly handles multiple authors, print them all
    try:
        authors = [author.name for author in entry.authors]
    except AttributeError:
        pass
    # The journal reference, comments and primary_category sections are
    # under the arxiv namespace
    if hasattr(entry, "arxiv_journal_ref"):
        journal_ref = entry.arxiv_journal_ref
        journal_ref = (
            journal_ref.replace(" \n", "")
            .replace("\n ", "")
            .replace("\n", " ")
            .replace("  ", " ")
        )
    else:
        journal_ref = None

    # get the links to the abs page and pdf for this e-print
    abs_page = None
    pdf_link = None
    doi_link = None
    for link in entry.links:
        if link.rel == "alternate":
            abs_page = link.href
        elif link.title == "pdf":
            pdf_link = link.href
        elif link.title == "doi":
            doi_link = link.href
    if hasattr(entry, "arxiv_doi"):
        doi = entry.arxiv_doi
    else:
        if doi_link is not None:
            doi_link = doi_link.split("/")[-1]
        doi = None
    if hasattr(entry, "arxiv_comment"):
        comment = entry.arxiv_comment
        comment = entry.arxiv_comment
        comment = (
            comment.replace(" \n", "")
            .replace("\n ", "")
            .replace("\n", " ")
            .replace("  ", " ")
        )
    else:
        comment = None
    # Since the <arxiv:primary_category> element has no data, only
    # attributes, feedparser does not store anything inside
    # entry.arxiv_primary_category
    # This is a dirty hack to get the primary_category, just take the
    # first element in entry.tags.  If anyone knows a better way to do
    # this, please email the list!
    primary_category = entry.tags[0]["term"].strip()
    all_categories = [t["term"] for t in entry.tags]
    arxiv_entry = ArxivEntry(
        arxiv_id=arxiv_id,
        title=title,
        published=published,
        abstract=summary,
        abstract_url=abs_page,
        author=author,
        authors=authors,
        doi_id=doi,
        doi_url=doi_link,
        pdf_url=pdf_link,
        primary_category=primary_category,
        categories=all_categories,
        affiliation=affiliation,
        comment=comment,
        journal_ref=journal_ref,
    )
    return arxiv_entry


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "term",
        type=str,
        metavar="search_term",
        default="electron",
        help="Search term",
    )
    parser.add_argument(
        "-n",
        "--number",
        type=int,
        dest="number",
        default=10,
        help="Limit the Number of results",
    )
    parser.add_argument(
        "--start",
        type=int,
        dest="start",
        default=0,
        help="Start index",
    )
    parser.add_argument(
        "--sort-by",
        type=str,
        dest="sort_by",
        default="relevance",
        help="Sort By",
        choices=["relevance", "lastUpdatedDate", "submittedDate"],
    )
    parser.add_argument(
        "--order",
        type=str,
        dest="sort_order",
        default="descending",
        help="Sort Order",
        choices=["ascending", "descending"],
    )
    args = parser.parse_args()
    # Search parameters
    start = args.start  # retreive the first 5 results
    max_results = args.number  # retreive the first 5 results
    # search for electron in all fields
    term = args.term

    cat_intrest = (cs_categories + stat_categories +
                   math_categories + eess_categories,)
    prepended = [f"cat:{c}" for c in cat_intrest]
    or_cat_query = " OR ".join(prepended)
    inparens = f"({or_cat_query})"
    _ = inparens
    # search_query = f"all:'{term}' AND " + inparens
    search_query = f"all:'{term}'"
    query_params = dict(
        search_query=search_query,
        start=start,
        max_results=max_results,
        sortBy=args.sort_by,
        sortOrder=args.sort_order,
    )
    gathered_entries = []

    # perform a GET request using the base_url and query
    response = requests.get(base_url, params=query_params)

    # parse the response using feedparser
    feed = feedparser.parse(response.content)

    # print out feed information
    arxiv_query_title = feed.feed.title
    print("Feed title: %s" % arxiv_query_title)
    last_updated = feed.feed.updated
    print("Feed last updated: %s" % last_updated)
    # print opensearch metadata
    opensearch_startindex, opensearch_itemsperpage, opensearch_totalresults = (
        feed.feed.opensearch_startindex,
        feed.feed.opensearch_itemsperpage,
        feed.feed.opensearch_totalresults,
    )
    print(
        "startIndex: %s, itemsPerPage: %s, totalResults: %s"
        % (
            opensearch_startindex,
            opensearch_itemsperpage,
            opensearch_totalresults,
        ),
    )

    # Run through each entry, and print out information
    for entry in feed.entries:
        # print(type(entry)) FeedParserDict
        print()
        if (
            entry.title.lower().strip().startswith("error")
            and len(entry.id.split("/abs")) < 2
        ):
            # id,title,summary,updated,link,author for error
            logging.error("%s" % colored(entry.title, color="white"))
            logging.warning("%s" % colored(entry.author, color="white"))
            logging.error("%s" % colored(entry.summary, color="red"))
            try:
                logging.warning(
                    "Details: %s" % colored(entry.link, color="yellow"),
                )
            except AttributeError:
                pass
            break
        arxiv_entry = extract_arxiv_entry(entry)
        arxiv_entry.debug_print()
        gathered_entries.append(arxiv_entry)
        print("---" * 21)


if __name__ == "__main__":
    main()
