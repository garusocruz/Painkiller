FROM python:3.9-slim

ENV APP_HOME /app
WORKDIR $APP_HOME

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && apt-get install -y -- \
    gettext \
    git \
    build-essential \
    libpq-dev

COPY ./poetry.toml poetry.toml
COPY ./pyproject.toml pyproject.toml
COPY ./pytest.ini pytest.ini
COPY ./scripts scripts
COPY ./src/apps/patient src/apps/patient

RUN pip install poetry
RUN poetry install

ENV PORT=8000
EXPOSE 8000

CMD sh scripts/run_patient.sh
