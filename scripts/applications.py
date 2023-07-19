"""
fast_api module have many scripts to run fast api commands
"""
from os import system as shcmd

def patients_api() -> None:
    """
    The function start a fast api server using a uvicorn with arguments like port
    following example:

    poetry run patients
    """

    shcmd(f"uvicorn apps.patients.core.main:app --reload")