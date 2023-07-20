"""
Measurement Service module put all business logic inside of this file
"""
from src.apps.measurement.models.measurement_model import MeasurementModel
from src.apps.measurement.schemas.pydantic.measurement_schema import (
    PostMeasurementSchema,
)
from src.utils.uuid import generate_uuid
from src.apps.measurement.interfaces.app import get_orm


class MeasurementService:
    """MeasurementService is a proxy layer to query actions in Database"""

    def __init__(self) -> None:
        """Initializing Prisma ORM"""
        self.orm = get_orm().orm

    async def create(self, measurement: PostMeasurementSchema) -> MeasurementModel:
        """Create a Measurement

        Returns:
            MeasurementModel: A proxy to Prisma Models
        """
        if not measurement.measurement_id:
            measurement.measurement_id = generate_uuid().hex

        return await self.orm.measurement.create(measurement.dict())
