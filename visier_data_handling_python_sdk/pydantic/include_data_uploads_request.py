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

from visier_data_handling_python_sdk.pydantic.upload_to_include_model import UploadToIncludeModel

class IncludeDataUploadsRequest(BaseModel):
    # A form body key that contains a collection of key-value pairs.
    model: typing.Optional[UploadToIncludeModel] = Field(None, alias='model')
    class Config:
        arbitrary_types_allowed = True
