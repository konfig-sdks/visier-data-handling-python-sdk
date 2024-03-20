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


class RequiredDataVersionObject(TypedDict):
    pass

class OptionalDataVersionObject(TypedDict, total=False):
    # The tenant code for the analytic tenant that you are disabling a data version.
    tenantCode: str

    # The data version to disable for a particular analytic tenant.
    dataVersions: str

class DataVersionObject(RequiredDataVersionObject, OptionalDataVersionObject):
    pass