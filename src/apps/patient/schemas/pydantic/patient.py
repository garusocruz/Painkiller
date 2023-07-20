"""PatientSchema is an interface with Pydantic layer and Patient Prisma ORM Model
"""
from typing import Optional
from src.apps.patient.models.patient import PatientModel


class PostPatientSchema(PatientModel):
    """PostPatientSchema is an chield of Patient model replacing the patient_id to be an empty field in a primary instance

    Args:
        Patient (Prisma Model): inherit of Patient Prisma ORM Model
    """

    patient_id: Optional[str] | None = None
