---
layout: flat
title: Possible TAXII 2.0 REST-based Query API
---

Tactical goal
=============
* Create a TAXII API that allows easy querying of data stored in CTI
  repositories so that building integrations with external systems
  (ie, dynamically populating an edge router blacklist of known C2 IP
  addresses) becomes dead simple.

General principles
==================
* CybOX is huge. For the initial pass, we'll constrain the effort to
  supporting IP addresses, email addresses, file hashes, URLs, FQDNs,
  and Windows registry key observable types.
* Minimize the burden on the consumer, don't make parsing a STIX
  package their default option!
  * Allow them to retrieve raw STIX or CybOX but give them a
    simplified JSON representation by default.
* Use global query parameters to allow more granular filtering on a
  query:
  * confidence_min, confidence_max => high, medium, low, none, unknown
  * tlp_min, tlp_max => white, green, amber, red
  * earliest, latest => timestamp
  * feed_producers => list of feed producers
  * output_format => json, oasis (raw STIX/CybOX)

Query scoping
=============
* Use the optional broadcast query parameter to allow targeting a
  query *either* at a single TAXII endpoint *or* as a broadcast query
  against selected trustgroup(s), in which case the TAXII endpoint
  receiving the broadcast query request will act as a proxy,
  forwarding the query to all the hosts implied by the specified
  trustgroup parameter, accumulating the result set, and passing it
  back to the query client.
  * broadcast => local, single trustgroup, list of trustgroups, or 'all'
  * if broadcast flag is omitted, assume it's a local query

Immutability of objects under a URL-based object id scheme
==========================================================
* If we move to using URLs as object ids, the underlying *data* a
  URL-based object id refers to *MUST* be treated as immutable. Here's
  why:
* Let's take a strawman Indicator. Currently, the object id would be
  something like: `example.org:indicator-14adf303-bd57-4dad-bf84-4ba8e8ef175c`
* If we move to URLs, the object id would be something like: `taxii.example.org/api/query/indicators/14adf303-bd57-4dad-bf84-4ba8e8ef175c`
* Now, why should the object behind the URL be immutable? Let's say
  I'm at Org A and I generate a Report object that links to the Org B
  Indicator (above). I'm making an direct assertion regarding that
  *particular* Indicator version. Now, if Org B goes and publishes a
  revision of the original Indicator *under the same URL*, it creates
  a problem for Org A. Do we still support our original assertion from
  our Report, given that Org B are effectively shifting the ground
  under our feet? Maybe, who knows? Definitely problematic, QED these
  things should be immutable.

Implications for object versioning
==================================
* Object versioning has long been a painful subject. Mark and I came
  up with an interesting approach. (Again, assuming a REST-based TAXII
  Query API.)
* One can envisage a REST-based approach where I can refer to an
  object like this: `taxii.example.org/api/query/indicators/14adf303-bd57-4dad-bf84-4ba8e8ef175c/latest/`
* ...and get the latest revision of the object.
* Additionally, one can envisage a REST-based approach where I can
  refer to an object like this: `taxii.example.org/api/query/indicators/14adf303-bd57-4dad-bf84-4ba8e8ef175c/history/`
* ...and get back a JSON blob something like this:
`[{'version': 0, 'object_id':
'taxii.example.org/api/query/indicators/14adf303-bd57-4dad-bf84-4ba8e8ef175c',
'changelog': 'initial publication of indicator'},
{'version': 1, 'object_id':
'taxii.example.org/api/query/indicators/14adf303-bd57-4dad-bf84-4ba8e8ef175d',
'changelog': 'typo fix'},
{'version': 2, 'object_id':
'taxii.example.org/api/query/indicators/14adf303-bd57-4dad-bf84-4ba8e8ef175e',
'changelog': 'revoking indicator, this was actually innocuous'}]`
* This is an intriguing approach to the age-old versioning problem.


CybOX-specific queries
======================
AddressObj (just the IP networking bits)
----------------------------------------
* **use cases**
  * **Have you seen this thing?**
      * **query:** `/api/v0.1/observable/address/ip/<value>/` (where
        value can be a single IP, an IP range, or a CIDR block)
      * **result:** json blob containing a boolean and a list of matching
        uuids
  * **Give me everything related to this thing.**
      * **query:** `/api/v0.1/observable/related/<value>/` (where
        value is a valid uuid)
      * **result:** json blob containing a simplified (value-oriented
        json representation) of datatypes supported by TAXII 2.0 Query
        API (currently AddressObj, FileObj, EmailMessageObj, URIObj,
        WinRegistryKeyObj) as well as a list of uuids for optional
        retrieval of raw CybOX
  * **Give me all the things you've got.**
      * **query:** `/api/v0.1/observable/address/ips/`
      * **result:** json blob containing a list of dicts like:
        `[{'value': '192.168.0.1', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
* **additional query params**
  * type => list of IPv4, IPv6 addresses

FileObj (initially, just hashes)
--------------------------------
* **use cases**:
  * **Have you seen this thing?**
      * **query:** `/api/v0.1/observable/file/hash/<value>/` (where
        value is a file hash)
      * **result:** json blob containing a boolean and a list of
        matching uuids
  * **Give me everything related to this thing.**
      * **query:** `/api/v0.1/observable/related/<value>/` (where
        value is a valid uuid)
      * **result:** json blob containing a simplified (value-oriented
        json representation) of datatypes supported by TAXII 2.0 Query
        API (currently AddressObj, FileObj, EmailMessageObj, URIObj,
        WinRegistryKeyObj) as well as a list of uuids for optional
        retrieval of raw CybOX
  * **Give me all the things you've got.**
      * **query:** `/api/v0.1/observable/file/hashes/`
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'md5', 'value': 'ea5e11d4c71cd0311a27875c53789624', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
* **additional query params**
  * type => list of hash types (cf. CybOXVocabs:HashNameEnum-1.0)

EmailMessageObj (initially, just email addresses)
-------------------------------------------------
* **use cases**:
  * **Have you seen this thing?**
      * **query:** `/api/v0.1/observable/email/address/<value>/`
        (where value is a valid email address; by default searches
        _all_ address_types described below, unless the optional
        address_type parameter is passed)
      * **result:** json blob containing a boolean and a list of
        matching uuids
  * **Give me everything related to this thing.**
      * **query:** `/api/v0.1/observable/related/<value>/` (where
        value is a valid uuid)
      * **result:** json blob containing a simplified (value-oriented
        json representation) of datatypes supported by TAXII 2.0 Query
        API (currently AddressObj, FileObj, EmailMessageObj, URIObj,
        WinRegistryKeyObj) as well as a list of uuids for optional
        retrieval of raw CybOX
  * **Give me all the things you've got.**
      * **query:** `/api/v0.1/observable/email/addresses/`
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'sender', 'value': 'badguy@foobar.com', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
* **additional query params**
  * type => list of headers to search (to, from, cc, bcc, sender,
    reply_to, recipient)

URIObj (initially, just URLs)
-----------------------------
* **use cases**:
  * **Have you seen this thing?**
      * **query:** `/api/v0.1/observable/uri/url/<value>/` (where value is a
        valid url)
      * **result:** json blob containing a boolean and a list of
        matching uuids
  * **Give me everything related to this thing.**
      * **query:** `/api/v0.1/observable/related/<value>/` (where value
        is a valid uuid)
      * **result:** json blob containing a simplified (value-oriented
        json representation) of datatypes supported by TAXII 2.0 Query
        API (currently AddressObj, FileObj, EmailMessageObj, URIObj,
        WinRegistryKeyObj) as well as a list of uuids for optional
        retrieval of raw CybOX
  * **Give me all the things you've got.**
      * **query:** `/api/v0.1/observable/uri/urls/`
      * **result:** json blob containing a list of dicts like
        `[{'value': 'http://www.foobar.com', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
* **additional query params**
  * none at this time

DomainNameObj
-------------
* **use cases**:
  * **Have you seen this thing?**
      * **query:** `/api/v0.1/observable/domain_name/<value>/` (where
        value is a valid FQDN or TLD)
      * **result:** json blob containing a boolean and a list of
        matching uuids
  * **Give me everything related to this thing.**
      * **query:** `/api/v0.1/observable/related/<value>/` (where value is a
        valid uuid)
      * **result:** json blob containing a simplified (value-oriented
        json representation) of datatypes supported by TAXII 2.0 Query
        API (currently AddressObj, FileObj, EmailMessageObj, URIObj,
        WinRegistryKeyObj) as well as a list of uuids for optional
        retrieval of raw CybOX
  * **Give me all the things you've got.**
      * **query:** `/api/v0.1/observable/domain_names/`
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'fqdn', 'value': foobar.com', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
* **additional query params**
  * type => list of fqdn, tld

WinRegistryKeyObj
-----------------
* **use cases**:
  * **Have you seen this thing?**
      * **query:** `/api/v0.1/observable/win_registry/value/<value>/`
        (where value is a valid windows registry value)
      * **query:** `/api/v0.1/observable/win_registry/key/<value>/`
        (where value is a valid windows registry key)
      * **result:** json blob containing a boolean and a list of
        matching uuids
  * **Give me everything related to this thing.**
      * **query:** `/api/v0.1/observable/related/<value>/` (where
        value is a valid uuid)
      * **result:** json blob containing a simplified (value-oriented
        json representation) of datatypes supported by TAXII 2.0 Query
        API (currently AddressObj, FileObj, EmailMessageObj, URIObj,
        WinRegistryKeyObj) as well as a list of uuids for optional
        retrieval of raw CybOX
  * **Give me all the things you've got.** (Not sure how valuable this
    is for windows registry data but including for completeness)
      * **query:** `/api/v0.1/observable/win_registry/values/`
      * **query:** `/api/v0.1/observable/win_registry/keys/`
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'REG_DWORD', 'value': 'blahblah', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
* **additional query params**
  * hive => valid windows registry hive
  * key => valid windows registry key (path, excluding hive)


STIX-specific queries
=====================
Campaign
--------
* **use cases**:
  * **Have you seen this thing?**
      * **query:** `/api/v0.1/campaign/<value>/` (where value is a
        valid uuid)
      * **result:** json blob containing a boolean and (if true) a
        blob of STIX
  * **Give me everything related to this thing.**
      * **query:** `/api/v0.1/campaign/<value>/related/` (where value
        is a valid uuid)
      * **result:** json blob of stix representing a stix package
        containing all top-level stix objects matching the query
      * **query:** `/api/v0.1/campaign/<value>/related/ttps/` (where
        value is a valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'ttp', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * **query:** `/api/v0.1/campaign/<value>/related/incidents/` (where
        value is a valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'incident', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * **query:** `/api/v0.1/campaign/<value>/related/indicators/` (where
        value is a valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'indicator', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * **query:** `/api/v0.1/campaign/<value>/related/campaigns/` (where
        value is a valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'campaign', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * NOTE: ignoring related packages, as this is deprecated
  * **Give me all the things you've got.**
      * **query:** `/api/v0.1/campaigns/`
      * **result:** json blob of stix representing a stix package
        containing all campaign objects matching the query
* **additional query params**
    * status => cf. CampaignStatusType controlled vocabulary
    * attribution => filter on related threat actor uuid

COA
---
* **use cases**:
  * **Have you seen this thing?**
      * **query:** `/api/v0.1/coa/<value>/` (where value is a valid uuid)
      * **result:** json blob containing a boolean and (if true) a blob
        of STIX
  * **Give me everything related to this thing.**
      * **query:** `/api/v0.1/coa/<value>/related/` (where value is a valid
        uuid)
      * **query:** `/api/v0.1/coa/<value>/related/coas/` (where value is a
        valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'coa', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * NOTE: since COAs can only be related to COAs, the previous two
        queries are functionally equivalent but listed separately for
        consistency's sake
      * NOTE: ignoring related packages, as this is deprecated
  * **Give me all the things you've got.**
      * **query:** `/api/v0.1/coas/`
      * **result:** json blob of stix representing a stix package
        containing all coa objects matching the query
  * **additional query params**
    * none at this time

Threat Actor
------------
* **use cases**:
  * **Have you seen this thing?**
      * **query:** `/api/v0.1/threat_actor/<value>/` (where value is a valid
        uuid)
      * **result:** json blob containing a boolean and (if true) a blob
        of STIX
  * **Give me everything related to this thing.**
      * **query:** `/api/v0.1/threat_actor/<value>/related/`
      * **result:** json blob of stix representing a stix package
        containing all top-level stix objects matching the query
      * **query:** `/api/v0.1/threat_actor/<value>/related/ttps/` (where
        value is a valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'ttp', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * **query:** `/api/v0.1/threat_actor/<value>/related/campaigns/`
        (where value is a valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'campaign', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * **query:** `/api/v0.1/threat_actor/<value>/related/threat_actors/`
        (where value is a valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'threat_actor', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * NOTE: ignoring related packages, as this is deprecated
  * **Give me all the things you've got.**
      * **query:** `/api/v0.1/threat_actors/`
      * **result:** json blob of stix representing a stix package
        containing all threat actor objects matching the query
* **additional query params**
  * none at this time

Indicator
---------
* **use cases**:
  * **Have you seen this thing?**
      * **query:** `/api/v0.1/indicator/<value>/` (where value is a valid
        uuid)
      * **result:** json blob containing a boolean and (if true) a blob
        of STIX
  * **Give me everything related to this thing.**
      * **query:** `/api/v0.1/indicator/<value>/related/`
      * **result:** json blob of stix representing a stix package
        containing all top-level stix objects matching the query
      * **query:** `/api/v0.1/indicator/<value>/related/observable/` (where
        value is a valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'observable', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * **query:** `/api/v0.1/indicator/<value>/related/indicators/` (where
        value is a valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'indicator', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * **query:** `/api/v0.1/indicator/<value>/related/ttps/` (where value
        is a valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'ttp', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * **query:** `/api/v0.1/indicator/<value>/related/coas/` (where value
        is a valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'coa', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * **query:** `/api/v0.1/indicator/<value>/related/campaigns/` (where
        value is a valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'campaigns', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * NOTE: ignoring related packages, as this is deprecated
  * **Give me all the things you've got.**
      * **query:** `/api/v0.1/indicators/`
      * **result:** json blob of stix representing a stix package
        containing all indicator objects matching the query
* **additional query params**
  * type => cf. IndicatorTypeVocab

Exploit Target
--------------
* **use cases**:
  * **Have you seen this thing?**
      * **query:** `/api/v0.1/exploit_target/<value>/` (where value is a
        valid uuid)
      * **result:** json blob containing a boolean and (if true) a blob
        of STIX
  * **Give me everything related to this thing.**
      * **query:** `/api/v0.1/exploit_target/<value>/related/`
      * **result:** json blob of stix representing a stix package
        containing all top-level stix objects matching the query
      * **query:** `/api/v0.1/exploit_target/<value>/related/coas/` (where
        value is a valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'coa', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * **query:**
        `/api/v0.1/exploit_target/<value>/related/exploit_targets/`
        (where value is a valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'campaigns', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * NOTE: ignoring related packages, as this is deprecated
  * **Give me all the things you've got.**
      * **query:** `/api/v0.1/exploit_targets/`
      * **result:** json blob of stix representing a stix package
        containing all exploit_target objects matching the query
* **additional query params**
  * none at this time

Incident
--------
* **use cases**:
  * **Have you seen this thing?**
      * **query:** `/api/v0.1/incident/<value>/` (where value is a valid
        uuid)
      * **result:** json blob containing a boolean and (if true) a blob
        of STIX
  * **Give me everything related to this thing.**
      * **query:** `/api/v0.1/incident/<value>/related/`
      * **result:** json blob of stix representing a stix package
        containing all top-level stix objects matching the query
      * **query:** `/api/v0.1/incident/<value>/related/indicators/` (where
        value is a valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'indicator', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * **query:** `/api/v0.1/incident/<value>/related/observables/` (where
        value is a valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'observable', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * **query:** `/api/v0.1/incident/<value>/related/ttps/` (where value
        is a valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'ttp', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * **query:** `/api/v0.1/incident/<value>/related/threat_actors/`
        (where value is a valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'threat_actor', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * **query:** `/api/v0.1/incident/<value>/related/incidents/` (where
        value is a valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'incident', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * **query:** `/api/v0.1/incident/<value>/related/coas/` (where value
        is a valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'coa', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * **query:** `/api/v0.1/incident/<value>/related/exploit_targets/`
        (where value is a valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'campaigns', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * NOTE: ignoring related packages, as this is deprecated
  * **Give me all the things you've got.**
      * **query:** `/api/v0.1/incidents/`
      * **result:** json blob of stix representing a stix package
        containing all incident objects matching the query
* **additional query params**
  * none at this time

TTP
---
* **use cases**:
  * **Have you seen this thing?**
      * **query:** `/api/v0.1/ttp/<value>/` (where value is a valid uuid)
      * **result:** json blob containing a boolean and (if true) a blob
        of STIX
  * **Give me everything related to this thing.**
      * **query:** `/api/v0.1/ttp/<value>/related/` (where value is a valid
        uuid)
      * **query:** `/api/v0.1/ttp/<value>/related/ttps/` (where value is a
        valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'ttp', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * NOTE: since TTPs can only be related to TTPs, the previous two
        queries are functionally equivalent but listed separately for
        consistency's sake
      * NOTE: ignoring related packages, as this is deprecated
  * **Give me all the things you've got.**
      * **query:** `/api/v0.1/ttps/`
      * **result:** json blob of stix representing a stix package
        containing all ttp objects matching the query
* **additional query params**
  * none at this time

Report
------
* **use cases**:
  * **Have you seen this thing?**
      * **query:** `/api/v0.1/report/<value>/` (where value is a valid uuid)
      * **result:** json blob containing a boolean and (if true) a blob
        of STIX
  * **Give me everything related to this thing.**
      * **query:** `/api/v0.1/report/<value>/related/`
      * **result:** json blob of stix representing a stix package
        containing all top-level stix objects matching the query
      * **query:** `/api/v0.1/report/<value>/related/observable/` (where
        value is a valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'observable', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * **query:** `/api/v0.1/report/<value>/related/indicators/` (where
        value is a valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'indicator', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * **query:** `/api/v0.1/report/<value>/related/ttps/` (where value is
        a valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'ttp', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * **query:** `/api/v0.1/report/<value>/related/coas/` (where value is
        a valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'coa', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * **query:** `/api/v0.1/report/<value>/related/campaigns/` (where
        value is a valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'campaigns', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * **query:** `/api/v0.1/report/<value>/related/exploit_targets/`
        (where value is a valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'exploit_target', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * **query:** `/api/v0.1/report/<value>/related/incidents/` (where
        value is a valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'incident', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * **query:** `/api/v0.1/report/<value>/related/threat_actors/` (where
        value is a valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'threat_actor', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * **query:** `/api/v0.1/report/<value>/related/reports/` (where value
        is a valid uuid)
      * **result:** json blob containing a list of dicts like:
        `[{'type': 'report', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`
      * NOTE: ignoring related packages, as this is deprecated
  * **Give me all the things you've got.**
      * **query:** `/api/v0.1/reports/`
      * **result:** json blob of stix representing a stix package
        containing all report objects matching the query
* **additional query params**
  * none at this time
