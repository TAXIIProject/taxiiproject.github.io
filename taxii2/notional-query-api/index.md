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


CybOX-specific queries
======================
AddressObj
----------
* (just the IP networking bits)
* use cases:

  0) Have you seen this thing?
    * query: `/api/v0.1/observable/address/ip/<value>/` (where value
      can be a single IP, an IP range, or a CIDR block)
      * result: json blob containing a boolean and a list of matching
        uuids
        
  1) Give me everything related to this thing.
    * query: `/api/v0.1/observable/related/<value>/` (where value is a
      valid uuid)
      * result: json blob containing a simplified (value-oriented json
        representation) of datatypes supported by TAXII 2.0 Query API
        (currently AddressObj, FileObj, EmailMessageObj, URIObj,
        WinRegistryKeyObj) as well as a list of uuids for optional
        retrieval of raw CybOX

  2) Give me all the things you've got.
    * query: `/api/v0.1/observable/address/ips/`
      * result: json blob containing a list of dicts like
        `[{'value': '192.168.0.1', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]`

* additional query params
  * type => list of IPv4, IPv6 addresses

* CybOX observable type: FileObj (initially, just hashes)
  * use cases:
    0) Have you seen this thing?
      * query: /api/v0.1/observable/file/hash/<value>/ (where value is
        a file hash)
        * result: json blob containing a boolean and a list of
          matching uuids
    1) Give me everything related to this thing.
      * query: /api/v0.1/observable/related/<value>/ (where value is a
        valid uuid)
        * result: json blob containing a simplified (value-oriented
          json representation) of datatypes supported by TAXII 2.0
          Query API (currently AddressObj, FileObj, EmailMessageObj,
          URIObj, WinRegistryKeyObj) as well as a list of uuids for
          optional retrieval of raw CybOX
    2) Give me all the things you've got.
      * query: /api/v0.1/observable/file/hashes/
        * result: json blob containing a list of dicts like
          [{'type': 'md5', 'value': 'ea5e11d4c71cd0311a27875c53789624', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
  * additional query params
    * type => list of hash types (cf. CybOXVocabs:HashNameEnum-1.0)

* CybOX observable type: EmailMessageObj (initially, just email addresses)
  * use cases:
    0) Have you seen this thing?
      * query: /api/v0.1/observable/email/address/<value>/ (where
        value is a valid email address; by default searches _all_
        address_types described below, unless the optional
        address_type parameter is passed)
        * result: json blob containing a boolean and a list of
          matching uuids
    1) Give me everything related to this thing.
      * query: /api/v0.1/observable/related/<value>/ (where value is a
        valid uuid)
        * result: json blob containing a simplified (value-oriented
          json representation) of datatypes supported by TAXII 2.0
          Query API (currently AddressObj, FileObj, EmailMessageObj,
          URIObj, WinRegistryKeyObj) as well as a list of uuids for
          optional retrieval of raw CybOX
    2) Give me all the things you've got.
      * query: /api/v0.1/observable/email/addresses/
        * result: json blob containing a list of dicts like
          [{'type': 'sender', 'value': 'engineering@soltra.com', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
  * additional query params
    * type => list of headers to search (to, from, cc, bcc, sender,
      reply_to, recipient)

* CybOX observable type: URIObj (initially, just URLs)
  * use cases:
    0) Have you seen this thing?
      * query: /api/v0.1/observable/uri/url/<value>/ (where value is a
        valid url)
        * result: json blob containing a boolean and a list of
          matching uuids
    1) Give me everything related to this thing.
      * query: /api/v0.1/observable/related/<value>/ (where value is a
        valid uuid)
        * result: json blob containing a simplified (value-oriented
          json representation) of datatypes supported by TAXII 2.0
          Query API (currently AddressObj, FileObj, EmailMessageObj,
          URIObj, WinRegistryKeyObj) as well as a list of uuids for
          optional retrieval of raw CybOX
    2) Give me all the things you've got.
      * query: /api/v0.1/observable/uri/urls/
        * result: json blob containing a list of dicts like
          [{'value': 'http://www.soltra.com', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
  * additional query params
    * none

* CybOX observable type: DomainNameObj
  * use cases:
    0) Have you seen this thing?
      * query: /api/v0.1/observable/domain_name/<value>/ (where value
        is a valid FQDN or TLD)
        * result: json blob containing a boolean and a list of
          matching uuids
    1) Give me everything related to this thing.
      * query: /api/v0.1/observable/related/<value>/ (where value is a
        valid uuid)
        * result: json blob containing a simplified (value-oriented
          json representation) of datatypes supported by TAXII 2.0
          Query API (currently AddressObj, FileObj, EmailMessageObj,
          URIObj, WinRegistryKeyObj) as well as a list of uuids for
          optional retrieval of raw CybOX
    2) Give me all the things you've got.
      * query: /api/v0.1/observable/domain_names/
        * result: json blob containing a list of dicts like
          [{'type': 'fqdn', 'value': 'wiki.corp.soltra.com', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
  * additional query params
    * type => list of fqdn, tld

* CybOX observable type: WinRegistryKeyObj
    0) Have you seen this thing?
      * query: /api/v0.1/observable/win_registry/value/<value>/ (where
        value is a valid windows registry value)
      * query: /api/v0.1/observable/win_registry/key/<value>/ (where
        value is a valid windows registry key)
        * result: json blob containing a boolean and a list of matching uuids
    1) Give me everything related to this thing.
      * query: /api/v0.1/observable/related/<value>/ (where value is a
        valid uuid)
        * result: json blob containing a simplified (value-oriented
          json representation) of datatypes supported by TAXII 2.0
          Query API (currently AddressObj, FileObj, EmailMessageObj,
          URIObj, WinRegistryKeyObj) as well as a list of uuids for
          optional retrieval of raw CybOX
    2) Give me all the things you've got. (Not sure how valuable this
    is for windows registry data but including for completeness)
      * query: /api/v0.1/observable/win_registry/values/
      * query: /api/v0.1/observable/win_registry/keys/
        * result: json blob containing a list of dicts like
          [{'type': 'REG_DWORD', 'value': 'blahblah', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
  * additional query params
    * hive => valid windows registry hive
    * key => valid windows registry key (path, excluding hive)


STIX-specific queries
=====================
* STIX type: Campaign
    0) Have you seen this thing?
      * query: /api/v0.1/campaign/<value>/ (where value is a valid
        uuid)
        * result: json blob containing a boolean and (if true) a blob
          of STIX
    1) Give me everything related to this thing.
      * query: /api/v0.1/campaign/<value>/related/ (where value is a
        valid uuid)
        * result: json blob of stix representing a stix package
          containing all top-level stix objects matching the query
      * query: /api/v0.1/campaign/<value>/related/ttps/ (where value
        is a valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'ttp', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * query: /api/v0.1/campaign/<value>/related/incidents/ (where
        value is a valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'incident', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * query: /api/v0.1/campaign/<value>/related/indicators/ (where
        value is a valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'indicator', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * query: /api/v0.1/campaign/<value>/related/campaigns/ (where
        value is a valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'campaign', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * NOTE: ignoring related packages, as this is deprecated
    2) Give me all the things you've got.
      * query: /api/v0.1/campaigns/
        * result: json blob of stix representing a stix package
          containing all campaign objects matching the query
  * additional query params
    * status => cf. CampaignStatusType controlled vocabulary
    * attribution => filter on related threat actor uuid

* STIX type: COA
    0) Have you seen this thing?
      * query: /api/v0.1/coa/<value>/ (where value is a valid uuid)
        * result: json blob containing a boolean and (if true) a blob
          of STIX
    1) Give me everything related to this thing.
      * query: /api/v0.1/coa/<value>/related/ (where value is a valid
        uuid)
      * query: /api/v0.1/coa/<value>/related/coas/ (where value is a
        valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'coa', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * NOTE: since COAs can only be related to COAs, the previous two
        queries are functionally equivalent but listed separately for
        consistency's sake
      * NOTE: ignoring related packages, as this is deprecated
    2) Give me all the things you've got.
      * query: /api/v0.1/coas/
        * result: json blob of stix representing a stix package
          containing all coa objects matching the query
  * additional query params
    * none at this time

* STIX type: Threat Actor
    0) Have you seen this thing?
      * query: /api/v0.1/threat_actor/<value>/ (where value is a valid
        uuid)
        * result: json blob containing a boolean and (if true) a blob
          of STIX
    1) Give me everything related to this thing.
      * query: /api/v0.1/threat_actor/<value>/related/
        * result: json blob of stix representing a stix package
          containing all top-level stix objects matching the query
      * query: /api/v0.1/threat_actor/<value>/related/ttps/ (where
        value is a valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'ttp', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * query: /api/v0.1/threat_actor/<value>/related/campaigns/
        (where value is a valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'campaign', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * query: /api/v0.1/threat_actor/<value>/related/threat_actors/
        (where value is a valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'threat_actor', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * NOTE: ignoring related packages, as this is deprecated
    2) Give me all the things you've got.
      * query: /api/v0.1/threat_actors/
        * result: json blob of stix representing a stix package
          containing all threat actor objects matching the query
  * additional query params
    * none at this time

* STIX type: Indicator
    0) Have you seen this thing?
      * query: /api/v0.1/indicator/<value>/ (where value is a valid
        uuid)
        * result: json blob containing a boolean and (if true) a blob
          of STIX
    1) Give me everything related to this thing.
      * query: /api/v0.1/indicator/<value>/related/
        * result: json blob of stix representing a stix package
          containing all top-level stix objects matching the query
      * query: /api/v0.1/indicator/<value>/related/observable/ (where
        value is a valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'observable', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * query: /api/v0.1/indicator/<value>/related/indicators/ (where
        value is a valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'indicator', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * query: /api/v0.1/indicator/<value>/related/ttps/ (where value
        is a valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'ttp', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * query: /api/v0.1/indicator/<value>/related/coas/ (where value
        is a valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'coa', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * query: /api/v0.1/indicator/<value>/related/campaigns/ (where
        value is a valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'campaigns', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * NOTE: ignoring related packages, as this is deprecated
    2) Give me all the things you've got.
      * query: /api/v0.1/indicators/
        * result: json blob of stix representing a stix package
          containing all indicator objects matching the query
  * additional query params
    * type => cf. IndicatorTypeVocab

* STIX type: Exploit Target
    0) Have you seen this thing?
      * query: /api/v0.1/exploit_target/<value>/ (where value is a
        valid uuid)
        * result: json blob containing a boolean and (if true) a blob
          of STIX
    1) Give me everything related to this thing.
      * query: /api/v0.1/exploit_target/<value>/related/
        * result: json blob of stix representing a stix package
          containing all top-level stix objects matching the query
      * query: /api/v0.1/exploit_target/<value>/related/coas/ (where
        value is a valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'coa', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * query:
        /api/v0.1/exploit_target/<value>/related/exploit_targets/
        (where value is a valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'campaigns', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * NOTE: ignoring related packages, as this is deprecated
    2) Give me all the things you've got.
      * query: /api/v0.1/exploit_targets/
        * result: json blob of stix representing a stix package
          containing all exploit_target objects matching the query
  * additional query params
    * none at this time

* STIX type: Incident
    0) Have you seen this thing?
      * query: /api/v0.1/incident/<value>/ (where value is a valid
        uuid)
        * result: json blob containing a boolean and (if true) a blob
          of STIX
    1) Give me everything related to this thing.
      * query: /api/v0.1/incident/<value>/related/
        * result: json blob of stix representing a stix package
          containing all top-level stix objects matching the query
      * query: /api/v0.1/incident/<value>/related/indicators/ (where
        value is a valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'indicator', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * query: /api/v0.1/incident/<value>/related/observables/ (where
        value is a valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'observable', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * query: /api/v0.1/incident/<value>/related/ttps/ (where value
        is a valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'ttp', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * query: /api/v0.1/incident/<value>/related/threat_actors/
        (where value is a valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'threat_actor', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * query: /api/v0.1/incident/<value>/related/incidents/ (where
        value is a valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'incident', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * query: /api/v0.1/incident/<value>/related/coas/ (where value
        is a valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'coa', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * query: /api/v0.1/incident/<value>/related/exploit_targets/
        (where value is a valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'campaigns', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * NOTE: ignoring related packages, as this is deprecated
    2) Give me all the things you've got.
      * query: /api/v0.1/incidents/
        * result: json blob of stix representing a stix package
          containing all incident objects matching the query
  * additional query params
    * none at this time

* STIX type: TTP
    0) Have you seen this thing?
      * query: /api/v0.1/ttp/<value>/ (where value is a valid uuid)
        * result: json blob containing a boolean and (if true) a blob
          of STIX
    1) Give me everything related to this thing.
      * query: /api/v0.1/ttp/<value>/related/ (where value is a valid
        uuid)
      * query: /api/v0.1/ttp/<value>/related/ttps/ (where value is a
        valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'ttp', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * NOTE: since TTPs can only be related to TTPs, the previous two
        queries are functionally equivalent but listed separately for
        consistency's sake
      * NOTE: ignoring related packages, as this is deprecated
    2) Give me all the things you've got.
      * query: /api/v0.1/ttps/
        * result: json blob of stix representing a stix package
          containing all ttp objects matching the query
  * additional query params
    * none at this time

* STIX type: Report
    0) Have you seen this thing?
      * query: /api/v0.1/report/<value>/ (where value is a valid uuid)
        * result: json blob containing a boolean and (if true) a blob
          of STIX
    1) Give me everything related to this thing.
      * query: /api/v0.1/report/<value>/related/
        * result: json blob of stix representing a stix package
          containing all top-level stix objects matching the query
      * query: /api/v0.1/report/<value>/related/observable/ (where
        value is a valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'observable', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * query: /api/v0.1/report/<value>/related/indicators/ (where
        value is a valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'indicator', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * query: /api/v0.1/report/<value>/related/ttps/ (where value is
        a valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'ttp', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * query: /api/v0.1/report/<value>/related/coas/ (where value is
        a valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'coa', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * query: /api/v0.1/report/<value>/related/campaigns/ (where
        value is a valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'campaigns', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * query: /api/v0.1/report/<value>/related/exploit_targets/
        (where value is a valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'exploit_target', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * query: /api/v0.1/report/<value>/related/incidents/ (where
        value is a valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'incident', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * query: /api/v0.1/report/<value>/related/threat_actors/ (where
        value is a valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'threat_actor', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * query: /api/v0.1/report/<value>/related/reports/ (where value
        is a valid uuid)
        * result: json blob containing a list of dicts like
          [{'type': 'report', 'uuid': 'foobar.com:Object-2a1f9a17-b799-4a17-b4ca-f3cb018ad89f'},]
      * NOTE: ignoring related packages, as this is deprecated
    2) Give me all the things you've got.
      * query: /api/v0.1/reports/
        * result: json blob of stix representing a stix package
          containing all report objects matching the query
  * additional query params
    * none at this time
