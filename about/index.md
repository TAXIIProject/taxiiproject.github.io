---
title: About TAXII
layout: flat
---

[Trusted Automated eXchange of Indicator Information (TAXII™)](/releases) is a free and open transport mechanism that standardizes the automated exchange of cyber threat information. 


### Impetus
Sharing cyber-risk intelligence and defensive strategies has become imperative in today’s threat landscape. No organization can realistically sit in isolation and still be able to defend itself.

By understanding adversaries’ behavior against a range of targets over a period of time, defenders gain valuable insights into an attacker’s overall goals and strategies. 

TAXII empowers organizations to share situational awareness about threats with the partners they choose, while leveraging existing relationships and systems.

> TAXII is the preferred exchange mechanism for [Structured Threat Information eXpression (STIX™)](https://stixproject.github.io).

### Goals 
- Enable timely and secure sharing of threat information in cyber defender communities.
- Support a broad range of use cases and practices common to cyber threat information sharing communities.
- Minimize operational changes needed to adopt TAXII.

> By using TAXII, organizations can share STIX content in a secure and automated manner.


### Sharing Models
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


## TAXII Community
TAXII has been transitioned to [OASIS](https://www.oasis-open.org/committees/cti). See the [Community](http://taxiiproject.github.io/community/) page for details. 

Some shortcuts:  

[OASIS Cyber Threat Intelligence (CTI) Technical Committee (TC)](https://www.oasis-open.org/committees/cti) - TAXII is developed by the TAXII subcommittee of the CTI TC. 

[Mailing Lists](/community/#discussion-lists-amp-archives) - Stay up-to-date on development and usage. 

[Developer Resources](/developers) - The central location for development of the specifications, tools, and documentation (including this site). 

[STIX/TAXII Supporters](http://stixproject.github.io/supporters) - A growing list of products, services, and sharing communities using TAXII and STIX. 

## Frequently Asked Questions

#### What is TAXII?
TAXII is a community effort to standardize the trusted, automated exchange of cyber threat information. TAXII defines a set of services and message exchanges that, when implemented, enable sharing of actionable cyber threat information across organization and product/service boundaries for the detection, prevention, and mitigation of cyber threats. 

TAXII is not a specific information sharing initiative, and it does not define trust agreements, governance, or non-technical aspects of cyber threat information sharing. 

Instead, TAXII empowers organizations to achieve improved situational awareness about emerging threats, and enables organizations to easily share the information they choose with the partners they choose, while leveraging existing relationships and systems.

#### Where can I get TAXII?
See [TAXII Releases](/releases/).

#### How is TAXII licensed?
See the [Terms of Use](/legal/).

#### Who is using TAXII?
[Many organizations](http://stixproject.github.io/supporters) have announced support for TAXII and STIX, and are listed on our [STIX/TAXII Supporters](http://stixproject.github.io/supporters) page on the STIX website. Please use our [submission form](http://goo.gl/forms/jKQH7a6TfW) to request that your organization’s products and services be added to the list.

Our [STIX/TAXII Blog](http://stixproject.tumblr.com/) also lists press releases and other vendor announcements.

#### What can I do with TAXII?
TAXII implementations enable secure, consistent, and automated exchange of cyber threat information. TAXII services can be used to support a wide range of sharing models and community requirements. With standardized services, messages, and message exchanges, TAXII implementations facilitate automation and eliminate the need for multiple, custom, point-to-point exchange implementations. TAXII simplifies and speeds cyber threat information exchange.

#### What data formats and message protocols does TAXII support? Is future expansion anticipated?
At present, TAXII defines an XML data format and HTTP/HTTPS message protocols. Details can be found in the TAXII XML Message Binding Specification and the TAXII HTTP Protocol Binding Specification. Future expansion to other protocols and message formats is possible, depending on community demand. The TAXII specifications are written in a modular fashion to accommodate multiple message formats and message protocols. Due to community interest and widespread use, XML and HTTP/HTTPS were selected as the initial TAXII message format and Specifications.

#### Can I use TAXII to share indicator lists? If so, how?
TAXII implementations can share any content as long as it can be represented in a TAXII Message. Use of [STIX](https://stixproject.github.io/) is recommended to capture indicator list (or other cyber threat) data for seamless sharing through TAXII.

#### How do you communicate available TAXII services and their use?
Available TAXII services and their use can be communicated via the TAXII Discovery Service. The Discovery Service provides a requester with a list of TAXII Services and how these Services can be invoked. Specific details can be found in the TAXII Services Specification.

#### Can I exchange encrypted data using TAXII? If so, how?
Yes, encrypted data can be exchanged using TAXII. Content can be encrypted directly within a TAXII Message, and the TAXII Protocol Bindings can also support encryption of the entire TAXII Message over the network. Specific details can be found in the TAXII Services Specification and the TAXII Content Binding Reference.

#### Is a content provider expected to store content using different bindings and/or translate between various content bindings?
A content provider is not required to store content using different bindings, and is not required to translate between content bindings. The idea behind a consumer indicating a list of Content Bindings is to allow the consumer to avoid receiving content it is unable to parse, rather than an expectation that the hub will have copies of all of its content in each of the requested formats. A content provider MIGHT make the same piece of content available in multiple formats in order to support a wider range of recipients but doing so is not required.

#### Why does the XML schema seem more permissive than the XML Binding in some cases?
In the XML binding specification an element might be required under some circumstances but optional in others, but in the schema it always appears as optional. For example, in a "Subscription Management Response Message" the "Subscription" field is optional if the requested action is STATUS and otherwise is required, yet the XML binding says "0-n" for the count. Due to the limits of XML schema definitions, it was necessary to use the more flexible definition, even though it would appear exactly once for the other action types. Remember that the XML schema is not considered to be normative — it is present as an aid only, but it is known that it is somewhat more permissive than the specification.

## Relationships to Other Efforts

#### STIX
[Structured Threat Information eXpression (STIX™)](http://stixproject.github.io/) is a structured language for describing cyber threat information so it can be shared, stored, and analyzed in a consistent manner. STIX is one payload that TAXII can convey. STIX represents cyber threat information in a standardized and structured manner. STIX characterizes what is being shared, while TAXII defines how the STIX payload is shared.

#### CybOX
[Cyber Observable eXpression (CybOX™)](https://cyboxproject.github.io/) is a structured language for describing elements that are observable within the cyber operational environment. STIX is one payload that TAXII can convey, and STIX uses CybOX to represent cyber observables.

#### MAEC
[Malware Attribute Enumeration and Characterization (MAEC™)](http://maecproject.github.io/) is a structured language for encoding and communicating high-fidelity information about malware based upon attributes such as behaviors, artifacts, and attack patterns. STIX is one payload that TAXII can convey, and STIX can describe malware using MAEC.
