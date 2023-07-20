# -*- coding: utf-8 -*-
# code generated by Prisma. DO NOT EDIT.
# pyright: reportUnusedImport=false
# fmt: off

# global imports for type checking
from builtins import bool as _bool
from builtins import int as _int
from builtins import float as _float
from builtins import str as _str
import sys
import decimal
import datetime
from typing import (
    TYPE_CHECKING,
    Optional,
    Iterable,
    Iterator,
    Sequence,
    Callable,
    ClassVar,
    NoReturn,
    TypeVar,
    Generic,
    Mapping,
    Tuple,
    Union,
    List,
    Dict,
    Type,
    Any,
    Set,
    overload,
    cast,
)
from typing_extensions import TypedDict, Literal


LiteralString = str
# -- template engine/http.py.jinja --

import logging

from . import utils, errors
from .abstract import AbstractEngine
from ..http import HTTP
from .._types import Method


__all__ = (
    'HTTPEngine',
)

log: logging.Logger = logging.getLogger(__name__)


class HTTPEngine(AbstractEngine):
    """Engine wrapper that communicates to the underlying engine over HTTP"""
    url: Optional[str]
    session: HTTP
    headers: Dict[str, str]

    def __init__(
        self,
        url: Optional[str],
        headers: Optional[Dict[str, str]] = None,
        **kwargs: Any,
    ) -> None:
        super().__init__()
        self.url = url
        self.session = HTTP(**kwargs)
        self.headers = headers if headers is not None else {}

    def close(self, *, timeout: Optional[float] = None) -> None:
        pass

    async def aclose(self, *, timeout: Optional[float] = None) -> None:
        await self._close_session()

    async def _close_session(self) -> None:
        if self.session and not self.session.closed:
            await self.session.close()

    async def request(
        self,
        method: Method,
        path: str,
        *,
        content: Any = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Any:
        if self.url is None:
            raise errors.NotConnectedError('Not connected to the query engine')

        kwargs = {
            'headers': {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                **self.headers,
            }
        }

        if headers is not None:
            kwargs['headers'].update(headers)

        if content is not None:
            kwargs['content'] = content

        url = self.url + path
        log.debug('Sending %s request to %s', method, url)
        log.debug('Request headers: %s', kwargs['headers'])
        log.debug('Request content: %s', content)

        resp = await self.session.request(method, url, **kwargs)
        log.debug('%s %s returned status %s', method, url, resp.status)

        if 300 > resp.status >= 200:
            response = await resp.json()
            log.debug('%s %s returned %s', method, url, response)

            errors_data = response.get('errors')
            if errors_data:
                return utils.handle_response_errors(resp, errors_data)

            return response

        if resp.status == 422:
            raise errors.UnprocessableEntityError(resp)

        # TODO: handle errors better
        raise errors.EngineRequestError(resp, await resp.text())


# black does not respect the fmt: off comment without this
# fmt: on
