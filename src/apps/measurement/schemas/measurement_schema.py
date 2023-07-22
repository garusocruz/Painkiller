"""MeasurementSchema is an interface with Pydantic layer and Measurement Prisma ORM Model
"""
from typing import Optional

# from src.apps.measurement.models.measurement_model import MeasurementModel
from src.clients.measurement.models import Measurement


class PostMeasurementSchema(Measurement):
    """PostMeasurementSchema is an chield of Measurement model replacing the measurement_id to be an empty field in a primary instance

    Args:
        Measurement (Prisma Model): inherit of Measurement Prisma ORM Model
    """

    measurement_id: Optional[str] = None
