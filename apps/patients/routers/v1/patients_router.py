"""PatientsRouter module

    All Patients view is aborded bellow
"""
from fastapi import APIRouter
from apps.patients.interfaces.app import get_orm
from apps.patients.models.patient import PatientModel
from apps.patients.schemas.pydantic.patient import PostPatientSchema
from apps.patients.services.patient import PatientService

orm = get_orm()
router = APIRouter(prefix="/v1/patients", tags=["patient"])
service = PatientService()


@router.post("/api/v1/patient", response_model=PatientModel)
async def create(patient: PostPatientSchema) -> PatientModel:
    """create method, trigger a DB query instruction to create a new Patient row

    Args:
        patient (PostPatient): Patient Model

    Returns:
        Patient: Patient Prisma Model
    """

    return await service.create(patient)


@router.get("/api/v1/patient/{patient_id}", response_model=PatientModel)
async def read_by_id(patient_id: str):
    """read_by_id method, trigger ap DN query instruction to fetch patient row according a patient_id

    Args:
        patient_id (str): PK of Patient Model

    Returns:
        Patient: Patient Prisma ORM Model
    """

    return await service.read_by_id(patient_id)
