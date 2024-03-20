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

from visier_data_handling_python_sdk.pydantic.connector import Connector

class AssignConnectorCredentialRequest(BaseModel):
    # A list of objects representing the data connectors to be assigned with credentials.
    connectors: typing.Optional[typing.List[Connector]] = Field(None, alias='connectors')
    class Config:
        arbitrary_types_allowed = True
