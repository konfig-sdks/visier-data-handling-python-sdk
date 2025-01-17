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

from visier_data_handling_python_sdk.pydantic.data_provider_auth_params_dto import DataProviderAuthParamsDTO
from visier_data_handling_python_sdk.pydantic.data_provider_basic_information_dto import DataProviderBasicInformationDTO
from visier_data_handling_python_sdk.pydantic.data_provider_basic_metadata_dto import DataProviderBasicMetadataDTO

class DataProviderAuthInformationDTO(BaseModel):
    # The authentication information for the credential.
    data_provider_auth_params: typing.Optional[DataProviderAuthParamsDTO] = Field(None, alias='dataProviderAuthParams')

    # The display name and description for the credential.
    data_provider_basic_information: typing.Optional[DataProviderBasicInformationDTO] = Field(None, alias='dataProviderBasicInformation')

    data_provider_metadata: typing.Optional[DataProviderBasicMetadataDTO] = Field(None, alias='dataProviderMetadata')
    class Config:
        arbitrary_types_allowed = True
