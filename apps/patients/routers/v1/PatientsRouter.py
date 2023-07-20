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


@router.get("/api/v1/patient/{patient_id}", response_model=Patient)
async def read_by_id(patient_id: str):
    """read_by_id method, trigger a DN query instruction to fetch patient row according a patient_id

    Args:
        patient_id (str): PK of Patient Model

    Returns:
        Patient: Patient Prisma ORM Model
    """
    from ...core.main import prisma

    return await prisma.patient.find_first(where={"patient_id": patient_id})
