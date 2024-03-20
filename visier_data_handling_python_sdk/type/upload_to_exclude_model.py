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

from visier_data_handling_python_sdk.type.upload_to_exclude import UploadToExclude

class RequiredUploadToExcludeModel(TypedDict):
    pass

class OptionalUploadToExcludeModel(TypedDict, total=False):
    # A list of objects representing the data uploads to exclude for a particular analytic tenant.
    uploads: typing.List[UploadToExclude]

class UploadToExcludeModel(RequiredUploadToExcludeModel, OptionalUploadToExcludeModel):
    pass