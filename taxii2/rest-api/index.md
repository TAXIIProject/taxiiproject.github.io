---
layout: flat
title: TAXII 2 REST API
---

The TAXII SC has a general consensus that TAXII should have a REST API. There are many factors to consider when designing 
a REST API. This page documents the current state of the proposed REST API and documents open questions where they are known.

This page is written as normative text so that it can be used as the basis for a specification. This phrasing should not deter
readers from raising questions.

This page defines the REST API and some other related items (e.g., Authentication, DNS SRV).

### DNS SRV
DNS Service (SRV) records are used for advertising network services via DNS. This section defines a service name for TAXII
so that TAXII implementations that conform to this specification can be advertised in DNS. 
This section also defines rules for using the TAXII DNS SRV record to determine the Discovery URL and the Default API Base.

The service name for this version of TAXII is: `taxii2`. Future versions of TAXII may define alternate service names.

An example DNS SRV record, advertising a TAXII server located at `taxii.example.com:443`:

`_taxii2._tcp.example.com. 86400 IN SRV 0 5 443 taxii.example.com`

**Discovery URL:**

The Discovery URL is created from the TAXII DNS SRV record using the following production:

Discovery URL: `https://` + hostname + `:` + port + `/taxii2/api-bases/`

Example Discovery URL: `https://taxii.example.com:443/taxii2/api-bases/`

**Default API Base:**

The Default API Base is created from the TAXII DNS SRV record using the following production:

Default API Base: `https://` + hostname + `:` + port + `/taxii2/default/`

Example Default API Base: `https://taxii.example.com:443/taxii2/default/`

Ref: https://www.ietf.org/rfc/rfc2782.txt

### Authentication
The current proposal that seem to have acceptance is HTTPS + HTTP Basic + JWT (JSON Web Tokens).

**Open Questions:**

 * Can this approach be accredited?
 * What needs to be specified to guarantee interoperability?
 
### HTTPS Only
This specification defines requirements for using HTTPS; this specification does not define requirements for using HTTP. TAXII
Clients and Servers MUST use HTTPS. While the additional use of HTTP is recognized as a straightforward and perhaps trivial to
implement, and while Clients and Servers may choose to use HTTP, those uses are not considered 
conformant with this specification. ONLY the use of HTTPS is considered conformant with this specification.

**Open Questions:**
 * Should TAXII2 be an HTTPS-only protocol? What are the pros/cons?

### HTTP X-Headers
This specifications defines HTTP X-Headers that are used for TAXII.

#### X-Max-Size

**Header Name**: `X-Max-Size`

**Use**: The `X-Max-Size` MAY be used in HTTP Requests. The `X-Max-Size` header MUST NOT be used in HTTP Responses.

**Meaning**: The `X-Max-Size` header identifies the maxmimum response size in decimal number of OCTETs (aka bytes) that the client 
is capable of receiving. The `Content-Length` of the response MUST NOT be larger than the `X-Max-Size` value, if specified.

**Allowable Values**: The mimimum allowable value is `9437184` (9mb). There is no maximum allowable value.

**Default Value**: If the `X-Max-Size` header is not specified in the HTTP Request, the value should be treated as the minimum allowable value.

**Open Questions:** 

* This is too small for many PCAPs/EXEs, etc. Maybe some other REST API thing?
* What happens when a single message exceeds the max-size value? Discarded? Who should get alerted?

#### X-Rate-Limit
Not sure exactly what this means yet, other than it's ben asked for and is a way to get clients to make slower requests. Need 
more detail on this one.

### API-Base
Note that in this version of TAXII, the creation, modification, and deletion of API-Bases is not specified; only the 
listing of available API-Bases is specified. Implementers are free to implement (or not) create/modify/delete functionality in 
any way they wish.

An API-Base is any valid HTTPS URL (e.g., `https://subdomain.example.com:12345/whatever/`)

From the API-Base, the following URLs are valid:

* `[API-Base]/channels/<channel-name>/`
* `[API-Base]/channels/`

### API Methods
In this section, each URL is specified, along with a set of possible responses.

* `GET [API-Base]/channels/` - Returns a list of channels
 * HTTP 200 - Returns a list of channels accessible by the requestor (e.g., channel-list message)
 * HTTP 400 - Invalid request
 * HTTP 403 - Permission denied, you are not allowed to view the channel list
* `GET [API-Base]/channels/<channel-name>/` - Returns info about a specific channel
 * HTTP 200 - Returns channel information (e.g., channel-info message)
 * HTTP 400 - Invalid request
 * HTTP 403 - Permission denied, you are not allowed to view this channel's information
* `POST <channel object> to [API-Base]/channels/` - Create a new channel
 * HTTP 201 - Message accepted, channel will be created
 * HTTP 400 - Invalid request, something wrong with your channel structure
 * HTTP 403 - Permission denied, you are not allowed to make new channels
 * HTTP 501 - Not implemented, this server has a fixed set of available channels
* `POST <taxii message(s)> to /channels/<channel-name>/` - Add TAXII message(s) to the channel
 * HTTP 202 - Message(s) accepted, message will be transmitted to the channel
 * HTTP 400 - Invalid request, something wrong with your message structure
 * HTTP 403 - Permission denied, you can not post to this channel
 * HTTP 501 - Not implemented (This is a read only channel)
* `GET /channels/<channel-name>/[?param1=val1...]` - Get or Create a subscription and get TAXII messages from the channel with the specified filter. For more on subscriptions, see below.
 * HTTP 200 - Response fulfilled
 * HTTP 204 - No new data
 * HTTP 400 - Invalid request
 * HTTP 403 - Permission denied
 * HTTP 501 - Not implemented (This is a write-only channel)

**Open Questions:**

* If we permit POSTing multiple messages, how are different message dispositions handled? (e.g., message 1 was accepted, message 2 was re-written, and message 3 was rejected)
* How is content negotiated? At the channel level, at the message level? Something else?
 * MSD Opinion: Should try to leverage HTTP Content-Types/MIME Types
* Should there be update and destroy (PUT and DELETE)? Renaming channels could be complicated and have weird side effects given the name is in the URL, but changing permissions for existing channels might be a requirement.
* We should think about long polling vs. other options
 * https://developer.mozilla.org/en-US/docs/Web/API/EventSource
 * WebSockets? (Though, WebSockets are a completely different protocol)
* Should the REST API include mechanisms for modifying permissions, or should that be an implementation-specific thing?
* Should getting messages be a GET? These responses shouldn't be cached, so maybe not.

### Control Messages (DRAFT)

**Channel Create Object**

```python
{
 "name": "<channel-name>",
 "description": "<channel-description>", # Optional user-friendly description of what is on the channel
 "permitted_messages": ['msg1', 'msg2'],  # Empty list denotes ALL messages are permitted (?)
 "content_type": "<content type>" # Content type of the channel (MIME types? text/x-stix, text/x-openioc? ),
 "ttl":<TTL_in_seconds> # TTL of any content in this channel before it is purged from your view. IE, how often you must poll to guarantee to not miss any messages.
}
```

Open questions:

* Should permissions be somehow provided/optional in the message?
* Is there a way to "invite" people to a channel?

### Subscriptions

Subscriptions are currently proposed as an implementation of the PubSub subscription model - a client requests messages from a channel that meet a particular filter. A subscription is uniquely identified by a user-id, API-Base + channel name, and the selector (e.g., GET parameters).

Subscription lifecycle:

1. An authenticated client does an HTTP GET to a channel
2. Server does a "get or create" action on the subscription
3. If the subscription already existed, the server responds with queued messages (if any)
4. If the subscription was created, the server waits for some new messages before returning

**Other parameters:**

* If a client does not reconnect within <timeout>, the subscription can be automatically discarded
* The number of messages queued for a particular subscription may be enforced, either by total message size or by number of outstanding messages.
* There is no subscription ID (at least in terms of client/server comms; the server can do whatever it wants to track subscriptions) - the subscription ID is implicit and is nominally a triple of user-id, channel URL, and selector.
