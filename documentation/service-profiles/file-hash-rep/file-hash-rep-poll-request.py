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

value = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
target = '**/Simple_Hash_Value'

def main():
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

if __name__ == '__main__':
    main()