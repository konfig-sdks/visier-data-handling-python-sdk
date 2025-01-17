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


class TenantDataUploadUpdateStatusResponseDTO(BaseModel):
    # The analytic tenant that the exclusion operation was conducted for.
    tenant_code: typing.Optional[str] = Field(None, alias='tenantCode')

    # The upload time of the data upload
    upload_time: typing.Optional[str] = Field(None, alias='uploadTime')

    # The outcome of the exclusion operation.
    status: typing.Optional[str] = Field(None, alias='status')

    # If applicable, the message explains why errors were encountered during the exclusion operation.
    message: typing.Optional[str] = Field(None, alias='message')
    class Config:
        arbitrary_types_allowed = True
