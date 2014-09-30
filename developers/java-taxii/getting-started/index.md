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
