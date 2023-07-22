"""
fast_api module have many scripts to run fast api commands
"""
from os import system as shcmd


def patient_api() -> None:
    """
    The function start a fast api server using a uvicorn with arguments like port
    following example:

    poetry run patients
    """

    shcmd(f"uvicorn src.apps.patient.core.main:app --reload")


def measurement_api() -> None:
    """
    The function start a fast api server using a uvicorn with arguments like port
    following example:

    poetry run measurements
    """

    shcmd(f"uvicorn src.apps.measurement.core.main:app --reload --port 8001")


def docker_up() -> None:
    """
    The function start a docker up command providing your Api's running on:
    patient - http://localhost:8000
    measurement - http://localhost:8001
    """

    shcmd(f"sudo docker compose -f .docker/docker-compose.yml up")


def coverage() -> None:
    """
    The function start the test layer exporting the apllication coverage
    """

    shcmd(f"./scripts/coverage.sh")
