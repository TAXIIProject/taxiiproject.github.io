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
from stix.common.vocabs import VocabString
from stix.indicator import Indicator
from cybox.objects.file_object import File


def main():

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


if __name__ == '__main__':
    main()