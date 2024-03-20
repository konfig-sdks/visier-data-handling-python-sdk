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

from visier_data_handling_python_sdk.type.subject_missing_access_dto import SubjectMissingAccessDTO

class RequiredCredentialCreationAPIResponseDTO(TypedDict):
    pass

class OptionalCredentialCreationAPIResponseDTO(TypedDict, total=False):
    # The unique ID of the newly created credential.
    uuid: str

    # The symbol name of the newly created credential.
    symbolName: str

    # The object name of the newly created credential.
    objectName: str

    # The properties that the credential cannot access despite successful authentication.  This is only returned for authentications that do not grant access to all data.
    missingConnectionProperties: typing.List[SubjectMissingAccessDTO]

class CredentialCreationAPIResponseDTO(RequiredCredentialCreationAPIResponseDTO, OptionalCredentialCreationAPIResponseDTO):
    pass