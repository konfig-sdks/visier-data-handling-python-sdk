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

from visier_data_handling_python_sdk.type.extractor_credential_apidto import ExtractorCredentialAPIDTO

class RequiredExtractorCredentialsAPIDTO(TypedDict):
    pass

class OptionalExtractorCredentialsAPIDTO(TypedDict, total=False):
    # A list of objects representing all the available connector credentials in Production.
    connectorCredentials: typing.List[ExtractorCredentialAPIDTO]

    # The number of connector credentials to return. The maximum number of data connector credentials to return is 1000.
    limit: int

    # The index to start retrieving values from, also known as offset. The index begins at 0.
    start: int

class ExtractorCredentialsAPIDTO(RequiredExtractorCredentialsAPIDTO, OptionalExtractorCredentialsAPIDTO):
    pass
