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


class CredentialCreationAPIResponseDTO(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            uuid = schemas.StrSchema
            symbolName = schemas.StrSchema
            objectName = schemas.StrSchema
            
            
            class missingConnectionProperties(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SubjectMissingAccessDTO']:
                        return SubjectMissingAccessDTO
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['SubjectMissingAccessDTO'], typing.List['SubjectMissingAccessDTO']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'missingConnectionProperties':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SubjectMissingAccessDTO':
                    return super().__getitem__(i)
            __annotations__ = {
                "uuid": uuid,
                "symbolName": symbolName,
                "objectName": objectName,
                "missingConnectionProperties": missingConnectionProperties,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["symbolName"]) -> MetaOapg.properties.symbolName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["objectName"]) -> MetaOapg.properties.objectName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["missingConnectionProperties"]) -> MetaOapg.properties.missingConnectionProperties: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["uuid", "symbolName", "objectName", "missingConnectionProperties", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> typing.Union[MetaOapg.properties.uuid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["symbolName"]) -> typing.Union[MetaOapg.properties.symbolName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["objectName"]) -> typing.Union[MetaOapg.properties.objectName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["missingConnectionProperties"]) -> typing.Union[MetaOapg.properties.missingConnectionProperties, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["uuid", "symbolName", "objectName", "missingConnectionProperties", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        uuid: typing.Union[MetaOapg.properties.uuid, str, schemas.Unset] = schemas.unset,
        symbolName: typing.Union[MetaOapg.properties.symbolName, str, schemas.Unset] = schemas.unset,
        objectName: typing.Union[MetaOapg.properties.objectName, str, schemas.Unset] = schemas.unset,
        missingConnectionProperties: typing.Union[MetaOapg.properties.missingConnectionProperties, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CredentialCreationAPIResponseDTO':
        return super().__new__(
            cls,
            *args,
            uuid=uuid,
            symbolName=symbolName,
            objectName=objectName,
            missingConnectionProperties=missingConnectionProperties,
            _configuration=_configuration,
            **kwargs,
        )

from visier_data_handling_python_sdk.model.subject_missing_access_dto import SubjectMissingAccessDTO