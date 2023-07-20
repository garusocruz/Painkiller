# Painkiller

This test is designed to assess the technical skills of the candidate for the Senior Software Engineer role in areas such as backend development at A3Data company.

---

## _**`To run application in your local environment, follow the steps bellow:`**_

---

<details>
  <summary>Create a virtual environment</summary>

`Create a virtual env`

```shellscript
python -m venv .venv
```

---

`load a virtual environment`

```shellscript
source .venv/bin/activate
```

</details>
<details>
  <summary>Install poetry</summary>

`Install poetry package manager`

```shellscript
pip install poetry
```

</details>
<details>
  <summary>Install project dependencies</summary>

`Install project dependencies using poetry`

```shellscript
poetry install
```

</details>
<details>
  <summary>Starting applications</summary>

`Starting a Patients fast api server application`

```shellscript
poetry run patient
```

---

```shellscript
poetry run measurement
```

</details>
<details>
  <summary>Run DB migrations</summary>

`Trigger a job to apply DB migrations`

```shellscript
poetry run migrate_patient
```

---

```shellscript
poetry run migrate_measurement
```

</details>
