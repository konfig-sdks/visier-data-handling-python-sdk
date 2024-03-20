import typing_extensions

from visier_data_handling_python_sdk.apis.tags import TagValues
from visier_data_handling_python_sdk.apis.tags.data_and_job_handling_api import DataAndJobHandlingApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DATA_AND_JOB_HANDLING: DataAndJobHandlingApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DATA_AND_JOB_HANDLING: DataAndJobHandlingApi,
    }
)
