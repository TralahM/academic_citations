Quickstart
===========

1. Install https://www.python.org/downloads/ and pip https://pip.pypa.io/en/stable/installing/.
2. Install the requirements: `pip install crossref`
3. Run the cli tool: `crossref` (or `python -m crossref.crossref_cli`)

You can also use the library in your own code:

.. code-block:: python

    from crossref import CrossrefAPIClient
    client = CrossrefAPIClient()

    works = client.get_works(
        {
            "rows": 20,
            "query": "Machine learning",
        }
    )
    print(works.json())

    work = client.get_work("10.5621/sciefictstud.40.2.0382")
    print(work.json())

    funders = client.get_funders(
        {
            "rows": 20,
            "query": "Machine learning",
        }
    )

    print(funders.json())

    funder = client.get_funder("100000003")

    print(funder.json())

    members = client.get_members(
        {
            "rows": 20,
            "query": "Machine learning",
        }
    )

    print(members.json())

    member = client.get_member("1")

    journals = client.get_journals(
        {
            "rows": 20,
            "query": "Machine learning",
        }
    )

    print(journals.json())

    journal = client.get_journal("2167-8359")

    print(journal.json())

    types = client.get_types(
        {
            "rows": 20,
            "query": "Machine learning",
        }
    )

    print(types.json())

    type = client.get_type("journal-article")

    print(type.json())

    licenses = client.get_licenses(
        {
            "rows": 20,
            "query": "Machine learning",
        }
    )

    print(licenses.json())

    prefix = client.get_prefix("10.1038")

    print(prefix.json())

    citation = client.get_work_reference("10.5621/sciefictstud.40.2.0382",style="apa")
    print(citation.text)

    citation = client.get_work_reference("10.5621/sciefictstud.40.2.0382",style="bibtex")
    print(citation.text)

    citation = client.get_work_reference("10.5621/sciefictstud.40.2.0382",style="mla")
    print(citation.text)

For more information, see the https://crossref.readthedocs.io/en/latest/.
