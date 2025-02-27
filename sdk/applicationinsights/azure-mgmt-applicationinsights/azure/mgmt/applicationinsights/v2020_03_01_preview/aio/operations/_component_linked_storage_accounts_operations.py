# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Optional, TypeVar, Union, overload

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.core.utils import case_insensitive_dict
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._component_linked_storage_accounts_operations import (
    build_create_and_update_request,
    build_delete_request,
    build_get_request,
    build_update_request,
)

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]


class ComponentLinkedStorageAccountsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.applicationinsights.v2020_03_01_preview.aio.ApplicationInsightsManagementClient`'s
        :attr:`component_linked_storage_accounts` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs) -> None:
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace_async
    async def get(
        self, resource_group_name: str, resource_name: str, storage_type: Union[str, _models.StorageType], **kwargs: Any
    ) -> _models.ComponentLinkedStorageAccounts:
        """Returns the current linked storage settings for an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource. Required.
        :type resource_name: str
        :param storage_type: The type of the Application Insights component data source for the linked
         storage account. "ServiceProfiler" Required.
        :type storage_type: str or
         ~azure.mgmt.applicationinsights.v2020_03_01_preview.models.StorageType
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ComponentLinkedStorageAccounts or the result of cls(response)
        :rtype:
         ~azure.mgmt.applicationinsights.v2020_03_01_preview.models.ComponentLinkedStorageAccounts
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2020-03-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2020-03-01-preview")
        )
        cls: ClsType[_models.ComponentLinkedStorageAccounts] = kwargs.pop("cls", None)

        request = build_get_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            storage_type=storage_type,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseLinkedStorage, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ComponentLinkedStorageAccounts", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/linkedStorageAccounts/{storageType}"
    }

    @overload
    async def create_and_update(
        self,
        resource_group_name: str,
        resource_name: str,
        storage_type: Union[str, _models.StorageType],
        linked_storage_accounts_properties: _models.ComponentLinkedStorageAccounts,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ComponentLinkedStorageAccounts:
        """Replace current linked storage account for an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource. Required.
        :type resource_name: str
        :param storage_type: The type of the Application Insights component data source for the linked
         storage account. "ServiceProfiler" Required.
        :type storage_type: str or
         ~azure.mgmt.applicationinsights.v2020_03_01_preview.models.StorageType
        :param linked_storage_accounts_properties: Properties that need to be specified to update
         linked storage accounts for an Application Insights component. Required.
        :type linked_storage_accounts_properties:
         ~azure.mgmt.applicationinsights.v2020_03_01_preview.models.ComponentLinkedStorageAccounts
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ComponentLinkedStorageAccounts or the result of cls(response)
        :rtype:
         ~azure.mgmt.applicationinsights.v2020_03_01_preview.models.ComponentLinkedStorageAccounts
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def create_and_update(
        self,
        resource_group_name: str,
        resource_name: str,
        storage_type: Union[str, _models.StorageType],
        linked_storage_accounts_properties: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ComponentLinkedStorageAccounts:
        """Replace current linked storage account for an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource. Required.
        :type resource_name: str
        :param storage_type: The type of the Application Insights component data source for the linked
         storage account. "ServiceProfiler" Required.
        :type storage_type: str or
         ~azure.mgmt.applicationinsights.v2020_03_01_preview.models.StorageType
        :param linked_storage_accounts_properties: Properties that need to be specified to update
         linked storage accounts for an Application Insights component. Required.
        :type linked_storage_accounts_properties: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ComponentLinkedStorageAccounts or the result of cls(response)
        :rtype:
         ~azure.mgmt.applicationinsights.v2020_03_01_preview.models.ComponentLinkedStorageAccounts
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def create_and_update(
        self,
        resource_group_name: str,
        resource_name: str,
        storage_type: Union[str, _models.StorageType],
        linked_storage_accounts_properties: Union[_models.ComponentLinkedStorageAccounts, IO],
        **kwargs: Any
    ) -> _models.ComponentLinkedStorageAccounts:
        """Replace current linked storage account for an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource. Required.
        :type resource_name: str
        :param storage_type: The type of the Application Insights component data source for the linked
         storage account. "ServiceProfiler" Required.
        :type storage_type: str or
         ~azure.mgmt.applicationinsights.v2020_03_01_preview.models.StorageType
        :param linked_storage_accounts_properties: Properties that need to be specified to update
         linked storage accounts for an Application Insights component. Is either a
         ComponentLinkedStorageAccounts type or a IO type. Required.
        :type linked_storage_accounts_properties:
         ~azure.mgmt.applicationinsights.v2020_03_01_preview.models.ComponentLinkedStorageAccounts or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ComponentLinkedStorageAccounts or the result of cls(response)
        :rtype:
         ~azure.mgmt.applicationinsights.v2020_03_01_preview.models.ComponentLinkedStorageAccounts
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2020-03-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2020-03-01-preview")
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ComponentLinkedStorageAccounts] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(linked_storage_accounts_properties, (IO, bytes)):
            _content = linked_storage_accounts_properties
        else:
            _json = self._serialize.body(linked_storage_accounts_properties, "ComponentLinkedStorageAccounts")

        request = build_create_and_update_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            storage_type=storage_type,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_and_update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseLinkedStorage, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ComponentLinkedStorageAccounts", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_and_update.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/linkedStorageAccounts/{storageType}"
    }

    @overload
    async def update(
        self,
        resource_group_name: str,
        resource_name: str,
        storage_type: Union[str, _models.StorageType],
        linked_storage_accounts_properties: _models.ComponentLinkedStorageAccountsPatch,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ComponentLinkedStorageAccounts:
        """Update linked storage accounts for an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource. Required.
        :type resource_name: str
        :param storage_type: The type of the Application Insights component data source for the linked
         storage account. "ServiceProfiler" Required.
        :type storage_type: str or
         ~azure.mgmt.applicationinsights.v2020_03_01_preview.models.StorageType
        :param linked_storage_accounts_properties: Properties that need to be specified to update a
         linked storage accounts for an Application Insights component. Required.
        :type linked_storage_accounts_properties:
         ~azure.mgmt.applicationinsights.v2020_03_01_preview.models.ComponentLinkedStorageAccountsPatch
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ComponentLinkedStorageAccounts or the result of cls(response)
        :rtype:
         ~azure.mgmt.applicationinsights.v2020_03_01_preview.models.ComponentLinkedStorageAccounts
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    async def update(
        self,
        resource_group_name: str,
        resource_name: str,
        storage_type: Union[str, _models.StorageType],
        linked_storage_accounts_properties: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.ComponentLinkedStorageAccounts:
        """Update linked storage accounts for an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource. Required.
        :type resource_name: str
        :param storage_type: The type of the Application Insights component data source for the linked
         storage account. "ServiceProfiler" Required.
        :type storage_type: str or
         ~azure.mgmt.applicationinsights.v2020_03_01_preview.models.StorageType
        :param linked_storage_accounts_properties: Properties that need to be specified to update a
         linked storage accounts for an Application Insights component. Required.
        :type linked_storage_accounts_properties: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ComponentLinkedStorageAccounts or the result of cls(response)
        :rtype:
         ~azure.mgmt.applicationinsights.v2020_03_01_preview.models.ComponentLinkedStorageAccounts
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace_async
    async def update(
        self,
        resource_group_name: str,
        resource_name: str,
        storage_type: Union[str, _models.StorageType],
        linked_storage_accounts_properties: Union[_models.ComponentLinkedStorageAccountsPatch, IO],
        **kwargs: Any
    ) -> _models.ComponentLinkedStorageAccounts:
        """Update linked storage accounts for an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource. Required.
        :type resource_name: str
        :param storage_type: The type of the Application Insights component data source for the linked
         storage account. "ServiceProfiler" Required.
        :type storage_type: str or
         ~azure.mgmt.applicationinsights.v2020_03_01_preview.models.StorageType
        :param linked_storage_accounts_properties: Properties that need to be specified to update a
         linked storage accounts for an Application Insights component. Is either a
         ComponentLinkedStorageAccountsPatch type or a IO type. Required.
        :type linked_storage_accounts_properties:
         ~azure.mgmt.applicationinsights.v2020_03_01_preview.models.ComponentLinkedStorageAccountsPatch
         or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ComponentLinkedStorageAccounts or the result of cls(response)
        :rtype:
         ~azure.mgmt.applicationinsights.v2020_03_01_preview.models.ComponentLinkedStorageAccounts
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2020-03-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2020-03-01-preview")
        )
        content_type: Optional[str] = kwargs.pop("content_type", _headers.pop("Content-Type", None))
        cls: ClsType[_models.ComponentLinkedStorageAccounts] = kwargs.pop("cls", None)

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(linked_storage_accounts_properties, (IO, bytes)):
            _content = linked_storage_accounts_properties
        else:
            _json = self._serialize.body(linked_storage_accounts_properties, "ComponentLinkedStorageAccountsPatch")

        request = build_update_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            storage_type=storage_type,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseLinkedStorage, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize("ComponentLinkedStorageAccounts", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    update.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/linkedStorageAccounts/{storageType}"
    }

    @distributed_trace_async
    async def delete(  # pylint: disable=inconsistent-return-statements
        self, resource_group_name: str, resource_name: str, storage_type: Union[str, _models.StorageType], **kwargs: Any
    ) -> None:
        """Delete linked storage accounts for an Application Insights component.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param resource_name: The name of the Application Insights component resource. Required.
        :type resource_name: str
        :param storage_type: The type of the Application Insights component data source for the linked
         storage account. "ServiceProfiler" Required.
        :type storage_type: str or
         ~azure.mgmt.applicationinsights.v2020_03_01_preview.models.StorageType
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version: Literal["2020-03-01-preview"] = kwargs.pop(
            "api_version", _params.pop("api-version", "2020-03-01-preview")
        )
        cls: ClsType[None] = kwargs.pop("cls", None)

        request = build_delete_request(
            resource_group_name=resource_group_name,
            resource_name=resource_name,
            storage_type=storage_type,
            subscription_id=self._config.subscription_id,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response: PipelineResponse = await self._client._pipeline.run(  # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponseLinkedStorage, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {
        "url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/components/{resourceName}/linkedStorageAccounts/{storageType}"
    }
