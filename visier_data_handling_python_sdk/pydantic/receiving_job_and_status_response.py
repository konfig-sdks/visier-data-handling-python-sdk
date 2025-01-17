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

from visier_data_handling_python_sdk.pydantic.receiving_job import ReceivingJob

class ReceivingJobAndStatusResponse(BaseModel):
    # The ID of the dispatching job that generated the extraction jobs.
    parent_job_id: typing.Optional[str] = Field(None, alias='parentJobId')

    # The tenant that owns the dispatching job. This is usually the administrating tenant.
    parent_tenant_code: typing.Optional[str] = Field(None, alias='parentTenantCode')

    # The number of receiving jobs to return. The maximum number of jobs to return is 1000.
    limit: typing.Optional[int] = Field(None, alias='limit')

    # The index to start retrieving results from, also known as offset. The index begins at 0.
    start: typing.Optional[int] = Field(None, alias='start')

    # A list of receiving job information.
    receiving_jobs: typing.Optional[typing.List[ReceivingJob]] = Field(None, alias='receivingJobs')
    class Config:
        arbitrary_types_allowed = True
