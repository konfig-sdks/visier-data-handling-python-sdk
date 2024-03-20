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


class GoogleSheetsAuthParamsDTO(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            authCode = schemas.StrSchema
            configuration = schemas.StrSchema
            clientId = schemas.StrSchema
            clientSecret = schemas.StrSchema
            __annotations__ = {
                "authCode": authCode,
                "configuration": configuration,
                "clientId": clientId,
                "clientSecret": clientSecret,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authCode"]) -> MetaOapg.properties.authCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["configuration"]) -> MetaOapg.properties.configuration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clientId"]) -> MetaOapg.properties.clientId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clientSecret"]) -> MetaOapg.properties.clientSecret: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["authCode", "configuration", "clientId", "clientSecret", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authCode"]) -> typing.Union[MetaOapg.properties.authCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["configuration"]) -> typing.Union[MetaOapg.properties.configuration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clientId"]) -> typing.Union[MetaOapg.properties.clientId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clientSecret"]) -> typing.Union[MetaOapg.properties.clientSecret, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["authCode", "configuration", "clientId", "clientSecret", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        authCode: typing.Union[MetaOapg.properties.authCode, str, schemas.Unset] = schemas.unset,
        configuration: typing.Union[MetaOapg.properties.configuration, str, schemas.Unset] = schemas.unset,
        clientId: typing.Union[MetaOapg.properties.clientId, str, schemas.Unset] = schemas.unset,
        clientSecret: typing.Union[MetaOapg.properties.clientSecret, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GoogleSheetsAuthParamsDTO':
        return super().__new__(
            cls,
            *args,
            authCode=authCode,
            configuration=configuration,
            clientId=clientId,
            clientSecret=clientSecret,
            _configuration=_configuration,
            **kwargs,
        )
