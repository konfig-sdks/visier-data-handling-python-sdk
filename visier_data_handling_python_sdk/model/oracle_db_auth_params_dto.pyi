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


class OracleDbAuthParamsDTO(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            host = schemas.StrSchema
            port = schemas.StrSchema
            username = schemas.StrSchema
            password = schemas.StrSchema
            serviceName = schemas.StrSchema
            __annotations__ = {
                "host": host,
                "port": port,
                "username": username,
                "password": password,
                "serviceName": serviceName,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["host"]) -> MetaOapg.properties.host: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["port"]) -> MetaOapg.properties.port: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["password"]) -> MetaOapg.properties.password: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serviceName"]) -> MetaOapg.properties.serviceName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["host", "port", "username", "password", "serviceName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["host"]) -> typing.Union[MetaOapg.properties.host, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["port"]) -> typing.Union[MetaOapg.properties.port, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> typing.Union[MetaOapg.properties.username, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["password"]) -> typing.Union[MetaOapg.properties.password, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serviceName"]) -> typing.Union[MetaOapg.properties.serviceName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["host", "port", "username", "password", "serviceName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        host: typing.Union[MetaOapg.properties.host, str, schemas.Unset] = schemas.unset,
        port: typing.Union[MetaOapg.properties.port, str, schemas.Unset] = schemas.unset,
        username: typing.Union[MetaOapg.properties.username, str, schemas.Unset] = schemas.unset,
        password: typing.Union[MetaOapg.properties.password, str, schemas.Unset] = schemas.unset,
        serviceName: typing.Union[MetaOapg.properties.serviceName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OracleDbAuthParamsDTO':
        return super().__new__(
            cls,
            *args,
            host=host,
            port=port,
            username=username,
            password=password,
            serviceName=serviceName,
            _configuration=_configuration,
            **kwargs,
        )
