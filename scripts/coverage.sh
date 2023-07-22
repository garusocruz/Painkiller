#!/usr/bin/env bash
sudo docker compose -f .docker/docker-compose.yml run --rm painkiller-coverage bash -c "
   poetry run client_measurement && 
   poetry run client_patient && 
   pip install pytest-trio && coverage run -m pytest"