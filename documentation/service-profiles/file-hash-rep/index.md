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
File Hash's "badness" - how likely the file identified by that File Hash will contain malware. This example
uses TAXII Query to convey the request for information based on a File Hash, and uses STIX to represent the
result. All code examples use [libtaxii](https://pypi.python.org/pypi/libtaxii/) and 
[python-stix](https://pypi.python.org/pypi/stix/), two publicly available libraries.

This TAXII Service Profile demonstrates the production and consumption of TAXII Messages, as well as the 
creation of STIX content. This TAXII Service Profile does not demonstrate transmitting TAXII Messages across 
 a network (that documentation can be found [here](TBD)).

## Requirements
These are the requirements to implement a File Hash Reputation Service as described in this TAXII Service Profile:

1. Implement a Poll Service that supports TAXII Default Query
1. Have a Data Collection named :code:`file_hash_reputation`

 1. This Data Collection is a Data Set (as opposed to a Data Feed)

3. Have a database that (nominally) contains the following information: 

 1. File Hash
 1. Badness (0-100; 100 is *REALLY BAD*)

4. Use STIX as the Targeting Expression Vocabulary

For the sake of example, we'll assume that the table containing File Hash and Badness is
a SQL Table that looks like the table below. The table is named :code:`file_hash_badness` and 
has an index on md5_hash.


| md5_hash                             | badness |
|--------------------------------------|---------|
| AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA     | 0       |
| BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB     | 50      |
| CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC     | 100     |


## Workflow
The workflow for this Service Profile is:

1. [**Discovery:**](#1) The querying party discovers the query provider's capabilities 
1. [**Poll Request:**](#2) The querying party sends a Poll Request with a TAXII Default Query
1. [**Inbound Mapping:**](#3) The query provider maps the TAXII Default Query into a query for the application's database
1. [**Database Query:**](#4) The query provider executes the query against the applications database
1. [**Outbound Mapping:**](#5) The query provider maps the database result set into STIX
1. [**Poll Response:**](#6) The query provider packages up the STIX into a Poll Response and return it

### <a name="1"></a>Step 1 - Discovery ###
In this step, the party that will be issuing the File Hash Reputation Query discovers
the query provider's capabilities by accessing the query provider's Discovery Service.

#### Discovery Request - XML
{% highlight xml linenos %}
<taxii_11:Discovery_Request  
    xmlns:taxii_11="http://taxii.mitre.org/messages/taxii_xml_binding-1.1" 
    message_id="1"/>
{% endhighlight %}
[XML Source](file-hash-rep-discovery-request.xml)

#### Discovery Request - Python
{% highlight python linenos %}
import libtaxii.messages_11 as tm11
dr = tm11.DiscoveryRequest(message_id="1")
print dr.to_xml(pretty_print=True)
{% endhighlight %}
[Python Source](file-hash-rep-discovery-request.py)

Upon receiving the Discovery Request, a Discovery Response is provided.

#### Discovery Response - XML
{% highlight xml linenos %}
<taxii_11:Discovery_Response 
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
[XML Source](file-hash-rep-discovery-response.xml)

#### Discovery Response - Python
{% highlight python linenos %}
discovery_response = tm11.DiscoveryResponse(message_id = generate_message_id(),
                                            in_response_to = '1')

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
[Python Source](file-hash-rep-discovery-response.py)

### <a name="2"></a>Step 2 - Poll Request
The party querying on a file hash, having learned the query provider's supported TAXII
 efault Query scopes, issues a Poll Request with a query. 
#### Poll Request - XML
{% highlight xml linenos %}
<taxii_11:Poll_Request
        xmlns:taxii_11="http://taxii.mitre.org/messages/taxii_xml_binding-1.1"
        xmlns:tdq="http://taxii.mitre.org/query/taxii_default_query-1"
        message_id="55134" collection_name="file_hash_reputation">
  <taxii_11:Poll_Parameters allow_asynch="false">
    <taxii_11:Response_Type>FULL</taxii_11:Response_Type>
    <taxii_11:Content_Binding binding_id="urn:stix.mitre.org:xml:1.1.1"/>
    <taxii_11:Query format_id="urn:taxii.mitre.org:query:default:1.0">
      <tdq:Default_Query targeting_expression_id="urn:stix.mitre.org:xml:1.1.1">
        <tdq:Criteria operator="AND">
          <tdq:Criterion negate="false">
            <tdq:Target>**/Simple_Hash_Value</tdq:Target>
            <tdq:Test capability_id="urn:taxii.mitre.org:query:capability:core-1" relationship="equals">
              <tdq:Parameter name="match_type">case_insensitive_string</tdq:Parameter>
              <tdq:Parameter name="value">AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA</tdq:Parameter>
            </tdq:Test>
          </tdq:Criterion>
        </tdq:Criteria>
      </tdq:Default_Query>
    </taxii_11:Query>
  </taxii_11:Poll_Parameters>
</taxii_11:Poll_Request>
{% endhighlight %}
[XML Source](file-hash-rep-poll-request.xml)

#### Poll Request - Python
{% highlight python linenos %}
import libtaxii.taxii_default_query as tdq
import libtaxii.messages_11 as tm11
from libtaxii.common import generate_message_id
from libtaxii.constants import *

value = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
target = '**/Simple_Hash_Value'

# Create the test portion of the query
my_test = tdq.Test(capability_id = CM_CORE,
                   relationship = R_EQUALS,
                   parameters = {P_VALUE: value,
                                 P_MATCH_TYPE: 'case_insensitive_string'}
                   )

#Put the test into a Criterion
my_criterion = tdq.Criterion(target=target, test=my_test)

# Put the Criterion into a Criteria
my_criteria = tdq.Criteria(operator=OP_AND,
                           criterion=[my_criterion], 
                           criteria=None)

# Create a query with the criteria
my_query = tdq.DefaultQuery(CB_STIX_XML_111, my_criteria)

# Create a Poll Parameters that indicates
# Only STIX 1.1.1 is accepted in response
# and with the query created previously
params = tm11.PollParameters(
                content_bindings = [tm11.ContentBinding(CB_STIX_XML_111)],
                query = my_query)

poll_request = tm11.PollRequest(
                    message_id = generate_message_id(),
                    collection_name = 'file_hash_reputation',
                    poll_parameters = params)

print poll_request.to_xml(pretty_print = True)
{% endhighlight %}
[Python Source](file-hash-rep-poll-request.py)


### <a name="3"></a>Step 3 - Inbound Mapping
The inbound mapping step is specific to each implementation's back end, requirements, and
other factors. While this TAXII Service Profile describes an inbound mapping for the database
table described above, implementers will likely make different choices based on factors
specific to their use case.

The **\*\*/SimpleHash** query is mapped to the database column **md5_hash**. As a result
The TAXII Query from the above Poll Request can be mapped into the following SQL
Query: :code:`select md5_hash, badness from file_hash_badness where md5_hash = '<value>'`
(Recall that the equals operator in SQL is case insensitive).

One important thing to note is that the inbound mapping is not a dynamic, or "runtime" operation. Instead,
the mapping of a TAXII Query to backend storage happens when the code is built. In the case of this TAXII
Service Profile, there is a one-to-one mapping between a TAXII Query scope and backend field. Other implementations
may support more complex operations.

### <a name="4"></a>Step 4 - Database Query
The inbound mapping is applied to the received TAXII Query, resulting in this SQL Statement:
:code:`select md5_hash, badness from file_hash_badness where md5_hash = 'AAA'`. Note: Use prepared statements!

Upon executing the query against the database, the following SQL result set is returned:

| md5_hash                             | badness |
|--------------------------------------|---------|
| AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA     | 0       |


This result set is used in the Outbound Mapping to generate the STIX response.

### <a name="5"></a>Step 5 - Outbound Mapping

This is best covered by the (TBD) File Hash Reputation STIX Idiom. A link
to the idiom will be added when that idiom is created.

### <a name="6"></a>Step 6 - Poll Response

#### Poll Response - XML
{% highlight xml linenos %}
<taxii_11:Poll_Response
    xmlns:taxii_11="http://taxii.mitre.org/messages/taxii_xml_binding-1.1"
    in_response_to="1234" collection_name="file_hash_reputation" more="false" result_part_number="1">
    <taxii_11:Content_Block>
        <taxii_11:Content_Binding binding_id="urn:stix.mitre.org:xml:1.1.1"/>
        <taxii_11:Content>
            <stix:STIX_Package xmlns:cyboxCommon="http://cybox.mitre.org/common-2"
                xmlns:cybox="http://cybox.mitre.org/cybox-2"
                xmlns:cyboxVocabs="http://cybox.mitre.org/default_vocabularies-2"
                xmlns:FileObj="http://cybox.mitre.org/objects#FileObject-2"
                xmlns:example="http://example.com" xmlns:incident="http://stix.mitre.org/Incident-1"
                xmlns:indicator="http://stix.mitre.org/Indicator-2"
                xmlns:stixCommon="http://stix.mitre.org/common-1"
                xmlns:stixVocabs="http://stix.mitre.org/default_vocabularies-1"
                xmlns:stix="http://stix.mitre.org/stix-1"
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                xsi:schemaLocation="  http://cybox.mitre.org/common-2 http://cybox.mitre.org/XMLSchema/common/2.1/cybox_common.xsd  http://cybox.mitre.org/cybox-2 http://cybox.mitre.org/XMLSchema/core/2.1/cybox_core.xsd  http://cybox.mitre.org/default_vocabularies-2 http://cybox.mitre.org/XMLSchema/default_vocabularies/2.1/cybox_default_vocabularies.xsd  http://cybox.mitre.org/objects#FileObject-2 http://cybox.mitre.org/XMLSchema/objects/File/2.1/File_Object.xsd  http://stix.mitre.org/Incident-1 http://stix.mitre.org/XMLSchema/incident/1.1.1/incident.xsd  http://stix.mitre.org/Indicator-2 http://stix.mitre.org/XMLSchema/indicator/2.1.1/indicator.xsd  http://stix.mitre.org/common-1 http://stix.mitre.org/XMLSchema/common/1.1.1/stix_common.xsd  http://stix.mitre.org/default_vocabularies-1 http://stix.mitre.org/XMLSchema/default_vocabularies/1.1.1/stix_default_vocabularies.xsd  http://stix.mitre.org/stix-1 http://stix.mitre.org/XMLSchema/core/1.1.1/stix_core.xsd"
                id="example:Package-177636e2-5bda-45b1-a93c-666f716c875c" version="1.1.1"
                timestamp="2014-09-23T13:08:42.185000+00:00">
                <stix:STIX_Header>
                    <stix:Title>File Hash Reputation for AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA</stix:Title>
                    <stix:Package_Intent xsi:type="stixVocabs:PackageIntentVocab-1.0">Indicators - Malware Artifacts</stix:Package_Intent>
                    <stix:Information_Source>
                        <stixCommon:Identity
                            id="example:Identity-5554612a-ae33-4ce8-8819-5541b30a0c99">
                            <stixCommon:Name>TAXII Service Profile: File Hash Reputation</stixCommon:Name>
                        </stixCommon:Identity>
                    </stix:Information_Source>
                </stix:STIX_Header>
                <stix:Indicators>
                    <stix:Indicator id="example:indicator-4010e0d1-9e9f-4442-aff9-74d45551d005"
                        timestamp="2014-09-23T13:08:42.185000+00:00"
                        xsi:type="indicator:IndicatorType" negate="false" version="2.1.1">
                        <indicator:Title>File Hash Reputation</indicator:Title>
                        <indicator:Observable
                            id="example:Observable-f2b84d35-c2ae-4358-8b3a-a279ae08f037">
                            <cybox:Object id="example:File-ce81a436-5db4-4867-9fb8-0a069cd2f3e5">
                                <cybox:Properties xsi:type="FileObj:FileObjectType">
                                    <FileObj:Hashes>
                                        <cyboxCommon:Hash>
                                            <cyboxCommon:Type
                                                xsi:type="cyboxVocabs:HashNameVocab-1.0"
                                                >MD5</cyboxCommon:Type>
                                            <cyboxCommon:Simple_Hash_Value condition="Equals"
                                                >AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA</cyboxCommon:Simple_Hash_Value>
                                        </cyboxCommon:Hash>
                                    </FileObj:Hashes>
                                </cybox:Properties>
                            </cybox:Object>
                        </indicator:Observable>
                        <indicator:Likely_Impact timestamp="2014-09-23T13:08:42.185000+00:00">
                            <stixCommon:Value
                                vocab_reference="http://en.wikipedia.org/wiki/Percentage"
                                vocab_name="percentage">100</stixCommon:Value>
                        </indicator:Likely_Impact>
                    </stix:Indicator>
                </stix:Indicators>
            </stix:STIX_Package>
        </taxii_11:Content>
    </taxii_11:Content_Block>
</taxii_11:Poll_Response>
{% endhighlight %}
[XML Source](file-hash-rep-poll-response.xml)

#### Poll Response - Python

{% highlight python linenos %}
import libtaxii.messages_11 as tm11
from libtaxii.common import generate_message_id
from libtaxii.constants import *

from stix.core import STIXPackage, STIXHeader
from stix.common import InformationSource, Identity
from stix.common.vocabs import VocabString
from stix.indicator import Indicator
from cybox.objects.file_object import File

file_hash = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
badness = 0 # Value between 0-100, or None if the badness is unknown

sp = STIXPackage()
sp.stix_header = STIXHeader()
sp.stix_header.title = "File Hash Reputation for %s" % file_hash
sp.stix_header.add_package_intent("Indicators - Malware Artifacts")
sp.stix_header.information_source = InformationSource()
sp.stix_header.information_source.identity = Identity()
sp.stix_header.information_source.identity.name = "TAXII Service Profile: File Hash Reputation"

file_obj = File()
file_obj.add_hash(file_hash)
file_obj.hashes[0].simple_hash_value.condition = "Equals"

indicator = Indicator(title="File Hash Reputation")
indicator.indicator_type = "File Hash Reputation"
indicator.add_observable(file_obj)
if badness is None:
    indicator.likely_impact = "Unknown"
else:
    vs = VocabString(str(badness))
    vs.vocab_name = 'percentage'
    vs.vocab_reference = "http://en.wikipedia.org/wiki/Percentage"
    indicator.likely_impact = vs

sp.add_indicator(indicator)

stix_xml = sp.to_xml()

poll_response = tm11.PollResponse(message_id=generate_message_id(),
                                  in_response_to="1234",
                                  collection_name='file_hash_reputation')
cb = tm11.ContentBlock(content_binding=CB_STIX_XML_111,
                       content=stix_xml)
poll_response.content_blocks.append(cb)
print poll_response.to_xml(pretty_print=True)
{% endhighlight %}
[Python Source](file-hash-rep-poll-response.py)

### Conclusion
Hopefully that helps!

This is brand new documentation. If there is something missing, something that could be 
explained better, or something you'd like to see added, please send a message to 
 taxii@mitre.org and we'll be happy to hear you're feedback!