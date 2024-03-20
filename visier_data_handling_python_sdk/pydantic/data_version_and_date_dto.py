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


class DataVersionAndDateDTO(BaseModel):
    # The data version ID.
    data_version: typing.Optional[str] = Field(None, alias='dataVersion')

    # The date that the data version was created.
    data_version_date: typing.Optional[str] = Field(None, alias='dataVersionDate')
    class Config:
        arbitrary_types_allowed = True
