"""
main module all configurations from fast api application
"""
from fastapi import FastAPI
from prisma import Prisma
from ..routers.v1.PatientsRouter import router as patient_router


app = FastAPI(
    title="PainKiller - Patients",
)
prisma = Prisma(auto_register=True)

# Add Routers
app.include_router(patient_router)


@app.on_event("startup")
async def startup() -> None:
    """Start DB connection"""
    await prisma.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    """Ends DB connection"""
    if prisma.is_connected():
        await prisma.disconnect()


@app.get("/")
def index() -> dict:
    """index view method

    Returns:
        dict: with a sample message
    """
    return {
        "message": "Wellcome to a PainKiller Patients BackEnd Challenger, please visit http://localhost:8000/docs"
    }
