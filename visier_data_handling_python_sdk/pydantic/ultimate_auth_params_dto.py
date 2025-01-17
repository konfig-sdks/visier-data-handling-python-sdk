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


class UltimateAuthParamsDTO(BaseModel):
    host_domain_name: typing.Optional[str] = Field(None, alias='hostDomainName')

    api_key: typing.Optional[str] = Field(None, alias='apiKey')

    username: typing.Optional[str] = Field(None, alias='username')

    password: typing.Optional[str] = Field(None, alias='password')

    user_access_key: typing.Optional[str] = Field(None, alias='userAccessKey')
    class Config:
        arbitrary_types_allowed = True
