---
layout: flat
title: File Hash Reputation
use_cases:
    - Reputation
services:
    - Poll Service
summary: The File Hash Reputation TAXII Service Profile documents a File Hash Reputation Service in TAXII.
---

A File Hash Reputation service allows requesters to specify a File Hash and receive an assertion about that
File Hash's "badness" (or, more correctly, an assertion about the file with that File Hash). This example
uses TAXII Query to convey the request for information based on a File Hash, and uses STIX to represent the
result. All code examples use libtaxii and django-taxii-services, two publically available TAXII libraries.

## Requirements
These are the requirements to implement a File Hash Reputation Service as described in this TAXII Service Profile:

1. Implement a Poll Service that supports TAXII Default Query
1. Have a Data Collection named :code:`file_hash_reputation`

 1. This Data Collection is a Data Set (as opposed to a Data Feed)

3. Have a database that (nominally) contains the following information: 

 1. File Hash
 1. Badness (0-100)

4. Use STIX as the Targeting Expression Vocabulary

## Workflow
The workflow for this Service Profile is:

1. Receive a Poll Request with a TAXII Default Query
1. Check for various errors, including Targeting Expressions that are not explicitly permitted
1. Map the TAXII Default Query into a query for the application's database
1. Execute the query against the applications database
1. Map the database query result into STIX
1. Package up the STIX into a Poll Response and return it

### Step 1 - Receive a Poll Request
A Poll Request querying for a File Hash would look like this:

#### XML

#### Python

### Step 2 - Error Checking
This step does not attempt to define a robust error checking methodology. Rather,
this step merely reminds application developers of certain aspects that they might
want to check.

1. Protocol-level errors
1. Check Poll_Parameters/Content_Binding to see if a

### Step

## Building Block - Discovery Response
This section shows a Discovery Response advertising the File Hash Reputation Poll Service.

#### XML
{% highlight xml linenos %}
<taxii_11:Discovery_Response 
    xmlns:taxii="http://taxii.mitre.org/messages/taxii_xml_binding-1" 
    xmlns:taxii_11="http://taxii.mitre.org/messages/taxii_xml_binding-1.1" 
    xmlns:tdq="http://taxii.mitre.org/query/taxii_default_query-1" 
    message_id="25984" 
    in_response_to="1">
  <taxii_11:Service_Instance service_type="POLL" service_version="urn:taxii.mitre.org:services:1.1" available="true">
    <taxii_11:Protocol_Binding>urn:taxii.mitre.org:protocol:http:1.0</taxii_11:Protocol_Binding>
    <taxii_11:Address>http://example.com/poll-service/</taxii_11:Address>
    <taxii_11:Message_Binding>urn:taxii.mitre.org:message:xml:1.1</taxii_11:Message_Binding>
    <taxii_11:Supported_Query format_id="urn:taxii.mitre.org:query:default:1.0">
      <tdq:Default_Query_Info>
        <tdq:Targeting_Expression_Info targeting_expression_id="urn:stix.mitre.org:xml:1.1.1">
          <tdq:Preferred_Scope>**/Simple_Hash_Value</tdq:Preferred_Scope>
        </tdq:Targeting_Expression_Info>
        <tdq:Capability_Module>urn:taxii.mitre.org:query:capability:core-1</tdq:Capability_Module>
      </tdq:Default_Query_Info>
    </taxii_11:Supported_Query>
    <taxii_11:Message>This is a File Hash Reputation Poll Service</taxii_11:Message>
  </taxii_11:Service_Instance>
</taxii_11:Discovery_Response>
{% endhighlight %}
[Full XML](file-hash-rep-discovery-response.xml)

#### Python
{% highlight python linenos %}
request_id = '1'

discovery_response = tm11.DiscoveryResponse(
                                    message_id = generate_message_id(),
                                    in_response_to = request_id)

# Create a targeting expression info 
# indicating STIX XML 1.1.1 and that only 
# Hash Value targets are allowed
my_tei = tdq.TargetingExpressionInfo(CB_STIX_XML_111,
                                     preferred_scope=['**/Simple_Hash_Value'],
                                     allowed_scope=None)

my_supported_query = tdq.DefaultQueryInfo([my_tei], [CM_CORE])

si = tm11.ServiceInstance(
                service_type = SVC_POLL,
                services_version = VID_TAXII_SERVICES_11,
                protocol_binding = VID_TAXII_HTTP_10,
                service_address = 'http://example.com/poll-service/',
                message_bindings = [VID_TAXII_XML_11],
                available = True,
                message = 'This is a File Hash Reputation Poll Service',
                supported_query = [my_supported_query])

discovery_response.service_instances.append(si)

print discovery_response.to_xml(pretty_print=True)
{% endhighlight %}
[Full Python](file-hash-rep-discovery-response.py)

This section describes some simple building blocks for the TAXII Service

### Discovery Response (Nice-to-have)
A sample Discovery Response containing information about the Poll Service:


## Supporting Features
Some implementers will want to advertise their TAXII Capabilities through
the Discovery Service and/or Collection Management Service. The Supporting 
Features in this section are optional, but are documented for completeness.

TODO: TAXII Discovery Service advertising the Poll Service

TODO: Collection Information Response advertising the Data Set