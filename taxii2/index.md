---
layout: flat
title: TAXII 2 Homepage
---

This is the landing page for information related to TAXII 2. This page is intended to be an index into
the latest information and resources, so please bookmark it if you are interested in TAXII!

If you'd like to contribute to the conversation, please join the [OASIS CTI TC](https://www.oasis-open.org/committees/cti/),
send an email to the CTI Users list [cti-users@lists.oasis-open.org](cti-users@lists.oasis-open.org, or send an email to the 
OASIS CTI TAXII SC co-chairs, Mark Davidson ([mdavidson@soltra.com](mdavidson@soltra.com)) and Bret Jordan ([bret.jordan@bluecoat.com](bret.jordan@bluecoat.com)).

## Vision Statement
> TAXII is an open protocol for the communication of cyber threat information. Focusing on simplicity and scalability, TAXII enables authenticated and secure communication of cyber threat information across products and organizations.

**Open Question(s):**

* Should it be "cyber threat information" or just "threat information"?

## Design Artifacts
Design artifacts include Use Cases, Requirements, etc.

* [Requirements](https://github.com/TAXIIProject/TAXII-Specifications/wiki/TAXII-2.0-Requirements)
* [Use Cases](https://github.com/TAXIIProject/TAXII-Specifications/wiki/TAXII-2.0-Use-Cases)
* [Formats and Protocols](https://github.com/TAXIIProject/TAXII-Specifications/wiki/TAXII-2.0-Formats-and-Protocols)
* [TAXII 1.x Pain Points](https://github.com/TAXIIProject/TAXII-Specifications/wiki/TAXII-1.1-1.0-Pain-Points)
* [Open Questions](https://github.com/TAXIIProject/TAXII-Specifications/wiki/TAXII-2.0-Open-Questions)
* [Candidate Protocol Bindings](/docs/taxii-protocols-comparison.xlsx)

## Decisions
This is a list of discussion topics that appear to have rough consensus in the TAXII SC and can be considered decisions.

* Vision Statement (See above)
* HTTP as an MTI protocol
* [REST API](/taxii2/rest-api/)
  * Includes "Groups of Channels" as an API Base
  * Includes DNS SRV record definition
* [Authentication](/taxii2/rest-api/)

## Current Proposals
The TAXII Subcommittee (SC) is currently in the process of requesting and evaluating proposals for TAXII 2. 
The current list of proposals under evaluation is here:

* [Channel-Based Proposal](https://github.com/TAXIIProject/TAXII-Specifications/wiki/Possible-TAXII-2.0:-Channel-based-TAXII)
  * [Concept Overview](https://github.com/TAXIIProject/TAXII-Specifications/wiki/TAXII-2.0-Concept-Overview)
* [Incremental Improvement Proposal](https://github.com/TAXIIProject/TAXII-Specifications/wiki/Possible-TAXII-:-Incremental-Improvement)
  * [Concept Overview](https://github.com/TAXIIProject/TAXII-Specifications/wiki/Incremental-Improvement-Concept-Overview)
* [Trust Group Proposal](http://blog.threatloop.com/post/127598238937/taxii-stix-v20-proposal)
* [Notional Query](/taxii2/notional-query-api/)
* If you have another proposal, please let us know!

## Resources
* [OASIS CTI Wiki](https://wiki.oasis-open.org/cti/)
  * [TAXII portion of the wiki](https://wiki.oasis-open.org/cti/taxii)

## Related Work and Related Reading
This is a list of related work, in no particular order. If you see something missing, please let us know and we'll add it.

**Related Work**

* [AbuseHelper](http://abusehelper.be/)
* [WOMBAT](http://www.wombat-project.eu/)
* [N6](http://n6.cert.pl/)


**Related Reading**

These readings cover a variety of topics, from messaging to threat sharing to standards processes and more. They represent resources
that have informed the thinking of the OASIS CTI TAXII SC.

* [TAXII 1.0/1.1 Pain Points](https://github.com/TAXIIProject/TAXII-Specifications/wiki/TAXII-1.1-1.0-Pain-Points)
* [Controlled Data Sharing for Collaborative Predictive Blacklisting](http://arxiv.org/pdf/1502.05337.pdf)
* [iMatix AMQP rant](http://www.imatix.com/articles:whats-wrong-with-amqp/)
* [Clarifying AMQP](http://kellabyte.com/2012/10/20/clarifying-amqp/)
* [Problems and Criticisms of CORBA](https://en.wikipedia.org/wiki/Common_Object_Request_Broker_Architecture#Problems_and_criticism)
* [Java Message Service (JMS)](https://en.wikipedia.org/wiki/Java_Message_Service)
* [Network Based Security Systems](https://www.sans.org/reading-room/whitepapers/detection/network-based-security-systems-search-stix-taxii-based-indicators-compromise-36147)
* [Asynchronous Processing in Web Applications](http://blog.codepath.com/2013/01/06/asynchronous-processing-in-web-applications-part-2-developers-need-to-understand-message-queues/)
