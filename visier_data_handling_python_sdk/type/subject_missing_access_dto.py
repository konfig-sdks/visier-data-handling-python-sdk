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

from visier_data_handling_python_sdk.type.subject_missing_access_dto_attributes import SubjectMissingAccessDTOAttributes

class RequiredSubjectMissingAccessDTO(TypedDict):
    pass

class OptionalSubjectMissingAccessDTO(TypedDict, total=False):
    # The subjects that cannot be accessed.
    subject: str

    attributes: SubjectMissingAccessDTOAttributes

class SubjectMissingAccessDTO(RequiredSubjectMissingAccessDTO, OptionalSubjectMissingAccessDTO):
    pass