---
layout: flat
title: TAXII 1.1
---

This page provides information on TAXII 1.1. All information about the version is included 
in this centralized location. Join the [TAXII Community](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=cti) to participate in the next version of TAXII.

## Specifications
#### TAXII Overview, Version 1.1 [[PDF](TAXII_Overview.pdf)]
An overview document that defines the primary concepts of TAXII, as well as the organization of TAXII component documents.

#### TAXII Services Specification, Version 1.1 [[PDF] (TAXII_Services_Specification.pdf)]
The TAXII Services Specification provides requirements that govern TAXII core concepts, such as services and exchanges. 
It does not provide details on data formatting or how TAXII messages are transported over a network; such details and 
requirements can be found in the HTTP Protocol Binding Specification and XML Message Binding Specification below.

#### TAXII HTTP Protocol Binding Specification, Version 1.0 [[PDF] (TAXII_HTTPProtocolBinding_Specification.pdf)]
This specification defines the requirements for representing TAXII messages in Hypertext Transfer Protocol (HTTP) and HTTPS.

#### TAXII XML Message Binding Specification, Version 1.1 [[PDF] (TAXII_XMLMessageBinding_Specification.pdf), [XSD] (TAXII_XMLMessageBinding_Schema.xsd)]
This specification defines the requirements for representing TAXII messages in Extensible Markup Language (XML).

#### TAXII Default Query Specification, Version 1.0 [[PDF] (TAXII_Default_Query_Specification.pdf), [XSD] (TAXII_DefaultQuery_Schema.xsd)]
This specification defines the default TAXII Query Language used in TAXII 1.1.

#### TAXII Content Binding Reference, Version 3 [[PDF] (TAXII_ContentBinding_Reference_v3.pdf)]
This document is a non-normative document that lists Content Binding Identifiers (IDs) for use within TAXII.

#### TAXII Version 1.1 Errata, Released July 2, 2014 [[PDF] (TAXII_Errata_02July2014.pdf)]
This document is a list of known errors in the TAXII Version 1.1 Specifications, along with their corrections.

## Release Notes
The major highlights of Version 1.1 are listed below:

* Added the ability to include content-based query instructions in Poll Requests and Subscription Requests.
* Added the concepts of unordered Data Sets to the previous, ordered Data Feeds.
* Added the ability for Inbox Messages to request their contained content be added to one or more Data Collections hosted by the recipient.
* Added the ability to Pause and Resume active subscriptions.
* Added the ability to request record counts instead of receiving full record lists.
* Added the ability to provide prose messages with individual pieces of content.
* Added the ability for Producers to characterize the volume of content associated with individual Data Collections.
* Expanded the format for Message IDs.
* Addressed problems related to mixed use of inclusive and exclusive ranges of Timestamp Labels.
* Multiple fixes and clarifications.
* Added a new TAXII Default Query Specification in support of the newly defined TAXII Query capability.

See the full [release notes] (release_notes.pdf).