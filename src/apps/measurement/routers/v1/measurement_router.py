"""measurement  module
    All Measurement view is aborded bellow
"""
from fastapi import APIRouter
from src.apps.measurement.interfaces.app import get_orm

# from src.apps.measurement.models.measurement_model import MeasurementModel, Men
from src.clients.measurement.models import Measurement
from src.apps.measurement.schemas.pydantic.measurement_schema import (
    PostMeasurementSchema,
)
from src.apps.measurement.services.measurement_service import MeasurementService

orm = get_orm()
router = APIRouter(prefix="/v1/measurements", tags=["measurement"])
service = MeasurementService()


@router.post("/", response_model=Measurement)
async def create(measurement: PostMeasurementSchema):
    """create method, trigger a DB query instruction to create a new Measurement row

    Args:
        measure (PostMeasurementSchema): Measure Model

    Returns:
        MeasurementModel: Measurement Prisma Model
    """

    return await service.create(measurement)