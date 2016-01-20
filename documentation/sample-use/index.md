---
title: Sample Use
layout: flat
tagline: Sample usage for TAXII
---

This page contains sample HTTP Request/Responses for TAXII. Note that these examples do not demonstrate the full spectrum of TAXII capabilities. Each type of TAXII Message is listed at least once. 

Please send any comments or questions to taxii@mitre.org.


## TAXII Services
A **TAXII Service** is a single unit of capability within TAXII. TAXII defines four TAXII Services:

* **Inbox Service** - Used by a TAXII Client to push information to a TAXII Server.
* **Poll Service** - Used by a TAXII Client to request information from a TAXII Server.
* **Collection Management Service** - Used by a TAXII Client to request information about available **Data Collections** or request a subscription.
* **Discovery Service** - Used by a TAXII Client to discover available TAXII Services (e.g., "An Inbox Service is located at http://example.com/inbox_service ").

## Data Collections
A TAXII **Data Collection** is a grouping of cyber threat information that can be exchanged using TAXII. 
Each TAXII Data Collection has a name that identifies it among Data Collections from an information producer. 
There are two types of TAXII Data Collections: TAXII **Data Feeds** and TAXII **Data Sets**.

A TAXII **Data Feed** is an ordered Data Collection. A TAXII Data Feed's organization allows specific 
portions of TAXII Data Feeds to be requested (e.g., "Give me all content since XYZ").

A TAXII **Data Set** is an unordered Data Collection.

## TAXII Clients and TAXII Servers; Information Producers and Information Consumers
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
 * The **TAXII Client** is an **Information Producer**.
 * The **TAXII Server** is an **Information Consumer**.
* Scenario: A **TAXII Client** connects to a **TAXII Server** to request information (TAXII Poll Service): 
 * The **TAXII Client** is an **Information Consumer**.
 * The **TAXII Server** is an **Information Producer**.


## TAXII 1.1 Discovery Service
### Sample TAXII 1.1 Discovery Request
```http
POST http://taxiitest.mitre.org/services/discovery/ HTTP/1.1
Host: taxiitest.mitre.org
Proxy-Connection: keep-alive
Content-Length: 97
X-TAXII-Content-Type: urn:taxii.mitre.org:message:xml:1.1
X-TAXII-Accept: urn:taxii.mitre.org:message:xml:1.1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36
Content-Type: application/xml
Accept: application/xml
Cache-Control: no-cache
X-TAXII-Services: urn:taxii.mitre.org:services:1.1
X-TAXII-Protocol: urn:taxii.mitre.org:protocol:http:1.0
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.8

<Discovery_Request xmlns="http://taxii.mitre.org/messages/taxii_xml_binding-1.1" message_id="1"/>
```

### Sample TAXII 1.1 Discovery Response
```http
HTTP/1.1 200 OK
Date: Fri, 19 Dec 2014 13:22:04 GMT
Server: Apache/2.2.15 (Red Hat)
X-TAXII-Protocol: urn:taxii.mitre.org:protocol:http:1.0
X-TAXII-Content-Type: urn:taxii.mitre.org:message:xml:1.1
X-TAXII-Services: urn:taxii.mitre.org:services:1.1
Content-Type: application/xml
Transfer-Encoding: chunked
Connection: keep-alive
Proxy-Connection: keep-alive

<taxii_11:Discovery_Response xmlns:taxii_11="http://taxii.mitre.org/messages/taxii_xml_binding-1.1"
    message_id="1466" in_response_to="1">
    <taxii_11:Service_Instance service_type="INBOX"
        service_version="urn:taxii.mitre.org:services:1.1" available="true">
        <taxii_11:Protocol_Binding>urn:taxii.mitre.org:protocol:http:1.0</taxii_11:Protocol_Binding>
        <taxii_11:Address>http://taxiitest.mitre.org/services/inbox/default</taxii_11:Address>
        <taxii_11:Message_Binding>urn:taxii.mitre.org:message:xml:1.1</taxii_11:Message_Binding>
        <taxii_11:Content_Binding binding_id="urn:stix.mitre.org:xml:1.0"/>
    </taxii_11:Service_Instance>
    <taxii_11:Service_Instance service_type="POLL"
        service_version="urn:taxii.mitre.org:services:1.1" available="true">
        <taxii_11:Protocol_Binding>urn:taxii.mitre.org:protocol:http:1.0</taxii_11:Protocol_Binding>
        <taxii_11:Address>http://taxiitest.mitre.org/services/poll</taxii_11:Address>
        <taxii_11:Message_Binding>urn:taxii.mitre.org:message:xml:1.1</taxii_11:Message_Binding>
    </taxii_11:Service_Instance>
    <taxii_11:Service_Instance service_type="DISCOVERY"
        service_version="urn:taxii.mitre.org:services:1.1" available="true">
        <taxii_11:Protocol_Binding>urn:taxii.mitre.org:protocol:http:1.0</taxii_11:Protocol_Binding>
        <taxii_11:Address>http://taxiitest.mitre.org/services/discovery</taxii_11:Address>
        <taxii_11:Message_Binding>urn:taxii.mitre.org:message:xml:1.1</taxii_11:Message_Binding>
    </taxii_11:Service_Instance>
</taxii_11:Discovery_Response>
```

## TAXII 1.1 Inbox Service
### Sample TAXII 1.1 Inbox Message
```http
POST http://taxiitest.mitre.org/services/inbox/default/ HTTP/1.1
Host: taxiitest.mitre.org
Proxy-Connection: keep-alive
Content-Length: 2702
X-TAXII-Content-Type: urn:taxii.mitre.org:message:xml:1.1
X-TAXII-Accept: urn:taxii.mitre.org:message:xml:1.1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36
Content-Type: application/xml
Accept: application/xml
Cache-Control: no-cache
X-TAXII-Services: urn:taxii.mitre.org:services:1.1
X-TAXII-Protocol: urn:taxii.mitre.org:protocol:http:1.0
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.8

<taxii_11:Inbox_Message xmlns:taxii="http://taxii.mitre.org/messages/taxii_xml_binding-1" xmlns:taxii_11="http://taxii.mitre.org/messages/taxii_xml_binding-1.1" xmlns:tdq="http://taxii.mitre.org/query/taxii_default_query-1" message_id="34502">
  <taxii_11:Content_Block>
    <taxii_11:Content_Binding binding_id="urn:stix.mitre.org:xml:1.1.1"/>
    <taxii_11:Content>
      <stix:STIX_Package xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:stix="http://stix.mitre.org/stix-1" xmlns:indicator="http://stix.mitre.org/Indicator-2" xmlns:cybox="http://cybox.mitre.org/cybox-2" xmlns:DomainNameObj="http://cybox.mitre.org/objects#DomainNameObject-1" xmlns:cyboxVocabs="http://cybox.mitre.org/default_vocabularies-2" xmlns:stixVocabs="http://stix.mitre.org/default_vocabularies-1" xmlns:example="http://example.com/" xsi:schemaLocation="http://stix.mitre.org/stix-1 ../stix_core.xsd     http://stix.mitre.org/Indicator-2 ../indicator.xsd     http://cybox.mitre.org/default_vocabularies-2 ../cybox/cybox_default_vocabularies.xsd     http://stix.mitre.org/default_vocabularies-1 ../stix_default_vocabularies.xsd     http://cybox.mitre.org/objects#DomainNameObject-1 ../cybox/objects/Domain_Name_Object.xsd" id="example:STIXPackage-f61cd874-494d-4194-a3e6-6b487dbb6d6e" timestamp="2014-05-08T09:00:00.000000Z" version="1.1.1">
    <stix:STIX_Header>
        <stix:Title>Example watchlist that contains domain information.</stix:Title>
        <stix:Package_Intent xsi:type="stixVocabs:PackageIntentVocab-1.0">Indicators - Watchlist</stix:Package_Intent>
    </stix:STIX_Header>
    <stix:Indicators>
        <stix:Indicator xsi:type="indicator:IndicatorType" id="example:Indicator-2e20c5b2-56fa-46cd-9662-8f199c69d2c9" timestamp="2014-05-08T09:00:00.000000Z">
            <indicator:Type xsi:type="stixVocabs:IndicatorTypeVocab-1.1">Domain Watchlist</indicator:Type>
            <indicator:Description>Sample domain Indicator for this watchlist</indicator:Description>
            <indicator:Observable id="example:Observable-87c9a5bb-d005-4b3e-8081-99f720fad62b">
                <cybox:Object id="example:Object-12c760ba-cd2c-4f5d-a37d-18212eac7928">
                    <cybox:Properties xsi:type="DomainNameObj:DomainNameObjectType" type="FQDN">
                        <DomainNameObj:Value condition="Equals" apply_condition="ANY">malicious1.example.com##comma##malicious2.example.com##comma##malicious3.example.com</DomainNameObj:Value>
                    </cybox:Properties>
                </cybox:Object>
            </indicator:Observable>
        </stix:Indicator>
    </stix:Indicators>
</stix:STIX_Package>
    </taxii_11:Content>
  </taxii_11:Content_Block>
</taxii_11:Inbox_Message>
```

### Sample TAXII 1.1 Status Message
```http
HTTP/1.1 200 OK
Date: Fri, 19 Dec 2014 13:22:04 GMT
Server: Apache/2.2.15 (Red Hat)
X-TAXII-Protocol: urn:taxii.mitre.org:protocol:http:1.0
X-TAXII-Content-Type: urn:taxii.mitre.org:message:xml:1.1
X-TAXII-Services: urn:taxii.mitre.org:services:1.1
Content-Type: application/xml
Transfer-Encoding: chunked
Connection: keep-alive
Proxy-Connection: keep-alive

<taxii_11:Status_Message xmlns:taxii_11="http://taxii.mitre.org/messages/taxii_xml_binding-1.1" message_id="42902" in_response_to="34502" status_type="SUCCESS"/>
```

## TAXII 1.1 Poll Service
### Sample TAXII 1.1 Poll Request
```http
POST http://taxiitest.mitre.org/services/poll/ HTTP/1.1
Host: taxiitest.mitre.org
Proxy-Connection: keep-alive
Content-Length: 2702
X-TAXII-Content-Type: urn:taxii.mitre.org:message:xml:1.1
X-TAXII-Accept: urn:taxii.mitre.org:message:xml:1.1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36
Content-Type: application/xml
Accept: application/xml
Cache-Control: no-cache
X-TAXII-Services: urn:taxii.mitre.org:services:1.1
X-TAXII-Protocol: urn:taxii.mitre.org:protocol:http:1.0
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.8

<taxii_11:Poll_Request 
    xmlns:taxii_11="http://taxii.mitre.org/messages/taxii_xml_binding-1.1"
    message_id="42158"
    collection_name="default">
    <taxii_11:Exclusive_Begin_Timestamp>2014-12-19T00:00:00Z</taxii_11:Exclusive_Begin_Timestamp>
    <taxii_11:Inclusive_End_Timestamp>2014-12-19T12:00:00Z</taxii_11:Inclusive_End_Timestamp>
    <taxii_11:Poll_Parameters allow_asynch="false">
        <taxii_11:Response_Type>FULL</taxii_11:Response_Type>
    </taxii_11:Poll_Parameters>
</taxii_11:Poll_Request>
```

### Sample TAXII 1.1 Poll Fulfillment Request
```http
POST http://taxiitest.mitre.org/services/poll/ HTTP/1.1
Host: taxiitest.mitre.org
Proxy-Connection: keep-alive
Content-Length: 2702
X-TAXII-Content-Type: urn:taxii.mitre.org:message:xml:1.1
X-TAXII-Accept: urn:taxii.mitre.org:message:xml:1.1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36
Content-Type: application/xml
Accept: application/xml
Cache-Control: no-cache
X-TAXII-Services: urn:taxii.mitre.org:services:1.1
X-TAXII-Protocol: urn:taxii.mitre.org:protocol:http:1.0
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.8

<taxii_11:Poll_Fulfillment xmlns:taxii_11="http://taxii.mitre.org/messages/taxii_xml_binding-1.1" message_id="83013" collection_name="default" result_id="29321" result_part_number="1"/>
```

### Sample TAXII 1.1 Poll Response
```http
HTTP/1.1 200 OK
Date: Fri, 19 Dec 2014 13:22:04 GMT
Server: Apache/2.2.15 (Red Hat)
X-TAXII-Protocol: urn:taxii.mitre.org:protocol:http:1.0
X-TAXII-Content-Type: urn:taxii.mitre.org:message:xml:1.1
X-TAXII-Services: urn:taxii.mitre.org:services:1.1
Content-Type: application/xml
Transfer-Encoding: chunked
Connection: keep-alive
Proxy-Connection: keep-alive

<taxii_11:Poll_Response xmlns:taxii_11="http://taxii.mitre.org/messages/taxii_xml_binding-1.1" 
    message_id="42158"  in_response_to="20079" 
    collection_name="default" more="false" result_part_number="1">
    <taxii_11:Inclusive_End_Timestamp>2014-12-19T12:00:00Z</taxii_11:Inclusive_End_Timestamp>
    <taxii_11:Record_Count partial_count="false">1</taxii_11:Record_Count>
    <taxii_11:Content_Block>
        <taxii_11:Content_Binding binding_id="urn:stix.mitre.org:xml:1.1.1"/>
        <taxii_11:Content>
            <stix:STIX_Package xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:stix="http://stix.mitre.org/stix-1" xmlns:indicator="http://stix.mitre.org/Indicator-2" xmlns:cybox="http://cybox.mitre.org/cybox-2" xmlns:DomainNameObj="http://cybox.mitre.org/objects#DomainNameObject-1" xmlns:cyboxVocabs="http://cybox.mitre.org/default_vocabularies-2" xmlns:stixVocabs="http://stix.mitre.org/default_vocabularies-1" xmlns:example="http://example.com/" xsi:schemaLocation="http://stix.mitre.org/stix-1 ../stix_core.xsd     http://stix.mitre.org/Indicator-2 ../indicator.xsd     http://cybox.mitre.org/default_vocabularies-2 ../cybox/cybox_default_vocabularies.xsd     http://stix.mitre.org/default_vocabularies-1 ../stix_default_vocabularies.xsd     http://cybox.mitre.org/objects#DomainNameObject-1 ../cybox/objects/Domain_Name_Object.xsd" id="example:STIXPackage-f61cd874-494d-4194-a3e6-6b487dbb6d6e" timestamp="2014-05-08T09:00:00.000000Z" version="1.1.1">
                <stix:STIX_Header>
                    <stix:Title>Example watchlist that contains domain information.</stix:Title>
                    <stix:Package_Intent xsi:type="stixVocabs:PackageIntentVocab-1.0">Indicators - Watchlist</stix:Package_Intent>
                </stix:STIX_Header>
                <stix:Indicators>
                    <stix:Indicator xsi:type="indicator:IndicatorType" id="example:Indicator-2e20c5b2-56fa-46cd-9662-8f199c69d2c9" timestamp="2014-05-08T09:00:00.000000Z">
                        <indicator:Type xsi:type="stixVocabs:IndicatorTypeVocab-1.1">Domain Watchlist</indicator:Type>
                        <indicator:Description>Sample domain Indicator for this watchlist</indicator:Description>
                        <indicator:Observable id="example:Observable-87c9a5bb-d005-4b3e-8081-99f720fad62b">
                            <cybox:Object id="example:Object-12c760ba-cd2c-4f5d-a37d-18212eac7928">
                                <cybox:Properties xsi:type="DomainNameObj:DomainNameObjectType" type="FQDN">
                                    <DomainNameObj:Value condition="Equals" apply_condition="ANY">malicious1.example.com##comma##malicious2.example.com##comma##malicious3.example.com</DomainNameObj:Value>
                                </cybox:Properties>
                            </cybox:Object>
                        </indicator:Observable>
                    </stix:Indicator>
                </stix:Indicators>
            </stix:STIX_Package>
        </taxii_11:Content>
    </taxii_11:Content_Block>
</taxii_11:Poll_Response>
```

## TAXII 1.1 Collection Management Service
### Sample TAXII 1.1 Collection Information Request
```http
POST http://taxiitest.mitre.org/services/collection-management/ HTTP/1.1
Host: taxiitest.mitre.org
Proxy-Connection: keep-alive
Content-Length: 2702
X-TAXII-Content-Type: urn:taxii.mitre.org:message:xml:1.1
X-TAXII-Accept: urn:taxii.mitre.org:message:xml:1.1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36
Content-Type: application/xml
Accept: application/xml
Cache-Control: no-cache
X-TAXII-Services: urn:taxii.mitre.org:services:1.1
X-TAXII-Protocol: urn:taxii.mitre.org:protocol:http:1.0
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.8

<taxii_11:Collection_Information_Request xmlns:taxii_11="http://taxii.mitre.org/messages/taxii_xml_binding-1.1"message_id="26300"/>
```

### Sample TAXII 1.1 Collection Subscription Management Request
```http
POST http://taxiitest.mitre.org/services/collection-management/ HTTP/1.1
Host: taxiitest.mitre.org
Proxy-Connection: keep-alive
Content-Length: 2702
X-TAXII-Content-Type: urn:taxii.mitre.org:message:xml:1.1
X-TAXII-Accept: urn:taxii.mitre.org:message:xml:1.1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36
Content-Type: application/xml
Accept: application/xml
Cache-Control: no-cache
X-TAXII-Services: urn:taxii.mitre.org:services:1.1
X-TAXII-Protocol: urn:taxii.mitre.org:protocol:http:1.0
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.8

<taxii_11:Subscription_Management_Request
    xmlns:taxii_11="http://taxii.mitre.org/messages/taxii_xml_binding-1.1" 
    message_id="96485"
    collection_name="default" 
    action="SUBSCRIBE">
    <taxii_11:Subscription_Parameters>
        <taxii_11:Response_Type>FULL</taxii_11:Response_Type>
    </taxii_11:Subscription_Parameters>
</taxii_11:Subscription_Management_Request>
```

### Sample TAXII 1.1 Collection Information Response
```http
HTTP/1.1 200 OK
Date: Fri, 19 Dec 2014 13:22:04 GMT
Server: Apache/2.2.15 (Red Hat)
X-TAXII-Protocol: urn:taxii.mitre.org:protocol:http:1.0
X-TAXII-Content-Type: urn:taxii.mitre.org:message:xml:1.1
X-TAXII-Services: urn:taxii.mitre.org:services:1.1
Content-Type: application/xml
Transfer-Encoding: chunked
Connection: keep-alive
Proxy-Connection: keep-alive

<taxii_11:Collection_Information_Response
    xmlns:taxii_11="http://taxii.mitre.org/messages/taxii_xml_binding-1.1"
    message_id="28663"
    in_response_to="26300">
    <taxii_11:Collection collection_name="default" collection_type="DATA_FEED" available="true">
        <taxii_11:Description/>
        <taxii_11:Polling_Service>
            <taxii_11:Protocol_Binding>urn:taxii.mitre.org:protocol:http:1.0</taxii_11:Protocol_Binding>
            <taxii_11:Address>/services/poll/</taxii_11:Address>
            <taxii_11:Message_Binding>urn:taxii.mitre.org:message:xml:1.1</taxii_11:Message_Binding>
        </taxii_11:Polling_Service>
        <taxii_11:Polling_Service>
            <taxii_11:Protocol_Binding>urn:taxii.mitre.org:protocol:https:1.0</taxii_11:Protocol_Binding>
            <taxii_11:Address>/services/poll/</taxii_11:Address>
            <taxii_11:Message_Binding>urn:taxii.mitre.org:message:xml:1.1</taxii_11:Message_Binding>
        </taxii_11:Polling_Service>
        <taxii_11:Subscription_Service>
            <taxii_11:Protocol_Binding>urn:taxii.mitre.org:protocol:http:1.0</taxii_11:Protocol_Binding>
            <taxii_11:Address>/services/collection-management/</taxii_11:Address>
            <taxii_11:Message_Binding>urn:taxii.mitre.org:message:xml:1.1</taxii_11:Message_Binding>
        </taxii_11:Subscription_Service>
        <taxii_11:Subscription_Service>
            <taxii_11:Protocol_Binding>urn:taxii.mitre.org:protocol:https:1.0</taxii_11:Protocol_Binding>
            <taxii_11:Address>/services/collection-management/</taxii_11:Address>
            <taxii_11:Message_Binding>urn:taxii.mitre.org:message:xml:1.1</taxii_11:Message_Binding>
        </taxii_11:Subscription_Service>
        <taxii_11:Receiving_Inbox_Service>
            <taxii_11:Protocol_Binding>urn:taxii.mitre.org:protocol:http:1.0</taxii_11:Protocol_Binding>
            <taxii_11:Address>/services/inbox/</taxii_11:Address>
            <taxii_11:Message_Binding>urn:taxii.mitre.org:message:xml:1.1</taxii_11:Message_Binding>
        </taxii_11:Receiving_Inbox_Service>
        <taxii_11:Receiving_Inbox_Service>
            <taxii_11:Protocol_Binding>urn:taxii.mitre.org:protocol:https:1.0</taxii_11:Protocol_Binding>
            <taxii_11:Address>/services/inbox/</taxii_11:Address>
            <taxii_11:Message_Binding>urn:taxii.mitre.org:message:xml:1.1</taxii_11:Message_Binding>
        </taxii_11:Receiving_Inbox_Service>
    </taxii_11:Collection>
</taxii_11:Collection_Information_Response>
```

### Sample TAXII 1.1 Collection Subscription Management Response
```http
HTTP/1.1 200 OK
Date: Fri, 19 Dec 2014 13:22:04 GMT
Server: Apache/2.2.15 (Red Hat)
X-TAXII-Protocol: urn:taxii.mitre.org:protocol:http:1.0
X-TAXII-Content-Type: urn:taxii.mitre.org:message:xml:1.1
X-TAXII-Services: urn:taxii.mitre.org:services:1.1
Content-Type: application/xml
Transfer-Encoding: chunked
Connection: keep-alive
Proxy-Connection: keep-alive

<taxii_11:Subscription_Management_Response 
    xmlns:taxii_11="http://taxii.mitre.org/messages/taxii_xml_binding-1.1"
    message_id="58469" in_response_to="96485" collection_name="default">
    <taxii_11:Subscription status="ACTIVE">
        <taxii_11:Subscription_ID>Subscription001</taxii_11:Subscription_ID>
    </taxii_11:Subscription>
</taxii_11:Subscription_Management_Response>
```
