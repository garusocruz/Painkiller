"""MeasurementSchema is an interface with Pydantic layer and Measurement Prisma ORM Model
"""
from typing import Optional
from apps.measurement.models.measurement_model import MeasurementModel


class PostMeasurementSchema(MeasurementModel):
    """PostMeasurementSchema is an chield of Measurement model replacing the measurement_id to be an empty field in a primary instance

    Args:
        Measurement (Prisma Model): inherit of Measurement Prisma ORM Model
    """

    measurement_id: Optional[str] | None = None
