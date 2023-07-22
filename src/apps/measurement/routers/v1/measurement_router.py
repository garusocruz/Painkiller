"""measurement  module
    All Measurement view is aborded bellow
"""
from fastapi import APIRouter, Response, status
from src.clients.measurement.models import Measurement
from src.apps.measurement.schemas.measurement_schema import (
    PostMeasurementSchema,
)
from src.apps.measurement.services.measurement_service import MeasurementService


router = APIRouter(prefix="/v1/measurements", tags=["measurement"])
service = MeasurementService()


@router.post("/", response_model=Measurement)
async def create(measurement: PostMeasurementSchema, response: Response):
    """create method, trigger a DB query instruction to create a new Measurement row

    Args:
        measure (PostMeasurementSchema): Measure Model

    Returns:
        MeasurementModel: Measurement Prisma Model
    """
    measurement = await service.create(measurement)
    response.status_code = status.HTTP_201_CREATED
    return measurement
