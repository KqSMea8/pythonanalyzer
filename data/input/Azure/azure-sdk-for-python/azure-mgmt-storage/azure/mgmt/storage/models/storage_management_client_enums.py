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

from enum import Enum


class Reason(Enum):

    account_name_invalid = "AccountNameInvalid"
    already_exists = "AlreadyExists"


class AccountType(Enum):

    standard_lrs = "Standard_LRS"
    standard_zrs = "Standard_ZRS"
    standard_grs = "Standard_GRS"
    standard_ragrs = "Standard_RAGRS"
    premium_lrs = "Premium_LRS"


class ProvisioningState(Enum):

    creating = "Creating"
    resolving_dns = "ResolvingDNS"
    succeeded = "Succeeded"


class AccountStatus(Enum):

    available = "Available"
    unavailable = "Unavailable"


class UsageUnit(Enum):

    count = "Count"
    bytes = "Bytes"
    seconds = "Seconds"
    percent = "Percent"
    counts_per_second = "CountsPerSecond"
    bytes_per_second = "BytesPerSecond"
