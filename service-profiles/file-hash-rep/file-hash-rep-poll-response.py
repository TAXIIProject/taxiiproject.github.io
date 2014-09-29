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
from cybox.objects.file_object import File


def main():

    file_hash = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
    confidence = 'Low'  # High, Medium, Low, None, or Unknown

    sp = STIXPackage()
    sp.stix_header = STIXHeader()
    sp.stix_header.title = "File Hash Reputation for %s" % file_hash
    sp.stix_header.add_package_intent("Indicators - Malware Artifacts")
    sp.stix_header.information_source = InformationSource()
    sp.stix_header.information_source.identity = Identity()
    sp.stix_header.information_source.identity.name = "Mark's Malware Metadata Mart"

    file_obj = File()
    file_obj.add_hash(file_hash)
    file_obj.hashes[0].type_.condition = "Equals"
    file_obj.hashes[0].simple_hash_value.condition = "Equals"

    indicator = Indicator(title="File Hash Reputation")
    indicator.indicator_type = "File Hash Reputation"
    indicator.add_observable(file_obj)

    ttp = TTP()
    ttp.title = "Malicious File"

    indicator.add_indicated_ttp(TTP(idref=ttp.id_))
    indicator.indicated_ttps[0].confidence = confidence

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