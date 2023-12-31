"""
Measurement Service module put all business logic inside of this file
"""
from src.utils.uuid import generate_uuid
from src.clients.measurement.models import Measurement
from src.apps.measurement.schemas.measurement_schema import (
    PostMeasurementSchema,
)
from src.apps.measurement.interfaces.app import get_orm


class MeasurementService:
    """MeasurementService is a proxy layer to query actions in Database"""

    def __init__(self) -> None:
        """Initializing Prisma ORM"""
        self.orm = get_orm()

    async def create(self, measurement: PostMeasurementSchema) -> Measurement:
        """Create a Measurement

        Returns:
            MeasurementModel: A proxy to Prisma Models
        """
        if not measurement.measurement_id:
            measurement.measurement_id = generate_uuid().hex

        return await self.orm.measurement.create(measurement.dict())
