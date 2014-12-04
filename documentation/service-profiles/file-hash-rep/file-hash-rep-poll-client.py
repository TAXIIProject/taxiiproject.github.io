#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
The following code requires libtaxii v1.1.103 or greater installed.
For installation instructions, please refer to http://libtaxii.readthedocs.org/en/latest/installation.html
'''

import libtaxii.taxii_default_query as tdq
import libtaxii.messages_11 as tm11
import libtaxii.clients as tc
from libtaxii.common import generate_message_id
from libtaxii.constants import *

poll_request = None  # This value is "from" file-hash-rep-poll-request.py


def main():
    client = tc.HttpClient()
    client.set_use_https(True)
    client.set_auth_type(tc.HttpClient.AUTH_CERT)
    response = client.call_taxii_service2(host='HOSTNAME',
                                          path='/path/to/service',
                                          message_binding=VID_TAXII_XML_11,
                                          post_data=request_message.to_xml(pretty_print=True),
                                          port=args.port)
    response_message = t.get_message_from_http_response(response, 0)
    print response_message.to_xml(pretty_print=True)


if __name__ == '__main__':
    main()
