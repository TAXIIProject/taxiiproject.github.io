#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
The following code requires libtaxii v1.1.103 or greater installed.
For installation instructions, please refer to http://libtaxii.readthedocs.org/en/latest/installation.html
'''

import libtaxii.messages_11 as tm11
from libtaxii.common import generate_message_id
from libtaxii.constants import *

from stix.core import STIXPackage, STIXHeader
from stix.common import InformationSource, Identity
from stix.indicator import Indicator
from stix.ttp import TTP
from stix.utils import set_id_namespace as stix_sin
from cybox.common import Hash
from cybox.objects.file_object import File
from cybox.utils import set_id_namespace as cybox_sin, Namespace


def main():

    # "hardcoded" values
    ns = "urn:example.com:marks_malware_metadata_mart"
    ns_alias = "m4"

    # Set the STIX ID Namespace
    stix_namespace = {ns: ns_alias}
    stix_sin(stix_namespace)

    # Set the CybOX ID Namespace
    cybox_namespace = Namespace(ns, ns_alias)
    cybox_sin(cybox_namespace)

    ttp_id = 'ttp-d539bb85-9363-4814-83c8-fa9975045686'
    ttp_timestamp = '2014-09-30T15:56:27.000000+00:00'

    # Fake database values
    md5_hash = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
    object_id = 'File-927731f2-cc2c-421c-a40e-dc6f4a6c75a4'
    observable_id = 'Observable-45e3e64c-8438-441e-bc49-51e417466e29'
    confidence = 'High'
    confidence_timestamp = '2014-09-29T14:32:00.000000'
    indicator_id = 'Indicator-54baefc1-4742-4b40-ba83-afd51115015b'
    indicator_timestamp = '2014-09-29T14:32:00.000000'

    # Code to create the STIX Package
    sp = STIXPackage()
    sp.stix_header = STIXHeader()
    sp.stix_header.title = "File Hash Reputation for %s" % md5_hash
    sp.stix_header.add_package_intent("Indicators - Malware Artifacts")
    sp.stix_header.information_source = InformationSource()
    sp.stix_header.information_source.identity = Identity()
    sp.stix_header.information_source.identity.name = "Mark's Malware Metadata Mart"

    file_hash = Hash(hash_value=md5_hash, type_='MD5', exact=True)
    file_hash.type_.condition = "Equals"

    file_obj = File()
    file_obj.id_ = (ns_alias + ':' + object_id)
    file_obj.add_hash(file_hash)

    indicator = Indicator(title="File Hash Reputation",
                          id_=(ns_alias + ':' + indicator_id),
                          timestamp=indicator_timestamp)
    indicator.indicator_type = "File Hash Reputation"
    indicator.add_observable(file_obj)
    indicator.observables[0].id_ = ns_alias + ':' + observable_id

    ttp = TTP()
    ttp.id_ = ns_alias + ':' + ttp_id
    ttp.timestamp = ttp_timestamp
    ttp.title = "Malicious File"

    indicator.add_indicated_ttp(TTP(idref=ttp.id_, timestamp=ttp.timestamp))
    indicator.indicated_ttps[0].confidence = confidence
    indicator.indicated_ttps[0].confidence.timestamp = confidence_timestamp

    sp.add_indicator(indicator)
    sp.add_ttp(ttp)

    stix_xml = sp.to_xml()

    poll_response = tm11.PollResponse(message_id=generate_message_id(),
                                      in_response_to="1234",
                                      collection_name='file_hash_reputation')
    cb = tm11.ContentBlock(content_binding=CB_STIX_XML_111,
                           content=stix_xml)
    poll_response.content_blocks.append(cb)
    print poll_response.to_xml(pretty_print=True)


if __name__ == '__main__':
    main()