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


class SalesforceAuthParamsDTO(BaseModel):
    refresh_token: typing.Optional[str] = Field(None, alias='refreshToken')

    client_id: typing.Optional[str] = Field(None, alias='clientId')
    class Config:
        arbitrary_types_allowed = True
