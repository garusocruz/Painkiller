"""
main module all configurations from fast api application
"""
from src.apps.patient.interfaces.app import get_app, get_orm
from src.apps.patient.routers.v1.patient_router import router as patient_router

DB = get_orm()
app = get_app()


### Fast Api events
@app.on_event("startup")
async def startup() -> None:
    """Start DB connection"""
    await DB.connect()


@app.on_event("shutdown")
async def shutdown() -> None:
    """Ends DB connection"""
    if DB.is_connected():
        await DB.disconnect()


### Routers
app.include_router(patient_router)
