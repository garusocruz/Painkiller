# -*- coding: utf-8 -*-
# code generated by Prisma. DO NOT EDIT.
# pyright: reportUnusedImport=false
# fmt: off
from __future__ import annotations

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
# -- template actions.py.jinja --
from typing import TypeVar
import warnings

from . import types, errors, bases

if TYPE_CHECKING:
    from .client import Client
    from .bases import _PrismaModel


_PrismaModelT = TypeVar('_PrismaModelT', bound='_PrismaModel')


class MeasurementActions(Generic[_PrismaModelT]):
    __slots__ = (
        '_client',
        '_model',
    )

    def __init__(self, client: 'Client', model: Type[_PrismaModelT]) -> None:
        self._client = client
        self._model = model

    async def query_raw(
        self,
        query: LiteralString,
        *args: Any,
    ) -> List[_PrismaModelT]:
        """Execute a raw SQL query

        Parameters
        ----------
        query
            The raw SQL query string to be executed
        *args
            Parameters to be passed to the SQL query, these MUST be used over
            string formatting to avoid an SQL injection vulnerability

        Returns
        -------
        List[prisma.models.Measurement]
            The records returned by the SQL query

        Raises
        ------
        prisma_errors.RawQueryError
            This could be due to invalid syntax, mismatched number of parameters or any other error
        prisma.errors.PrismaError
            Catch all for every exception raised by Prisma Client Python

        Example
        -------
        ```py
        users = await Measurement.prisma().query_raw(
            'SELECT * FROM Measurement WHERE measurement_id = ?',
            'bbadfchfja',
        )
        ```
        """
        return await self._client.query_raw(query, *args, model=self._model)

    async def query_first(
        self,
        query: LiteralString,
        *args: Any,
    ) -> Optional[_PrismaModelT]:
        """Execute a raw SQL query, returning the first result

        Parameters
        ----------
        query
            The raw SQL query string to be executed
        *args
            Parameters to be passed to the SQL query, these MUST be used over
            string formatting to avoid an SQL injection vulnerability

        Returns
        -------
        prisma.models.Measurement
            The first record returned by the SQL query
        None
            The raw SQL query did not return any records

        Raises
        ------
        prisma_errors.RawQueryError
            This could be due to invalid syntax, mismatched number of parameters or any other error
        prisma.errors.PrismaError
            Catch all for every exception raised by Prisma Client Python

        Example
        -------
        ```py
        user = await Measurement.prisma().query_first(
            'SELECT * FROM Measurement WHERE patient_id = ?',
            'dhheabfhf',
        )
        ```
        """
        return await self._client.query_first(query, *args, model=self._model)

    async def create(
        self,
        data: types.MeasurementCreateInput,
        include: Optional[types.MeasurementInclude] = None
    ) -> _PrismaModelT:
        """Create a new Measurement record.

        Parameters
        ----------
        data
            Measurement record data
        include
            Specifies which relations should be loaded on the returned Measurement model

        Returns
        -------
        prisma.models.Measurement
            The created Measurement record

        Raises
        ------
        prisma.errors.MissingRequiredValueError
            Value is required but was not found
        prisma.errors.PrismaError
            Catch all for every exception raised by Prisma Client Python

        Example
        -------
        ```py
        # create a Measurement record from just the required fields
        measurement = await Measurement.prisma().create(
            data={
                # data to create a Measurement record
                'patient_id': 'ggciceaie',
                'blood_pressure': 1147902781.203501,
                'temperature': 'dgiiaaijj',
            },
        )
        ```
        """
        resp = await self._client._execute(
            method='create',
            model=self._model,
            arguments={
                'data': data,
                'include': include,
            },
        )
        return self._model.parse_obj(resp['data']['result'])

    async def create_many(
        self,
        data: List[types.MeasurementCreateWithoutRelationsInput],
        *,
        skip_duplicates: Optional[bool] = None,
    ) -> int:
        """Create multiple Measurement records at once.

        This function is *not* available when using SQLite.

        Parameters
        ----------
        data
            List of Measurement record data
        skip_duplicates
            Boolean flag for ignoring unique constraint errors

        Returns
        -------
        int
            The total number of records created

        Raises
        ------
        prisma.errors.UnsupportedDatabaseError
            Attempting to query when using SQLite
        prisma.errors.UniqueViolationError
            A unique constraint check has failed, these can be ignored with the `skip_duplicates` argument
        prisma.errors.MissingRequiredValueError
            Value is required but was not found
        prisma.errors.PrismaError
            Catch all for every exception raised by Prisma Client Python

        Example
        -------
        ```py
        total = await Measurement.prisma().create_many(
            data=[
                {
                    # data to create a Measurement record
                    'patient_id': 'bfaiacjjfc',
                    'blood_pressure': 486256185.106251,
                    'temperature': 'cghideieh',
                },
                {
                    # data to create a Measurement record
                    'patient_id': 'biabhbdai',
                    'blood_pressure': 836760821.59533,
                    'temperature': 'hjaecfifb',
                },
            ],
            skip_duplicates=True,
        )
        ```
        """
        if self._client._active_provider == 'sqlite':
            raise errors.UnsupportedDatabaseError('sqlite', 'create_many()')

        resp = await self._client._execute(
            method='create_many',
            model=self._model,
            arguments={
                'data': data,
                'skipDuplicates': skip_duplicates,
            },
            root_selection=['count'],
        )
        return int(resp['data']['result']['count'])

    async def delete(
        self,
        where: types.MeasurementWhereUniqueInput,
        include: Optional[types.MeasurementInclude] = None
    ) -> Optional[_PrismaModelT]:
        """Delete a single Measurement record.

        Parameters
        ----------
        where
            Measurement filter to select the record to be deleted, must be unique
        include
            Specifies which relations should be loaded on the returned Measurement model

        Returns
        -------
        prisma.models.Measurement
            The deleted Measurement record
        None
            Could not find a record to delete

        Raises
        ------
        prisma.errors.PrismaError
            Catch all for every exception raised by Prisma Client Python
        prisma.errors.MissingRequiredValueError
            Value is required but was not found

        Example
        -------
        ```py
        measurement = await Measurement.prisma().delete(
            where={
                'measurement_id': 'cbbbjbfcii',
            },
        )
        ```
        """
        try:
            resp = await self._client._execute(
                method='delete',
                model=self._model,
                arguments={
                    'where': where,
                    'include': include,
                },
            )
        except errors.RecordNotFoundError:
            return None

        return self._model.parse_obj(resp['data']['result'])

    async def find_unique(
        self,
        where: types.MeasurementWhereUniqueInput,
        include: Optional[types.MeasurementInclude] = None
    ) -> Optional[_PrismaModelT]:
        """Find a unique Measurement record.

        Parameters
        ----------
        where
            Measurement filter to find the record, must be unique
        include
            Specifies which relations should be loaded on the returned Measurement model

        Returns
        -------
        prisma.models.Measurement
            The found Measurement record
        None
            No record matching the given input could be found

        Raises
        ------
        prisma.errors.PrismaError
            Catch all for every exception raised by Prisma Client Python
        prisma.errors.MissingRequiredValueError
            Value is required but was not found

        Example
        -------
        ```py
        measurement = await Measurement.prisma().find_unique(
            where={
                'measurement_id': 'bbejhfidcb',
            },
        )
        ```
        """
        resp = await self._client._execute(
            method='find_unique',
            model=self._model,
            arguments={
                'where': where,
                'include': include,
            },
        )
        result = resp['data']['result']
        if result is None:
            return None
        return self._model.parse_obj(result)

    async def find_unique_or_raise(
        self,
        where: types.MeasurementWhereUniqueInput,
        include: Optional[types.MeasurementInclude] = None
    ) -> _PrismaModelT:
        """Find a unique Measurement record. Raises `RecordNotFoundError` if no record is found.

        Parameters
        ----------
        where
            Measurement filter to find the record, must be unique
        include
            Specifies which relations should be loaded on the returned Measurement model

        Returns
        -------
        prisma.models.Measurement
            The found Measurement record

        Raises
        ------
        prisma.errors.RecordNotFoundError
            No record was found
        prisma.errors.PrismaError
            Catch all for every exception raised by Prisma Client Python
        prisma.errors.MissingRequiredValueError
            Value is required but was not found

        Example
        -------
        ```py
        measurement = await Measurement.prisma().find_unique_or_raise(
            where={
                'measurement_id': 'bgeecijdgg',
            },
        )
        ```
        """
        resp = await self._client._execute(
            method='find_unique_or_raise',
            model=self._model,
            arguments={
                'where': where,
                'include': include,
            },
        )
        return self._model.parse_obj(resp['data']['result'])

    async def find_many(
        self,
        take: Optional[int] = None,
        skip: Optional[int] = None,
        where: Optional[types.MeasurementWhereInput] = None,
        cursor: Optional[types.MeasurementWhereUniqueInput] = None,
        include: Optional[types.MeasurementInclude] = None,
        order: Optional[Union[types.MeasurementOrderByInput, List[types.MeasurementOrderByInput]]] = None,
        distinct: Optional[List[types.MeasurementScalarFieldKeys]] = None,
    ) -> List[_PrismaModelT]:
        """Find multiple Measurement records.

        An empty list is returned if no records could be found.

        Parameters
        ----------
        take
            Limit the maximum number of Measurement records returned
        skip
            Ignore the first N results
        where
            Measurement filter to select records
        cursor
            Specifies the position in the list to start returning results from, (typically an ID field)
        include
            Specifies which relations should be loaded on the returned Measurement model
        order
            Order the returned Measurement records by any field
        distinct
            Filter Measurement records by either a single distinct field or distinct combinations of fields

        Returns
        -------
        List[prisma.models.Measurement]
            The list of all Measurement records that could be found

        Raises
        ------
        prisma.errors.PrismaError
            Catch all for every exception raised by Prisma Client Python

        Example
        -------
        ```py
        # find the first 10 Measurement records
        measurements = await Measurement.prisma().find_many(take=10)

        # find the first 5 Measurement records ordered by the blood_pressure field
        measurements = await Measurement.prisma().find_many(
            take=5,
            order={
                'blood_pressure': 'desc',
            },
        )
        ```
        """
        resp = await self._client._execute(
            method='find_many',
            model=self._model,
            arguments={
                'take': take,
                'skip': skip,
                'where': where,
                'order_by': order,
                'cursor': cursor,
                'include': include,
                'distinct': distinct,
            },
        )
        return [self._model.parse_obj(r) for r in resp['data']['result']]

    async def find_first(
        self,
        skip: Optional[int] = None,
        where: Optional[types.MeasurementWhereInput] = None,
        cursor: Optional[types.MeasurementWhereUniqueInput] = None,
        include: Optional[types.MeasurementInclude] = None,
        order: Optional[Union[types.MeasurementOrderByInput, List[types.MeasurementOrderByInput]]] = None,
        distinct: Optional[List[types.MeasurementScalarFieldKeys]] = None,
    ) -> Optional[_PrismaModelT]:
        """Find a single Measurement record.

        Parameters
        ----------
        skip
            Ignore the first N records
        where
            Measurement filter to select the record
        cursor
            Specifies the position in the list to start returning results from, (typically an ID field)
        include
            Specifies which relations should be loaded on the returned Measurement model
        order
            Order the returned Measurement records by any field
        distinct
            Filter Measurement records by either a single distinct field or distinct combinations of fields

        Returns
        -------
        prisma.models.Measurement
            The first Measurement record found, matching the given arguments
        None
            No record could be found

        Raises
        ------
        prisma.errors.PrismaError
            Catch all for every exception raised by Prisma Client Python

        Example
        -------
        ```py
        # find the second Measurement record ordered by the temperature field
        measurement = await Measurement.prisma().find_first(
            skip=1,
            order={
                'temperature': 'desc',
            },
        )
        ```
        """
        resp = await self._client._execute(
            method='find_first',
            model=self._model,
            arguments={
                'skip': skip,
                'where': where,
                'order_by': order,
                'cursor': cursor,
                'include': include,
                'distinct': distinct,
            },
        )
        result = resp['data']['result']
        if result is None:
            return None
        return self._model.parse_obj(result)

    async def find_first_or_raise(
        self,
        skip: Optional[int] = None,
        where: Optional[types.MeasurementWhereInput] = None,
        cursor: Optional[types.MeasurementWhereUniqueInput] = None,
        include: Optional[types.MeasurementInclude] = None,
        order: Optional[Union[types.MeasurementOrderByInput, List[types.MeasurementOrderByInput]]] = None,
        distinct: Optional[List[types.MeasurementScalarFieldKeys]] = None,
    ) -> _PrismaModelT:
        """Find a single Measurement record. Raises `RecordNotFoundError` if no record was found.

        Parameters
        ----------
        skip
            Ignore the first N records
        where
            Measurement filter to select the record
        cursor
            Specifies the position in the list to start returning results from, (typically an ID field)
        include
            Specifies which relations should be loaded on the returned Measurement model
        order
            Order the returned Measurement records by any field
        distinct
            Filter Measurement records by either a single distinct field or distinct combinations of fields

        Returns
        -------
        prisma.models.Measurement
            The first Measurement record found, matching the given arguments

        Raises
        ------
        prisma.errors.RecordNotFoundError
            No record was found
        prisma.errors.PrismaError
            Catch all for every exception raised by Prisma Client Python

        Example
        -------
        ```py
        # find the second Measurement record ordered by the measurement_id field
        measurement = await Measurement.prisma().find_first_or_raise(
            skip=1,
            order={
                'measurement_id': 'desc',
            },
        )
        ```
        """
        resp = await self._client._execute(
            method='find_first_or_raise',
            model=self._model,
            arguments={
                'skip': skip,
                'where': where,
                'order_by': order,
                'cursor': cursor,
                'include': include,
                'distinct': distinct,
            },
        )
        return self._model.parse_obj(resp['data']['result'])

    async def update(
        self,
        data: types.MeasurementUpdateInput,
        where: types.MeasurementWhereUniqueInput,
        include: Optional[types.MeasurementInclude] = None
    ) -> Optional[_PrismaModelT]:
        """Update a single Measurement record.

        Parameters
        ----------
        data
            Measurement record data specifying what to update
        where
            Measurement filter to select the unique record to create / update
        include
            Specifies which relations should be loaded on the returned Measurement model

        Returns
        -------
        prisma.models.Measurement
            The updated Measurement record
        None
            No record could be found

        Raises
        ------
        prisma.errors.PrismaError
            Catch all for every exception raised by Prisma Client Python

        Example
        -------
        ```py
        measurement = await Measurement.prisma().update(
            where={
                'measurement_id': 'bdiicjafbj',
            },
            data={
                # data to update the Measurement record to
            },
        )
        ```
        """
        try:
            resp = await self._client._execute(
                method='update',
                model=self._model,
                arguments={
                    'data': data,
                    'where': where,
                    'include': include,
                },
            )
        except errors.RecordNotFoundError:
            return None

        return self._model.parse_obj(resp['data']['result'])

    async def upsert(
        self,
        where: types.MeasurementWhereUniqueInput,
        data: types.MeasurementUpsertInput,
        include: Optional[types.MeasurementInclude] = None,
    ) -> _PrismaModelT:
        """Updates an existing record or create a new one

        Parameters
        ----------
        where
            Measurement filter to select the unique record to create / update
        data
            Data specifying what fields to set on create and update
        include
            Specifies which relations should be loaded on the returned Measurement model

        Returns
        -------
        prisma.models.Measurement
            The created or updated Measurement record

        Raises
        ------
        prisma.errors.PrismaError
            Catch all for every exception raised by Prisma Client Python
        prisma.errors.MissingRequiredValueError
            Value is required but was not found

        Example
        -------
        ```py
        measurement = await Measurement.prisma().upsert(
            where={
                'measurement_id': 'bgehebiafc',
            },
            data={
                'create': {
                    'measurement_id': 'bgehebiafc',
                    'patient_id': 'biabhbdai',
                    'blood_pressure': 836760821.59533,
                    'temperature': 'hjaecfifb',
                },
                'update': {
                    'patient_id': 'biabhbdai',
                    'blood_pressure': 836760821.59533,
                    'temperature': 'hjaecfifb',
                },
            },
        )
        ```
        """
        resp = await self._client._execute(
            method='upsert',
            model=self._model,
            arguments={
                'where': where,
                'include': include,
                'create': data.get('create'),
                'update': data.get('update'),
            },
        )
        return self._model.parse_obj(resp['data']['result'])

    async def update_many(
        self,
        data: types.MeasurementUpdateManyMutationInput,
        where: types.MeasurementWhereInput,
    ) -> int:
        """Update multiple Measurement records

        Parameters
        ----------
        data
            Measurement data to update the selected Measurement records to
        where
            Filter to select the Measurement records to update

        Returns
        -------
        int
            The total number of Measurement records that were updated

        Raises
        ------
        prisma.errors.PrismaError
            Catch all for every exception raised by Prisma Client Python

        Example
        -------
        ```py
        # update all Measurement records
        total = await Measurement.prisma().update_many(
            data={
                'patient_id': 'bghffegacj'
            },
            where={}
        )
        ```
        """
        resp = await self._client._execute(
            method='update_many',
            model=self._model,
            arguments={'data': data, 'where': where,},
            root_selection=['count'],
        )
        return int(resp['data']['result']['count'])

    @overload
    async def count(
        self,
        select: None = None,
        take: Optional[int] = None,
        skip: Optional[int] = None,
        where: Optional[types.MeasurementWhereInput] = None,
        cursor: Optional[types.MeasurementWhereUniqueInput] = None,
    ) -> int:
        """Count the number of Measurement records present in the database

        Parameters
        ----------
        select
            Select the Measurement fields to be counted
        take
            Limit the maximum result
        skip
            Ignore the first N records
        where
            Measurement filter to find records
        cursor
            Specifies the position in the list to start counting results from, (typically an ID field)
        order
            This parameter is deprecated and will be removed in a future release

        Returns
        -------
        int
            The total number of records found, returned if `select` is not given

        prisma.types.MeasurementCountAggregateOutput
            Data returned when `select` is used, the fields present in this dictionary will
            match the fields passed in the `select` argument

        Raises
        ------
        prisma.errors.PrismaError
            Catch all for every exception raised by Prisma Client Python

        Example
        -------
        ```py
        # total: int
        total = await Measurement.prisma().count()

        # results: prisma.types.MeasurementCountAggregateOutput
        results = await Measurement.prisma().count(
            select={
                '_all': True,
                'blood_pressure': True,
            },
        )
        ```
        """


    @overload
    async def count(
        self,
        select: types.MeasurementCountAggregateInput,
        take: Optional[int] = None,
        skip: Optional[int] = None,
        where: Optional[types.MeasurementWhereInput] = None,
        cursor: Optional[types.MeasurementWhereUniqueInput] = None,
    ) -> types.MeasurementCountAggregateOutput:
        ...

    async def count(
        self,
        select: Optional[types.MeasurementCountAggregateInput] = None,
        take: Optional[int] = None,
        skip: Optional[int] = None,
        where: Optional[types.MeasurementWhereInput] = None,
        cursor: Optional[types.MeasurementWhereUniqueInput] = None,
    ) -> Union[int, types.MeasurementCountAggregateOutput]:
        """Count the number of Measurement records present in the database

        Parameters
        ----------
        select
            Select the Measurement fields to be counted
        take
            Limit the maximum result
        skip
            Ignore the first N records
        where
            Measurement filter to find records
        cursor
            Specifies the position in the list to start counting results from, (typically an ID field)
        order
            This parameter is deprecated and will be removed in a future release

        Returns
        -------
        int
            The total number of records found, returned if `select` is not given

        prisma.types.MeasurementCountAggregateOutput
            Data returned when `select` is used, the fields present in this dictionary will
            match the fields passed in the `select` argument

        Raises
        ------
        prisma.errors.PrismaError
            Catch all for every exception raised by Prisma Client Python

        Example
        -------
        ```py
        # total: int
        total = await Measurement.prisma().count()

        # results: prisma.types.MeasurementCountAggregateOutput
        results = await Measurement.prisma().count(
            select={
                '_all': True,
                'temperature': True,
            },
        )
        ```
        """

        # TODO: this selection building should be moved to the QueryBuilder
        #
        # note the distinction between checking for `not select` here and `select is None`
        # later is to handle the case that the given select dictionary is empty, this
        # is a limitation of our types.
        if not select:
            root_selection = ['_count { _all }']
        else:

            root_selection = [
                '_count {{ {0} }}'.format(' '.join(k for k, v in select.items() if v is True))
            ]

        resp = await self._client._execute(
            method='count',
            model=self._model,
            arguments={
                'take': take,
                'skip': skip,
                'where': where,
                'cursor': cursor,
            },
            root_selection=root_selection,
        )

        if select is None:
            return cast(int, resp['data']['result']['_count']['_all'])
        else:
            return cast(types.MeasurementCountAggregateOutput, resp['data']['result']['_count'])

    async def delete_many(
        self,
        where: Optional[types.MeasurementWhereInput] = None
    ) -> int:
        """Delete multiple Measurement records.

        Parameters
        ----------
        where
            Optional Measurement filter to find the records to be deleted

        Returns
        -------
        int
            The total number of Measurement records that were deleted

        Raises
        ------
        prisma.errors.PrismaError
            Catch all for every exception raised by Prisma Client Python

        Example
        -------
        ```py
        # delete all Measurement records
        total = await Measurement.prisma().delete_many()
        ```
        """
        resp = await self._client._execute(
            method='delete_many',
            model=self._model,
            arguments={'where': where},
            root_selection=['count'],
        )
        return int(resp['data']['result']['count'])

    # TODO: make this easier to work with safely, currently output fields are typed as
    #       not required, we should refactor the return type
    # TODO: consider returning a Dict where the keys are a Tuple of the `by` selection
    # TODO: statically type that the order argument is required when take or skip are present
    async def group_by(
        self,
        by: List['types.MeasurementScalarFieldKeys'],
        *,
        where: Optional['types.MeasurementWhereInput'] = None,
        take: Optional[int] = None,
        skip: Optional[int] = None,
        avg: Optional['types.MeasurementAvgAggregateInput'] = None,
        sum: Optional['types.MeasurementSumAggregateInput'] = None,
        min: Optional['types.MeasurementMinAggregateInput'] = None,
        max: Optional['types.MeasurementMaxAggregateInput'] = None,
        having: Optional['types.MeasurementScalarWhereWithAggregatesInput'] = None,
        count: Optional[Union[bool, 'types.MeasurementCountAggregateInput']] = None,
        order: Optional[Union[Mapping['types.MeasurementScalarFieldKeys', 'types.SortOrder'], List[Mapping['types.MeasurementScalarFieldKeys', 'types.SortOrder']]]] = None,
    ) -> List['types.MeasurementGroupByOutput']:
        """Group Measurement records by one or more field values and perform aggregations
        each group such as finding the average.

        Parameters
        ----------
        by
            List of scalar Measurement fields to group records by
        where
            Measurement filter to select records
        take
            Limit the maximum number of Measurement records returned
        skip
            Ignore the first N records
        avg
            Adds the average of all values of the specified fields to the `_avg` field
            in the returned data.
        sum
            Adds the sum of all values of the specified fields to the `_sum` field
            in the returned data.
        min
            Adds the smallest available value for the specified fields to the `_min` field
            in the returned data.
        max
            Adds the largest available value for the specified fields to the `_max` field
            in the returned data.
        count
            Adds a count of non-fields to the `_count` field in the returned data.
        having
            Allows you to filter groups by an aggregate value - for example only return
            groups having an average age less than 50.
        order
            Lets you order the returned list by any property that is also present in `by`.
            Only **one** field is allowed at a time.

        Returns
        -------
        List[prisma.types.MeasurementGroupByOutput]
            A list of dictionaries representing the Measurement record,
            this will also have additional fields present if aggregation arguments
            are used (see the above parameters)

        Raises
        ------
        prisma.errors.PrismaError
            Catch all for every exception raised by Prisma Client Python

        Example
        -------
        ```py
        # group Measurement records by measurement_id values
        # and count how many records are in each group
        results = await Measurement.prisma().group_by(
            ['measurement_id'],
            count=True,
        )
        ```
        """
        if order is None:
            if take is not None:
                raise TypeError('Missing argument: \'order\' which is required when \'take\' is present')

            if skip is not None:
                raise TypeError('Missing argument: \'order\' which is required when \'skip\' is present')

        root_selection: List[str] = [*by]
        if avg is not None:
            root_selection.append(_select_fields('_avg', avg))

        if min is not None:
            root_selection.append(_select_fields('_min', min))

        if sum is not None:
            root_selection.append(_select_fields('_sum', sum))

        if max is not None:
            root_selection.append(_select_fields('_max', max))

        if count is not None:
            if count is True:
                root_selection.append('_count { _all }')
            elif isinstance(count, dict):
                root_selection.append(_select_fields('_count', count))

        resp = await self._client._execute(
            method='group_by',
            model=self._model,
            arguments={
                'by': by,
                'take': take,
                'skip': skip,
                'where': where,
                'having': having,
                'orderBy': order,
            },
            root_selection=root_selection,
        )
        return resp['data']['result']  # type: ignore[no-any-return]



def _select_fields(root: str, select: Mapping[str, Any]) -> str:
    """Helper to build a GraphQL selection string

    This is a work around until field selection is added to the query builder.
    """

    return root + ' {{ {0} }}'.format(' '.join(k for k, v in select.items() if v is True))


from . import models