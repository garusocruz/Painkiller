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


# Patient types

class PatientOptionalCreateInput(TypedDict, total=False):
    """Optional arguments to the Patient create method"""
    patient_id: _str


class PatientCreateInput(PatientOptionalCreateInput):
    """Required arguments to the Patient create method"""
    first_name: _str
    last_name: _str
    age: _int
    condition: _str


# TODO: remove this in favour of without explicit relations
# e.g. PostCreateWithoutAuthorInput

class PatientOptionalCreateWithoutRelationsInput(TypedDict, total=False):
    """Optional arguments to the Patient create method, without relations"""
    patient_id: _str


class PatientCreateWithoutRelationsInput(PatientOptionalCreateWithoutRelationsInput):
    """Required arguments to the Patient create method, without relations"""
    first_name: _str
    last_name: _str
    age: _int
    condition: _str


class PatientCreateNestedWithoutRelationsInput(TypedDict, total=False):
    create: 'PatientCreateWithoutRelationsInput'
    connect: 'PatientWhereUniqueInput'


class PatientCreateManyNestedWithoutRelationsInput(TypedDict, total=False):
    create: Union['PatientCreateWithoutRelationsInput', List['PatientCreateWithoutRelationsInput']]
    connect: Union['PatientWhereUniqueInput', List['PatientWhereUniqueInput']]


_PatientWhereUnique_patient_id_Input = TypedDict(
    '_PatientWhereUnique_patient_id_Input',
    {
        'patient_id': '_str',
    },
    total=True
)

PatientWhereUniqueInput = _PatientWhereUnique_patient_id_Input


class PatientUpdateInput(TypedDict, total=False):
    """Optional arguments for updating a record"""
    patient_id: _str
    first_name: _str
    last_name: _str
    age: Union[AtomicIntInput, _int]
    condition: _str


class PatientUpdateManyMutationInput(TypedDict, total=False):
    """Arguments for updating many records"""
    patient_id: _str
    first_name: _str
    last_name: _str
    age: Union[AtomicIntInput, _int]
    condition: _str


class PatientUpdateManyWithoutRelationsInput(TypedDict, total=False):
    create: List['PatientCreateWithoutRelationsInput']
    connect: List['PatientWhereUniqueInput']
    set: List['PatientWhereUniqueInput']
    disconnect: List['PatientWhereUniqueInput']
    delete: List['PatientWhereUniqueInput']

    # TODO
    # update: List['PatientUpdateWithWhereUniqueWithoutRelationsInput']
    # updateMany: List['PatientUpdateManyWithWhereUniqueWithoutRelationsInput']
    # deleteMany: List['PatientScalarWhereInput']
    # upsert: List['PatientUpserteWithWhereUniqueWithoutRelationsInput']
    # connectOrCreate: List['PatientCreateOrConnectWithoutRelationsInput']


class PatientUpdateOneWithoutRelationsInput(TypedDict, total=False):
    create: 'PatientCreateWithoutRelationsInput'
    connect: 'PatientWhereUniqueInput'
    disconnect: bool
    delete: bool

    # TODO
    # update: 'PatientUpdateInput'
    # upsert: 'PatientUpsertWithoutRelationsInput'
    # connectOrCreate: 'PatientCreateOrConnectWithoutRelationsInput'


class PatientUpsertInput(TypedDict):
    create: 'PatientCreateInput'
    update: 'PatientUpdateInput'  # pyright: ignore[reportIncompatibleMethodOverride]


_Patient_patient_id_OrderByInput = TypedDict(
    '_Patient_patient_id_OrderByInput',
    {
        'patient_id': 'SortOrder',
    },
    total=True
)

_Patient_first_name_OrderByInput = TypedDict(
    '_Patient_first_name_OrderByInput',
    {
        'first_name': 'SortOrder',
    },
    total=True
)

_Patient_last_name_OrderByInput = TypedDict(
    '_Patient_last_name_OrderByInput',
    {
        'last_name': 'SortOrder',
    },
    total=True
)

_Patient_age_OrderByInput = TypedDict(
    '_Patient_age_OrderByInput',
    {
        'age': 'SortOrder',
    },
    total=True
)

_Patient_condition_OrderByInput = TypedDict(
    '_Patient_condition_OrderByInput',
    {
        'condition': 'SortOrder',
    },
    total=True
)

PatientOrderByInput = Union[
    '_Patient_patient_id_OrderByInput',
    '_Patient_first_name_OrderByInput',
    '_Patient_last_name_OrderByInput',
    '_Patient_age_OrderByInput',
    '_Patient_condition_OrderByInput',
]



# recursive Patient types
# TODO: cleanup these types


# Dict[str, Any] is a mypy limitation
# see https://github.com/RobertCraigie/prisma-client-py/issues/45
# switch to pyright for improved types, see https://prisma-client-py.readthedocs.io/en/stable/reference/limitations/

PatientRelationFilter = TypedDict(
    'PatientRelationFilter',
    {
        'is': 'Dict[str, Any]',
        'is_not': 'Dict[str, Any]',
    },
    total=False,
)


class PatientListRelationFilter(TypedDict, total=False):
    some: 'Dict[str, Any]'
    none: 'Dict[str, Any]'
    every: 'Dict[str, Any]'


class PatientInclude(TypedDict, total=False):
    """Patient relational arguments"""


    

class PatientIncludeFromPatient(TypedDict, total=False):
    """Relational arguments for Patient"""


class PatientIncludeFromPatientRecursive1(TypedDict, total=False):
    """Relational arguments for Patient"""


class PatientIncludeFromPatientRecursive2(TypedDict, total=False):
    """Relational arguments for Patient"""


class PatientIncludeFromPatientRecursive3(TypedDict, total=False):
    """Relational arguments for Patient"""


class PatientIncludeFromPatientRecursive4(TypedDict, total=False):
    """Relational arguments for Patient"""

    

class PatientArgsFromPatient(TypedDict, total=False):
    """Arguments for Patient"""
    include: 'PatientIncludeFromPatientRecursive1'


class PatientArgsFromPatientRecursive1(TypedDict, total=False):
    """Arguments for Patient"""
    include: 'PatientIncludeFromPatientRecursive2'


class PatientArgsFromPatientRecursive2(TypedDict, total=False):
    """Arguments for Patient"""
    include: 'PatientIncludeFromPatientRecursive3'


class PatientArgsFromPatientRecursive3(TypedDict, total=False):
    """Arguments for Patient"""
    include: 'PatientIncludeFromPatientRecursive4'


class PatientArgsFromPatientRecursive4(TypedDict, total=False):
    """Arguments for Patient"""
    
    

class FindManyPatientArgsFromPatient(TypedDict, total=False):
    """Arguments for Patient"""
    take: int
    skip: int
    order_by: Union['PatientOrderByInput', List['PatientOrderByInput']]
    where: 'PatientWhereInput'
    cursor: 'PatientWhereUniqueInput'
    distinct: List['PatientScalarFieldKeys']
    include: 'PatientIncludeFromPatientRecursive1'


class FindManyPatientArgsFromPatientRecursive1(TypedDict, total=False):
    """Arguments for Patient"""
    take: int
    skip: int
    order_by: Union['PatientOrderByInput', List['PatientOrderByInput']]
    where: 'PatientWhereInput'
    cursor: 'PatientWhereUniqueInput'
    distinct: List['PatientScalarFieldKeys']
    include: 'PatientIncludeFromPatientRecursive2'


class FindManyPatientArgsFromPatientRecursive2(TypedDict, total=False):
    """Arguments for Patient"""
    take: int
    skip: int
    order_by: Union['PatientOrderByInput', List['PatientOrderByInput']]
    where: 'PatientWhereInput'
    cursor: 'PatientWhereUniqueInput'
    distinct: List['PatientScalarFieldKeys']
    include: 'PatientIncludeFromPatientRecursive3'


class FindManyPatientArgsFromPatientRecursive3(TypedDict, total=False):
    """Arguments for Patient"""
    take: int
    skip: int
    order_by: Union['PatientOrderByInput', List['PatientOrderByInput']]
    where: 'PatientWhereInput'
    cursor: 'PatientWhereUniqueInput'
    distinct: List['PatientScalarFieldKeys']
    include: 'PatientIncludeFromPatientRecursive4'


class FindManyPatientArgsFromPatientRecursive4(TypedDict, total=False):
    """Arguments for Patient"""
    take: int
    skip: int
    order_by: Union['PatientOrderByInput', List['PatientOrderByInput']]
    where: 'PatientWhereInput'
    cursor: 'PatientWhereUniqueInput'
    distinct: List['PatientScalarFieldKeys']
    


FindManyPatientArgs = FindManyPatientArgsFromPatient
FindFirstPatientArgs = FindManyPatientArgsFromPatient


    

class PatientWhereInput(TypedDict, total=False):
    """Patient arguments for searching"""
    patient_id: Union[_str, 'types.StringFilter']
    first_name: Union[_str, 'types.StringFilter']
    last_name: Union[_str, 'types.StringFilter']
    age: Union[_int, 'types.IntFilter']
    condition: Union[_str, 'types.StringFilter']

    # should be noted that AND and NOT should be Union['PatientWhereInputRecursive1', List['PatientWhereInputRecursive1']]
    # but this causes mypy to hang :/
    AND: List['PatientWhereInputRecursive1']
    OR: List['PatientWhereInputRecursive1']
    NOT: List['PatientWhereInputRecursive1']


class PatientWhereInputRecursive1(TypedDict, total=False):
    """Patient arguments for searching"""
    patient_id: Union[_str, 'types.StringFilter']
    first_name: Union[_str, 'types.StringFilter']
    last_name: Union[_str, 'types.StringFilter']
    age: Union[_int, 'types.IntFilter']
    condition: Union[_str, 'types.StringFilter']

    # should be noted that AND and NOT should be Union['PatientWhereInputRecursive2', List['PatientWhereInputRecursive2']]
    # but this causes mypy to hang :/
    AND: List['PatientWhereInputRecursive2']
    OR: List['PatientWhereInputRecursive2']
    NOT: List['PatientWhereInputRecursive2']


class PatientWhereInputRecursive2(TypedDict, total=False):
    """Patient arguments for searching"""
    patient_id: Union[_str, 'types.StringFilter']
    first_name: Union[_str, 'types.StringFilter']
    last_name: Union[_str, 'types.StringFilter']
    age: Union[_int, 'types.IntFilter']
    condition: Union[_str, 'types.StringFilter']

    # should be noted that AND and NOT should be Union['PatientWhereInputRecursive3', List['PatientWhereInputRecursive3']]
    # but this causes mypy to hang :/
    AND: List['PatientWhereInputRecursive3']
    OR: List['PatientWhereInputRecursive3']
    NOT: List['PatientWhereInputRecursive3']


class PatientWhereInputRecursive3(TypedDict, total=False):
    """Patient arguments for searching"""
    patient_id: Union[_str, 'types.StringFilter']
    first_name: Union[_str, 'types.StringFilter']
    last_name: Union[_str, 'types.StringFilter']
    age: Union[_int, 'types.IntFilter']
    condition: Union[_str, 'types.StringFilter']

    # should be noted that AND and NOT should be Union['PatientWhereInputRecursive4', List['PatientWhereInputRecursive4']]
    # but this causes mypy to hang :/
    AND: List['PatientWhereInputRecursive4']
    OR: List['PatientWhereInputRecursive4']
    NOT: List['PatientWhereInputRecursive4']


class PatientWhereInputRecursive4(TypedDict, total=False):
    """Patient arguments for searching"""
    patient_id: Union[_str, 'types.StringFilter']
    first_name: Union[_str, 'types.StringFilter']
    last_name: Union[_str, 'types.StringFilter']
    age: Union[_int, 'types.IntFilter']
    condition: Union[_str, 'types.StringFilter']



# aggregate Patient types


    

class PatientScalarWhereWithAggregatesInput(TypedDict, total=False):
    """Patient arguments for searching"""
    patient_id: Union[_str, 'types.StringWithAggregatesFilter']
    first_name: Union[_str, 'types.StringWithAggregatesFilter']
    last_name: Union[_str, 'types.StringWithAggregatesFilter']
    age: Union[_int, 'types.IntWithAggregatesFilter']
    condition: Union[_str, 'types.StringWithAggregatesFilter']

    AND: List['PatientScalarWhereWithAggregatesInputRecursive1']
    OR: List['PatientScalarWhereWithAggregatesInputRecursive1']
    NOT: List['PatientScalarWhereWithAggregatesInputRecursive1']


class PatientScalarWhereWithAggregatesInputRecursive1(TypedDict, total=False):
    """Patient arguments for searching"""
    patient_id: Union[_str, 'types.StringWithAggregatesFilter']
    first_name: Union[_str, 'types.StringWithAggregatesFilter']
    last_name: Union[_str, 'types.StringWithAggregatesFilter']
    age: Union[_int, 'types.IntWithAggregatesFilter']
    condition: Union[_str, 'types.StringWithAggregatesFilter']

    AND: List['PatientScalarWhereWithAggregatesInputRecursive2']
    OR: List['PatientScalarWhereWithAggregatesInputRecursive2']
    NOT: List['PatientScalarWhereWithAggregatesInputRecursive2']


class PatientScalarWhereWithAggregatesInputRecursive2(TypedDict, total=False):
    """Patient arguments for searching"""
    patient_id: Union[_str, 'types.StringWithAggregatesFilter']
    first_name: Union[_str, 'types.StringWithAggregatesFilter']
    last_name: Union[_str, 'types.StringWithAggregatesFilter']
    age: Union[_int, 'types.IntWithAggregatesFilter']
    condition: Union[_str, 'types.StringWithAggregatesFilter']

    AND: List['PatientScalarWhereWithAggregatesInputRecursive3']
    OR: List['PatientScalarWhereWithAggregatesInputRecursive3']
    NOT: List['PatientScalarWhereWithAggregatesInputRecursive3']


class PatientScalarWhereWithAggregatesInputRecursive3(TypedDict, total=False):
    """Patient arguments for searching"""
    patient_id: Union[_str, 'types.StringWithAggregatesFilter']
    first_name: Union[_str, 'types.StringWithAggregatesFilter']
    last_name: Union[_str, 'types.StringWithAggregatesFilter']
    age: Union[_int, 'types.IntWithAggregatesFilter']
    condition: Union[_str, 'types.StringWithAggregatesFilter']

    AND: List['PatientScalarWhereWithAggregatesInputRecursive4']
    OR: List['PatientScalarWhereWithAggregatesInputRecursive4']
    NOT: List['PatientScalarWhereWithAggregatesInputRecursive4']


class PatientScalarWhereWithAggregatesInputRecursive4(TypedDict, total=False):
    """Patient arguments for searching"""
    patient_id: Union[_str, 'types.StringWithAggregatesFilter']
    first_name: Union[_str, 'types.StringWithAggregatesFilter']
    last_name: Union[_str, 'types.StringWithAggregatesFilter']
    age: Union[_int, 'types.IntWithAggregatesFilter']
    condition: Union[_str, 'types.StringWithAggregatesFilter']



class PatientGroupByOutput(TypedDict, total=False):
    patient_id: _str
    first_name: _str
    last_name: _str
    age: _int
    condition: _str
    _sum: 'PatientSumAggregateOutput'
    _avg: 'PatientAvgAggregateOutput'
    _min: 'PatientMinAggregateOutput'
    _max: 'PatientMaxAggregateOutput'
    _count: 'PatientCountAggregateOutput'


class PatientAvgAggregateOutput(TypedDict, total=False):
    """Patient output for aggregating averages"""
    age: float


class PatientSumAggregateOutput(TypedDict, total=False):
    """Patient output for aggregating sums"""
    age: _int


class PatientScalarAggregateOutput(TypedDict, total=False):
    """Patient output including scalar fields"""
    patient_id: _str
    first_name: _str
    last_name: _str
    age: _int
    condition: _str


PatientMinAggregateOutput = PatientScalarAggregateOutput
PatientMaxAggregateOutput = PatientScalarAggregateOutput


class PatientMaxAggregateInput(TypedDict, total=False):
    """Patient input for aggregating by max"""
    patient_id: bool
    first_name: bool
    last_name: bool
    age: bool
    condition: bool


class PatientMinAggregateInput(TypedDict, total=False):
    """Patient input for aggregating by min"""
    patient_id: bool
    first_name: bool
    last_name: bool
    age: bool
    condition: bool


class PatientNumberAggregateInput(TypedDict, total=False):
    """Patient input for aggregating numbers"""
    age: bool


PatientAvgAggregateInput = PatientNumberAggregateInput
PatientSumAggregateInput = PatientNumberAggregateInput


PatientCountAggregateInput = TypedDict(
    'PatientCountAggregateInput',
    {
        'patient_id': bool,
        'first_name': bool,
        'last_name': bool,
        'age': bool,
        'condition': bool,
        '_all': bool,
    },
    total=False,
)

PatientCountAggregateOutput = TypedDict(
    'PatientCountAggregateOutput',
    {
        'patient_id': int,
        'first_name': int,
        'last_name': int,
        'age': int,
        'condition': int,
        '_all': int,
    },
    total=False,
)


PatientKeys = Literal[
    'patient_id',
    'first_name',
    'last_name',
    'age',
    'condition',
]
PatientScalarFieldKeys = Literal[
    'patient_id',
    'first_name',
    'last_name',
    'age',
    'condition',
]
PatientScalarFieldKeysT = TypeVar('PatientScalarFieldKeysT', bound=PatientScalarFieldKeys)

PatientRelationalFieldKeys = _NoneType



# we have to import ourselves as types can be namespaced to types
from . import types, enums, models, fields