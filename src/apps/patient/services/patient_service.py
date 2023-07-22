"""
Patient Service module put all business logic inside of this file
"""
from src.utils.uuid import generate_uuid
from src.clients.patient.models import Patient
from src.schemas.post_patienti_schema import PostPatientSchema
from src.apps.patient.interfaces.app import get_orm


class PatientService:
    """PatientService is a proxy layer to query actions in Database"""

    def __init__(self) -> None:
        """Initializing Prisma ORM"""
        self.orm = get_orm()

    async def create(self, patient: PostPatientSchema) -> Patient:
        """Create a Patient

        Returns:
            Patient: A proxy to Prisma Models
        """
        if not patient.patient_id:
            patient.patient_id = generate_uuid().hex

        return await self.orm.patient.create(patient.dict())

    async def read_by_id(self, patient_id: str) -> Patient:
        """query a patient according by patient_id

        Args:
            patient_id (str): pk of Patient

        Returns:
            Patient: A proxy to Prisma Models
        """
        return await self.orm.patient.find_first(where={"patient_id": patient_id})
