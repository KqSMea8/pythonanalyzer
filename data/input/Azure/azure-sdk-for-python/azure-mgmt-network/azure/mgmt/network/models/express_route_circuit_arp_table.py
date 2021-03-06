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

from msrest.serialization import Model


class ExpressRouteCircuitArpTable(Model):
    """
    The arp table associated with the ExpressRouteCircuit

    :param age: Age.
    :type age: int
    :param interface: Interface.
    :type interface: str
    :param ip_address: Gets ipAddress.
    :type ip_address: str
    :param mac_address: Gets macAddress.
    :type mac_address: str
    """ 

    _attribute_map = {
        'age': {'key': 'age', 'type': 'int'},
        'interface': {'key': 'interface', 'type': 'str'},
        'ip_address': {'key': 'ipAddress', 'type': 'str'},
        'mac_address': {'key': 'macAddress', 'type': 'str'},
    }

    def __init__(self, age=None, interface=None, ip_address=None, mac_address=None):
        self.age = age
        self.interface = interface
        self.ip_address = ip_address
        self.mac_address = mac_address
