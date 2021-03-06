# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .sub_resource import SubResource


class Route(SubResource):
    """
    Route resource

    :param id: Resource Id
    :type id: str
    :param address_prefix: Gets or sets the destination CIDR to which the
     route applies.
    :type address_prefix: str
    :param next_hop_type: Gets or sets the type of Azure hop the packet
     should be sent to. Possible values include: 'VirtualNetworkGateway',
     'VnetLocal', 'Internet', 'VirtualAppliance', 'None'
    :type next_hop_type: str
    :param next_hop_ip_address: Gets or sets the IP address packets should be
     forwarded to. Next hop values are only allowed in routes where the next
     hop type is VirtualAppliance.
    :type next_hop_ip_address: str
    :param provisioning_state: Gets or sets Provisioning state of the
     resource Updating/Deleting/Failed
    :type provisioning_state: str
    :param name: Gets name of the resource that is unique within a resource
     group. This name can be used to access the resource
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated
    :type etag: str
    """ 

    _validation = {
        'next_hop_type': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'address_prefix': {'key': 'properties.addressPrefix', 'type': 'str'},
        'next_hop_type': {'key': 'properties.nextHopType', 'type': 'RouteNextHopType'},
        'next_hop_ip_address': {'key': 'properties.nextHopIpAddress', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, next_hop_type, id=None, address_prefix=None, next_hop_ip_address=None, provisioning_state=None, name=None, etag=None):
        super(Route, self).__init__(id=id)
        self.address_prefix = address_prefix
        self.next_hop_type = next_hop_type
        self.next_hop_ip_address = next_hop_ip_address
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag
