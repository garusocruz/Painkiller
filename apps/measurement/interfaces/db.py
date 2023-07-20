from abc import ABC, abstractmethod


class DBInterface(ABC):
    @abstractmethod
    def __init__(self, orm) -> None:
        self.orm = orm

    @abstractmethod
    async def turn_db_on(self) -> NotImplemented:
        return NotImplemented

    @abstractmethod
    async def turn_db_off(self) -> NotImplemented:
        return NotImplemented
