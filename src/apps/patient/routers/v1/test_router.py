"""Module Testing: patient API endpoints
This module contains a series of asynchronous test functions to verify the behavior of the patient API endpoints. It uses the `httpx.AsyncClient` to make HTTP requests to a test server. The test functions include the following:
"""
from httpx import AsyncClient
from src.apps.patient.core.main import app, get_orm
from src.utils.uuid import generate_uuid

prisma = get_orm()
patient_data = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 550,
    "condition": "Healthy",
}


async def test_new_patient():
    """Verifies that a new patient can be successfully created using a POST request to `/v1/patients/`. It checks if the response status code is 201 (Created) and if the 'patient_id' is present in the response JSON."""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        if not prisma.is_connected():
            await prisma.connect()

        data = {**patient_data, "patient_id": f"{generate_uuid().hex}"}

        response = await ac.post(
            "/v1/patients/",
            json=data,
        )

    assert response.status_code == 201
    assert "patient_id" in response.json()


async def test_failed_new_patient_without_required_field():
    """Verifies that creating a new patient without providing the required fields results in a validation error. It checks if the response status code is 422 (Unprocessable Entity) and if the appropriate error message is returned for each missing required field."""

    async with AsyncClient(app=app, base_url="http://test") as ac:
        if not prisma.is_connected():
            await prisma.connect()

        response = await ac.post(
            "/v1/patients/",
            json={},
        )

    def _asd():
        for item in response.json()["detail"]:
            return "msg" in item and "field required" in item["msg"]

    assert response.status_code == 422
    assert _asd()


async def test_get_patient_by_id():
    """Verifies that a patient can be retrieved by their ID using a GET request to `/v1/patients/<patient_id>`. It checks if the response status code is 200 (OK) and if the 'patient_id' is present in the response JSON."""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        if not prisma.is_connected():
            await prisma.connect()
        response = await ac.post(
            "/v1/patients/",
            json=patient_data,
        )
        response = await ac.get(f"/v1/patients/{response.json().get('patient_id')}")

    assert response.status_code == 200
    assert "patient_id" in response.json()
