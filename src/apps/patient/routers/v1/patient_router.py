"""PatientsRouter module

    All Patients view is aborded bellow
"""
from fastapi import APIRouter, Response, status
from src.clients.patient.models import Patient
from src.apps.patient.schemas.post_patient_schema import PostPatientSchema
from src.apps.patient.services.patient_service import PatientService

router = APIRouter(prefix="/v1/patients", tags=["patient"])
service = PatientService()


@router.post("/", response_model=Patient)
async def create(patient: PostPatientSchema, response: Response) -> Patient:
    """create method, trigger a DB query instruction to create a new Patient row

    Args:
        patient (PostPatient): Patient Model

    Returns:
        Patient: Patient Prisma Model
    """

    patient = await service.create(patient)
    response.status_code = status.HTTP_201_CREATED
    return patient


@router.get("/{patient_id}", response_model=Patient)
async def read_by_id(patient_id: str):
    """read_by_id method, trigger ap DN query instruction to fetch patient row according a patient_id

    Args:
        patient_id (str): PK of Patient Model

    Returns:
        Patient: Patient Prisma ORM Model
    """

    return await service.read_by_id(patient_id)
