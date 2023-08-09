#!/usr/bin/env python

import backoff
import requests
import logging
import urllib.parse

logging.getLogger("backoff").addHandler(logging.StreamHandler())


class CrossRefAPIClient:
    def __init__(
        self,
        api_host="https://api.crossref.org",
        api_version="v1",
        api_auth_token=None,
        api_mailto=None,
    ):
        self.api_host = api_host
        self.api_version = api_version
        self.api_auth_token = api_auth_token
        self.api_mailto = api_mailto

    @property
    def user_agent(self):
        return (
            "crossrefapi.py/0.1.0; mailto:{}".format(self.api_mailto)
            if self.api_mailto
            else "crossrefapi.py/0.1.0"
        )

    @property
    def headers(self):
        headers = {"User-Agent": self.user_agent}
        if self.api_auth_token:
            headers.update(
                {
                    "Crossref-Plus-API-Token": f"Bearer {self.api_auth_token}"
                    if not self.api_auth_token.startswith("Bearer ")
                    else self.api_auth_token,
                }
            )
        return headers

    def get(self, path: str, params: dict = None, headers: dict = {}):
        url = (
            f"{self.api_host}/{self.api_version}/{path}"
            if self.api_version
            else f"{self.api_host}/{path}"
        )
        headers = headers.update(self.headers)
        return get_url(url, headers=headers, params=params)

    def get_works(self, params: dict = None):
        return self.get("works", params=params)

    def get_work(self, doi: str):
        doi = urllib.parse.quote(doi, safe="")
        return self.get(f"works/{doi}")

    def get_work_reference(self, doi: str, style: str):
        headers = {
            "Accept": f"text/x-bibliography; style={style}",
        }
        doi_url = f"https://doi.org/{doi}"
        return get_url(doi_url, headers=headers)

    def get_funders(self, params: dict = None):
        return self.get("funders", params=params)

    def get_funder(self, funder_id: str):
        funder_id = urllib.parse.quote(funder_id, safe="")
        return self.get(f"funders/{funder_id}")

    def get_funder_works(self, funder_id: str, params: dict = None):
        funder_id = urllib.parse.quote(funder_id, safe="")
        return self.get(f"funders/{funder_id}/works", params=params)

    def get_members(self, params: dict = None):
        return self.get("members", params=params)

    def get_member(self, member_id: int):
        member_id = urllib.parse.quote(member_id, safe="")
        return self.get(f"members/{member_id}")

    def get_member_works(self, member_id: int, params: dict = None):
        member_id = urllib.parse.quote(member_id, safe="")
        return self.get(f"members/{member_id}/works", params=params)

    def get_prefix_metadata(self, prefix_id: str):
        prefix_id = urllib.parse.quote(prefix_id, safe="")
        return self.get(f"prefixes/{prefix_id}")

    def get_prefix_works(self, prefix_id: str, params: dict = None):
        prefix_id = urllib.parse.quote(prefix_id, safe="")
        return self.get(f"prefixes/{prefix_id}/works", params=params)

    def get_types(self, params: dict = None):
        return self.get(f"types", params=params)

    def get_type(self, type_id: str):
        type_id = urllib.parse.quote(type_id, safe="")
        return self.get(f"types/{type_id}")

    def get_type_works(self, type_id: str, params: dict = None):
        type_id = urllib.parse.quote(type_id, safe="")
        return self.get(f"types/{type_id}/works", params=params)

    def get_licenses(self, params: dict = None):
        return self.get(f"licenses", params=params)

    def get_journals(self, params: dict = None):
        return self.get(f"journals", params=params)

    def get_journal(self, issn: str):
        issn = urllib.parse.quote(issn, safe="")
        return self.get(f"journals/{issn}")

    def get_journal_works(self, issn: str, params: dict = None):
        issn = urllib.parse.quote(issn, safe="")
        return self.get(f"journals/{issn}/works", params=params)


def backoff_hdlr(details):
    print(
        "Backing off {wait:0.1f} seconds after {tries} tries "
        "calling function {target} with args {args} and kwargs "
        "{kwargs}".format(**details)
    )


def giveup_hdlr(details):
    print(
        "Giving up after {tries} tries calling function "
        "{target} with args {args} and kwargs {kwargs}".format(**details)
    )


def log_request_headers(r):
    if r is None:
        return True
    hs = dict(r.headers)
    d = {
        "headers": {k: hs[k] for k in hs if k.lower().startswith("x")},
        "status_code": r.status_code,
        "url": r.url,
    }
    return False


def fatal_code(e):
    if e is None:
        return True
    return 400 <= e.response.status_code < 500


@backoff.on_predicate(
    backoff.runtime,
    predicate=log_request_headers,
    value=10,
    max_tries=1,
    jitter=None,
)
@backoff.on_exception(
    backoff.expo,
    requests.exceptions.RequestException,
    max_time=60,
    on_backoff=[backoff_hdlr],
    giveup=fatal_code,
    on_giveup=[giveup_hdlr],
)
@backoff.on_exception(
    backoff.expo,
    requests.exceptions.Timeout,
    max_time=300,
    on_giveup=[giveup_hdlr],
)
@backoff.on_exception(
    backoff.expo,
    requests.exceptions.ConnectionError,
    max_time=300,
    on_giveup=[giveup_hdlr],
    on_backoff=[backoff_hdlr],
)
def get_url(url, headers=None, params=None):
    return requests.get(url, headers=headers, params=params)
