# coding: utf-8

"""
    Visier Data and Job Handling APIs

    Visier APIs for data and job handling

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from visier_data_handling_python_sdk.type.multiple_tenant_data_versions_details_dto import MultipleTenantDataVersionsDetailsDTO

class RequiredMultipleTenantDataVersionsListDTO(TypedDict):
    pass

class OptionalMultipleTenantDataVersionsListDTO(TypedDict, total=False):
    # A list of analytic tenants and their latest enabled data versions.
    tenants: typing.List[MultipleTenantDataVersionsDetailsDTO]

    # The number of analytic tenants to retrieve. The maximum number to retrieve is 1000.
    limit: int

    # The index to start retrieving results from, also known as offset. The index begins at 0.
    start: int

class MultipleTenantDataVersionsListDTO(RequiredMultipleTenantDataVersionsListDTO, OptionalMultipleTenantDataVersionsListDTO):
    pass
