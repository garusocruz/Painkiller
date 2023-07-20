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
# -- template types.py.jinja --
from typing import TypeVar

import httpx
from .utils import _NoneType



# TODO: filters with aggregates should have their own recursive fields
# TODO: cleanup whitespace control
# TODO: add an argument to signify that the last iteration should be skipped


SortMode = Literal['default', 'insensitive']
SortOrder = Literal['asc', 'desc']


class _DatasourceOverrideOptional(TypedDict, total=False):
    env: str
    name: str


class DatasourceOverride(_DatasourceOverrideOptional):
    url: str


# NOTE: we don't support some options as their type hints are not publicly exposed
# https://github.com/encode/httpx/discussions/1977
class HttpConfig(TypedDict, total=False):
    app: Callable[[Mapping[str, Any], Any], Any]
    http1: bool
    http2: bool
    limits: httpx.Limits
    timeout: Union[None, float, httpx.Timeout]
    trust_env: bool
    max_redirects: int


# types that can be serialized to json by our query builder
Serializable = Union[
    None,
    bool,
    float,
    int,
    str,
    datetime.datetime,
    List[Any],
    Dict[None, Any],
    Dict[bool, Any],
    Dict[float, Any],
    Dict[int, Any],
    Dict[str, Any],
]


    

StringFilter = TypedDict(
    'StringFilter',
    {
        'equals': str,
        'not_in': List[str],
        'lt': str,
        'lte': str,
        'gt': str,
        'gte': str,
        'contains': str,
        'startswith': str,
        'endswith': str,
        'in': List[str],
        'not': Union[str, 'StringFilterRecursive1'],
            },
    total=False,
)


StringFilterRecursive1 = TypedDict(
    'StringFilterRecursive1',
    {
        'equals': str,
        'not_in': List[str],
        'lt': str,
        'lte': str,
        'gt': str,
        'gte': str,
        'contains': str,
        'startswith': str,
        'endswith': str,
        'in': List[str],
        'not': Union[str, 'StringFilterRecursive2'],
            },
    total=False,
)


StringFilterRecursive2 = TypedDict(
    'StringFilterRecursive2',
    {
        'equals': str,
        'not_in': List[str],
        'lt': str,
        'lte': str,
        'gt': str,
        'gte': str,
        'contains': str,
        'startswith': str,
        'endswith': str,
        'in': List[str],
        'not': Union[str, 'StringFilterRecursive3'],
            },
    total=False,
)


StringFilterRecursive3 = TypedDict(
    'StringFilterRecursive3',
    {
        'equals': str,
        'not_in': List[str],
        'lt': str,
        'lte': str,
        'gt': str,
        'gte': str,
        'contains': str,
        'startswith': str,
        'endswith': str,
        'in': List[str],
        'not': Union[str, 'StringFilterRecursive4'],
            },
    total=False,
)


StringFilterRecursive4 = TypedDict(
    'StringFilterRecursive4',
    {
        'equals': str,
        'not_in': List[str],
        'lt': str,
        'lte': str,
        'gt': str,
        'gte': str,
        'contains': str,
        'startswith': str,
        'endswith': str,
        'in': List[str],
                    },
    total=False,
)


class StringWithAggregatesFilter(StringFilter, total=False):
    _max: 'StringFilter'
    _min: 'StringFilter'
    _sum: 'StringFilter'
    _avg: 'StringFilter'
    _count: 'IntFilter'


    

DateTimeFilter = TypedDict(
    'DateTimeFilter',
    {
        'equals': datetime.datetime,
        'not_in': List[datetime.datetime],
        'lt': datetime.datetime,
        'lte': datetime.datetime,
        'gt': datetime.datetime,
        'gte': datetime.datetime,
        'in': List[datetime.datetime],
        'not': Union[datetime.datetime, 'DateTimeFilterRecursive1'],
    },
    total=False,
)


DateTimeFilterRecursive1 = TypedDict(
    'DateTimeFilterRecursive1',
    {
        'equals': datetime.datetime,
        'not_in': List[datetime.datetime],
        'lt': datetime.datetime,
        'lte': datetime.datetime,
        'gt': datetime.datetime,
        'gte': datetime.datetime,
        'in': List[datetime.datetime],
        'not': Union[datetime.datetime, 'DateTimeFilterRecursive2'],
    },
    total=False,
)


DateTimeFilterRecursive2 = TypedDict(
    'DateTimeFilterRecursive2',
    {
        'equals': datetime.datetime,
        'not_in': List[datetime.datetime],
        'lt': datetime.datetime,
        'lte': datetime.datetime,
        'gt': datetime.datetime,
        'gte': datetime.datetime,
        'in': List[datetime.datetime],
        'not': Union[datetime.datetime, 'DateTimeFilterRecursive3'],
    },
    total=False,
)


DateTimeFilterRecursive3 = TypedDict(
    'DateTimeFilterRecursive3',
    {
        'equals': datetime.datetime,
        'not_in': List[datetime.datetime],
        'lt': datetime.datetime,
        'lte': datetime.datetime,
        'gt': datetime.datetime,
        'gte': datetime.datetime,
        'in': List[datetime.datetime],
        'not': Union[datetime.datetime, 'DateTimeFilterRecursive4'],
    },
    total=False,
)


DateTimeFilterRecursive4 = TypedDict(
    'DateTimeFilterRecursive4',
    {
        'equals': datetime.datetime,
        'not_in': List[datetime.datetime],
        'lt': datetime.datetime,
        'lte': datetime.datetime,
        'gt': datetime.datetime,
        'gte': datetime.datetime,
        'in': List[datetime.datetime],
            },
    total=False,
)


class DateTimeWithAggregatesFilter(DateTimeFilter, total=False):
    _max: 'DateTimeFilter'
    _min: 'DateTimeFilter'
    _sum: 'DateTimeFilter'
    _avg: 'DateTimeFilter'
    _count: 'IntFilter'


    

BooleanFilter = TypedDict(
    'BooleanFilter',
    {
        'equals': bool,
        'not': Union[bool, 'BooleanFilterRecursive1'],
    },
    total=False,
)


BooleanFilterRecursive1 = TypedDict(
    'BooleanFilterRecursive1',
    {
        'equals': bool,
        'not': Union[bool, 'BooleanFilterRecursive2'],
    },
    total=False,
)


BooleanFilterRecursive2 = TypedDict(
    'BooleanFilterRecursive2',
    {
        'equals': bool,
        'not': Union[bool, 'BooleanFilterRecursive3'],
    },
    total=False,
)


BooleanFilterRecursive3 = TypedDict(
    'BooleanFilterRecursive3',
    {
        'equals': bool,
        'not': Union[bool, 'BooleanFilterRecursive4'],
    },
    total=False,
)


BooleanFilterRecursive4 = TypedDict(
    'BooleanFilterRecursive4',
    {
        'equals': bool,
            },
    total=False,
)


class BooleanWithAggregatesFilter(BooleanFilter, total=False):
    _max: 'BooleanFilter'
    _min: 'BooleanFilter'
    _sum: 'BooleanFilter'
    _avg: 'BooleanFilter'
    _count: 'IntFilter'


    

IntFilter = TypedDict(
    'IntFilter',
    {
        'equals': int,
        'not_in': List[int],
        'lt': int,
        'lte': int,
        'gt': int,
        'gte': int,
        'in': List[int],
        'not': Union[int, 'IntFilterRecursive1'],
    },
    total=False,
)


IntFilterRecursive1 = TypedDict(
    'IntFilterRecursive1',
    {
        'equals': int,
        'not_in': List[int],
        'lt': int,
        'lte': int,
        'gt': int,
        'gte': int,
        'in': List[int],
        'not': Union[int, 'IntFilterRecursive2'],
    },
    total=False,
)


IntFilterRecursive2 = TypedDict(
    'IntFilterRecursive2',
    {
        'equals': int,
        'not_in': List[int],
        'lt': int,
        'lte': int,
        'gt': int,
        'gte': int,
        'in': List[int],
        'not': Union[int, 'IntFilterRecursive3'],
    },
    total=False,
)


IntFilterRecursive3 = TypedDict(
    'IntFilterRecursive3',
    {
        'equals': int,
        'not_in': List[int],
        'lt': int,
        'lte': int,
        'gt': int,
        'gte': int,
        'in': List[int],
        'not': Union[int, 'IntFilterRecursive4'],
    },
    total=False,
)


IntFilterRecursive4 = TypedDict(
    'IntFilterRecursive4',
    {
        'equals': int,
        'not_in': List[int],
        'lt': int,
        'lte': int,
        'gt': int,
        'gte': int,
        'in': List[int],
            },
    total=False,
)


class IntWithAggregatesFilter(IntFilter, total=False):
    _max: 'IntFilter'
    _min: 'IntFilter'
    _sum: 'IntFilter'
    _avg: 'IntFilter'
    _count: 'IntFilter'


BigIntFilter = IntFilter
BigIntWithAggregatesFilter = IntWithAggregatesFilter
    

FloatFilter = TypedDict(
    'FloatFilter',
    {
        'equals': float,
        'not_in': List[float],
        'lt': float,
        'lte': float,
        'gt': float,
        'gte': float,
        'in': List[float],
        'not': Union[float, 'FloatFilterRecursive1'],
    },
    total=False,
)


FloatFilterRecursive1 = TypedDict(
    'FloatFilterRecursive1',
    {
        'equals': float,
        'not_in': List[float],
        'lt': float,
        'lte': float,
        'gt': float,
        'gte': float,
        'in': List[float],
        'not': Union[float, 'FloatFilterRecursive2'],
    },
    total=False,
)


FloatFilterRecursive2 = TypedDict(
    'FloatFilterRecursive2',
    {
        'equals': float,
        'not_in': List[float],
        'lt': float,
        'lte': float,
        'gt': float,
        'gte': float,
        'in': List[float],
        'not': Union[float, 'FloatFilterRecursive3'],
    },
    total=False,
)


FloatFilterRecursive3 = TypedDict(
    'FloatFilterRecursive3',
    {
        'equals': float,
        'not_in': List[float],
        'lt': float,
        'lte': float,
        'gt': float,
        'gte': float,
        'in': List[float],
        'not': Union[float, 'FloatFilterRecursive4'],
    },
    total=False,
)


FloatFilterRecursive4 = TypedDict(
    'FloatFilterRecursive4',
    {
        'equals': float,
        'not_in': List[float],
        'lt': float,
        'lte': float,
        'gt': float,
        'gte': float,
        'in': List[float],
            },
    total=False,
)


class FloatWithAggregatesFilter(FloatFilter, total=False):
    _max: 'FloatFilter'
    _min: 'FloatFilter'
    _sum: 'FloatFilter'
    _avg: 'FloatFilter'
    _count: 'IntFilter'


    

BytesFilter = TypedDict(
    'BytesFilter',
    {
        'equals': 'fields.Base64',
        'in': List['fields.Base64'],
        'not_in': List['fields.Base64'],
        'not': Union['fields.Base64', 'BytesFilterRecursive1'],
    },
    total=False,
)


BytesFilterRecursive1 = TypedDict(
    'BytesFilterRecursive1',
    {
        'equals': 'fields.Base64',
        'in': List['fields.Base64'],
        'not_in': List['fields.Base64'],
        'not': Union['fields.Base64', 'BytesFilterRecursive2'],
    },
    total=False,
)


BytesFilterRecursive2 = TypedDict(
    'BytesFilterRecursive2',
    {
        'equals': 'fields.Base64',
        'in': List['fields.Base64'],
        'not_in': List['fields.Base64'],
        'not': Union['fields.Base64', 'BytesFilterRecursive3'],
    },
    total=False,
)


BytesFilterRecursive3 = TypedDict(
    'BytesFilterRecursive3',
    {
        'equals': 'fields.Base64',
        'in': List['fields.Base64'],
        'not_in': List['fields.Base64'],
        'not': Union['fields.Base64', 'BytesFilterRecursive4'],
    },
    total=False,
)


BytesFilterRecursive4 = TypedDict(
    'BytesFilterRecursive4',
    {
        'equals': 'fields.Base64',
        'in': List['fields.Base64'],
        'not_in': List['fields.Base64'],
            },
    total=False,
)


class BytesWithAggregatesFilter(BytesFilter, total=False):
    _max: 'BytesFilter'
    _min: 'BytesFilter'
    _sum: 'BytesFilter'
    _avg: 'BytesFilter'
    _count: 'IntFilter'


# TODO: preview feature for improving JSON filtering
JsonFilter = TypedDict(
    'JsonFilter',
    {
        'equals': 'fields.Json',
        'not': 'fields.Json',
    },
    total=False,
)


class JsonWithAggregatesFilter(JsonFilter, total=False):
    _max: 'JsonFilter'
    _min: 'JsonFilter'
    _sum: 'JsonFilter'
    _avg: 'JsonFilter'
    _count: 'IntFilter'


    

DecimalFilter = TypedDict(
    'DecimalFilter',
    {
        'equals': decimal.Decimal,
        'not_in': List[decimal.Decimal],
        'lt': decimal.Decimal,
        'lte': decimal.Decimal,
        'gt': decimal.Decimal,
        'gte': decimal.Decimal,
        'in': List[decimal.Decimal],
        'not': Union[decimal.Decimal, 'DecimalFilterRecursive1'],
    },
    total=False,
)


DecimalFilterRecursive1 = TypedDict(
    'DecimalFilterRecursive1',
    {
        'equals': decimal.Decimal,
        'not_in': List[decimal.Decimal],
        'lt': decimal.Decimal,
        'lte': decimal.Decimal,
        'gt': decimal.Decimal,
        'gte': decimal.Decimal,
        'in': List[decimal.Decimal],
        'not': Union[decimal.Decimal, 'DecimalFilterRecursive2'],
    },
    total=False,
)


DecimalFilterRecursive2 = TypedDict(
    'DecimalFilterRecursive2',
    {
        'equals': decimal.Decimal,
        'not_in': List[decimal.Decimal],
        'lt': decimal.Decimal,
        'lte': decimal.Decimal,
        'gt': decimal.Decimal,
        'gte': decimal.Decimal,
        'in': List[decimal.Decimal],
        'not': Union[decimal.Decimal, 'DecimalFilterRecursive3'],
    },
    total=False,
)


DecimalFilterRecursive3 = TypedDict(
    'DecimalFilterRecursive3',
    {
        'equals': decimal.Decimal,
        'not_in': List[decimal.Decimal],
        'lt': decimal.Decimal,
        'lte': decimal.Decimal,
        'gt': decimal.Decimal,
        'gte': decimal.Decimal,
        'in': List[decimal.Decimal],
        'not': Union[decimal.Decimal, 'DecimalFilterRecursive4'],
    },
    total=False,
)


DecimalFilterRecursive4 = TypedDict(
    'DecimalFilterRecursive4',
    {
        'equals': decimal.Decimal,
        'not_in': List[decimal.Decimal],
        'lt': decimal.Decimal,
        'lte': decimal.Decimal,
        'gt': decimal.Decimal,
        'gte': decimal.Decimal,
        'in': List[decimal.Decimal],
            },
    total=False,
)


class DecimalWithAggregatesFilter(StringFilter, total=False):
    _max: 'DecimalFilter'
    _min: 'DecimalFilter'
    _sum: 'DecimalFilter'
    _avg: 'DecimalFilter'
    _count: 'IntFilter'


class _FloatSetInput(TypedDict):
    set: float


class _FloatDivideInput(TypedDict):
    divide: float


class _FloatMultiplyInput(TypedDict):
    multiply: float


class _FloatIncrementInput(TypedDict):
    increment: float


class _FloatDecrementInput(TypedDict):
    decrement: float


class _IntSetInput(TypedDict):
    set: int


class _IntDivideInput(TypedDict):
    divide: int


class _IntMultiplyInput(TypedDict):
    multiply: int


class _IntIncrementInput(TypedDict):
    increment: int


class _IntDecrementInput(TypedDict):
    decrement: int


AtomicFloatInput = Union[
    _FloatSetInput,
    _FloatDivideInput,
    _FloatMultiplyInput,
    _FloatIncrementInput,
    _FloatDecrementInput,
]
AtomicIntInput = Union[
    _IntSetInput,
    _IntDivideInput,
    _IntMultiplyInput,
    _IntIncrementInput,
    _IntDecrementInput,
]
AtomicBigIntInput = AtomicIntInput

class _StringListFilterEqualsInput(TypedDict):
    equals: Optional[List[_str]]


class _StringListFilterHasInput(TypedDict):
    has: _str


class _StringListFilterHasEveryInput(TypedDict):
    has_every: List[_str]


class _StringListFilterHasSomeInput(TypedDict):
    has_some: List[_str]


class _StringListFilterIsEmptyInput(TypedDict):
    is_empty: bool


StringListFilter = Union[
    _StringListFilterHasInput,
    _StringListFilterEqualsInput,
    _StringListFilterHasSomeInput,
    _StringListFilterIsEmptyInput,
    _StringListFilterHasEveryInput,
]


class _StringListUpdateSet(TypedDict):
    set: List[_str]


class _StringListUpdatePush(TypedDict):
    push: List[_str]


StringListUpdate = Union[
    List[_str],
    _StringListUpdateSet,
    _StringListUpdatePush,
]

class _BytesListFilterEqualsInput(TypedDict):
    equals: Optional[List['fields.Base64']]


class _BytesListFilterHasInput(TypedDict):
    has: 'fields.Base64'


class _BytesListFilterHasEveryInput(TypedDict):
    has_every: List['fields.Base64']


class _BytesListFilterHasSomeInput(TypedDict):
    has_some: List['fields.Base64']


class _BytesListFilterIsEmptyInput(TypedDict):
    is_empty: bool


BytesListFilter = Union[
    _BytesListFilterHasInput,
    _BytesListFilterEqualsInput,
    _BytesListFilterHasSomeInput,
    _BytesListFilterIsEmptyInput,
    _BytesListFilterHasEveryInput,
]


class _BytesListUpdateSet(TypedDict):
    set: List['fields.Base64']


class _BytesListUpdatePush(TypedDict):
    push: List['fields.Base64']


BytesListUpdate = Union[
    List['fields.Base64'],
    _BytesListUpdateSet,
    _BytesListUpdatePush,
]

class _DateTimeListFilterEqualsInput(TypedDict):
    equals: Optional[List[datetime.datetime]]


class _DateTimeListFilterHasInput(TypedDict):
    has: datetime.datetime


class _DateTimeListFilterHasEveryInput(TypedDict):
    has_every: List[datetime.datetime]


class _DateTimeListFilterHasSomeInput(TypedDict):
    has_some: List[datetime.datetime]


class _DateTimeListFilterIsEmptyInput(TypedDict):
    is_empty: bool


DateTimeListFilter = Union[
    _DateTimeListFilterHasInput,
    _DateTimeListFilterEqualsInput,
    _DateTimeListFilterHasSomeInput,
    _DateTimeListFilterIsEmptyInput,
    _DateTimeListFilterHasEveryInput,
]


class _DateTimeListUpdateSet(TypedDict):
    set: List[datetime.datetime]


class _DateTimeListUpdatePush(TypedDict):
    push: List[datetime.datetime]


DateTimeListUpdate = Union[
    List[datetime.datetime],
    _DateTimeListUpdateSet,
    _DateTimeListUpdatePush,
]

class _BooleanListFilterEqualsInput(TypedDict):
    equals: Optional[List[_bool]]


class _BooleanListFilterHasInput(TypedDict):
    has: _bool


class _BooleanListFilterHasEveryInput(TypedDict):
    has_every: List[_bool]


class _BooleanListFilterHasSomeInput(TypedDict):
    has_some: List[_bool]


class _BooleanListFilterIsEmptyInput(TypedDict):
    is_empty: bool


BooleanListFilter = Union[
    _BooleanListFilterHasInput,
    _BooleanListFilterEqualsInput,
    _BooleanListFilterHasSomeInput,
    _BooleanListFilterIsEmptyInput,
    _BooleanListFilterHasEveryInput,
]


class _BooleanListUpdateSet(TypedDict):
    set: List[_bool]


class _BooleanListUpdatePush(TypedDict):
    push: List[_bool]


BooleanListUpdate = Union[
    List[_bool],
    _BooleanListUpdateSet,
    _BooleanListUpdatePush,
]

class _IntListFilterEqualsInput(TypedDict):
    equals: Optional[List[_int]]


class _IntListFilterHasInput(TypedDict):
    has: _int


class _IntListFilterHasEveryInput(TypedDict):
    has_every: List[_int]


class _IntListFilterHasSomeInput(TypedDict):
    has_some: List[_int]


class _IntListFilterIsEmptyInput(TypedDict):
    is_empty: bool


IntListFilter = Union[
    _IntListFilterHasInput,
    _IntListFilterEqualsInput,
    _IntListFilterHasSomeInput,
    _IntListFilterIsEmptyInput,
    _IntListFilterHasEveryInput,
]


class _IntListUpdateSet(TypedDict):
    set: List[_int]


class _IntListUpdatePush(TypedDict):
    push: List[_int]


IntListUpdate = Union[
    List[_int],
    _IntListUpdateSet,
    _IntListUpdatePush,
]

class _BigIntListFilterEqualsInput(TypedDict):
    equals: Optional[List[_int]]


class _BigIntListFilterHasInput(TypedDict):
    has: _int


class _BigIntListFilterHasEveryInput(TypedDict):
    has_every: List[_int]


class _BigIntListFilterHasSomeInput(TypedDict):
    has_some: List[_int]


class _BigIntListFilterIsEmptyInput(TypedDict):
    is_empty: bool


BigIntListFilter = Union[
    _BigIntListFilterHasInput,
    _BigIntListFilterEqualsInput,
    _BigIntListFilterHasSomeInput,
    _BigIntListFilterIsEmptyInput,
    _BigIntListFilterHasEveryInput,
]


class _BigIntListUpdateSet(TypedDict):
    set: List[_int]


class _BigIntListUpdatePush(TypedDict):
    push: List[_int]


BigIntListUpdate = Union[
    List[_int],
    _BigIntListUpdateSet,
    _BigIntListUpdatePush,
]

class _FloatListFilterEqualsInput(TypedDict):
    equals: Optional[List[_float]]


class _FloatListFilterHasInput(TypedDict):
    has: _float


class _FloatListFilterHasEveryInput(TypedDict):
    has_every: List[_float]


class _FloatListFilterHasSomeInput(TypedDict):
    has_some: List[_float]


class _FloatListFilterIsEmptyInput(TypedDict):
    is_empty: bool


FloatListFilter = Union[
    _FloatListFilterHasInput,
    _FloatListFilterEqualsInput,
    _FloatListFilterHasSomeInput,
    _FloatListFilterIsEmptyInput,
    _FloatListFilterHasEveryInput,
]


class _FloatListUpdateSet(TypedDict):
    set: List[_float]


class _FloatListUpdatePush(TypedDict):
    push: List[_float]


FloatListUpdate = Union[
    List[_float],
    _FloatListUpdateSet,
    _FloatListUpdatePush,
]

class _JsonListFilterEqualsInput(TypedDict):
    equals: Optional[List['fields.Json']]


class _JsonListFilterHasInput(TypedDict):
    has: 'fields.Json'


class _JsonListFilterHasEveryInput(TypedDict):
    has_every: List['fields.Json']


class _JsonListFilterHasSomeInput(TypedDict):
    has_some: List['fields.Json']


class _JsonListFilterIsEmptyInput(TypedDict):
    is_empty: bool


JsonListFilter = Union[
    _JsonListFilterHasInput,
    _JsonListFilterEqualsInput,
    _JsonListFilterHasSomeInput,
    _JsonListFilterIsEmptyInput,
    _JsonListFilterHasEveryInput,
]


class _JsonListUpdateSet(TypedDict):
    set: List['fields.Json']


class _JsonListUpdatePush(TypedDict):
    push: List['fields.Json']


JsonListUpdate = Union[
    List['fields.Json'],
    _JsonListUpdateSet,
    _JsonListUpdatePush,
]

class _DecimalListFilterEqualsInput(TypedDict):
    equals: Optional[List[decimal.Decimal]]


class _DecimalListFilterHasInput(TypedDict):
    has: decimal.Decimal


class _DecimalListFilterHasEveryInput(TypedDict):
    has_every: List[decimal.Decimal]


class _DecimalListFilterHasSomeInput(TypedDict):
    has_some: List[decimal.Decimal]


class _DecimalListFilterIsEmptyInput(TypedDict):
    is_empty: bool


DecimalListFilter = Union[
    _DecimalListFilterHasInput,
    _DecimalListFilterEqualsInput,
    _DecimalListFilterHasSomeInput,
    _DecimalListFilterIsEmptyInput,
    _DecimalListFilterHasEveryInput,
]


class _DecimalListUpdateSet(TypedDict):
    set: List[decimal.Decimal]


class _DecimalListUpdatePush(TypedDict):
    push: List[decimal.Decimal]


DecimalListUpdate = Union[
    List[decimal.Decimal],
    _DecimalListUpdateSet,
    _DecimalListUpdatePush,
]


# Measurement types

class MeasurementOptionalCreateInput(TypedDict, total=False):
    """Optional arguments to the Measurement create method"""
    measurement_id: _str


class MeasurementCreateInput(MeasurementOptionalCreateInput):
    """Required arguments to the Measurement create method"""
    patient_id: _str
    blood_pressure: _float
    temperature: _str


# TODO: remove this in favour of without explicit relations
# e.g. PostCreateWithoutAuthorInput

class MeasurementOptionalCreateWithoutRelationsInput(TypedDict, total=False):
    """Optional arguments to the Measurement create method, without relations"""
    measurement_id: _str


class MeasurementCreateWithoutRelationsInput(MeasurementOptionalCreateWithoutRelationsInput):
    """Required arguments to the Measurement create method, without relations"""
    patient_id: _str
    blood_pressure: _float
    temperature: _str


class MeasurementCreateNestedWithoutRelationsInput(TypedDict, total=False):
    create: 'MeasurementCreateWithoutRelationsInput'
    connect: 'MeasurementWhereUniqueInput'


class MeasurementCreateManyNestedWithoutRelationsInput(TypedDict, total=False):
    create: Union['MeasurementCreateWithoutRelationsInput', List['MeasurementCreateWithoutRelationsInput']]
    connect: Union['MeasurementWhereUniqueInput', List['MeasurementWhereUniqueInput']]


_MeasurementWhereUnique_measurement_id_Input = TypedDict(
    '_MeasurementWhereUnique_measurement_id_Input',
    {
        'measurement_id': '_str',
    },
    total=True
)

MeasurementWhereUniqueInput = _MeasurementWhereUnique_measurement_id_Input


class MeasurementUpdateInput(TypedDict, total=False):
    """Optional arguments for updating a record"""
    measurement_id: _str
    patient_id: _str
    blood_pressure: Union[AtomicFloatInput, _float]
    temperature: _str


class MeasurementUpdateManyMutationInput(TypedDict, total=False):
    """Arguments for updating many records"""
    measurement_id: _str
    patient_id: _str
    blood_pressure: Union[AtomicFloatInput, _float]
    temperature: _str


class MeasurementUpdateManyWithoutRelationsInput(TypedDict, total=False):
    create: List['MeasurementCreateWithoutRelationsInput']
    connect: List['MeasurementWhereUniqueInput']
    set: List['MeasurementWhereUniqueInput']
    disconnect: List['MeasurementWhereUniqueInput']
    delete: List['MeasurementWhereUniqueInput']

    # TODO
    # update: List['MeasurementUpdateWithWhereUniqueWithoutRelationsInput']
    # updateMany: List['MeasurementUpdateManyWithWhereUniqueWithoutRelationsInput']
    # deleteMany: List['MeasurementScalarWhereInput']
    # upsert: List['MeasurementUpserteWithWhereUniqueWithoutRelationsInput']
    # connectOrCreate: List['MeasurementCreateOrConnectWithoutRelationsInput']


class MeasurementUpdateOneWithoutRelationsInput(TypedDict, total=False):
    create: 'MeasurementCreateWithoutRelationsInput'
    connect: 'MeasurementWhereUniqueInput'
    disconnect: bool
    delete: bool

    # TODO
    # update: 'MeasurementUpdateInput'
    # upsert: 'MeasurementUpsertWithoutRelationsInput'
    # connectOrCreate: 'MeasurementCreateOrConnectWithoutRelationsInput'


class MeasurementUpsertInput(TypedDict):
    create: 'MeasurementCreateInput'
    update: 'MeasurementUpdateInput'  # pyright: ignore[reportIncompatibleMethodOverride]


_Measurement_measurement_id_OrderByInput = TypedDict(
    '_Measurement_measurement_id_OrderByInput',
    {
        'measurement_id': 'SortOrder',
    },
    total=True
)

_Measurement_patient_id_OrderByInput = TypedDict(
    '_Measurement_patient_id_OrderByInput',
    {
        'patient_id': 'SortOrder',
    },
    total=True
)

_Measurement_blood_pressure_OrderByInput = TypedDict(
    '_Measurement_blood_pressure_OrderByInput',
    {
        'blood_pressure': 'SortOrder',
    },
    total=True
)

_Measurement_temperature_OrderByInput = TypedDict(
    '_Measurement_temperature_OrderByInput',
    {
        'temperature': 'SortOrder',
    },
    total=True
)

MeasurementOrderByInput = Union[
    '_Measurement_measurement_id_OrderByInput',
    '_Measurement_patient_id_OrderByInput',
    '_Measurement_blood_pressure_OrderByInput',
    '_Measurement_temperature_OrderByInput',
]



# recursive Measurement types
# TODO: cleanup these types


# Dict[str, Any] is a mypy limitation
# see https://github.com/RobertCraigie/prisma-client-py/issues/45
# switch to pyright for improved types, see https://prisma-client-py.readthedocs.io/en/stable/reference/limitations/

MeasurementRelationFilter = TypedDict(
    'MeasurementRelationFilter',
    {
        'is': 'Dict[str, Any]',
        'is_not': 'Dict[str, Any]',
    },
    total=False,
)


class MeasurementListRelationFilter(TypedDict, total=False):
    some: 'Dict[str, Any]'
    none: 'Dict[str, Any]'
    every: 'Dict[str, Any]'


class MeasurementInclude(TypedDict, total=False):
    """Measurement relational arguments"""


    

class MeasurementIncludeFromMeasurement(TypedDict, total=False):
    """Relational arguments for Measurement"""


class MeasurementIncludeFromMeasurementRecursive1(TypedDict, total=False):
    """Relational arguments for Measurement"""


class MeasurementIncludeFromMeasurementRecursive2(TypedDict, total=False):
    """Relational arguments for Measurement"""


class MeasurementIncludeFromMeasurementRecursive3(TypedDict, total=False):
    """Relational arguments for Measurement"""


class MeasurementIncludeFromMeasurementRecursive4(TypedDict, total=False):
    """Relational arguments for Measurement"""

    

class MeasurementArgsFromMeasurement(TypedDict, total=False):
    """Arguments for Measurement"""
    include: 'MeasurementIncludeFromMeasurementRecursive1'


class MeasurementArgsFromMeasurementRecursive1(TypedDict, total=False):
    """Arguments for Measurement"""
    include: 'MeasurementIncludeFromMeasurementRecursive2'


class MeasurementArgsFromMeasurementRecursive2(TypedDict, total=False):
    """Arguments for Measurement"""
    include: 'MeasurementIncludeFromMeasurementRecursive3'


class MeasurementArgsFromMeasurementRecursive3(TypedDict, total=False):
    """Arguments for Measurement"""
    include: 'MeasurementIncludeFromMeasurementRecursive4'


class MeasurementArgsFromMeasurementRecursive4(TypedDict, total=False):
    """Arguments for Measurement"""
    
    

class FindManyMeasurementArgsFromMeasurement(TypedDict, total=False):
    """Arguments for Measurement"""
    take: int
    skip: int
    order_by: Union['MeasurementOrderByInput', List['MeasurementOrderByInput']]
    where: 'MeasurementWhereInput'
    cursor: 'MeasurementWhereUniqueInput'
    distinct: List['MeasurementScalarFieldKeys']
    include: 'MeasurementIncludeFromMeasurementRecursive1'


class FindManyMeasurementArgsFromMeasurementRecursive1(TypedDict, total=False):
    """Arguments for Measurement"""
    take: int
    skip: int
    order_by: Union['MeasurementOrderByInput', List['MeasurementOrderByInput']]
    where: 'MeasurementWhereInput'
    cursor: 'MeasurementWhereUniqueInput'
    distinct: List['MeasurementScalarFieldKeys']
    include: 'MeasurementIncludeFromMeasurementRecursive2'


class FindManyMeasurementArgsFromMeasurementRecursive2(TypedDict, total=False):
    """Arguments for Measurement"""
    take: int
    skip: int
    order_by: Union['MeasurementOrderByInput', List['MeasurementOrderByInput']]
    where: 'MeasurementWhereInput'
    cursor: 'MeasurementWhereUniqueInput'
    distinct: List['MeasurementScalarFieldKeys']
    include: 'MeasurementIncludeFromMeasurementRecursive3'


class FindManyMeasurementArgsFromMeasurementRecursive3(TypedDict, total=False):
    """Arguments for Measurement"""
    take: int
    skip: int
    order_by: Union['MeasurementOrderByInput', List['MeasurementOrderByInput']]
    where: 'MeasurementWhereInput'
    cursor: 'MeasurementWhereUniqueInput'
    distinct: List['MeasurementScalarFieldKeys']
    include: 'MeasurementIncludeFromMeasurementRecursive4'


class FindManyMeasurementArgsFromMeasurementRecursive4(TypedDict, total=False):
    """Arguments for Measurement"""
    take: int
    skip: int
    order_by: Union['MeasurementOrderByInput', List['MeasurementOrderByInput']]
    where: 'MeasurementWhereInput'
    cursor: 'MeasurementWhereUniqueInput'
    distinct: List['MeasurementScalarFieldKeys']
    


FindManyMeasurementArgs = FindManyMeasurementArgsFromMeasurement
FindFirstMeasurementArgs = FindManyMeasurementArgsFromMeasurement


    

class MeasurementWhereInput(TypedDict, total=False):
    """Measurement arguments for searching"""
    measurement_id: Union[_str, 'types.StringFilter']
    patient_id: Union[_str, 'types.StringFilter']
    blood_pressure: Union[_float, 'types.FloatFilter']
    temperature: Union[_str, 'types.StringFilter']

    # should be noted that AND and NOT should be Union['MeasurementWhereInputRecursive1', List['MeasurementWhereInputRecursive1']]
    # but this causes mypy to hang :/
    AND: List['MeasurementWhereInputRecursive1']
    OR: List['MeasurementWhereInputRecursive1']
    NOT: List['MeasurementWhereInputRecursive1']


class MeasurementWhereInputRecursive1(TypedDict, total=False):
    """Measurement arguments for searching"""
    measurement_id: Union[_str, 'types.StringFilter']
    patient_id: Union[_str, 'types.StringFilter']
    blood_pressure: Union[_float, 'types.FloatFilter']
    temperature: Union[_str, 'types.StringFilter']

    # should be noted that AND and NOT should be Union['MeasurementWhereInputRecursive2', List['MeasurementWhereInputRecursive2']]
    # but this causes mypy to hang :/
    AND: List['MeasurementWhereInputRecursive2']
    OR: List['MeasurementWhereInputRecursive2']
    NOT: List['MeasurementWhereInputRecursive2']


class MeasurementWhereInputRecursive2(TypedDict, total=False):
    """Measurement arguments for searching"""
    measurement_id: Union[_str, 'types.StringFilter']
    patient_id: Union[_str, 'types.StringFilter']
    blood_pressure: Union[_float, 'types.FloatFilter']
    temperature: Union[_str, 'types.StringFilter']

    # should be noted that AND and NOT should be Union['MeasurementWhereInputRecursive3', List['MeasurementWhereInputRecursive3']]
    # but this causes mypy to hang :/
    AND: List['MeasurementWhereInputRecursive3']
    OR: List['MeasurementWhereInputRecursive3']
    NOT: List['MeasurementWhereInputRecursive3']


class MeasurementWhereInputRecursive3(TypedDict, total=False):
    """Measurement arguments for searching"""
    measurement_id: Union[_str, 'types.StringFilter']
    patient_id: Union[_str, 'types.StringFilter']
    blood_pressure: Union[_float, 'types.FloatFilter']
    temperature: Union[_str, 'types.StringFilter']

    # should be noted that AND and NOT should be Union['MeasurementWhereInputRecursive4', List['MeasurementWhereInputRecursive4']]
    # but this causes mypy to hang :/
    AND: List['MeasurementWhereInputRecursive4']
    OR: List['MeasurementWhereInputRecursive4']
    NOT: List['MeasurementWhereInputRecursive4']


class MeasurementWhereInputRecursive4(TypedDict, total=False):
    """Measurement arguments for searching"""
    measurement_id: Union[_str, 'types.StringFilter']
    patient_id: Union[_str, 'types.StringFilter']
    blood_pressure: Union[_float, 'types.FloatFilter']
    temperature: Union[_str, 'types.StringFilter']



# aggregate Measurement types


    

class MeasurementScalarWhereWithAggregatesInput(TypedDict, total=False):
    """Measurement arguments for searching"""
    measurement_id: Union[_str, 'types.StringWithAggregatesFilter']
    patient_id: Union[_str, 'types.StringWithAggregatesFilter']
    blood_pressure: Union[_float, 'types.FloatWithAggregatesFilter']
    temperature: Union[_str, 'types.StringWithAggregatesFilter']

    AND: List['MeasurementScalarWhereWithAggregatesInputRecursive1']
    OR: List['MeasurementScalarWhereWithAggregatesInputRecursive1']
    NOT: List['MeasurementScalarWhereWithAggregatesInputRecursive1']


class MeasurementScalarWhereWithAggregatesInputRecursive1(TypedDict, total=False):
    """Measurement arguments for searching"""
    measurement_id: Union[_str, 'types.StringWithAggregatesFilter']
    patient_id: Union[_str, 'types.StringWithAggregatesFilter']
    blood_pressure: Union[_float, 'types.FloatWithAggregatesFilter']
    temperature: Union[_str, 'types.StringWithAggregatesFilter']

    AND: List['MeasurementScalarWhereWithAggregatesInputRecursive2']
    OR: List['MeasurementScalarWhereWithAggregatesInputRecursive2']
    NOT: List['MeasurementScalarWhereWithAggregatesInputRecursive2']


class MeasurementScalarWhereWithAggregatesInputRecursive2(TypedDict, total=False):
    """Measurement arguments for searching"""
    measurement_id: Union[_str, 'types.StringWithAggregatesFilter']
    patient_id: Union[_str, 'types.StringWithAggregatesFilter']
    blood_pressure: Union[_float, 'types.FloatWithAggregatesFilter']
    temperature: Union[_str, 'types.StringWithAggregatesFilter']

    AND: List['MeasurementScalarWhereWithAggregatesInputRecursive3']
    OR: List['MeasurementScalarWhereWithAggregatesInputRecursive3']
    NOT: List['MeasurementScalarWhereWithAggregatesInputRecursive3']


class MeasurementScalarWhereWithAggregatesInputRecursive3(TypedDict, total=False):
    """Measurement arguments for searching"""
    measurement_id: Union[_str, 'types.StringWithAggregatesFilter']
    patient_id: Union[_str, 'types.StringWithAggregatesFilter']
    blood_pressure: Union[_float, 'types.FloatWithAggregatesFilter']
    temperature: Union[_str, 'types.StringWithAggregatesFilter']

    AND: List['MeasurementScalarWhereWithAggregatesInputRecursive4']
    OR: List['MeasurementScalarWhereWithAggregatesInputRecursive4']
    NOT: List['MeasurementScalarWhereWithAggregatesInputRecursive4']


class MeasurementScalarWhereWithAggregatesInputRecursive4(TypedDict, total=False):
    """Measurement arguments for searching"""
    measurement_id: Union[_str, 'types.StringWithAggregatesFilter']
    patient_id: Union[_str, 'types.StringWithAggregatesFilter']
    blood_pressure: Union[_float, 'types.FloatWithAggregatesFilter']
    temperature: Union[_str, 'types.StringWithAggregatesFilter']



class MeasurementGroupByOutput(TypedDict, total=False):
    measurement_id: _str
    patient_id: _str
    blood_pressure: _float
    temperature: _str
    _sum: 'MeasurementSumAggregateOutput'
    _avg: 'MeasurementAvgAggregateOutput'
    _min: 'MeasurementMinAggregateOutput'
    _max: 'MeasurementMaxAggregateOutput'
    _count: 'MeasurementCountAggregateOutput'


class MeasurementAvgAggregateOutput(TypedDict, total=False):
    """Measurement output for aggregating averages"""
    blood_pressure: float


class MeasurementSumAggregateOutput(TypedDict, total=False):
    """Measurement output for aggregating sums"""
    blood_pressure: _float


class MeasurementScalarAggregateOutput(TypedDict, total=False):
    """Measurement output including scalar fields"""
    measurement_id: _str
    patient_id: _str
    blood_pressure: _float
    temperature: _str


MeasurementMinAggregateOutput = MeasurementScalarAggregateOutput
MeasurementMaxAggregateOutput = MeasurementScalarAggregateOutput


class MeasurementMaxAggregateInput(TypedDict, total=False):
    """Measurement input for aggregating by max"""
    measurement_id: bool
    patient_id: bool
    blood_pressure: bool
    temperature: bool


class MeasurementMinAggregateInput(TypedDict, total=False):
    """Measurement input for aggregating by min"""
    measurement_id: bool
    patient_id: bool
    blood_pressure: bool
    temperature: bool


class MeasurementNumberAggregateInput(TypedDict, total=False):
    """Measurement input for aggregating numbers"""
    blood_pressure: bool


MeasurementAvgAggregateInput = MeasurementNumberAggregateInput
MeasurementSumAggregateInput = MeasurementNumberAggregateInput


MeasurementCountAggregateInput = TypedDict(
    'MeasurementCountAggregateInput',
    {
        'measurement_id': bool,
        'patient_id': bool,
        'blood_pressure': bool,
        'temperature': bool,
        '_all': bool,
    },
    total=False,
)

MeasurementCountAggregateOutput = TypedDict(
    'MeasurementCountAggregateOutput',
    {
        'measurement_id': int,
        'patient_id': int,
        'blood_pressure': int,
        'temperature': int,
        '_all': int,
    },
    total=False,
)


MeasurementKeys = Literal[
    'measurement_id',
    'patient_id',
    'blood_pressure',
    'temperature',
]
MeasurementScalarFieldKeys = Literal[
    'measurement_id',
    'patient_id',
    'blood_pressure',
    'temperature',
]
MeasurementScalarFieldKeysT = TypeVar('MeasurementScalarFieldKeysT', bound=MeasurementScalarFieldKeys)

MeasurementRelationalFieldKeys = _NoneType



# we have to import ourselves as types can be namespaced to types
from . import types, enums, models, fields