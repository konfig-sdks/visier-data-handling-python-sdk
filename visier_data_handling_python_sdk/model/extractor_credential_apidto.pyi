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


class ExtractorCredentialAPIDTO(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            credentialId = schemas.StrSchema
            displayName = schemas.StrSchema
            dataProvider = schemas.StrSchema
            isInherited = schemas.BoolSchema
            authContext = schemas.StrSchema
            __annotations__ = {
                "credentialId": credentialId,
                "displayName": displayName,
                "dataProvider": dataProvider,
                "isInherited": isInherited,
                "authContext": authContext,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["credentialId"]) -> MetaOapg.properties.credentialId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayName"]) -> MetaOapg.properties.displayName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataProvider"]) -> MetaOapg.properties.dataProvider: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isInherited"]) -> MetaOapg.properties.isInherited: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authContext"]) -> MetaOapg.properties.authContext: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["credentialId", "displayName", "dataProvider", "isInherited", "authContext", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["credentialId"]) -> typing.Union[MetaOapg.properties.credentialId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayName"]) -> typing.Union[MetaOapg.properties.displayName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataProvider"]) -> typing.Union[MetaOapg.properties.dataProvider, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isInherited"]) -> typing.Union[MetaOapg.properties.isInherited, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authContext"]) -> typing.Union[MetaOapg.properties.authContext, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["credentialId", "displayName", "dataProvider", "isInherited", "authContext", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        credentialId: typing.Union[MetaOapg.properties.credentialId, str, schemas.Unset] = schemas.unset,
        displayName: typing.Union[MetaOapg.properties.displayName, str, schemas.Unset] = schemas.unset,
        dataProvider: typing.Union[MetaOapg.properties.dataProvider, str, schemas.Unset] = schemas.unset,
        isInherited: typing.Union[MetaOapg.properties.isInherited, bool, schemas.Unset] = schemas.unset,
        authContext: typing.Union[MetaOapg.properties.authContext, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ExtractorCredentialAPIDTO':
        return super().__new__(
            cls,
            *args,
            credentialId=credentialId,
            displayName=displayName,
            dataProvider=dataProvider,
            isInherited=isInherited,
            authContext=authContext,
            _configuration=_configuration,
            **kwargs,
        )
