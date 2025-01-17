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

from visier_data_handling_python_sdk.type.upload_to_exclude_upload_times import UploadToExcludeUploadTimes

class RequiredUploadToExclude(TypedDict):
    pass

class OptionalUploadToExclude(TypedDict, total=False):
    # The tenant code of the analytic tenant you are excluding a data upload for.
    tenantCode: str

    # If \"true\", all data uploads are excluded for the analytic tenant.
    excludeAll: bool

    uploadTimes: UploadToExcludeUploadTimes

class UploadToExclude(RequiredUploadToExclude, OptionalUploadToExclude):
    pass
