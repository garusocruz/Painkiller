#!/bin/bash
poetry run client_patient
uvicorn src.apps.patient.core.main:app --reload --host 0.0.0.0 --port 8000