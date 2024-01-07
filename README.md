<img src="https://img.shields.io/github/license/TralahM/academic_citations"> <img src="https://img.shields.io/github/last-commit/TralahM/academic_citations"> <img src="https://img.shields.io/github/contributors/TralahM/academic_citations"> <img src="https://img.shields.io/github/issues-pr-raw/TralahM/academic_citations?color=blue"> <img src="https://img.shields.io/github/issues-pr-closed-raw/TralahM/academic_citations?color=red"> <img src="https://img.shields.io/github/issues-raw/TralahM/academic_citations?color=green">
<img src="https://img.shields.io/github/issues-closed-raw/TralahM/academic_citations?color=yellow"> <img src="https://img.shields.io/github/forks/TralahM/academic_citations?label=Forks&style=social"> <img src="https://img.shields.io/github/forks/TralahM/academic_citations?label=Forks&style=social"> <img src="https://img.shields.io/github/stars/TralahM/academic_citations?style=social">
<img src="https://img.shields.io/github/watchers/TralahM/academic_citations?label=Watch&style=social"> <img src="https://img.shields.io/github/downloads/TralahM/academic_citations/total"> <img src="https://img.shields.io/github/repo-size/TralahM/academic_citations"> <img src="https://img.shields.io/github/languages/count/TralahM/academic_citations"> <img src="https://img.shields.io/github/v/tag/TralahM/academic_citations"> <img src="https://img.shields.io/readthedocs/crossref"> <img src="https://img.shields.io/pypi/v/crossref"> <img src="https://img.shields.io/pypi/pyversions/crossref"> <img src="https://img.shields.io/pypi/wheel/crossref"> <img src="https://img.shields.io/pypi/status/crossref?label=pypi%20status"> <img src="https://img.shields.io/pypi/format/crossref?label=pypi%20format">

# academic_citations
> UnOffical Python Crossref.org API Wrapper and CLI.

---

### Table of Contents
- [QuickStart](#QuickStart)
- [Documentation/Usage](#Documentation)
- [Contributing](#Contributing)
- [Credits](#Credits)

---
## QuickStart
#### Installation

```
pip install crossref
```
#### From Source
```
git clone https://github.com/TralahM/academic_citations
cd academic_citations

python setup.py bdist_wheel
pip install -e .

```
---

## CLI Usage

```console
usage: crossref [-h] [--mailto MAILTO] [--auth-token AUTH_TOKEN]
                [--api-version API_VERSION] [-o OUTFILE] [--rows ROWS]
                [--format-on]
                [--sample SAMPLE | --offset OFFSET | --cursor CURSOR]
                {pubs,works,publications,w,p,journals,journal,jnl,j,members,member,m,funders,funder,f,types,type,t,licenses,license,lc,lcs,cite,citation,citations,ref,refs,reference,references,prefix,pre,px}
                ...

options:
  -h, --help            show this help message and exit
  --mailto MAILTO       mailto address for polite users
  --auth-token AUTH_TOKEN
                        auth token for authenticated (Plus) users
  --api-version API_VERSION
                        API version to use (default=v1)
  -o OUTFILE            Json filename to also store the output
  --rows ROWS           Number of Rows to return (default=20)
  --format-on           Format json output using pygments syntax highlighting?
  --sample SAMPLE       Sample size
  --offset OFFSET       Offset
  --cursor CURSOR       Cursor parameter

commands:
  {pubs,works,publications,w,p,journals,journal,jnl,j,members,member,m,funders,funder,f,types,type,t,licenses,license,lc,lcs,cite,citation,citations,ref,refs,reference,references,prefix,pre,px}
    pubs (works, publications, w, p)
                        Interact with the Works API. Supports the following
                        parameters: - Queries: (query) and (query.field(s)) -
                        Filters: (filter=type-name:filter)(s) or dot filters
                        (filter=type-name.field-name:filter)(s) - Pagination
                        with offsets: (offset) and (rows) - Deep paging:
                        (cursor=*) initially and (cursor=next-cursor) in
                        subsequent requests - Elements: (select=field-name(s))
                        - Sort: (sort) and (order) - Facets: (facet=type-
                        name:*) - Sample: (sample) And returns a list of works
                        (journal articles, conference proceedings, books,
                        components, etc), or a single work (if you specify a
                        DOI).
    journals (journal, jnl, j)
                        Interact with the Journals API. Supports the following
                        parameters: - Queries: (query) and (query.field(s)) -
                        Pagination with offsets: (offset) and (rows) - Deep
                        paging: (cursor=*) initially and (cursor=next-cursor)
                        in subsequent requests
    members (member, m)
                        Interact with the Members API. Supports the following
                        parameters: - Queries: (query) and (query.field(s)) -
                        Pagination with offsets: (offset) and (rows) - Deep
                        paging: (cursor=*) initially and (cursor=next-cursor)
                        in subsequent requests - Filters: (filter=type-
                        name:filter)(s) or dot filters (filter=type-
                        name.field-name:filter)(s)
    funders (funder, f)
                        Interact with the Funders API. Supports the following
                        parameters: - Queries: (query) and (query.field(s)) -
                        Pagination with offsets: (offset) and (rows) - Deep
                        paging: (cursor=*) initially and (cursor=next-cursor)
                        in subsequent requests - Filters:
                        (filter=location:filter) - location = funders located
                        in given country
    types (type, t)     Interact with the Types API. Supports the following
                        parameters: - Pagination with offsets: (offset) and
                        (rows)
    licenses (license, lc, lcs)
                        Interact with the Licenses API. Supports the following
                        parameters: - Queries: (query) and (query.field(s)) -
                        Pagination with offsets: (offset) and (rows) - Deep
                        paging: (cursor=*) initially and (cursor=next-cursor)
                        in subsequent requests
    cite (citation, citations, ref, refs, reference, references)
                        Get Citation/ Reference Text of the given DOI In the
                        Specified Style (apa, mla, bibtex, etc).
    prefix (pre, px)    Interact with the Types API. Supports the following
                        parameters: - Pagination with offsets: (offset) and
                        (rows)

Author: Tralah M Brian (TralahM) <briantralah@gmail.com>. Project:
<https://github.com/TralahM/academic_citations>

```

## Documentation

[![Documentation](https://img.shields.io/badge/Docs-crossref-blue.svg?style=for-the-badge)](https://crossref.readthedocs.io)


#### API Reference

---
## Contributing

---

## Credits
[![TralahTek](https://img.shields.io/badge/Organization-TralahTek-black.svg?style=for-the-badge&logo=github)](https://github.com/TralahTek)
[![TralahM](https://img.shields.io/badge/Engineer-TralahM-blue.svg?style=for-the-badge&logo=github)](https://github.com/TralahM)
[![TralahM](https://img.shields.io/badge/Maintainer-TralahM-green.svg?style=for-the-badge&logo=github)](https://github.com/TralahM)



[![](https://img.shields.io/badge/Github-TralahM-green?style=for-the-badge&logo=github)](https://github.com/TralahM)
[![](https://img.shields.io/badge/Twitter-%40tralahtek-blue?style=for-the-badge&logo=twitter)](https://twitter.com/TralahM)
[![TralahM](https://img.shields.io/badge/Kaggle-TralahM-purple.svg?style=for-the-badge&logo=kaggle)](https://kaggle.com/TralahM)
[![TralahM](https://img.shields.io/badge/LinkedIn-TralahM-white.svg?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/TralahM)


[![Blog](https://img.shields.io/badge/Blog-tralahm.tralahtek.com-blue.svg?style=for-the-badge&logo=rss)](https://tralahm.tralahtek.com)

[![TralahTek](https://img.shields.io/badge/Organization-TralahTek-cyan.svg?style=for-the-badge)](https://org.tralahtek.com)
---
