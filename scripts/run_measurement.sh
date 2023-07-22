#!/bin/bash
poetry run client_measurement
uvicorn src.apps.measurement.core.main:app --reload --host 0.0.0.0 --port 8001