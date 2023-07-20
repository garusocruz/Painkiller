"""
fast_api module have many scripts to run fast api commands
"""
from os import system as shcmd

def migrate_patients() -> None:
    """
    The function start a fast api server using a uvicorn with arguments like port
    following example:

    poetry run patients
    """

    shcmd(f"prisma migrate dev --schema=apps/patients/prisma/schema.prisma")