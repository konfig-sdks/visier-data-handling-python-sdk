# coding: utf-8
"""
    Visier Data and Job Handling APIs

    Visier APIs for data and job handling

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

import typing
import inspect
from datetime import date, datetime
from visier_data_handling_python_sdk.client_custom import ClientCustom
from visier_data_handling_python_sdk.configuration import Configuration
from visier_data_handling_python_sdk.api_client import ApiClient
from visier_data_handling_python_sdk.type_util import copy_signature
from visier_data_handling_python_sdk.apis.tags.data_and_job_handling_api import DataAndJobHandlingApi



class VisierDataHandling(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.data_and_job_handling: DataAndJobHandlingApi = DataAndJobHandlingApi(api_client)
