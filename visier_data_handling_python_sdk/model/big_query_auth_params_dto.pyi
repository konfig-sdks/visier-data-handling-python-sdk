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


class BigQueryAuthParamsDTO(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            projectId = schemas.StrSchema
            datasetLocation = schemas.StrSchema
            refreshToken = schemas.StrSchema
            clientId = schemas.StrSchema
            clientSecret = schemas.StrSchema
            defaultDataset = schemas.StrSchema
        
            @staticmethod
            def serviceAccountParams() -> typing.Type['BigQueryServiceAccountParamsDTO']:
                return BigQueryServiceAccountParamsDTO
            __annotations__ = {
                "projectId": projectId,
                "datasetLocation": datasetLocation,
                "refreshToken": refreshToken,
                "clientId": clientId,
                "clientSecret": clientSecret,
                "defaultDataset": defaultDataset,
                "serviceAccountParams": serviceAccountParams,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projectId"]) -> MetaOapg.properties.projectId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["datasetLocation"]) -> MetaOapg.properties.datasetLocation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["refreshToken"]) -> MetaOapg.properties.refreshToken: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clientId"]) -> MetaOapg.properties.clientId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clientSecret"]) -> MetaOapg.properties.clientSecret: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultDataset"]) -> MetaOapg.properties.defaultDataset: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serviceAccountParams"]) -> 'BigQueryServiceAccountParamsDTO': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["projectId", "datasetLocation", "refreshToken", "clientId", "clientSecret", "defaultDataset", "serviceAccountParams", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projectId"]) -> typing.Union[MetaOapg.properties.projectId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["datasetLocation"]) -> typing.Union[MetaOapg.properties.datasetLocation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["refreshToken"]) -> typing.Union[MetaOapg.properties.refreshToken, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clientId"]) -> typing.Union[MetaOapg.properties.clientId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clientSecret"]) -> typing.Union[MetaOapg.properties.clientSecret, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultDataset"]) -> typing.Union[MetaOapg.properties.defaultDataset, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serviceAccountParams"]) -> typing.Union['BigQueryServiceAccountParamsDTO', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["projectId", "datasetLocation", "refreshToken", "clientId", "clientSecret", "defaultDataset", "serviceAccountParams", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        projectId: typing.Union[MetaOapg.properties.projectId, str, schemas.Unset] = schemas.unset,
        datasetLocation: typing.Union[MetaOapg.properties.datasetLocation, str, schemas.Unset] = schemas.unset,
        refreshToken: typing.Union[MetaOapg.properties.refreshToken, str, schemas.Unset] = schemas.unset,
        clientId: typing.Union[MetaOapg.properties.clientId, str, schemas.Unset] = schemas.unset,
        clientSecret: typing.Union[MetaOapg.properties.clientSecret, str, schemas.Unset] = schemas.unset,
        defaultDataset: typing.Union[MetaOapg.properties.defaultDataset, str, schemas.Unset] = schemas.unset,
        serviceAccountParams: typing.Union['BigQueryServiceAccountParamsDTO', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BigQueryAuthParamsDTO':
        return super().__new__(
            cls,
            *args,
            projectId=projectId,
            datasetLocation=datasetLocation,
            refreshToken=refreshToken,
            clientId=clientId,
            clientSecret=clientSecret,
            defaultDataset=defaultDataset,
            serviceAccountParams=serviceAccountParams,
            _configuration=_configuration,
            **kwargs,
        )

from visier_data_handling_python_sdk.model.big_query_service_account_params_dto import BigQueryServiceAccountParamsDTO