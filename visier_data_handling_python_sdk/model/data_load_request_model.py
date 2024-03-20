# coding: utf-8

"""
    Visier Data and Job Handling APIs

    Visier APIs for data and job handling

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from visier_data_handling_python_sdk import schemas  # noqa: F401


class DataLoadRequestModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A form body key that contains a collection of key-value pairs.

 **Note:** The only supported key value is `files` and the value is a comma-separated list of file names.
 Example:
 `"files": "/path/to/file1.zip.gpg,/path/to/another/file.zip.gpg"`
    """


    class MetaOapg:
        
        @staticmethod
        def additional_properties() -> typing.Type['MapValue']:
            return MapValue
    
    def __getitem__(self, name: typing.Union[str, ]) -> 'MapValue':
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    def get_item_oapg(self, name: typing.Union[str, ]) -> 'MapValue':
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: 'MapValue',
    ) -> 'DataLoadRequestModel':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from visier_data_handling_python_sdk.model.map_value import MapValue
