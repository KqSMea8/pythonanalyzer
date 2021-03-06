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

from .resource import Resource


class VnetInfo(Resource):
    """
    VNETInfo contract. This contract is public and is a stripped down version
    of VNETInfoInternal

    :param id: Resource Id
    :type id: str
    :param name: Resource Name
    :type name: str
    :param kind: Kind of resource
    :type kind: str
    :param location: Resource Location
    :type location: str
    :param type: Resource type
    :type type: str
    :param tags: Resource tags
    :type tags: dict
    :param vnet_resource_id: The vnet resource id
    :type vnet_resource_id: str
    :param cert_thumbprint: The client certificate thumbprint
    :type cert_thumbprint: str
    :param cert_blob: A certificate file (.cer) blob containing the public
     key of the private key used to authenticate a
     Point-To-Site VPN connection.
    :type cert_blob: str
    :param routes: The routes that this virtual network connection uses.
    :type routes: list of :class:`VnetRoute <azure.mgmt.web.models.VnetRoute>`
    :param resync_required: Flag to determine if a resync is required
    :type resync_required: bool
    :param dns_servers: Dns servers to be used by this VNET. This should be a
     comma-separated list of IP addresses.
    :type dns_servers: str
    """ 

    _validation = {
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'vnet_resource_id': {'key': 'properties.vnetResourceId', 'type': 'str'},
        'cert_thumbprint': {'key': 'properties.certThumbprint', 'type': 'str'},
        'cert_blob': {'key': 'properties.certBlob', 'type': 'str'},
        'routes': {'key': 'properties.routes', 'type': '[VnetRoute]'},
        'resync_required': {'key': 'properties.resyncRequired', 'type': 'bool'},
        'dns_servers': {'key': 'properties.dnsServers', 'type': 'str'},
    }

    def __init__(self, location, id=None, name=None, kind=None, type=None, tags=None, vnet_resource_id=None, cert_thumbprint=None, cert_blob=None, routes=None, resync_required=None, dns_servers=None):
        super(VnetInfo, self).__init__(id=id, name=name, kind=kind, location=location, type=type, tags=tags)
        self.vnet_resource_id = vnet_resource_id
        self.cert_thumbprint = cert_thumbprint
        self.cert_blob = cert_blob
        self.routes = routes
        self.resync_required = resync_required
        self.dns_servers = dns_servers
