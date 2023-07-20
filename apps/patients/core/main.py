"""
main module all configurations from fast api application
"""
from ..interfaces.app import get_app, get_orm
from ..routers.v1.patients_router import router as patient_router

DB = get_orm()
app = get_app()


### Fast Api events
@app.on_event("startup")
async def startup() -> None:
    """Start DB connection"""
    await DB.turn_db_on()


@app.on_event("shutdown")
async def shutdown() -> None:
    """Ends DB connection"""
    if DB.is_connected():
        await DB.disconnect()


### Routers
app.include_router(patient_router)
