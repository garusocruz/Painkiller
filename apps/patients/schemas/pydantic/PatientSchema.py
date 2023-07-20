"""PatientSchema is an interface with Pydantic layer and Patient Prisma ORM Model
"""
from typing import Optional
from prisma.models import Patient


class PostPatient(Patient):
    """PostPatient is an chield of Patient model replacing the patient_id to be an empty field in a primary instance

    Args:
        Patient (Prisma Model): inherit of Patient Prisma ORM Model
    """

    patient_id: Optional[str] | None = None
