"""
main module all configurations from fast api application
"""
from fastapi import FastAPI

app = FastAPI(
    title="PainKiller - Patients", 
)

@app.get('/')
def index() -> dict:
    """index view method

    Returns:
        dict: with a sample message
    """
    return {"message":'Wellcome to a PainKiller Patients BackEnd Challenger, please visit http://localhost:8000/docs'}