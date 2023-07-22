"""Module Testing: measurement API endpoints
This module contains a series of asynchronous test functions to verify the behavior of the measurement API endpoints. It uses the `httpx.AsyncClient` to make HTTP requests to a test server. The test functions include the following:
"""
from httpx import AsyncClient
from src.apps.measurement.core.main import app, get_orm
from src.utils.uuid import generate_uuid

prisma = get_orm()
measurement_data = {"blood_pressure": 110, "temperature": "High"}


async def test_new_measurement():
    """Verifies that a new measurement can be successfully created using a POST request to `/v1/measurements/`. It checks if the response status code is 201 (Created) and if the 'measurement_id' is present in the response JSON."""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        if not prisma.is_connected():
            await prisma.connect()

        data = {**measurement_data, "patient_id": f"{generate_uuid().hex}"}

        response = await ac.post(
            "/v1/measurements/",
            json=data,
        )

    assert response.status_code == 201
    assert "measurement_id" in response.json()


async def test_failed_new_measurement_without_required_field():
    """Verifies that creating a new measurement without providing the required fields results in a validation error. It checks if the response status code is 422 (Unprocessable Entity) and if the appropriate error message is returned for each missing required field."""

    async with AsyncClient(app=app, base_url="http://test") as ac:
        if not prisma.is_connected():
            await prisma.connect()

        response = await ac.post(
            "/v1/measurements/",
            json={},
        )

    def _check_required_field():
        for item in response.json()["detail"]:
            return "msg" in item and "field required" in item["msg"]

    assert response.status_code == 422
    assert _check_required_field()
