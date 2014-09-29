#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
The following code requires libtaxii v1.1.103 or greater installed.
For installation instructions, please refer to http://libtaxii.readthedocs.org/en/latest/installation.html
'''

import libtaxii.taxii_default_query as tdq
import libtaxii.messages_11 as tm11
from libtaxii.common import generate_message_id
from libtaxii.constants import *

def main():
    discovery_response = tm11.DiscoveryResponse(message_id=generate_message_id(),
                                                in_response_to='1')

    # Create a targeting expression info
    # indicating STIX XML 1.1.1 and that only
    # Hash Value targets are allowed
    my_tei = tdq.TargetingExpressionInfo(CB_STIX_XML_111,
                                         preferred_scope=['**/Simple_Hash_Value'],
                                         allowed_scope=None)

    my_supported_query = tdq.DefaultQueryInfo([my_tei], [CM_CORE])

    si = tm11.ServiceInstance(service_type=SVC_POLL,
                              services_version=VID_TAXII_SERVICES_11,
                              protocol_binding=VID_TAXII_HTTP_10,
                              service_address='http://example.com/poll-service/',
                              message_bindings=[VID_TAXII_XML_11],
                              available=True,
                              message='This is a File Hash Reputation Poll Service',
                              supported_query=[my_supported_query])

    discovery_response.service_instances.append(si)

    print discovery_response.to_xml(pretty_print=True)

if __name__ == '__main__':
    main()