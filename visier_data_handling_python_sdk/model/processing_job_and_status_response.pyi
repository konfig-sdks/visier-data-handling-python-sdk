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


class ProcessingJobAndStatusResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            parentJobId = schemas.StrSchema
            parentTenantCode = schemas.StrSchema
            limit = schemas.Int32Schema
            start = schemas.Int32Schema
            
            
            class processingJobs(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ProcessingJob']:
                        return ProcessingJob
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ProcessingJob'], typing.List['ProcessingJob']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'processingJobs':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ProcessingJob':
                    return super().__getitem__(i)
            __annotations__ = {
                "parentJobId": parentJobId,
                "parentTenantCode": parentTenantCode,
                "limit": limit,
                "start": start,
                "processingJobs": processingJobs,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parentJobId"]) -> MetaOapg.properties.parentJobId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parentTenantCode"]) -> MetaOapg.properties.parentTenantCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["limit"]) -> MetaOapg.properties.limit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start"]) -> MetaOapg.properties.start: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["processingJobs"]) -> MetaOapg.properties.processingJobs: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["parentJobId", "parentTenantCode", "limit", "start", "processingJobs", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parentJobId"]) -> typing.Union[MetaOapg.properties.parentJobId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parentTenantCode"]) -> typing.Union[MetaOapg.properties.parentTenantCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["limit"]) -> typing.Union[MetaOapg.properties.limit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start"]) -> typing.Union[MetaOapg.properties.start, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["processingJobs"]) -> typing.Union[MetaOapg.properties.processingJobs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["parentJobId", "parentTenantCode", "limit", "start", "processingJobs", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        parentJobId: typing.Union[MetaOapg.properties.parentJobId, str, schemas.Unset] = schemas.unset,
        parentTenantCode: typing.Union[MetaOapg.properties.parentTenantCode, str, schemas.Unset] = schemas.unset,
        limit: typing.Union[MetaOapg.properties.limit, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        start: typing.Union[MetaOapg.properties.start, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        processingJobs: typing.Union[MetaOapg.properties.processingJobs, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProcessingJobAndStatusResponse':
        return super().__new__(
            cls,
            *args,
            parentJobId=parentJobId,
            parentTenantCode=parentTenantCode,
            limit=limit,
            start=start,
            processingJobs=processingJobs,
            _configuration=_configuration,
            **kwargs,
        )

from visier_data_handling_python_sdk.model.processing_job import ProcessingJob
