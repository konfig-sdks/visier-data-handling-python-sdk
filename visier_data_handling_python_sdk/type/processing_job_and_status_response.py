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

from visier_data_handling_python_sdk.type.processing_job import ProcessingJob

class RequiredProcessingJobAndStatusResponse(TypedDict):
    pass

class OptionalProcessingJobAndStatusResponse(TypedDict, total=False):
    # The ID of the dispatching job that generated the extraction jobs.
    parentJobId: str

    # The tenant that owns the dispatching job. This is usually the administrating tenant.
    parentTenantCode: str

    # The number of processing jobs to return. The maximum number of jobs to return is 1000.
    limit: int

    # The index to start retrieving results from, also known as offset. The index begins at 0.
    start: int

    # A list of processing job information.
    processingJobs: typing.List[ProcessingJob]

class ProcessingJobAndStatusResponse(RequiredProcessingJobAndStatusResponse, OptionalProcessingJobAndStatusResponse):
    pass