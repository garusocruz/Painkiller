"""
main module all configurations from fast api application
"""
from fastapi import FastAPI
from prisma import Prisma

app = FastAPI(
    title="PainKiller - Patients", 
)
prisma = Prisma(auto_register=True)

@app.on_event("startup")
async def startup() -> None:
    await prisma.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    if prisma.is_connected():
        await prisma.disconnect()

@app.get('/')
def index() -> dict:
    """index view method

    Returns:
        dict: with a sample message
    """
    return {"message":'Wellcome to a PainKiller Patients BackEnd Challenger, please visit http://localhost:8000/docs'}