# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
The following code requires libtaxii v1.1.103 or greater installed.
For installation instructions, please refer to http://libtaxii.readthedocs.org/en/latest/installation.html
'''

import libtaxii.messages_11 as tm11
from libtaxii.constants import *
from stix.core import STIXPackage
from StringIO import StringIO


def get_indicated_ttp(stix_package, ttp_id):
    """

    :param stix_package: The STIX Package to search
    :param ttp_id: The ID of the TTP to look for
    :return: a TTP if found, None otherwise
    """
    for ttp in stix_package.ttps:
        if ttp.id_ == ttp_id:
            return ttp

    return None

def get_first_matching_indicator(stix_package, hash_, hash_type):
    """

    :param stix_package: The STIX package to search
    :param hash_: The hash value to look for
    :param hash_type: The type of hash (e.g., MD5)
    :return: Returns an indicator with the given hash_ and hash_type, or None
    """

    for indicator in stix_package.indicators:
        hash_list = indicator.observable.object_.properties.hashes
        for h in hash_list:
            print h.simple_hash_value
            print h.type_
            print hash_
            print hash_type
            if h.simple_hash_value == hash_ and h.type_ == hash_type:
                return indicator

    return None

def get_first_parseable_indicated_ttp(indicator):
    """

    Only certain indicated TTPs are parseable by this script. This
    function returns the first instance of a parseable TTP.

    :param indicator: The indicator to search
    :return: An indicated or None
    """

    for indicated_ttp in indicator.indicated_ttps:
        if indicated_ttp.confidence.value._xsi_type_ == 'stixVocabs:HighMediumLowVocab-1.0':
            return indicated_ttp

    return None


def main():
    poll_response = 'file-hash-rep-poll-response.xml'
    f = open(poll_response, 'r')
    msg = tm11.get_message_from_xml(f.read())

    requested_hash = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
    requested_hash_type = 'MD5'

    #Iterate over the content blocks
    for content_block in msg.content_blocks:
        if content_block.content_binding.binding_id != CB_STIX_XML_111:
            raise ValueError('Something other than STIX 1.1.1 was attempted!')

        # Deserialize the STIX_Package
        stix_package = STIXPackage.from_xml(StringIO(content_block.content))
        indicator = get_first_matching_indicator(stix_package, requested_hash, requested_hash_type)
        indicated_ttp = get_first_parseable_indicated_ttp(indicator)
        confidence = indicated_ttp.confidence.value
        ttp = get_indicated_ttp(stix_package, indicated_ttp.id_)
        if ttp.title != 'Malicious File':
            raise ValueError('Don\'t know how to handle that TTP')


        if confidence in ('High','Medium'):
            print "DO NOT OPEN THE FILE"
        elif confidence in ('Low', 'Unknown'):
            print "THINK TWICE ABOUT OPENING THE FILE"
        elif confidence in ('None', ):
            print "Go ahead!"
        else:
            raise ValueError("Unknown confidence: %s!" % confidence)


if __name__ == '__main__':
    main()