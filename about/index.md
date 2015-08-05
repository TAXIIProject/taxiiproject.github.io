---
title: About TAXII
layout: flat
---

TAXII is a free and open transport mechanism that standardizes the automated exchange of cyber threat information. 


## Impetus
Sharing cyber-risk intelligence and defensive strategies has become imperative in today’s threat landscape. No organization can realistically sit in isolation and still be able to defend itself.

By understanding adversaries’ behavior against a range of targets over a period of time, defenders gain valuable insights into an attacker’s overall goals and strategies. 

TAXII empowers organizations share situational awareness about threats with the partners they while leveraging existing relationships and systems.

> TAXII is the preferred exchange mechanism for [Structured Threat Information eXpression (STIX™) ](https://stixproject.github.io) 

## Goals 
- Enable timely and secure sharing of threat information in cyber defender communities.
- Support a broad range of use cases and practices common to cyber threat information sharing communities.
- Minimize operational changes needed to adopt TAXII.

> By using TAXII, organizations can share STIX content in a secure and automated manner.


## Sharing Models
TAXII is designed to integrate with existing sharing agreements, including access control limitations.

`Push` and `Pull` messages are supported - supporting both subscription feeds and on-demand queries.

> TAXII leverages existing protocols when possible - with native support for `HTTP` and `HTTPS`.


<div class="row">
  <div class="col-lg-4 col-md-6">
    <div class="panel panel-default">
      <div class="panel-heading">
        <h3 class="panel-title">Hub and Spoke</h3>
      </div>
      <div class="panel-body">
        <p><strong>Hub and Spoke</strong> is a sharing model where one organization functions as the central clearinghouse for information, or hub, coordinating information exchange between partner organizations, or spokes. Spokes can produce and/or consume information from the Hub.</p>
        <div class="text-center">
          <img src="/images/hub_and_spoke.png" width="300" alt="Hub and Spoke Model" />
        </div>
      </div>
    </div>
  </div>
  <div class="col-lg-4 col-md-6">
    <div class="panel panel-default">
      <div class="panel-heading">
        <h3 class="panel-title">Source/Subscriber</h3>
      </div>
      <div class="panel-body">
        <p><strong>Source/Subscriber</strong> is a sharing model where one organization functions as the single source of information and sends that information to subscribers.</p>
        <div class="text-center">
          <img src="/images/source_subscriber.png" width="300" alt="Source/Subscriber Model" />
        </div>
      </div>
    </div>
  </div>
  <div class="col-lg-4 col-md-6">
    <div class="panel panel-default">
      <div class="panel-heading">
        <h3 class="panel-title">Peer to Peer</h3>
      </div>
      <div class="panel-body">
        <p><strong>Peer to Peer</strong> is a sharing model where two or more organizations share information directly with one another. A Peer to Peer sharing model may be ad-hoc, where information exchange is not coordinated ahead of time and is done on an as-needed basis, may be well defined with legal agreements and established procedures, or somewhere in the middle.</p>
        <div class="text-center">
          <img src="/images/peer_to_peer.png" width="300" alt="Peer to Peer Model" />
        </div>
      </div>
    </div>
  </div>
</div>


## Related Links
- [Formal TAXII Specifications](http://taxii.mitre.org/specifications/version1.1/). 
- Sign up for the [discussion list](http://taxii.mitre.org/community/registration.html)
- [Developer Resources](/developers)

## Frequently Asked Questions

### General
#### A1. What is TAXII?
Trusted Automated eXchange of Indicator Information (TAXII™) is a U.S. Department of Homeland Security (DHS)-led, community-driven effort to standardize the trusted, automated exchange of cyber threat information. TAXII defines a set of services and message exchanges that, when implemented, enable sharing of actionable cyber threat information across organization and product/service boundaries for the detection, prevention, and mitigation of cyber threats. TAXII is not a specific information sharing initiative, and it does not define trust agreements, governance, or non-technical aspects of cyber threat information sharing. Instead, TAXII empowers organizations to achieve improved situational awareness about emerging threats, and enables organizations to easily share the information they choose with the partners they choose, while leveraging existing relationships and systems.

#### A2. How and why was TAXII developed?
The U.S. Department of Homeland Security (DHS) initiated TAXII to simplify and speed the secure exchange of cyber threat information. TAXII’s standardized services and message exchanges eliminate the need for custom sharing solutions with each sharing partner, and widespread automated exchange of cyber threat information is now possible. DHS solicited community input and engaged MITRE to write the TAXII Specifications.

#### A3. Where can I get TAXII?
TAXII specifications, documentation, and related information can be found in the TAXII Specifications section of the TAXII website. Additional materials are also hosted in TAXIIProject on GitHub.com.

#### A4. How is TAXII licensed?
See the Terms of Use.

#### A5. Who owns TAXII?
TAXII is an open community effort and is sponsored by the office of Cybersecurity and Communications at the U.S. Department of Homeland Security (DHS). Operating as DHS’s Federally Funded Research and Development Center (FFRDC), MITRE has copyrighted the TAXII Specifications for the benefit of the community in order to ensure TAXII remains a free and open standard, as well as to legally protect the ongoing use of TAXII and any resulting content created by government, vendors, and/or users. In addition, MITRE has trademarked ™ the TAXII acronym and the TAXII logo to protect their sole and ongoing use by the TAXII effort within the information security arena.

#### A6. How can my organization and I be involved?
Broad and diverse community participation is an integral component of the TAXII effort. Visit the TAXII Community page for additional information.

#### A7. Is someone from TAXII available to speak or participate on panel discussions at industry-related events, meetings, etc.?
Yes, contact stix-taxii@hq.dhs.gov to have the TAXII team present a briefing or participate in a panel discussion about TAXII and/or information sharing at your event.

### TAXII Effort
#### B1. What can I do with TAXII?
TAXII implementations enable secure, consistent, and automated exchange of cyber threat information. TAXII services can be used to support a wide range of sharing models and community requirements. With standardized services, messages, and message exchanges, TAXII implementations facilitate automation and eliminate the need for multiple, custom, point-to-point exchange implementations. TAXII simplifies and speeds cyber threat information exchange.

#### B2. What data formats and message protocols does TAXII support? Is future expansion anticipated?
At present, TAXII defines an XML data format and HTTP/HTTPS message protocols. Details can be found in the TAXII XML Message Binding Specification and the TAXII HTTP Protocol Binding Specification, respectively in the TAXII Specifications section. Future expansion to other protocols and message formats is possible, depending on community demand. The TAXII specifications are written in a modular fashion to accommodate multiple message formats and message protocols. Due to community interest and widespread use, XML and HTTP/HTTPS were selected as the initial TAXII message format and Specifications.

#### B3. What are the TAXII Specifications and how do I use them?
The TAXII Specifications define the messages, message exchanges, message formats and message protocols that enable standardized sharing of cyber threat information. To use the TAXII Specifications, an entity needs to be capable of representing cyber threat information in a TAXII message, as well as send and receive TAXII messages in a manner that conforms to the TAXII Specifications.

#### B4. How can I contribute to the development of this effort?
TAXII is an open effort that welcomes community participation. Visit the TAXII Community page for additional information.

#### B5. How do I submit questions related to this effort?
Questions regarding the TAXII effort may be submitted to the TAXII Community Email Discussion List or sent to the MITRE TAXII community management team at taxii@mitre.org

#### B6. How is this effort versioned?
See the Versioning Policy.

### Relationships to Other Efforts
#### C1. What is the relationship between TAXII and STIX?
The Structured Threat Information eXpression (STIX™) is a related U.S. Department of Homeland Security—led effort of the office of Cybersecurity and Communications to characterize a rich set of cyber threat information. STIX is one payload that TAXII can convey. STIX represents cyber threat information in a standardized and structured manner. STIX characterizes what is being shared, while TAXII defines how the STIX payload is shared.

#### C2. What is the relationship between TAXII and CybOX?
The Cyber Oberservable eXpression (CybOX™) is a U.S. Department of Homeland Security—led effort of the office of Cybersecurity and Communications that provides a structured language for describing elements within the cyber operational environment. Structured Threat Information eXpression (STIX™) is one payload that TAXII can convey, and STIX uses CybOX to represent cyber observables.

#### C3. What is the relationship between TAXII and MAEC?
Malware Attribute Enumeration and Characterization (MAEC™) is a U.S. Department of Homeland Security—led effort of the office of Cybersecurity and Communications that provides a standardized language for encoding and communicating high-fidelity information about malware based upon attributes such as behaviors, artifacts, and attack patterns. Structured Threat Information eXpression (STIX™) is one payload that TAXII can convey, and STIX can describe malware using MAEC.

### Using TAXII
#### D1. What is included in a TAXII release?
A TAXII release includes a set of technical specifications that describe precisely how to exchange cyber threat information in a consistent, secure manner with another entity. See the TAXII Specifications section for more information.

#### D2. Can I use TAXII to share indicator lists? If so, how?
TAXII implementations can share any content as long as it can be represented in a TAXII Message. Use of the Structured Threat Information eXpression (STIX™) is recommended to capture indicator list (or other cyber threat) data for seamless sharing through TAXII.

#### D3. How do you communicate available TAXII services and their use?
Available TAXII services and their use can be communicated via the TAXII Discovery Service. The Discovery Service provides a requester with a list of TAXII Services and how these Services can be invoked. Specific details can be found in the TAXII Services Specification in the TAXII Specifications section.

#### D4. Can I exchange encrypted data using TAXII? If so, how?
Yes, encrypted data can be exchanged using TAXII. Content can be encrypted directly within a TAXII Message, and the TAXII Protocol Bindings can also support encryption of the entire TAXII Message over the network. Specific details can be found in the TAXII Services Specification and the TAXII Content Binding Reference in the TAXII Specifications section.

### TAXII Community
#### E1. What is the role of the TAXII Community and how can I join?
The TAXII Community helps build this growing, open-source industry effort by participating in the development of the TAXII Specifications, Utilities and Libraries through the following:

TAXII Community Email Discussion List — where community members discuss the latest drafts of the TAXII Specifications, schemas utilities, technical documents, and other items integral to the ongoing development of TAXII.
TAXIIProject GitHub Repositories — the central location for TAXII Community members to make open-source contributions to TAXII development.
Periodic face-to-face interactions at meetings, conferences and birds-of-a-feather sessions.
You may also email us directly at taxii@mitre.org with any comments or concerns.

#### E2. What is MITRE?
The MITRE Corporation is a not-for-profit company that operates multiple federally funded research and development centers (FFRDCs). MITRE provides innovative, practical solutions for some of our nation's most critical challenges in defense and intelligence, aviation, civil systems, homeland security, the judiciary, and healthcare.

Please see the MITRE Corporate Overview for more information.

#### E3. What is MITRE’s role in TAXII?
MITRE acts as the TAXII community facilitator and coordinator. In that role MITRE manages the TAXII website, community engagement, and discussion lists to enable open and public collaboration with all stakeholders.

#### E4. Why is MITRE maintaining TAXII, and how long does MITRE plan to maintain it?
In accordance with its mission, MITRE acts in the public interest. MITRE’s unique role allows it to provide an objective perspective to this effort. MITRE will maintain TAXII as long as it serves the public interest to do so.

#### E5. Who pays for TAXII? Who is the Sponsor?
TAXII is sponsored by the office of Cybersecurity and Communications at the U.S. Department of Homeland Security.

### TAXII Specifications
#### F1. Is a content provider expected to store content using different bindings and/or translate between various content bindings?
A content provider is not required to store content using different bindings, and is not required to translate between content bindings. The idea behind a consumer indicating a list of Content Bindings is to allow the consumer to avoid receiving content it is unable to parse, rather than an expectation that the hub will have copies of all of its content in each of the requested formats. A content provider MIGHT make the same piece of content available in multiple formats in order to support a wider range of recipients but doing so is not required.

#### F2. Why does the XML schema seem more permissive than the XML Binding in some cases?
In the XML binding specification an element might be required under some circumstances but optional in others, but in the schema it always appears as optional. For example, in a "Subscription Management Response Message" the "Subscription" field is optional if the requested action is STATUS and otherwise is required, yet the XML binding says "0-n" for the count. Due to the limits of XML schema definitions, it was necessary to use the more flexible definition, even though it would appear exactly once for the other action types. Remember that the XML schema is not considered to be normative — it is present as an aid only, but it is known that it is somewhat more permissive than the specification.

