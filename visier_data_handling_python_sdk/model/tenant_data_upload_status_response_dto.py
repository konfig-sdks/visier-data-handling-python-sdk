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


class TenantDataUploadStatusResponseDTO(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            uploadTime = schemas.StrSchema
            included = schemas.BoolSchema
            __annotations__ = {
                "uploadTime": uploadTime,
                "included": included,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uploadTime"]) -> MetaOapg.properties.uploadTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["included"]) -> MetaOapg.properties.included: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["uploadTime", "included", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uploadTime"]) -> typing.Union[MetaOapg.properties.uploadTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["included"]) -> typing.Union[MetaOapg.properties.included, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["uploadTime", "included", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        uploadTime: typing.Union[MetaOapg.properties.uploadTime, str, schemas.Unset] = schemas.unset,
        included: typing.Union[MetaOapg.properties.included, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TenantDataUploadStatusResponseDTO':
        return super().__new__(
            cls,
            *args,
            uploadTime=uploadTime,
            included=included,
            _configuration=_configuration,
            **kwargs,
        )