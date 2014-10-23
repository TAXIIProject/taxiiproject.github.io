---
title: TAXII Introduction
layout: flat
tagline: TAXII Introduction
---

### On This Page
This page is intended to be a quick introduction to TAXII for newcomers and a quick reference for everyone else.

Reading this page you will learn:

* What TAXII is and why TAXII was created 
* The basic "vocabulary" of TAXII: TAXII Services, Data Collections, and supported Sharing Models

### What is TAXII?
TAXII is a transport mechanism that standardizes the automated exchange of cyber threat information. TAXII is a free
and open specification that any software can implement.
 
TAXII is a U.S. Department of Homeland Security (DHS)-led, community-driven effort to standardize the trusted, 
automated exchange of cyber threat information. TAXII is a technology that enables sharing of actionable 
cyber threat information across organization and product/service 
boundaries for the detection, prevention, and mitigation of cyber threats. TAXII is not a specific information 
sharing initiative, and it does not define trust agreements, governance, or non-technical aspects of cyber 
threat information sharing. Instead, TAXII empowers organizations to achieve improved situational awareness about 
emerging threats, and enables organizations to easily share the information they choose with the partners they choose, 
while leveraging existing relationships and systems.

### How and why was TAXII created?
The U.S. Department of Homeland Security (DHS) initiated TAXII to simplify and speed the secure exchange of cyber 
threat information. TAXII eliminates the need for custom sharing solutions with each sharing partner, and 
widespread automated exchange of cyber threat information is now possible. DHS solicited community 
input and engaged MITRE to create TAXII.

### Sharing Models
TAXII is designed to support three common cyber threat information sharing models: Hub and Spoke, Source/Subscriber, 
and Peer to Peer. 

<table width="80%" align="center">
 <tr>
   <td style="word-wrap:break-word"><b>Hub and Spoke</b> is a sharing model where one organization functions as the central clearinghouse 
       for information, or hub, coordinating information exchange between partner organizations, or spokes.
       Spokes can produce and/or consume information from the Hub.</td>
   <td><img src="/images/hub_and_spoke.png" width="400" alt="Hub and Spoke Icon" /></td>
 </tr>
 <tr>
   <td style="word-wrap:break-word"><img src="/images/source_subscriber.png" width="300" alt="Source/Subscriber Icon" /></td>
   <td><b>Source/Subscriber</b> is a sharing model where one organization functions as the single source
   of information and sends that information to subscribers.</td>
 </tr>
 <tr>
   <td style="word-wrap:break-word"><b>Peer to Peer</b> is a sharing model where two or more organizations share information directly with 
   one another. A Peer to Peer sharing model may be ad-hoc, where information exchange is not coordinated ahead of time
   and is done on an as-needed basis, may be well defined with legal agreements and established procedures, or somewhere
   in the middle.</td>
   <td><img src="/images/peer_to_peer.png" width="300" alt="Peer to Peer Icon" /></td>
 </tr>
</table>

### TAXII Services
A **TAXII Service** is a single unit of capability within TAXII. TAXII defines four TAXII Services:

* **Inbox Service** - Used by a TAXII Client to push information to a TAXII Server
* **Poll Service** - Used by a TAXII Client to request information from a TAXII Server
* **Collection Management Service** - Used by a TAXII Client to request information about available **Data Collections** or request a subscription.
* **Discovery Service** - Used by a TAXII Client to discover available TAXII Services (e.g., "An Inbox Service is located at http://example.com/inbox_service ")

### Data Collections
A TAXII **Data Collection** is a grouping of cyber threat information that can be exchanged using TAXII. 
Each TAXII Data Collection has a name that identifies it among Data Collections from an information producer. 
There are two types of TAXII Data Collections: TAXII **Data Feeds** and TAXII **Data Sets**.

A TAXII **Data Feed** is an ordered Data Collection. A TAXII Data Feed's organization allows specific 
portions of TAXII Data Feeds to be requested (e.g., "Give me all content since XYZ").

A TAXII **Data Set** is an unordered Data Collection.

### TAXII Clients and TAXII Servers; Information Producers and Information Consumers
A point of confusion that may come up is how TAXII Clients and/or TAXII Servers can be both Information Producers and/or 
Information Consumers. This section attempts to clarify these distinctions.

* TAXII Servers and Clients:
 * A **TAXII Server** is TAXII Software that offers one or more **TAXII Services**. A TAXII Server listens for connections from TAXII Clients.
 * A **TAXII Client** is TAXII Software that connects to one or more **TAXII Services**. A TAXII Client initiates connections with a TAXII Server.
 * The **TAXII Client** and **TAXII Server** distinction is based on computer networking. 
 * Note that **a single piece of software can be both** a TAXII Client and TAXII Server.
* Information Producers and Consumers: 
 * An **Information Producer** is software that sends information to another system.
 * An **Information Consumer** is software that receives information from another system.
 * The **Information Producer** and **Information Consumer** distinction is based on information flows.
 * Note that **a single piece of software can be both** an Information Producer and Information Consumer.

Two scenarios are illustrated in attempt to clarify the information above:

* Scenario: A **TAXII Client** connects to a **TAXII Server** to send information (TAXII Inbox Service): 
 * The **TAXII Client** is an **Information Producer**
 * The **TAXII Server** is an **Information Consumer**
* Scenario: A **TAXII Client** connects to a **TAXII Server** to request information (TAXII Poll Service): 
 * The **TAXII Client** is an **Information Consumer**
 * The **TAXII Server** is an **Information Producer** 

### Further Information
The information on this page is an overview. For a full understanding of TAXII, please read the 
[TAXII Specifications](http://taxii.mitre.org/specifications/version1.1/). For a further discussion of TAXII, please
sign up for the [discussion list](http://taxii.mitre.org/community/registration.html). Also, check out our 
[Developer Resources](/developers).

### Conclusion (the TL;DR)

* **TAXII** is a technology that standardizes automated information sharing
* TAXII defines four **TAXII Services**: The **Inbox Service**, **Poll Service**, **Collection Management Service**, and the **Discovery Service**
 * TAXII software can host any number of TAXII Services (including zero) and/or connect to any number of TAXII Services (including zero). The TAXII Services that a piece of software hosts and/or connects to is a design decision.
* **Data Collections** are named groupings of data. A Data Collection can be a Data Feed or a Data Set.
 * A **Data Feed** is an ordered Data Collection
 * A **Data Set** is an unordered Data Collection
* TAXII Software can be a **TAXII Client**, **TAXII Server**, or **both**, depending on the role and purpose of the TAXII Software.
* TAXII Software can be an **Information Producer**, **Information Consumer**, or **both**, depending on the role and purpose of the TAXII Software.
