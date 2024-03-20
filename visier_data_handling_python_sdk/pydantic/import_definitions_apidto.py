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

from visier_data_handling_python_sdk.pydantic.import_definition_apidto import ImportDefinitionAPIDTO

class ImportDefinitionsAPIDTO(BaseModel):
    # A list of objects representing all the available data connectors in Production.
    data_connectors: typing.Optional[typing.List[ImportDefinitionAPIDTO]] = Field(None, alias='dataConnectors')

    # The number of data connectors to return. The maximum number of data connectors to return is 1000.
    limit: typing.Optional[int] = Field(None, alias='limit')

    # The index to start retrieving values from, also known as offset. The index begins at 0.
    start: typing.Optional[int] = Field(None, alias='start')
    class Config:
        arbitrary_types_allowed = True