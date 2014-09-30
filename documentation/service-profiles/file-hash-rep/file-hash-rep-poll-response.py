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
from cybox.common import Hash
from cybox.objects.file_object import File


def main():

    # "hardcoded" values
    ns = "urn:taxii.mitre.org:service_profile:file_hash_reputation"
    ns_alias = "file_hash_rep"

    # Fake database values
    md5_hash = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
    object_id = 'File-927731f2-cc2c-421c-a40e-dc6f4a6c75a4'
    object_timestamp = '2014-09-29T14:32:00.000000'
    observable_id = 'Observable-45e3e64c-8438-441e-bc49-51e417466e29'
    observable_timestamp = '2014-09-29T14:32:00.000000'
    confidence = 'High'
    confidence_timestamp = '2014-09-29T14:32:00.000000'
    indicator_id = 'Indicator-54baefc1-4742-4b40-ba83-afd51115015b'
    indicator_timestamp = '2014-09-29T14:32:00.000000'

    sp = STIXPackage()
    sp.stix_header = STIXHeader()
    sp.stix_header.title = "File Hash Reputation for %s" % md5_hash
    sp.stix_header.add_package_intent("Indicators - Malware Artifacts")
    sp.stix_header.information_source = InformationSource()
    sp.stix_header.information_source.identity = Identity()
    sp.stix_header.information_source.identity.name = "Mark's Malware Metadata Mart"

    file_hash = Hash(hash_value=md5_hash, type_='MD5', exact=True)

    file_obj = File(id_=(ns_alias + object_id), timestamp=object_timestamp)
    file_obj.add_hash(md5_hash)
    file_obj.hashes[0].type_.condition = "Equals"
    file_obj.hashes[0].simple_hash_value.condition = "Equals"

    indicator = Indicator(title="File Hash Reputation", id_=(ns_alias + indicator_id), timestamp=indicator_timestamp)
    indicator.indicator_type = "File Hash Reputation"
    indicator.add_observable(file_obj)
    indicator.observables[0].id_ = ns_alias + observable_id
    indicator.observables[0].timestamp = observable_timestamp

    ttp = TTP()
    ttp.title = "Malicious File"

    indicator.add_indicated_ttp(TTP(idref=ttp.id_))
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