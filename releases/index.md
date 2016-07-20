---
layout: flat
title: TAXII Releases
---

|Release|Release Date|Link|
|-------|------------|---|
|TAXII 1.1|January 13, 2014|[/releases/1.1/](/releases/1.1/)|
|TAXII 1.0|April 30, 2013|[/releases/1.0/](/releases/1.0/)|
|TAXII 1.0 Draft 1|November 16, 2012|[/releases/1.0-draft1/](/releases/1.0-draft1/)|


### Specification Versioning
**Note: This information applies to TAXII 1.0 and TAXII 1.1. This does not apply to OASIS Versions of TAXII**

The version numbers in all TAXII Specifications are formatted as: 'Major.Minor.Update'. The Update value may be omitted if it is 0.

* **Major Version** — A major release is for adding features that require breaking backward compatibility with previous versions or represent fundamental changes to concepts. For a major release, the MAJOR component is incremented by one and the MINOR and UPDATE components are set to zero.
* **Minor Version** — A minor release is for adding features that do not break backward compatibility with previous versions. For a minor release, the MINOR component is incremented by one and the UPDATE component is set to zero.
* **Update Version** — An update release may only be initiated to address critical defects that affect usability. Fixes may break backward compatibility if necessary. New functionality outside of what was intended in the previous MAJOR.MINOR release is not permitted. However, once an update release is agreed to, other non-critical fixes and clarifications may be addressed. When an update version change is made, the UPDATE component is incremented by one.

A particular release of TAXII as a whole pins the following:

* The Major, Minor, and Update values of the TAXII Services Specification. The version of this document is always identical to the version of the TAXII release it supports.
* A list of message and protocol binding specifications and their versions which are compatible with the indicated TAXII Services Specification.
  * It is possible that this list of message and binding specifications may grow within a particular release of TAXII as new binding specifications are defined.
  * It is possible (although unlikely) that revisions of a particular protocol or message binding specification may be defined within a single TAXII release. If this happens, the two versions of the given binding are both considered to be valid bindings under the given TAXII release, although the later revision will be considered preferable.

 
### Backwards Compatibility in TAXII
**Note: This information applies to TAXII 1.0 and TAXII 1.1. This does not apply to OASIS Versions of TAXII**

The concept of backwards compatibility is central to what differentiates a major from a minor release in TAXII. This document sets out a detailed description of what constitutes a backwards compatible change to TAXII.

#### TAXII Release Backwards Compatibility
As noted above, a release of TAXII consists of a specific version of the TAXII Services Specification and a list of message and protocol bindings that are compatible with that version of the TAXII Services Specification. The version of TAXII always equals the version of the TAXII Services Specification associated with that release. A minor release of TAXII follows these rules:
The TAXII Services Specification cannot require functionality that was not required in preceding releases within the same major version.
The TAXII Services Specification cannot remove functionality that was present (optional or required) in preceding releases within the same major version.
All protocol and message bindings denoted as compatible with a given version of the TAXII Services Specification must remain compatible with all subsequent minor revisions of the TAXII Services Specification. In other words, a minor revision of the TAXII Services Specification cannot change in such a way as to break compatibility with protocol or message bindings that were part of the previous TAXII release.

#### Message and Protocol Bindings
The major number of a binding corresponds to the major number of the TAXII release that it supports. As such, a minor revision of a binding will always be compatible with the same major release of TAXII as its predecessor. However, a minor revision of a given binding is not necessarily compatible with the previous version of that binding.

TAXII clients and daemons support a specific set of bindings, indicated by Version IDs. Recall that Version IDs denote both the binding and the binding version. If the set of bindings supported by a client and daemon is not disjoint, they will be able to communicate directly; if the set of supported bindings is disjoint they will not be able to communicate directly (although a gateway might allow translations between one version of a binding and another). When comparing sets of supported bindings, only exact Version ID matches count.

For example, assume two participants, Alice and Bob. Alice supports the following message bindings: X version 1.0, X version 1.1, and Y version 1.1. For this example, assume Alice and Bob both support the same protocol binding.

* If Bob supports any of those listed message bindings, it can directly communicate with Alice.
* If Bob does not support any of those listed message bindings, it cannot directly communicate with Alice. This is true even if it supports binding Y version 1.0 (an earlier version of a binding A supports) or binding X version 1.2 (a later version of a binding A supports). In this case, Alice and Bob are only able to interoperate through a gateway that can translate between some binding supported by Alice and some binding supported by Bob.

All minor revisions of binding specifications include procedures for translating content expressed using the previous version of the binding to the new version and back in a deterministic, lossless manner.

TAXII clients and daemons are encouraged to support older versions of their supported bindings since this greatly enhances interoperability and there should only be small differences between minor releases of bindings. However, clients and daemons are not required to do so.

#### Non-Normative Document Versioning
Non-normative documents, such as the TAXII Overview, Content Binding Reference, Errata, and other documents may be revised at any time and will be versioned separately from the TAXII Specifications.