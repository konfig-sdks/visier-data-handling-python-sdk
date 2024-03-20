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


class UploadToInclude(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            tenantCode = schemas.StrSchema
            includeAll = schemas.BoolSchema
        
            @staticmethod
            def uploadTimes() -> typing.Type['UploadToIncludeUploadTimes']:
                return UploadToIncludeUploadTimes
            __annotations__ = {
                "tenantCode": tenantCode,
                "includeAll": includeAll,
                "uploadTimes": uploadTimes,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tenantCode"]) -> MetaOapg.properties.tenantCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["includeAll"]) -> MetaOapg.properties.includeAll: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uploadTimes"]) -> 'UploadToIncludeUploadTimes': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["tenantCode", "includeAll", "uploadTimes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tenantCode"]) -> typing.Union[MetaOapg.properties.tenantCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["includeAll"]) -> typing.Union[MetaOapg.properties.includeAll, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uploadTimes"]) -> typing.Union['UploadToIncludeUploadTimes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tenantCode", "includeAll", "uploadTimes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        tenantCode: typing.Union[MetaOapg.properties.tenantCode, str, schemas.Unset] = schemas.unset,
        includeAll: typing.Union[MetaOapg.properties.includeAll, bool, schemas.Unset] = schemas.unset,
        uploadTimes: typing.Union['UploadToIncludeUploadTimes', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UploadToInclude':
        return super().__new__(
            cls,
            *args,
            tenantCode=tenantCode,
            includeAll=includeAll,
            uploadTimes=uploadTimes,
            _configuration=_configuration,
            **kwargs,
        )

from visier_data_handling_python_sdk.model.upload_to_include_upload_times import UploadToIncludeUploadTimes
