---
layout: flat
title: java-taxii | Getting Started
---

### Introduction
The java-taxii library is designed to aid developers writing programs that create and manipulate TAXII messages.
You should be familiar with TAXII before reading this document. The java-taxii library is built using JAXB to 
convert the TAXII XML schema documents into Java object representations. Some familiarity with JAXB will be helpful
in understanding the organization and usage of the library.

java-taxii provides classes to interact with TAXII service providers over HTTP/S. These classes use
Apache's HTTP Components library to establish the HTTP connection and transport the messages. Familiarity with
the Apache HTTP Components library, especially the CloseableHTTPClient class, will be helpful when using java-taxii.

### Installation
Download the java-taxii .jar and place it in your classpath.

#### Dependencies

* <a href="https://jaxb.java.net">Java XML Bind (JAXB) API</a>

    Provides the standard JAXB runtime environment.

* <a href="http://confluence.highsource.org/display/J2B/Home">JAXB2 Basics</a>
    
    This library provides extensions to the standard JAXB environment.

* <a href="http://saxon.sourceforge.net">Saxon XSLT processor</a>

    Provides Schematron validation support.

* <a href="http://hc.apache.org/httpcomponents-client-ga/index.html">Apache HTTP Components Client</a>

    Provides HTTP connection support.

All of these dependencies are available in the Maven Central repository. It is recommended that you use
a build environment that installs the required libraries from there.

java-taxii uses the Gradle build tool. Below is an example of importing the dependencies using Gradle:

    repositories {
        mavenCentral()
    }

    dependencies {
        compile 'javax.xml.bind:jaxb-api:2.2.+'
        compile 'org.jvnet.jaxb2_commons:jaxb2-basics-runtime:0.6.5'
        compile 'net.sf.saxon:Saxon-HE:9.5.1-5'
        compile 'org.apache.httpcomponents:httpclient:4.3.5'
        compile 'org.apache.httpcomponents:httpclient-cache:4.3.5'
        compile 'org.apache.httpcomponents:httpmime:4.3.5'
        compile 'org.apache.httpcomponents:fluent-hc:4.3.5'    
        compile files(lib/java-taxii.jar')
    }

### Sample Usage

#### Object Creation
The simplest usage of the library is to create TAXII message objects

    import org.mitre.taxii.messages.xml11.ObjectFactory;
    import org.mitre.taxii.messages.xml11.DiscoveryRequest;
    import org.mitre.taxii.messages.xml11.MessageHelper;

    ...
    ObjectFactory factory = new ObjectFactory();
    DiscoveryRequest request = factory.createDiscoveryRequest().withMessageId(MessageHelper.generateMessageId());

or 

    DiscoveryRequest dr = new DiscoveryRequest().withMessageId(MessageHelper.generateMessageId());

JAXB convention recommends the use of the ObjectFactory to create instances of the TAXII objects but it is not necessary.

#### Message Marshaling
Once a TAXII message object is created, the next step is to render it as XML. To do this, you need a JAXB context that
understands how to serialize or marshal the object to XML. This context is provided by a TaxiiXml object which is created
using a TaxiiXmlFactory. There is quite a bit of configuration work done by the TaxiiXmlFactory behind the scenes, so it should
always be used to create a properly configured TaxiiXml.

    import org.mitre.taxii.messages.xml11.TaxiiXmlFactory;
    import org.mitre.taxii.messages.xml11.TaxiiXml;
    import org.mitre.taxii.messages.xml11.ObjectFactory;
    import org.mitre.taxii.messages.xml11.DiscoveryRequest;
    import org.mitre.taxii.messages.xml11.MessageHelper;
    ...

    TaxiiXmlFactory txf = new TaxiiXmlFactory();
    TaxiiXml taxiiXml = txf.createTaxiiXml();

    ObjectFactory of = new ObjectFactory();
    DiscoveryRequest dr = of.createDiscoveryRequest().withMessageId(MessageHelper.generateMessageId());

    String xmlString = taxiiXml.marshalToString(dr, true);

#### Message Unmarshaling
To parse an XML string into an object representation is also done using a TaxiiXml object.

    import javax.xml.bind.Unmarshaller;
    import org.mitre.taxii.messages.xml11.TaxiiXmlFactory;
    import org.mitre.taxii.messages.xml11.TaxiiXml;
    ...

    String xml = "<Status_Message status_type='SUCCESS' in_response_to='urn:uuid:8fef148a-b186-45a0-a2da-9915daf621b1' "
                 +" message_id='SM02' xmlns='http://taxii.mitre.org/messages/taxii_xml_binding-1.1'/>";

    TaxiiXmlFactory txf = new TaxiiXmlFactory();
    TaxiiXml taxiiXml = txf.createTaxiiXml();

    Unmarshaller unmarshaller = taxiiXml.getJaxbContext().createUnmarshaller();

    StatusMessage message = (StatusMessage) unmarshaller.unmarshal(new StringReader(xml));

Notice that you need to know the type of the item being parsed beforehand. The Unmarshaller will return an Object which 
must be cast to the expected type.

#### Validation
Creating and unmarshaling TAXII items does not guarantee that they are schema or business rule valid. You could create an
object and not populate member objects that the schema requires. For example, a Status Message with status type of "PENDING"
is required to have a Status Detail with name "ESTIMATED_WAIT"; further, the value of the Status Detail must be a positive
integer. Those interrelations and constraints are not expressed in the schema but as Schematron rules.
