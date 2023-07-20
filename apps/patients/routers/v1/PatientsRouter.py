"""PatientsRouter module

    All Patients view is aborded bellow
"""
from ...schemas.pydantic.PatientSchema import PostPatient, Patient
from fastapi import APIRouter
from ...utils.uuid import generate_uuid


router = APIRouter(prefix="/v1/patients", tags=["patient"])


@router.post("/api/v1/patient", response_model=Patient)
async def create(patient: PostPatient) -> Patient:
    """create method, trigger a DB query instruction to create a new Patient row

    Args:
        patient (PostPatient): Patient Model

    Returns:
        Patient: Patient Prisma Model
    """
    from ...core.main import prisma

    if not patient.patient_id:
        patient.patient_id = generate_uuid().hex

    return await prisma.patient.create(patient.dict())
