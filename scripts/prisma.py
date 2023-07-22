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

    shcmd(f"prisma migrate dev --schema=src/apps/patient/prisma/schema.prisma")


def migrate_measurement() -> None:
    """
    The function apply the latest migration
    following example:

    prisma migrate dev
    """

    shcmd(f"prisma migrate dev --schema=src/apps/measurement/prisma/schema.prisma")


def client_patient() -> None:
    """
    The function create prisma client to patient app
    following example:

    prisma generate
    """

    shcmd(f"prisma generate --schema=src/apps/patient/prisma/schema.prisma")


def client_measurement() -> None:
    """
    The function create prisma client to measurement app
    following example:

    prisma generate
    """

    shcmd(f"prisma generate --schema=src/apps/measurement/prisma/schema.prisma")
