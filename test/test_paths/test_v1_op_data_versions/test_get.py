# coding: utf-8

"""
    Visier Data and Job Handling APIs

    Visier APIs for data and job handling

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import visier_data_handling_python_sdk
from visier_data_handling_python_sdk.paths.v1_op_data_versions import get
from visier_data_handling_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestV1OpDataVersions(ApiTestMixin, unittest.TestCase):
    """
    V1OpDataVersions unit test stubs
        Retrieve the latest enabled data versions for all analytic tenants
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
