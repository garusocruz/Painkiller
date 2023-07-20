"""
prisma module have many scripts to execute ORM commands
"""
from os import system as shcmd


def migrate_patient() -> None:
    """
    The function apply the latest migration
    following example:

    prisma migrate dev
    """

    shcmd(f"prisma migrate dev --schema=apps/patient/prisma/schema.prisma")


def migrate_measurement() -> None:
    """
    The function apply the latest migration
    following example:

    prisma migrate dev
    """

    shcmd(f"prisma migrate dev --schema=apps/measurement/prisma/schema.prisma")
