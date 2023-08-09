.. crossref documentation master file, created by
   sphinx-quickstart on Wed, Aug 09 23:00:39 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to crossref's documentation!
======================================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   QuickStart <contents.rst>
   API Reference <api.rst>

The Crossref API is a RESTful API based on HTTP and JSON. It is designed to be friendly and helpful. It is also rate limited to ensure fair usage.

The Crossref API is organized around [DOIs](https://www.doi.org/). DOIs are persistent identifiers for scholarly content on the internet. They take the form of a prefix and a suffix separated by a slash. The prefix is assigned to a publisher by [Crossref](https://www.crossref.org/). The suffix is created by the publisher and must be unique for each item they publish. The Crossref API allows you to retrieve metadata for a DOI as well as perform full text search and faceted queries.

The Crossref API is a [Hypermedia API](https://en.wikipedia.org/wiki/Hypermedia). This means that it is designed to be browsed with a web browser. You can use a web browser to explore the API and discover new resources. The API is also designed to be consumed by machines. You can use a programming language like Python or Ruby to write programs that interact with the API.

.. admonition:: Rate Limits

    The Crossref API is rate limited to ensure fair usage. The rate limit is 50 requests per second. If you exceed this rate you will receive a 503 response code. If you receive a 503 or 429 response code you should back off and retry after a few seconds.

.. admonition:: Authentication

    The Crossref API does not require authentication. You can make requests to the API without providing any credentials.
    However, if you are making a large number of requests to the API you should consider using an API key. You can obtain an API key by registering for a Crossref account at https://crossref.org/. You can then pass your API key as a query parameter with each request to the API. For example:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
