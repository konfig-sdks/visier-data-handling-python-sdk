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

from visier_data_handling_python_sdk.type.connector import Connector

class RequiredAssignConnectorCredentialRequest(TypedDict):
    pass

class OptionalAssignConnectorCredentialRequest(TypedDict, total=False):
    # A list of objects representing the data connectors to be assigned with credentials.
    connectors: typing.List[Connector]

class AssignConnectorCredentialRequest(RequiredAssignConnectorCredentialRequest, OptionalAssignConnectorCredentialRequest):
    pass
