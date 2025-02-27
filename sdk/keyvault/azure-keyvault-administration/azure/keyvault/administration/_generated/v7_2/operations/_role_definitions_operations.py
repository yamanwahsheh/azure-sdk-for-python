# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import sys
from typing import Any, Callable, Dict, IO, Iterable, Optional, TypeVar, Union, overload
import urllib.parse

from azure.core.exceptions import (
    ClientAuthenticationError,
    HttpResponseError,
    ResourceExistsError,
    ResourceNotFoundError,
    ResourceNotModifiedError,
    map_error,
)
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator import distributed_trace
from azure.core.utils import case_insensitive_dict

from .. import models as _models
from ..._serialization import Serializer
from .._vendor import KeyVaultClientMixinABC, _convert_request, _format_url_section

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_delete_request(scope: str, role_definition_name: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "7.2"))  # type: Literal["7.2"]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/{scope}/providers/Microsoft.Authorization/roleDefinitions/{roleDefinitionName}")
    path_format_arguments = {
        "scope": _SERIALIZER.url("scope", scope, "str", skip_quote=True),
        "roleDefinitionName": _SERIALIZER.url("role_definition_name", role_definition_name, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="DELETE", url=_url, params=_params, headers=_headers, **kwargs)


def build_create_or_update_request(scope: str, role_definition_name: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "7.2"))  # type: Literal["7.2"]
    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/{scope}/providers/Microsoft.Authorization/roleDefinitions/{roleDefinitionName}")
    path_format_arguments = {
        "scope": _SERIALIZER.url("scope", scope, "str", skip_quote=True),
        "roleDefinitionName": _SERIALIZER.url("role_definition_name", role_definition_name, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="PUT", url=_url, params=_params, headers=_headers, **kwargs)


def build_get_request(scope: str, role_definition_name: str, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "7.2"))  # type: Literal["7.2"]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/{scope}/providers/Microsoft.Authorization/roleDefinitions/{roleDefinitionName}")
    path_format_arguments = {
        "scope": _SERIALIZER.url("scope", scope, "str", skip_quote=True),
        "roleDefinitionName": _SERIALIZER.url("role_definition_name", role_definition_name, "str"),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


def build_list_request(scope: str, *, filter: Optional[str] = None, **kwargs: Any) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "7.2"))  # type: Literal["7.2"]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop("template_url", "/{scope}/providers/Microsoft.Authorization/roleDefinitions")
    path_format_arguments = {
        "scope": _SERIALIZER.url("scope", scope, "str", skip_quote=True),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    if filter is not None:
        _params["$filter"] = _SERIALIZER.query("filter", filter, "str")
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="GET", url=_url, params=_params, headers=_headers, **kwargs)


class RoleDefinitionsOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.keyvault.v7_2.KeyVaultClient`'s
        :attr:`role_definitions` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @distributed_trace
    def delete(
        self, vault_base_url: str, scope: str, role_definition_name: str, **kwargs: Any
    ) -> _models.RoleDefinition:
        """Deletes a custom role definition.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net. Required.
        :type vault_base_url: str
        :param scope: The scope of the role definition to delete. Managed HSM only supports '/'.
         Required.
        :type scope: str
        :param role_definition_name: The name (GUID) of the role definition to delete. Required.
        :type role_definition_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RoleDefinition or the result of cls(response)
        :rtype: ~azure.keyvault.v7_2.models.RoleDefinition
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", "7.2"))  # type: Literal["7.2"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.RoleDefinition]

        request = build_delete_request(
            scope=scope,
            role_definition_name=role_definition_name,
            api_version=api_version,
            template_url=self.delete.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.KeyVaultError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("RoleDefinition", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    delete.metadata = {"url": "/{scope}/providers/Microsoft.Authorization/roleDefinitions/{roleDefinitionName}"}  # type: ignore

    @overload
    def create_or_update(
        self,
        vault_base_url: str,
        scope: str,
        role_definition_name: str,
        parameters: _models.RoleDefinitionCreateParameters,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.RoleDefinition:
        """Creates or updates a custom role definition.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net. Required.
        :type vault_base_url: str
        :param scope: The scope of the role definition to create or update. Managed HSM only supports
         '/'. Required.
        :type scope: str
        :param role_definition_name: The name of the role definition to create or update. It can be any
         valid GUID. Required.
        :type role_definition_name: str
        :param parameters: Parameters for the role definition. Required.
        :type parameters: ~azure.keyvault.v7_2.models.RoleDefinitionCreateParameters
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RoleDefinition or the result of cls(response)
        :rtype: ~azure.keyvault.v7_2.models.RoleDefinition
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def create_or_update(
        self,
        vault_base_url: str,
        scope: str,
        role_definition_name: str,
        parameters: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> _models.RoleDefinition:
        """Creates or updates a custom role definition.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net. Required.
        :type vault_base_url: str
        :param scope: The scope of the role definition to create or update. Managed HSM only supports
         '/'. Required.
        :type scope: str
        :param role_definition_name: The name of the role definition to create or update. It can be any
         valid GUID. Required.
        :type role_definition_name: str
        :param parameters: Parameters for the role definition. Required.
        :type parameters: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RoleDefinition or the result of cls(response)
        :rtype: ~azure.keyvault.v7_2.models.RoleDefinition
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def create_or_update(
        self,
        vault_base_url: str,
        scope: str,
        role_definition_name: str,
        parameters: Union[_models.RoleDefinitionCreateParameters, IO],
        **kwargs: Any
    ) -> _models.RoleDefinition:
        """Creates or updates a custom role definition.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net. Required.
        :type vault_base_url: str
        :param scope: The scope of the role definition to create or update. Managed HSM only supports
         '/'. Required.
        :type scope: str
        :param role_definition_name: The name of the role definition to create or update. It can be any
         valid GUID. Required.
        :type role_definition_name: str
        :param parameters: Parameters for the role definition. Is either a model type or a IO type.
         Required.
        :type parameters: ~azure.keyvault.v7_2.models.RoleDefinitionCreateParameters or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RoleDefinition or the result of cls(response)
        :rtype: ~azure.keyvault.v7_2.models.RoleDefinition
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", "7.2"))  # type: Literal["7.2"]
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.RoleDefinition]

        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(parameters, (IO, bytes)):
            _content = parameters
        else:
            _json = self._serialize.body(parameters, "RoleDefinitionCreateParameters")

        request = build_create_or_update_request(
            scope=scope,
            role_definition_name=role_definition_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            content=_content,
            template_url=self.create_or_update.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.KeyVaultError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("RoleDefinition", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    create_or_update.metadata = {"url": "/{scope}/providers/Microsoft.Authorization/roleDefinitions/{roleDefinitionName}"}  # type: ignore

    @distributed_trace
    def get(self, vault_base_url: str, scope: str, role_definition_name: str, **kwargs: Any) -> _models.RoleDefinition:
        """Get the specified role definition.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net. Required.
        :type vault_base_url: str
        :param scope: The scope of the role definition to get. Managed HSM only supports '/'. Required.
        :type scope: str
        :param role_definition_name: The name of the role definition to get. Required.
        :type role_definition_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RoleDefinition or the result of cls(response)
        :rtype: ~azure.keyvault.v7_2.models.RoleDefinition
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

        api_version = kwargs.pop("api_version", _params.pop("api-version", "7.2"))  # type: Literal["7.2"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.RoleDefinition]

        request = build_get_request(
            scope=scope,
            role_definition_name=role_definition_name,
            api_version=api_version,
            template_url=self.get.metadata["url"],
            headers=_headers,
            params=_params,
        )
        request = _convert_request(request)
        path_format_arguments = {
            "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, "str", skip_quote=True),
        }
        request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

        pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
            request, stream=False, **kwargs
        )

        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.KeyVaultError, pipeline_response)
            raise HttpResponseError(response=response, model=error)

        deserialized = self._deserialize("RoleDefinition", pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {"url": "/{scope}/providers/Microsoft.Authorization/roleDefinitions/{roleDefinitionName}"}  # type: ignore

    @distributed_trace
    def list(
        self, vault_base_url: str, scope: str, filter: Optional[str] = None, **kwargs: Any
    ) -> Iterable["_models.RoleDefinition"]:
        """Get all role definitions that are applicable at scope and above.

        :param vault_base_url: The vault name, for example https://myvault.vault.azure.net. Required.
        :type vault_base_url: str
        :param scope: The scope of the role definition. Required.
        :type scope: str
        :param filter: The filter to apply on the operation. Use atScopeAndBelow filter to search below
         the given scope as well. Default value is None.
        :type filter: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either RoleDefinition or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.keyvault.v7_2.models.RoleDefinition]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = kwargs.pop("headers", {}) or {}
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop("api_version", _params.pop("api-version", "7.2"))  # type: Literal["7.2"]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.RoleDefinitionListResult]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})

        def prepare_request(next_link=None):
            if not next_link:

                request = build_list_request(
                    scope=scope,
                    filter=filter,
                    api_version=api_version,
                    template_url=self.list.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, "str", skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore

            else:
                # make call to next link with the client's api-version
                _parsed_next_link = urllib.parse.urlparse(next_link)
                _next_request_params = case_insensitive_dict(
                    {
                        key: [urllib.parse.quote(v) for v in value]
                        for key, value in urllib.parse.parse_qs(_parsed_next_link.query).items()
                    }
                )
                _next_request_params["api-version"] = self._config.api_version
                request = HttpRequest(
                    "GET", urllib.parse.urljoin(next_link, _parsed_next_link.path), params=_next_request_params
                )
                request = _convert_request(request)
                path_format_arguments = {
                    "vaultBaseUrl": self._serialize.url("vault_base_url", vault_base_url, "str", skip_quote=True),
                }
                request.url = self._client.format_url(request.url, **path_format_arguments)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("RoleDefinitionListResult", pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link or None, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(  # type: ignore # pylint: disable=protected-access
                request, stream=False, **kwargs
            )
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code, response=response, error_map=error_map)
                error = self._deserialize.failsafe_deserialize(_models.KeyVaultError, pipeline_response)
                raise HttpResponseError(response=response, model=error)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    list.metadata = {"url": "/{scope}/providers/Microsoft.Authorization/roleDefinitions"}  # type: ignore
