---
layout: flat
title: TAXII 1.0
---

This page provides information on TAXII 1.0. All information about the version is included 
in this centralized location. Join the [TAXII Community](https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=cti) to participate in the next version of TAXII.

Please note that there is a [newer version of TAXII](/releases/current/)

## Specifications
#### TAXII Overview, Version 1.0 [[PDF](TAXII_Overview.pdf)]
An overview document that defines the primary concepts of TAXII, as well as the organization of TAXII component documents.

#### TAXII Services Specification, Version 1.0 [[PDF] (TAXII_Services_Specification.pdf)]
The TAXII Services Specification provides requirements that govern TAXII core concepts, such as services and exchanges. 
It does not provide details on data formatting or how TAXII messages are transported over a network; such details and 
requirements can be found in the HTTP Protocol Binding Specification and XML Message Binding Specification below.

#### TAXII HTTP Protocol Binding Specification, Version 1.0 [[PDF] (TAXII_HTTPProtocolBinding_Specification.pdf)]
This specification defines the requirements for representing TAXII messages in Hypertext Transfer Protocol (HTTP) and HTTPS.

#### TAXII XML Message Binding Specification, Version 1.0 [[PDF] (TAXII_XMLMessageBinding_Specification.pdf), [XSD] (TAXII_XMLMessageBinding_Schema.xsd)]
This specification defines the requirements for representing TAXII messages in Extensible Markup Language (XML).

#### TAXII Content Binding Reference, Version 3 [[PDF] (TAXII_ContentBinding_Reference_v3.pdf)]
This document is a non-normative document that lists Content Binding Identifiers (IDs) for use within TAXII.

#### TAXII Version 1.0 Errata, Released June 21, 2013 [[PDF] (TAXII_Errata_21June2013.pdf)]
This document is a list of known errors in the TAXII Version 1.1 Specifications, along with their corrections.

## Release Notes
The major highlights of Version 1.0 are listed below:

* Added a TAXII Overview document to serve as the main entry point into the TAXII Specifications.
* Updated the TAXII Services Specification including heavily modifying the Manage Feed Subscription Request/Response to simplify the exchange, adding a new ‘TAXII Content Handling’ section to provide greater clarity on a number of topics, and adding a Content Block concept, among other changes.
* Updated the TAXII HTTP Binding Specification so that all HTTP Requests now use POST in order to support digital signatures in all TAXII Messages, and added handling for cases where TAXII-conformant HTTP Clients encounter responses that do not contain a TAXII Message.
* Updated the TAXII XML Binding Specification to support changes made in the TAXII Services Specification
* Added a TAXII Content Binding Reference document to provide a canonical list of supported Content Bindings in the spirit of an IANA table. Previously, content bindings were defined in Message Binding specifications.

See the full [release notes] (release_notes.pdf).