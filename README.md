# Painkiller

[This test](https://github.com/Painkiller-AI/painkiller-eng-software-challenge/tree/main) is designed to assess the technical skills of the candidate for the Senior Software Engineer role in areas such as backend development at A3Data company.

---

## _**`To run application in your local environment, follow the steps bellow:`**_

---

<details>
  <summary>Check docker compose</summary>

It's very important to check if you already can use a docker compose command.
More info :[here](https://docs.docker.com/compose/install/):

</details>
<details>
  <summary>Create a virtual environment</summary>

```shellscript
python -m venv .venv
```

</details>
<details>
  <summary>load a virtual environment</summary>

```shellscript
source .venv/bin/activate
```

</details>
<details>
  <summary>Install poetry package manager</summary>

```shellscript
pip install poetry
```

</details>
<details>
  <summary>Install project dependencies</summary>

```shellscript
poetry install
```

</details>
<details>
  <summary>Starting applications</summary>

```shellscript
poetry run docker_up
```

</details>
<details>
  <summary>Run coverage</summary>

```shellscript
poetry run coverage
```

</details>

---

**`For more poetry commands please visit:`**

- [applications cmds](https://github.com/garusocruz/Painkiller/blob/main/scripts/applications.py)
- [prisma cmds](https://github.com/garusocruz/Painkiller/blob/main/scripts/prisma.py)

---
