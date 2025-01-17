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
from pydantic import BaseModel, Field, RootModel

from visier_data_handling_python_sdk.pydantic.subject_missing_access_dto import SubjectMissingAccessDTO

class CredentialCreationAPIResponseDTO(BaseModel):
    # The unique ID of the newly created credential.
    uuid: typing.Optional[str] = Field(None, alias='uuid')

    # The symbol name of the newly created credential.
    symbol_name: typing.Optional[str] = Field(None, alias='symbolName')

    # The object name of the newly created credential.
    object_name: typing.Optional[str] = Field(None, alias='objectName')

    # The properties that the credential cannot access despite successful authentication.  This is only returned for authentications that do not grant access to all data.
    missing_connection_properties: typing.Optional[typing.List[SubjectMissingAccessDTO]] = Field(None, alias='missingConnectionProperties')
    class Config:
        arbitrary_types_allowed = True
