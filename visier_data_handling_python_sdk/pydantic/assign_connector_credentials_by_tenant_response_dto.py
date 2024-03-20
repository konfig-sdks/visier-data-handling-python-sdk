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

from visier_data_handling_python_sdk.pydantic.assign_connector_with_credentials_response_dto import AssignConnectorWithCredentialsResponseDTO

class AssignConnectorCredentialsByTenantResponseDTO(BaseModel):
    # The unique identifier associated with the tenant.
    tenant_code: typing.Optional[str] = Field(None, alias='tenantCode')

    # A list of objects representing the assigned credentials and connectors.
    connectors: typing.Optional[typing.List[AssignConnectorWithCredentialsResponseDTO]] = Field(None, alias='connectors')

    # The state of the credential assignment. Valid values are Succeed or Failed.
    status: typing.Optional[Literal["Unknown", "Succeed", "Failed"]] = Field(None, alias='status')

    message: typing.Optional[str] = Field(None, alias='message')
    class Config:
        arbitrary_types_allowed = True