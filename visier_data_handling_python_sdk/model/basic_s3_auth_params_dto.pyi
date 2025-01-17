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


class BasicS3AuthParamsDTO(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            bucketName = schemas.StrSchema
            bucketRegion = schemas.StrSchema
            accessKey = schemas.StrSchema
            secretKey = schemas.StrSchema
            path = schemas.StrSchema
            __annotations__ = {
                "bucketName": bucketName,
                "bucketRegion": bucketRegion,
                "accessKey": accessKey,
                "secretKey": secretKey,
                "path": path,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bucketName"]) -> MetaOapg.properties.bucketName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bucketRegion"]) -> MetaOapg.properties.bucketRegion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accessKey"]) -> MetaOapg.properties.accessKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secretKey"]) -> MetaOapg.properties.secretKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["path"]) -> MetaOapg.properties.path: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["bucketName", "bucketRegion", "accessKey", "secretKey", "path", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bucketName"]) -> typing.Union[MetaOapg.properties.bucketName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bucketRegion"]) -> typing.Union[MetaOapg.properties.bucketRegion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accessKey"]) -> typing.Union[MetaOapg.properties.accessKey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secretKey"]) -> typing.Union[MetaOapg.properties.secretKey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["path"]) -> typing.Union[MetaOapg.properties.path, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["bucketName", "bucketRegion", "accessKey", "secretKey", "path", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        bucketName: typing.Union[MetaOapg.properties.bucketName, str, schemas.Unset] = schemas.unset,
        bucketRegion: typing.Union[MetaOapg.properties.bucketRegion, str, schemas.Unset] = schemas.unset,
        accessKey: typing.Union[MetaOapg.properties.accessKey, str, schemas.Unset] = schemas.unset,
        secretKey: typing.Union[MetaOapg.properties.secretKey, str, schemas.Unset] = schemas.unset,
        path: typing.Union[MetaOapg.properties.path, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BasicS3AuthParamsDTO':
        return super().__new__(
            cls,
            *args,
            bucketName=bucketName,
            bucketRegion=bucketRegion,
            accessKey=accessKey,
            secretKey=secretKey,
            path=path,
            _configuration=_configuration,
            **kwargs,
        )
