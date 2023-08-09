
        Free form search queries can be made, for example, works that include renear or ontologies (or both):

            /works?query=renear+ontologies
        Field Queries:
            Field queries allow for queries that match only particular fields of metadata. For example, this query matches records that contain the tokens richard or feynman (or both) in any author field:

            /works?query.author=richard+feynman
            Field queries can be combined with the general query parameter and each other. Each query parameter is ANDed with the others:

            /works?query.title=room+at+the+bottom&query.author=richard+feynman
            This endpoint supports the following field queries:

            query.affiliation - query contributor affiliations
            query.author - query author given and family names
            query.bibliographic - query bibliographic information, useful for citation look up, includes titles, authors, ISSNs and publication years
            query.chair - query chair given and family names
            query.container-title - query container title aka. publication name
            query.contributor - query author, editor, chair and translator given and family names
            query.degree - query degree
            query.description - query description
            query.editor - query editor given and family names
            query.event-acronym - query acronym of the event
            query.event-location - query location of the event
            query.event-name - query name of the event
            query.event-sponsor - query sponsor of the event
            query.event-theme - query theme of the event
            query.funder-name - query name of the funder
            query.publisher-location - query location of the publisher
            query.publisher-name - query publisher name
            query.standards-body-acronym - query acronym of the standards body
            query.standards-body-name - query standards body name
            query.title - query title
            query.translator - query translator given and family names


        Results can be sorted by applying the sort and order parameters. sort sets the field by which results will be sorted. order sets the result ordering, either asc or desc (default is desc).

        An example that sorts results in order of publication, beginning with the least recent:

            /works?query=josiah+carberry&sort=published&order=asc
        This endpoint supports sorting by the following elements:

            created - sort by created date
            deposited - sort by time of most recent deposit
            indexed - sort by time of most recent index
            is-referenced-by-count - sort by number of times this DOI is referenced by other Crossref DOIs
            issued - sort by issued date (earliest known publication date)
            published - sort by publication date
            published-online - sort by online publication date
            published-print - sort by print publication date
            references-count - sort by number of references included in the references section of the document identified by this DOI
            relevance - sort by relevance score
            score - sort by relevance score
            updated - sort by date of most recent change to metadata, currently the same as deposited

        Facet counts can be retrieved by enabling faceting. Facets are enabled by providing facet field names along with a maximum number of returned term values. The larger the number of returned values, the longer the query will take. Some facet fields can accept a * as their maximum, which indicates that all values should be returned.

        For example, to get facet counts for all work types:

            /works?facet=type-name:*
            This endpoint supports the following facets:

            affiliation - author affiliation
            archive - archive location
            assertion - custom Crossmark assertion name
            assertion-group - custom Crossmark assertion group name
            category-name - category name of work
            container-title - [max value 100], work container title, such as journal title, or book title
            funder-doi - funder DOI
            funder-name - funder literal name as deposited alongside DOI
            issn - [max value 100], journal ISSN (any - print, electronic, link)
            journal-issue - journal issue number
            journal-volume - journal volume
            license - license URI of work
            link-application - intended application of the full text link
            orcid - [max value 100], contributor ORCID
            published - earliest year of publication
            publisher-name - publisher name of work
            relation-type - relation type described by work or described by another work with work as object
            ror-id - institution ROR ID
            source - source of the DOI
            type-name - work type name, such as journal-article or book-chapter
            update-type - significant update type



        Filters allow you to select items based on specific criteria. All filter results are lists.

        For example:

            /works?filter=type:dataset
            Multiple filters
            Multiple filters can be specified in a single query. In such a case, different filters will be applied with AND semantics, while specifying the same filter multiple times will result in OR semantics - that is, specifying the filters:

            is-update:true
            from-pub-date:2014-03-03
            funder:10.13039/100000001
            funder:10.13039/100000050
            would locate documents that are updates, were published on or after 3rd March 2014 and were funded by either the National Science Foundation (10.13039/100000001) or the National Heart, Lung, and Blood Institute (10.13039/100000050). These filters would be specified by joining each filter together with a comma:

                /works?filter=is-update:true,from-pub-date:2014-03-03,funder:10.13039/100000001,funder:10.13039/100000050
            Dot filters
            A filter with a dot in its name is special. The dot signifies that the filter will be applied to some other record type that is related to primary resource record type. For example, with work queries, one can filter on works that have an award, where the same award has a particular award number and award-giving funding agency:

                /works?filter=award.number:CBET-0756451,award.funder:10.13039/100000001
            Here we filter on works that have an award by the National Science Foundation that also has the award number CBET-0756451.

            Note on dates
            The dates in filters should always be of the form YYYY-MM-DD, YYYY-MM or YYYY. The date filters are inclusive. For example:

                from-pub-date:2018-09-18 filters works published on or after 18th September 2018
                from-created-date:2016-02-29,until-created-date:2016-02-29 filters works first deposited on 29th February 2016
                until-created-date:2010-06 filters works first deposited in or before June 2010
                from-update-date:2017,until-update-date:2017 filters works with metadata updated in 2017
            Also note that date information in Crossref metadata can often be incomplete. So, for example, a publisher may only include the year and month of publication for a journal article. For a monograph they might just include the year. In these cases the API selects the earliest possible date given the information provided. So, for instance, if the publisher only provided 2013-02 as the published date, then the date would be treated as 2013-02-01. Similarly, if the publisher only provided the year 2013 as the date, it would be treated at 2013-01-01.

        Note on owner prefixes
            The prefix of a Crossref DOI does NOT indicate who currently owns the DOI. It only reflects who originally registered the DOI. Crossref metadata has an prefix element that records the current owner of the Crossref DOI in question.

            Crossref also has member IDs for depositing organisations. A single member may control multiple owner prefixes, which in turn may control a number of DOIs. When looking at works published by a certain organisaton, member IDs and the member routes should be used.

        Notes on incremental metadata updates
                When using time filters to retrieve periodic, incremental metadata updates, the from-index-date filter should be used over from-update-date, from-deposit-date, from-created-date and from-pub-date. The timestamp that from-index-date filters on is guaranteed to be updated every time there is a change to metadata requiring a reindex.

            This endpoint supports the following filters:

                alternative-id - metadata for records with the given alternative ID, which may be a publisher-specific ID, or any other identifier a publisher may have provided
                archive - metadata where value of archive partner equals given archive name
                article-number - metadata for records with a given article number
                assertion - metadata for records with a given named assertion
                assertion-group - metadata for records with an assertion in a given group
                award
                award.funder - metadata for records with award funder equal to given funder, optionally combine with award.number
                award.number - metadata for records with award number equal to given number, optionally combine with award.funder
                category-name - metadata for records with category label equal to given name, category labels come from the list published by Scopus
                citation-id
                clinical-trial-number - metadata for records with given clinical trial number
                container-title - metadata with a publication title that exactly equals given title
                content-domain - metadata where the publisher records a given domain name as the location Crossmark content will appear
                doi - metadata describing given DOI
                from-accepted-date - [date], metadata where accepted date is since given date (inclusive)
                from-approved-date - [date], metadata where approved date is since given date (inclusive)
                from-awarded-date - [date], metadata where award date is since given date (inclusive)
                from-created-date - [date], metadata first deposited since given date (inclusive)
                from-deposit-date - [date], metadata last (re)deposited since given date (inclusive)
                from-event-end-date - [date], metadata where event end date is since given date (inclusive)
                from-event-start-date - [date], metadata where event start date is since given date (inclusive)
                from-index-date - [date], metadata indexed since given date (inclusive)
                from-issued-date - [date], metadata where issued date is since given date (inclusive)
                from-online-pub-date - [date], metadata where online published date is since given date (inclusive)
                from-posted-date - [date], metadata where posted date is since given date (inclusive)
                from-print-pub-date - [date], metadata where print published date is since given date (inclusive)
                from-pub-date - [date], metadata where published date is since given date (inclusive)
                from-update-date - [date], metadata updated since given date (inclusive), currently the same as from-deposit-date
                full-text
                full-text.type - metadata where resource element's content_type attribute equals given version mime type (e.g. application/pdf)
                full-text.application - [text-mining, similarity-checking or unspecified], metadata where resource link has given application
                full-text.version - metadata where resource element's content_version attribute equals given version
                funder - metadata which include given funder id in FundRef data
                funder-doi-asserted-by - metadata where funder DOI was asserted by given body
                group-title - metadata with given group title
                gte-award-amount - metadata where award is greater than or equals given number
                has-abstract - [0 or 1], metadata for records with/without an abstract
                has-affiliation - [0 or 1], metadata for records with/without affiliation information
                has-archive - [0 or 1], metadata which includes/does not include name of archive partner
                has-assertion - [0 or 1], metadata for records with/without assertions
                has-authenticated-orcid - [0 or 1], metadata which includes/does not include one or more ORCIDs where the depositing publisher claims to have witness the ORCID owner authenticate with ORCID
                has-award - [0 or 1], metadata for records with/without award
                has-clinical-trial-number - [0 or 1], metadata for records with/without a clinical trial number
                has-content-domain - [0 or 1], metadata where the publisher records/does not record a domain name location for Crossmark content
                has-description
                has-domain-restriction - [0 or 1], metadata where the publisher restricts/does not restrict Crossmark usage to content domains
                has-event - [0 or 1], metadata for records with/without event
                has-full-text - [0 or 1], metadata that includes/does not include any full text resource elements
                has-funder - [0 or 1], metadata which includes/does not include one or more funder entry
                has-funder-doi - [0 or 1], metadata for records with/without funder DOI
                has-license - [0 or 1], metadata that includes/does not include any license_ref elements
                has-orcid - [0 or 1], metadata which includes/does not include one or more ORCIDs
                has-references - [0 or 1], metadata for works that have/don't have a list of references
                has-relation - [0 or 1], metadata for records that either assert/do not assert or are/are not the object of a relation
                has-ror-id - [0 or 1], metadata for records with/without ROR ID
                has-update - [0 or 1], metadata for records with/without update information
                has-update-policy - [0 or 1], metadata for records that include/do not include a link to an editorial update policy
                is-update - [0 or 1], metadata for records that represent/do not represent editorial updates
                isbn - metadata with given ISBN
                issn - metadata with given ISSN, format is xxxx-xxxx
                license
                license.url - metadata where license_ref value equals given url
                license.version - metadata where the license_ref's applies_to attribute equals given version
                license.delay - metadata where difference between publication date and the license_ref's start_date attribute is <= than given delay (in days)
                lte-award-amount - metadata where award is less than or equals given number
                member - metadata belonging to a given Crossref member
                orcid - metadata where there is a contributor with given ORCID
                prefix - metadata belonging to a given DOI owner prefix (e.g. 10.1016)
                relation
                relation.type - metadata for records with a relation with the given type from the Crossref relations schema (e.g. is-referenced-by, is-parent-of, is-preprint-of)
                relation.object-type - metadata for records with a relation, where the object type matches given type from the Crossref relations schema (e.g. doi, issn)
                relation.object - metadata for records with a relation, where the object identifier matches given identifier
                ror-id - metadata with given ROR ID
                type - metadata records whose type equals given type, type must be an ID value from the list of types returned by the /types resource
                type-name - metadata for records with type name equal to given name
                until-accepted-date - [date], metadata where accepted date is before given date (inclusive)
                until-approved-date - [date], metadata where approved date is before given date (inclusive)
                until-awarded-date - [date], metadata where award date is before given date (inclusive)
                until-created-date - [date], metadata first deposited before given date (inclusive)
                until-deposit-date - [date], metadata last (re)deposited before given date (inclusive)
                until-event-end-date - [date], metadata where event end date is before given date (inclusive)
                until-event-start-date - [date], metadata where event start date is before given date (inclusive)
                until-index-date - [date], metadata indexed before given date (inclusive)
                until-issued-date - [date], metadata where issued date is before given date (inclusive)
                until-online-pub-date - [date], metadata where online published date is before given date (inclusive)
                until-posted-date - [date], metadata where posted date is before given date (inclusive)
                until-print-pub-date - [date], metadata where print published date is before given date (inclusive)
                until-pub-date - [date], metadata where published date is before given date (inclusive)
                until-update-date - [date], metadata updated before given date (inclusive), currently the same as until-deposit-date
                update-type - metadata with given update type
                updates - metadata for records that represent editorial updates to given DOI


        Crossref metadata records can be quite large. Sometimes you just want a few elements from the schema. You can "select" a subset of elements to return using the select parameter. This can make your API calls much more efficient. For example:

            /works?select=DOI,prefix,title
        This endpoint supports selecting the following elements.

            DOI
            ISBN
            ISSN
            URL
            abstract
            accepted
            alternative-id
            approved
            archive
            article-number
            assertion
            author
            chair
            clinical-trial-number
            container-title
            content-created
            content-domain
            created
            degree
            deposited
            editor
            event
            funder
            group-title
            indexed
            is-referenced-by-count
            issn-type
            issue
            issued
            license
            link
            member
            original-title
            page
            posted
            prefix
            published
            published-online
            published-print
            publisher
            publisher-location
            reference
            references-count
            relation
            score
            short-container-title
            short-title
            standards-body
            subject
            subtitle
            title
            translator
            type
            update-policy
            update-to
            updated-by
            volume


            Offsets are an easy way to iterate over results sets up to 10,000 items. This limit applies to the sum of values of parameters offset + rows.

            The number of items returned in a single response is controlled by rows parameter (default is 20, and maximum is 1,000). To limit results to 5, for example, you could do the following:

            /works?query=allen+renear&rows=5
        offset parameter can be used to retrieve items starting from a specific index of the result list. For example, to select the second set of 5 results (i.e. results 6 through 10), you would do the following:

            /works?query=allen+renear&rows=5&offset=5


            Deep paging using cursors can be used to iterate over large result sets, without any limits on their size.

            To use deep paging make a query as normal, but include the cursor parameter with a value of *, for example:

            /members/311/works?filter=type:journal-article&cursor=*
            A next-cursor field will be provided in the JSON response. To get the next page of results, pass the value of next-cursor as the cursor parameter (remember to URL-encode). For example:

                /members/311/works?filter=type:journal-article&cursor=<value of next-cursor parameter>
            Clients should check the number of returned items. If the number of returned items is equal to the number of expected rows then the end of the result set has been reached. Using next-cursor beyond this point will result in responses with an empty items list.


            Being able to select random results is useful for both testing and sampling. You can use the sample parameter to retrieve random results. So, for example, the following selects 10 random works:

            /works?sample=10
            Note that when you use the sample parameter, the rows and offset parameters are ignored.

        Parameter combinations:
            Any combination of query, query.*, filter, facet, select and sort can be used with offsets. Sampling cannot be combined with offsets.

            Any combination of query, query.*, filter, facet, select and sort may also be used with deep paging cursors. rows may also be specified.

