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
from azure.mgmt.core.exceptions import ARMErrorFormat

from .. import models as _models
from .._serialization import Serializer
from .._vendor import _convert_request, _format_url_section

if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports
T = TypeVar("T")
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

_SERIALIZER = Serializer()
_SERIALIZER.client_side_validation = False


def build_expand_request(
    resource_group_name: str, host_pool_name: str, subscription_id: str, **kwargs: Any
) -> HttpRequest:
    _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
    _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

    api_version = kwargs.pop("api_version", _params.pop("api-version", "2022-09-09"))  # type: Literal["2022-09-09"]
    content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
    accept = _headers.pop("Accept", "application/json")

    # Construct URL
    _url = kwargs.pop(
        "template_url",
        "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/hostPools/{hostPoolName}/expandMsixImage",
    )  # pylint: disable=line-too-long
    path_format_arguments = {
        "subscriptionId": _SERIALIZER.url("subscription_id", subscription_id, "str", min_length=1),
        "resourceGroupName": _SERIALIZER.url(
            "resource_group_name", resource_group_name, "str", max_length=90, min_length=1
        ),
        "hostPoolName": _SERIALIZER.url("host_pool_name", host_pool_name, "str", max_length=64, min_length=3),
    }

    _url = _format_url_section(_url, **path_format_arguments)

    # Construct parameters
    _params["api-version"] = _SERIALIZER.query("api_version", api_version, "str")

    # Construct headers
    if content_type is not None:
        _headers["Content-Type"] = _SERIALIZER.header("content_type", content_type, "str")
    _headers["Accept"] = _SERIALIZER.header("accept", accept, "str")

    return HttpRequest(method="POST", url=_url, params=_params, headers=_headers, **kwargs)


class MsixImagesOperations:
    """
    .. warning::
        **DO NOT** instantiate this class directly.

        Instead, you should access the following operations through
        :class:`~azure.mgmt.desktopvirtualization.DesktopVirtualizationMgmtClient`'s
        :attr:`msix_images` attribute.
    """

    models = _models

    def __init__(self, *args, **kwargs):
        input_args = list(args)
        self._client = input_args.pop(0) if input_args else kwargs.pop("client")
        self._config = input_args.pop(0) if input_args else kwargs.pop("config")
        self._serialize = input_args.pop(0) if input_args else kwargs.pop("serializer")
        self._deserialize = input_args.pop(0) if input_args else kwargs.pop("deserializer")

    @overload
    def expand(
        self,
        resource_group_name: str,
        host_pool_name: str,
        msix_image_uri: _models.MSIXImageURI,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> Iterable["_models.ExpandMsixImage"]:
        """Expands and Lists MSIX packages in an Image, given the Image Path.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param host_pool_name: The name of the host pool within the specified resource group. Required.
        :type host_pool_name: str
        :param msix_image_uri: Object containing URI to MSIX Image. Required.
        :type msix_image_uri: ~azure.mgmt.desktopvirtualization.models.MSIXImageURI
        :keyword content_type: Body Parameter content-type. Content type parameter for JSON body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ExpandMsixImage or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.desktopvirtualization.models.ExpandMsixImage]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @overload
    def expand(
        self,
        resource_group_name: str,
        host_pool_name: str,
        msix_image_uri: IO,
        *,
        content_type: str = "application/json",
        **kwargs: Any
    ) -> Iterable["_models.ExpandMsixImage"]:
        """Expands and Lists MSIX packages in an Image, given the Image Path.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param host_pool_name: The name of the host pool within the specified resource group. Required.
        :type host_pool_name: str
        :param msix_image_uri: Object containing URI to MSIX Image. Required.
        :type msix_image_uri: IO
        :keyword content_type: Body Parameter content-type. Content type parameter for binary body.
         Default value is "application/json".
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ExpandMsixImage or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.desktopvirtualization.models.ExpandMsixImage]
        :raises ~azure.core.exceptions.HttpResponseError:
        """

    @distributed_trace
    def expand(
        self,
        resource_group_name: str,
        host_pool_name: str,
        msix_image_uri: Union[_models.MSIXImageURI, IO],
        **kwargs: Any
    ) -> Iterable["_models.ExpandMsixImage"]:
        """Expands and Lists MSIX packages in an Image, given the Image Path.

        :param resource_group_name: The name of the resource group. The name is case insensitive.
         Required.
        :type resource_group_name: str
        :param host_pool_name: The name of the host pool within the specified resource group. Required.
        :type host_pool_name: str
        :param msix_image_uri: Object containing URI to MSIX Image. Is either a model type or a IO
         type. Required.
        :type msix_image_uri: ~azure.mgmt.desktopvirtualization.models.MSIXImageURI or IO
        :keyword content_type: Body Parameter content-type. Known values are: 'application/json'.
         Default value is None.
        :paramtype content_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: An iterator like instance of either ExpandMsixImage or the result of cls(response)
        :rtype: ~azure.core.paging.ItemPaged[~azure.mgmt.desktopvirtualization.models.ExpandMsixImage]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        _headers = case_insensitive_dict(kwargs.pop("headers", {}) or {})
        _params = case_insensitive_dict(kwargs.pop("params", {}) or {})

        api_version = kwargs.pop(
            "api_version", _params.pop("api-version", self._config.api_version)
        )  # type: Literal["2022-09-09"]
        content_type = kwargs.pop("content_type", _headers.pop("Content-Type", None))  # type: Optional[str]
        cls = kwargs.pop("cls", None)  # type: ClsType[_models.ExpandMsixImageList]

        error_map = {
            401: ClientAuthenticationError,
            404: ResourceNotFoundError,
            409: ResourceExistsError,
            304: ResourceNotModifiedError,
        }
        error_map.update(kwargs.pop("error_map", {}) or {})
        content_type = content_type or "application/json"
        _json = None
        _content = None
        if isinstance(msix_image_uri, (IO, bytes)):
            _content = msix_image_uri
        else:
            _json = self._serialize.body(msix_image_uri, "MSIXImageURI")

        def prepare_request(next_link=None):
            if not next_link:

                request = build_expand_request(
                    resource_group_name=resource_group_name,
                    host_pool_name=host_pool_name,
                    subscription_id=self._config.subscription_id,
                    api_version=api_version,
                    content_type=content_type,
                    json=_json,
                    content=_content,
                    template_url=self.expand.metadata["url"],
                    headers=_headers,
                    params=_params,
                )
                request = _convert_request(request)
                request.url = self._client.format_url(request.url)  # type: ignore

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
                request.url = self._client.format_url(request.url)  # type: ignore
                request.method = "GET"
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize("ExpandMsixImageList", pipeline_response)
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
                raise HttpResponseError(response=response, error_format=ARMErrorFormat)

            return pipeline_response

        return ItemPaged(get_next, extract_data)

    expand.metadata = {"url": "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DesktopVirtualization/hostPools/{hostPoolName}/expandMsixImage"}  # type: ignore
