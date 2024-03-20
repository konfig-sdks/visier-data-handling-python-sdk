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


class RequiredMySqlAuthParamsDTO(TypedDict):
    pass

class OptionalMySqlAuthParamsDTO(TypedDict, total=False):
    host: str

    port: str

    username: str

    password: str

    database: str

    sslMode: str

class MySqlAuthParamsDTO(RequiredMySqlAuthParamsDTO, OptionalMySqlAuthParamsDTO):
    pass
