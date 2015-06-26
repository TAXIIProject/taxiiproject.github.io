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
