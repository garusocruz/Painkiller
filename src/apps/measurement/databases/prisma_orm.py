"""
prisma orm module all configurations from prisma ORM
"""
import asyncio
from src.clients.measurement.client import Prisma
from src.apps.measurement.interfaces.db import DBInterface


class PrismaORM(DBInterface):
    """Prisma Orm Layer to interact with database interfaces"""

    orm: Prisma

    def __init__(self, orm=Prisma(auto_register=True)) -> None:
        """Initializing Prisma module with orm property"""
        self.orm = orm

    async def turn_db_on(self):
        """Start DB connection"""
        if not self.orm.is_connected():
            await self.orm.connect()

    async def turn_db_off(self):
        """Ends DB connection"""
        if self.orm.is_connected():
            await asyncio.wait(self.orm.disconnect())
