# coding: utf-8

"""
    Visier Data and Job Handling APIs

    Visier APIs for data and job handling

    The version of the OpenAPI document: 22222222.99201.1200
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from visier_data_handling_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from visier_data_handling_python_sdk.api_response import AsyncGeneratorResponse
from visier_data_handling_python_sdk import api_client, exceptions
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

from visier_data_handling_python_sdk.model.extraction_job_and_status_response import ExtractionJobAndStatusResponse as ExtractionJobAndStatusResponseSchema
from visier_data_handling_python_sdk.model.status import Status as StatusSchema

from visier_data_handling_python_sdk.type.extraction_job_and_status_response import ExtractionJobAndStatusResponse
from visier_data_handling_python_sdk.type.status import Status

from ...api_client import Dictionary
from visier_data_handling_python_sdk.pydantic.status import Status as StatusPydantic
from visier_data_handling_python_sdk.pydantic.extraction_job_and_status_response import ExtractionJobAndStatusResponse as ExtractionJobAndStatusResponsePydantic

# Query params
DispatchingJobIdSchema = schemas.StrSchema
TenantCodeSchema = schemas.StrSchema
LimitSchema = schemas.Int32Schema
StartSchema = schemas.Int32Schema
JobIdSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'dispatchingJobId': typing.Union[DispatchingJobIdSchema, str, ],
        'tenantCode': typing.Union[TenantCodeSchema, str, ],
        'limit': typing.Union[LimitSchema, decimal.Decimal, int, ],
        'start': typing.Union[StartSchema, decimal.Decimal, int, ],
        'jobId': typing.Union[JobIdSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_dispatching_job_id = api_client.QueryParameter(
    name="dispatchingJobId",
    style=api_client.ParameterStyle.FORM,
    schema=DispatchingJobIdSchema,
    explode=True,
)
request_query_tenant_code = api_client.QueryParameter(
    name="tenantCode",
    style=api_client.ParameterStyle.FORM,
    schema=TenantCodeSchema,
    explode=True,
)
request_query_limit = api_client.QueryParameter(
    name="limit",
    style=api_client.ParameterStyle.FORM,
    schema=LimitSchema,
    explode=True,
)
request_query_start = api_client.QueryParameter(
    name="start",
    style=api_client.ParameterStyle.FORM,
    schema=StartSchema,
    explode=True,
)
request_query_job_id = api_client.QueryParameter(
    name="jobId",
    style=api_client.ParameterStyle.FORM,
    schema=JobIdSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = ExtractionJobAndStatusResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ExtractionJobAndStatusResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ExtractionJobAndStatusResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor0ResponseBodyApplicationJson = StatusSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: Status


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: Status


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _extraction_job_and_status_mapped_args(
        self,
        dispatching_job_id: typing.Optional[str] = None,
        tenant_code: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        start: typing.Optional[int] = None,
        job_id: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if dispatching_job_id is not None:
            _query_params["dispatchingJobId"] = dispatching_job_id
        if tenant_code is not None:
            _query_params["tenantCode"] = tenant_code
        if limit is not None:
            _query_params["limit"] = limit
        if start is not None:
            _query_params["start"] = start
        if job_id is not None:
            _query_params["jobId"] = job_id
        args.query = _query_params
        return args

    async def _aextraction_job_and_status_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Retrieve a dispatching job&#x27;s extraction jobs with their statuses
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_dispatching_job_id,
            request_query_tenant_code,
            request_query_limit,
            request_query_start,
            request_query_job_id,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/op/jobs/dispatching-jobs/:jobId/extraction-jobs',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserializationAsync(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _extraction_job_and_status_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Retrieve a dispatching job&#x27;s extraction jobs with their statuses
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_dispatching_job_id,
            request_query_tenant_code,
            request_query_limit,
            request_query_start,
            request_query_job_id,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v1/op/jobs/dispatching-jobs/:jobId/extraction-jobs',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class ExtractionJobAndStatusRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aextraction_job_and_status(
        self,
        dispatching_job_id: typing.Optional[str] = None,
        tenant_code: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        start: typing.Optional[int] = None,
        job_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._extraction_job_and_status_mapped_args(
            dispatching_job_id=dispatching_job_id,
            tenant_code=tenant_code,
            limit=limit,
            start=start,
            job_id=job_id,
        )
        return await self._aextraction_job_and_status_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def extraction_job_and_status(
        self,
        dispatching_job_id: typing.Optional[str] = None,
        tenant_code: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        start: typing.Optional[int] = None,
        job_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._extraction_job_and_status_mapped_args(
            dispatching_job_id=dispatching_job_id,
            tenant_code=tenant_code,
            limit=limit,
            start=start,
            job_id=job_id,
        )
        return self._extraction_job_and_status_oapg(
            query_params=args.query,
        )

class ExtractionJobAndStatus(BaseApi):

    async def aextraction_job_and_status(
        self,
        dispatching_job_id: typing.Optional[str] = None,
        tenant_code: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        start: typing.Optional[int] = None,
        job_id: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> ExtractionJobAndStatusResponsePydantic:
        raw_response = await self.raw.aextraction_job_and_status(
            dispatching_job_id=dispatching_job_id,
            tenant_code=tenant_code,
            limit=limit,
            start=start,
            job_id=job_id,
            **kwargs,
        )
        if validate:
            return ExtractionJobAndStatusResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ExtractionJobAndStatusResponsePydantic, raw_response.body)
    
    
    def extraction_job_and_status(
        self,
        dispatching_job_id: typing.Optional[str] = None,
        tenant_code: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        start: typing.Optional[int] = None,
        job_id: typing.Optional[str] = None,
        validate: bool = False,
    ) -> ExtractionJobAndStatusResponsePydantic:
        raw_response = self.raw.extraction_job_and_status(
            dispatching_job_id=dispatching_job_id,
            tenant_code=tenant_code,
            limit=limit,
            start=start,
            job_id=job_id,
        )
        if validate:
            return ExtractionJobAndStatusResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ExtractionJobAndStatusResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        dispatching_job_id: typing.Optional[str] = None,
        tenant_code: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        start: typing.Optional[int] = None,
        job_id: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._extraction_job_and_status_mapped_args(
            dispatching_job_id=dispatching_job_id,
            tenant_code=tenant_code,
            limit=limit,
            start=start,
            job_id=job_id,
        )
        return await self._aextraction_job_and_status_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        dispatching_job_id: typing.Optional[str] = None,
        tenant_code: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        start: typing.Optional[int] = None,
        job_id: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._extraction_job_and_status_mapped_args(
            dispatching_job_id=dispatching_job_id,
            tenant_code=tenant_code,
            limit=limit,
            start=start,
            job_id=job_id,
        )
        return self._extraction_job_and_status_oapg(
            query_params=args.query,
        )

