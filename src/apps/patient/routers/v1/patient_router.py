"""PatientsRouter module

    All Patients view is aborded bellow
"""
from fastapi import APIRouter
from src.apps.patient.interfaces.app import get_orm
from src.clients.patient.models import Patient
from src.apps.patient.schemas.pydantic.patient import PostPatientSchema
from src.apps.patient.services.patient import PatientService

orm = get_orm()
router = APIRouter(prefix="/v1/patients", tags=["patient"])
service = PatientService()


@router.post("/", response_model=Patient)
async def create(patient: PostPatientSchema) -> Patient:
    """create method, trigger a DB query instruction to create a new Patient row

    Args:
        patient (PostPatient): Patient Model

    Returns:
        Patient: Patient Prisma Model
    """

    return await service.create(patient)


@router.get("/{patient_id}", response_model=Patient)
async def read_by_id(patient_id: str) -> Patient:
    """read_by_id method, trigger ap DN query instruction to fetch patient row according a patient_id

    Args:
        patient_id (str): PK of Patient Model

    Returns:
        Patient: Patient Prisma ORM Model
    """

    return await service.read_by_id(patient_id)
