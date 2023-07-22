"""Module used to mix Prisma and Fast Api in one Class Object
"""
from fastapi import FastAPI
from src.clients.patient.client import Prisma


class AppInterface:
    """App Interface is a mixed class Object containing Prisma and Fast Api injected modules"""

    def __init__(self) -> None:
        """Initialize prisma and fast api properties"""
        self.prisma = Prisma()
        self.fast_api = FastAPI(docs_url="/", title="PainKiller - Patients")


_SERVER = AppInterface()


def get_app() -> FastAPI:
    """Used to export app instance

    Returns:
        FastAPI: return a Fast Api instance
    """
    return _SERVER.fast_api


def get_orm() -> Prisma:
    """Used to export Prisma instance

    Returns:
        PrismaORM: return a PrismaORM abstraction of Prisma module
    """
    return _SERVER.prisma
